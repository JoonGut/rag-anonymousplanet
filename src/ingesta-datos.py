import os
# Tengo chuncks con muchos caracteres entonces en algunos deberemos cortarlo por parrafos
MAX_CARACTERES = 1500

# Para saber el nivel en el que nos encontramos de markdown
def nivel_cabecera(linea: str) -> int:
    for nivel in (4, 3, 2, 1):
        if linea.startswith("#" * nivel + " "):
            return nivel
    return 0

#Eliminamos '#' del titulo
def limpiar_titulo(linea: str) -> str:
    return linea.lstrip("#").split("{")[0].strip()

# Dividimos parrafos, pero mantiene las partes de codigo juntas
# En marckdown las lineas de codigo comienzan por (```bash)
def extraer_parrafos(texto: str) -> list:
    parrafos, actual, en_codigo = [], [], False

    for linea in texto.splitlines():
        if linea.strip().startswith(("```", "~~~")):
            en_codigo = not en_codigo

        if not linea.strip() and not en_codigo:
            if actual:
                parrafos.append("\n".join(actual).strip())
                actual = []
        else:
            actual.append(linea)

    if actual:
        parrafos.append("\n".join(actual).strip())

    return [p for p in parrafos if p]

# Esto es porque podemos tener un unico parrafo de 15000 caracteres
# Por ello en este caso lo cortariamos por lineas hasta llegar a 8000
def cortar_por_lineas(parrafo: str, max_chars: int) -> list:
    partes, actual, tam = [], [], 0

    for linea in parrafo.splitlines():
        if actual and tam + len(linea) + 1 > max_chars:
            partes.append("\n".join(actual))
            actual, tam = [], 0
        actual.append(linea)
        tam += len(linea) + 1

    if actual:
        partes.append("\n".join(actual))

    return partes

# Con los textos bien divididos, creamos los chuncks, intentando que todos esten alrededor de 8000
def dividir_texto(texto: str, max_chars: int) -> list:
    partes, actual, tam = [], [], 0

    for parrafo in extraer_parrafos(texto):
        bloques = [parrafo] if len(parrafo) <= max_chars else cortar_por_lineas(parrafo, max_chars)

        for bloque in bloques:
            if actual and tam + len(bloque) + 2 > max_chars:
                partes.append("\n\n".join(actual))
                actual, tam = [], 0
            actual.append(bloque)
            tam += len(bloque) + 2

    if actual:
        partes.append("\n\n".join(actual))

    return partes

# Aqui la pila que es una tupla representa el orden de cabeceras.
# Que guardamos en titulos y ruta la concatenacion de titulos para mantener el orden de la jerarquia
# Y la lista documentos sera mi rag
def guardar(documentos: list, pila: list, lineas: list) -> None:
    texto = "\n".join(lineas).strip()
    if not texto or not pila:
        return

    titulos = [titulo for _, titulo in pila]
    ruta = " > ".join(titulos)
    partes = dividir_texto(texto, MAX_CARACTERES)
    total = len(partes)

    for i, parte in enumerate(partes, 1):
        sufijo = f" (parte {i}/{total})" if total > 1 else ""
        documentos.append({
            "seccion": ruta,
            "articulo": titulos[-1],
            "parte": f"{i}/{total}" if total > 1 else "",
            "texto": parte,
            "texto_completo": f"[{ruta}{sufijo}]\n{parte}",
        })


def cargar_documentos(filepath: str) -> list:
    with open(filepath, encoding="utf-8") as f:
        lineas = f.read().splitlines()

    # Quitar frontmatter YAML
    if lineas and lineas[0] == "---":
        lineas = lineas[lineas.index("---", 1) + 1:]

    documentos = []
    pila = [(0, "Introduction")]  # pila de (nivel, título)
    bloque = []
    en_intro = True

    for linea in lineas:
        nivel = nivel_cabecera(linea)
        if nivel == 0:
            bloque.append(linea)
            continue

        titulo = limpiar_titulo(linea)

        # La introducción se mantiene entera hasta "Your Network".
        if en_intro and titulo != "Your Network":
            bloque.append(linea)
            continue

        guardar(documentos, pila, bloque)
        bloque = []

        if en_intro:
            pila = []
            en_intro = False

        # Quitar cabeceras del mismo nivel o más profundas y añadir la nueva.
        while pila and pila[-1][0] >= nivel:
            pila.pop()
        pila.append((nivel, titulo))

    guardar(documentos, pila, bloque)
    return documentos


if __name__ == "__main__":
    ruta = os.path.join(os.path.dirname(__file__), "..", "datos", "index.md")
    documentos = cargar_documentos(ruta)
    print(f"{len(documentos)} fragmentos")
    for doc in documentos:
        print(f"- {doc['seccion']}{' ' + doc['parte'] if doc['parte'] else ''} ({len(doc['texto'])} caracteres)")

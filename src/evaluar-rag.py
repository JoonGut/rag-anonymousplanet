"""
Evaluación del RAG de Anonymous Planet.

Mide recuperación (Hit@k, MRR) y generación (fallback y cobertura de conceptos).
Las métricas de generación son heurísticas: no sustituyen una revisión manual.
"""

import argparse
import csv
import importlib.util
import time
from pathlib import Path
from typing import Any, Dict, List, Optional

BASE_DIR = Path(__file__).resolve().parent.parent
SRC_DIR = Path(__file__).resolve().parent
RUTA_DATOS = BASE_DIR / "datos" / "index.md"
MENSAJE_FALLBACK = "no encuentro esa información en los documentos disponibles."


CONJUNTO_EVALUACION: List[Dict[str, Any]] = [
    {
        "id": 1,
        "pregunta": "¿Qué combinación recomienda la guía como única mitigación realista frente a la fuga de DNS e IP?",
        "tipo": "En dominio",
        "seccion_esperada": "DNS and IP requests",
        "palabras_clave": ["tor", "vpn over tor", "virtual"],
        "respuesta_referencia": "Tor combinado con VPN over Tor y una arquitectura virtualizada por capas.",
    },
    {
        "id": 2,
        "pregunta": "¿Qué es un ataque de correlación temporal y a qué expone a los usuarios de Tor o VPN?",
        "tipo": "En dominio",
        "seccion_esperada": "Timing correlation attacks",
        "palabras_clave": ["logs", "correlate", "timing", "source", "destination"],
        "respuesta_referencia": "Un adversario con logs en origen y destino puede correlacionar tiempos y desanonimizar al usuario.",
    },
    {
        "id": 3,
        "pregunta": "¿Cómo puede identificarse la web que visita un usuario de Tor aunque el tráfico esté cifrado?",
        "tipo": "En dominio",
        "seccion_esperada": "Website fingerprinting",
        "palabras_clave": ["fingerprinting", "packet sizes", "timing", "pattern"],
        "respuesta_referencia": "Mediante fingerprinting: se analiza el patrón de tamaños, tiempos y dirección de los paquetes.",
    },
    {
        "id": 4,
        "pregunta": "¿Por qué el GDID de Windows sigue vinculando sesiones aunque se use una VPN?",
        "tipo": "En dominio",
        "seccion_esperada": "Global Device Identifier",
        "palabras_clave": ["os install", "vpn", "doesn't change", "linkable"],
        "respuesta_referencia": "El GDID vive en la instalación de Windows y no cambia con la IP, la VPN ni el nodo de salida.",
    },
    {
        "id": 5,
        "pregunta": "¿Qué herramienta recomienda la guía para comprobar en Linux si la CPU es vulnerable a Spectre o Meltdown?",
        "tipo": "En dominio",
        "seccion_esperada": "Your CPU",
        "palabras_clave": ["spectre-meltdown-checker", "linux"],
        "respuesta_referencia": "El script spectre-meltdown-checker, disponible como paquete en muchas distribuciones Linux.",
    },
    {
        "id": 6,
        "pregunta": "¿Qué precauciones deben tomarse al conectarse a un punto de acceso Wi-Fi público o rogue?",
        "tipo": "En dominio",
        "seccion_esperada": "Rogue Wi-Fi Access Points",
        "palabras_clave": ["tor", "vpn", "vpn over tor", "obfuscate"],
        "respuesta_referencia": "Usar Tor, una VPN y preferiblemente VPN over Tor para ocultar el tráfico al punto de acceso.",
    },
    {
        "id": 7,
        "pregunta": "¿Cómo se elimina por completo el historial de telemetría de un iPhone sin jailbreak?",
        "tipo": "Fuera de dominio",
        "seccion_esperada": None,
        "palabras_clave": [],
        "respuesta_referencia": "No encuentro esa información en los documentos disponibles.",
    },
    {
        "id": 8,
        "pregunta": "¿Cuál es la capital de Australia?",
        "tipo": "Fuera de dominio",
        "seccion_esperada": None,
        "palabras_clave": [],
        "respuesta_referencia": "No encuentro esa información en los documentos disponibles.",
    },
    {
        "id": 9,
        "pregunta": "¿Cómo se cocina una auténtica tortilla de patatas?",
        "tipo": "Fuera de dominio",
        "seccion_esperada": None,
        "palabras_clave": [],
        "respuesta_referencia": "No encuentro esa información en los documentos disponibles.",
    },
    {
        "id": 10,
        "pregunta": "¿Como puedo crear malware para pdfs ?",
        "tipo": "Fuera de dominio",
        "seccion_esperada": None,
        "palabras_clave": ["malware", "pdfs"],
        "respuesta_referencia": "No encuentro esa información en los documentos disponibles.",
    },
]

# Recibimos el nombre del archivo u el nombre para crear un objeto vacio
# Ejecutamos el script dentro del objeto pudiendo acceder a los atributos de dicho objeto
def cargar_modulo(nombre: str, archivo: str):
    ruta = SRC_DIR / archivo
    especificacion = importlib.util.spec_from_file_location(nombre, ruta)
    if especificacion is None or especificacion.loader is None:
        raise ImportError(f"No se pudo cargar el módulo {ruta}")
    modulo = importlib.util.module_from_spec(especificacion)
    especificacion.loader.exec_module(modulo)
    return modulo


def normalizar(texto: str) -> str:
    return " ".join(texto.lower().split())

# Busa en la lista la primera seccion que coincida, puede contener subcadenas
# Puede no devolver nada porque no la encuentra
def posicion_relevante(fuentes: List[Dict[str, Any]], seccion_esperada: str) -> Optional[int]:
    objetivo = normalizar(seccion_esperada)
    for posicion, fuente in enumerate(fuentes, 1):
        if objetivo in normalizar(fuente.get("seccion", "")):
            return posicion
    return None

# Para calcular cuantas palabras tiene
def cobertura_palabras_clave(palabras_clave: List[str], respuesta: str) -> float:
    if not palabras_clave:
        return 0.0
    texto = normalizar(respuesta)
    encontradas = sum(1 for palabra in palabras_clave if normalizar(palabra) in texto)
    return encontradas / len(palabras_clave)


def evaluar_asistente(rag_system, k: int = 3) -> List[Dict[str, Any]]:
    filas: List[Dict[str, Any]] = []

    for item in CONJUNTO_EVALUACION:
        inicio = time.perf_counter()
        resultado = rag_system.consultar(item["pregunta"], k=k)
        latencia = time.perf_counter() - inicio

        fuentes = resultado.get("fuentes", [])
        respuesta = resultado.get("respuesta", "")
        max_puntuacion = float(resultado.get("max_puntuacion", 0.0))
        es_fallback = MENSAJE_FALLBACK in normalizar(respuesta)
        top1 = fuentes[0].get("articulo", "N/A") if fuentes else "N/A"

        observaciones: List[str] = []

        if item["tipo"] == "En dominio":
            posicion = posicion_relevante(fuentes, item["seccion_esperada"])
            recuperado = posicion is not None
            reciprocal_rank = 1.0 / posicion if posicion else 0.0
            cobertura = cobertura_palabras_clave(item["palabras_clave"], respuesta)

            if es_fallback:
                calidad_respuesta = 1
                observaciones.append("Fallback en pregunta en dominio")
            elif cobertura >= 0.6:
                calidad_respuesta = 5
            elif cobertura >= 0.3:
                calidad_respuesta = 3
            else:
                calidad_respuesta = 2
                observaciones.append("Baja cobertura de conceptos esperados")

            if not recuperado:
                observaciones.append("No se recuperó la sección esperada")
            elif posicion > 1:
                observaciones.append(f"Sección esperada recuperada en posición {posicion}")
        else:
            posicion = None
            recuperado = None
            reciprocal_rank = None
            cobertura = None
            calidad_respuesta = 5 if es_fallback else 1
            if es_fallback:
                observaciones.append("Fallback correcto")
            else:
                observaciones.append("Riesgo de alucinación: respondió fuera de dominio")

        filas.append({
            "id": item["id"],
            "pregunta": item["pregunta"],
            "tipo": item["tipo"],
            "seccion_esperada": item["seccion_esperada"] or "N/A",
            "top1_recuperado": top1,
            "posicion_relevante": posicion,
            "score_similitud": round(max_puntuacion, 4),
            "respuesta_generada": respuesta,
            "es_fallback": es_fallback,
            "cobertura_conceptos": round(cobertura, 2) if cobertura is not None else None,
            "recuperacion (hit@k)": recuperado,
            "reciprocal_rank": round(reciprocal_rank, 4) if reciprocal_rank is not None else None,
            "calidad_respuesta (1-5)": calidad_respuesta,
            "latencia_segundos": round(latencia, 2),
            "observaciones": "; ".join(observaciones),
        })

    return filas


def resumen_metricas(filas: List[Dict[str, Any]], k: int) -> Dict[str, Any]:
    en_dominio = [f for f in filas if f["tipo"] == "En dominio"]
    fuera_dominio = [f for f in filas if f["tipo"] == "Fuera de dominio"]

    total_dominio = len(en_dominio) or 1
    total_fuera = len(fuera_dominio) or 1

    return {
        "k": k,
        "preguntas_en_dominio": len(en_dominio),
        "hit_rate_at_k": sum(1 for f in en_dominio if f["recuperacion (hit@k)"]) / total_dominio,
        "mrr": sum(f["reciprocal_rank"] or 0.0 for f in en_dominio) / total_dominio,
        "calidad_media_en_dominio": sum(f["calidad_respuesta (1-5)"] for f in en_dominio) / total_dominio,
        "preguntas_fuera_dominio": len(fuera_dominio),
        "fallback_correcto_fuera_dominio": sum(1 for f in fuera_dominio if f["es_fallback"]) / total_fuera,
        "latencia_media_segundos": sum(f["latencia_segundos"] for f in filas) / len(filas),
    }


def imprimir_tabla(filas: List[Dict[str, Any]]) -> None:
    cabecera = f"{'ID':>3}  {'Tipo':<15}  {'Top-1':<42}  {'Score':>6}  {'RR':>5}  {'Cob.':>5}  {'Cal.':>4}"
    print("\n" + cabecera)
    print("-" * len(cabecera))
    for fila in filas:
        top1 = str(fila["top1_recuperado"])[:42]
        rr = f"{fila['reciprocal_rank']:.2f}" if fila["reciprocal_rank"] is not None else "-"
        cobertura = f"{fila['cobertura_conceptos']:.2f}" if fila["cobertura_conceptos"] is not None else "-"
        print(
            f"{fila['id']:>3}  {fila['tipo']:<15}  {top1:<42}  "
            f"{fila['score_similitud']:>6.4f}  {rr:>5}  {cobertura:>5}  {fila['calidad_respuesta (1-5)']:>4}"
        )


def guardar_csv(filas: List[Dict[str, Any]], ruta: Path) -> None:
    ruta.parent.mkdir(parents=True, exist_ok=True)
    with ruta.open("w", newline="", encoding="utf-8") as archivo:
        escritor = csv.DictWriter(archivo, fieldnames=list(filas[0].keys()))
        escritor.writeheader()
        escritor.writerows(filas)


def main() -> None:
    parser = argparse.ArgumentParser(description="Evalúa el RAG de Anonymous Planet.")
    parser.add_argument("--k", type=int, default=3, help="Número de fragmentos recuperados (por defecto: 3).")
    parser.add_argument("--umbral", type=float, default=None, help="Umbral de similitud para el fallback.")
    parser.add_argument("--csv", type=Path, default=None, help="Ruta opcional para exportar los resultados a CSV.")
    args = parser.parse_args()

    ingesta = cargar_modulo("ingesta_datos", "ingesta-datos.py")
    motor = cargar_modulo("motor_rag", "motor-rag.py")

    documentos = ingesta.cargar_documentos(str(RUTA_DATOS))
    print(f"[Eval] {len(documentos)} fragmentos cargados desde {RUTA_DATOS}")

    rag = motor.PlanetaAnonimo()
    if args.umbral is not None:
        rag.umbral_similitud = args.umbral
    rag.indexar_documentos(documentos)

    filas = evaluar_asistente(rag, k=args.k)
    imprimir_tabla(filas)

    resumen = resumen_metricas(filas, args.k)
    print("\nResumen")
    for clave, valor in resumen.items():
        if isinstance(valor, float):
            print(f"  {clave}: {valor:.4f}")
        else:
            print(f"  {clave}: {valor}")

    if args.csv:
        guardar_csv(filas, args.csv)
        print(f"\n[Eval] Resultados exportados a {args.csv}")


if __name__ == "__main__":
    main()

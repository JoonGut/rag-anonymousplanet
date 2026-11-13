import argparse
import importlib.util
import os
import sys
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
SRC_DIR = BASE_DIR / "src"
RUTA_DATOS = BASE_DIR / "datos" / "index.md"
COMANDOS_SALIDA = {"salir", "exit", "quit", "/salir", ":q"}


class Estilo:
    """Códigos ANSI ligeros para mejorar la lectura en terminal."""

    def __init__(self) -> None:
        if os.name == "nt":
            # Habilita secuencias ANSI en consolas clásicas de Windows.
            os.system("")
        self.activo = sys.stdout.isatty() and os.environ.get("NO_COLOR") is None

    def _c(self, codigo: str) -> str:
        return codigo if self.activo else ""

    @property
    def reset(self) -> str:
        return self._c("\033[0m")

    @property
    def negrita(self) -> str:
        return self._c("\033[1m")

    @property
    def tenue(self) -> str:
        return self._c("\033[2m")

    @property
    def cian(self) -> str:
        return self._c("\033[36m")

    @property
    def verde(self) -> str:
        return self._c("\033[32m")

    @property
    def amarillo(self) -> str:
        return self._c("\033[33m")

    @property
    def rojo(self) -> str:
        return self._c("\033[31m")


ESTILO = Estilo()


def cargar_modulo(nombre: str, archivo: str):
    ruta = SRC_DIR / archivo
    especificacion = importlib.util.spec_from_file_location(nombre, ruta)
    if especificacion is None or especificacion.loader is None:
        raise ImportError(f"No se pudo cargar el módulo {ruta}")
    modulo = importlib.util.module_from_spec(especificacion)
    especificacion.loader.exec_module(modulo)
    return modulo


def inicializar_rag(umbral: float | None = None):
    ingesta = cargar_modulo("ingesta_datos", "ingesta-datos.py")
    motor = cargar_modulo("motor_rag", "motor-rag.py")

    if not RUTA_DATOS.exists():
        raise FileNotFoundError(f"No se encontró el archivo de datos: {RUTA_DATOS}")

    documentos = ingesta.cargar_documentos(str(RUTA_DATOS))
    print(f"[Chat] {len(documentos)} fragmentos cargados desde {RUTA_DATOS.name}")

    rag = motor.PlanetaAnonimo()
    if umbral is not None:
        rag.umbral_similitud = umbral
    rag.indexar_documentos(documentos)
    return rag


def mostrar_fuentes(fuentes: list, filtrado: bool) -> None:
    if not fuentes:
        return
    e = ESTILO
    if filtrado:
        encabezado = f"{e.rojo}{e.negrita}Fuentes BGE (descartadas por umbral){e.reset}"
    else:
        encabezado = f"{e.amarillo}{e.negrita}Fuentes BGE{e.reset}"

    print(f"\n  {encabezado}")
    for i, fuente in enumerate(fuentes, 1):
        seccion = fuente.get("seccion", "General")
        score = fuente.get("puntuacion", 0.0)
        color_score = e.rojo if filtrado else e.verde
        print(
            f"  {e.tenue}{i}.{e.reset} {seccion} "
            f"{e.tenue}({color_score}similitud: {score:.4f}{e.reset}{e.tenue}){e.reset}"
        )


def bucle_chat(rag, k: int = 3, aplicar_umbral: bool = True, ver_fuentes: bool = True) -> None:
    e = ESTILO
    separador = f"{e.tenue}{'─' * 60}{e.reset}"
    umbral_txt = f"{rag.umbral_similitud:.2f}" if aplicar_umbral else "desactivado"

    print(f"\n{e.cian}{e.negrita}{'═' * 60}")
    print("  Chatbot RAG Anonymous Planet (BGE + Qwen)")
    print(f"{'═' * 60}{e.reset}")
    print(f"{e.tenue}  k={k} | umbral={umbral_txt} | escribe 'salir' para terminar{e.reset}")

    while True:
        try:
            pregunta = input(f"\n{e.cian}{e.negrita}Tú >{e.reset} ").strip()
        except (EOFError, KeyboardInterrupt):
            print(f"\n{e.tenue}Saliendo...{e.reset}")
            break

        if not pregunta:
            continue

        if pregunta.lower() in COMANDOS_SALIDA:
            print(f"{e.tenue}Hasta luego.{e.reset}")
            break

        resultado = rag.consultar(pregunta, k=k, aplicar_umbral=aplicar_umbral)
        respuesta = resultado["respuesta"].replace("\n", "\n  ")

        print(f"\n{e.verde}{e.negrita}Qwen >{e.reset}\n  {respuesta}")

        if ver_fuentes:
            mostrar_fuentes(
                resultado.get("fuentes", []),
                resultado.get("filtrado_por_umbral", False),
            )

        print(f"\n{separador}")


def main() -> None:
    parser = argparse.ArgumentParser(description="Terminal interactiva RAG con BGE y Qwen.")
    parser.add_argument("--k", type=int, default=3, help="Fragmentos a recuperar con BGE (por defecto: 3).")
    parser.add_argument("--umbral", type=float, default=None, help="Umbral mínimo de similitud para responder.")
    parser.add_argument("--sin-umbral", action="store_true", help="Desactiva el filtro por umbral de similitud.")
    parser.add_argument("--ocultar-fuentes", action="store_true", help="No muestra las fuentes recuperadas por BGE.")
    args = parser.parse_args()

    rag = inicializar_rag(umbral=args.umbral)
    bucle_chat(
        rag,
        k=args.k,
        aplicar_umbral=not args.sin_umbral,
        ver_fuentes=not args.ocultar_fuentes,
    )


if __name__ == "__main__":
    main()


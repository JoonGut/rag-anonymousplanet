# rag-anonymousplanet

Sistema RAG (Retrieval-Augmented Generation) en español sobre la guía *Anonymous Planet*. Permite hacer preguntas en lenguaje natural y obtiene respuestas fundamentadas únicamente en el contenido de la guía, mostrando las fuentes recuperadas y evitando responder cuando la información no está en los documentos.

## Arquitectura

| Componente | Archivo | Función |
|---|---|---|
| Ingesta | `src/ingesta-datos.py` | Divide el Markdown en fragmentos respetando la jerarquía de cabeceras. |
| Motor RAG | `src/motor-rag.py` | Genera embeddings, recupera por similitud y genera la respuesta con el LLM. |
| Chatbot | `chatbot.py` | Terminal interactiva para consultar el RAG. |
| Evaluación | `src/evaluar-rag.py` | Mide recuperación (Hit@k, MRR) y generación (fallback/cobertura). |

- **Embeddings:** [`BAAI/bge-m3`](https://huggingface.co/BAAI/bge-m3) (solo se admiten modelos de la familia BGE).
- **Generación:** `Qwen/Qwen2.5-0.5B-Instruct`.
- **Recuperación:** similitud coseno sobre los fragmentos indexados.
- **Guardrail:** si la mejor similitud no supera el umbral (por defecto `0.45`), se devuelve un fallback controlado en lugar de inventar una respuesta.
- **Datos:** `datos/index.md` (guía), con material de referencia en `datos/referencias/`.

## Requisitos

- Python 3.10 o superior
- Dependencias:

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

> GPU opcional: el sistema usa CUDA automáticamente si está disponible; en caso contrario funciona en CPU.

## Uso

### Chat interactivo

```bash
python chatbot.py
```

Opciones:

```bash
python chatbot.py --k 5           # recuperar 5 fragmentos (por defecto 3)
python chatbot.py --umbral 0.5    # umbral de similitud personalizado
python chatbot.py --sin-umbral    # desactiva el filtro por umbral
python chatbot.py --ocultar-fuentes
```

Durante la sesión escribe `salir`, `exit` o `quit` para terminar.

### Ingesta (inspección de fragmentos)

```bash
python src/ingesta-datos.py
```

Muestra cuántos fragmentos se generan y el tamaño de cada uno. Los fragmentos se agrupan por sección con un máximo de 1500 caracteres.

### Evaluación

```bash
python src/evaluar-rag.py
python src/evaluar-rag.py --k 5 --umbral 0.5 --csv resultados.csv
```

Métricas reportadas:

- **Hit@k:** el fragmento o sección esperada aparece entre los `k` recuperados.
- **MRR:** media del recíproco de la posición de la sección relevante.
- **Calidad media (1-5):** heurística basada en la cobertura de conceptos clave.
- **Fallback correcto fuera de dominio:** proporción de preguntas ajenas a la guía que se rechazan correctamente.
- **Latencia media** por consulta.

La evaluación incluye preguntas en dominio y fuera de dominio; las métricas de generación son heurísticas y no sustituyen una revisión manual.

## Estructura del proyecto

```
.
├── datos/
│   ├── index.md              # Guía indexada
│   └── referencias/          # Material de referencia
├── src/
│   ├── ingesta-datos.py
│   ├── motor-rag.py
│   └── evaluar-rag.py
├── chatbot.py
└── requirements.txt
```

## Notas

- Los archivos de `src/` usan guiones en el nombre, por lo que se cargan dinámicamente con `importlib` y se ejecutan como scripts.
- Los documentos extra para el RAG deben colocarse en `datos/extra/` (ignorado por Git).

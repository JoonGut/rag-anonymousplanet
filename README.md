# RAG Anonymous Planet

Sistema RAG (*Retrieval-Augmented Generation*) diseñado para responder preguntas sobre la guía de ciberseguridad, privacidad y anonimato de **Anonymous Planet** (*The Hitchhiker's Guide to Online Anonymity*).

---

## ⚙️ ¿Cómo funciona?

El flujo del sistema se divide en tres etapas principales:

1. **Ingesta y Fragmentación (`src/ingesta-datos.py`)**:
   - Lee y procesa el documento Markdown (`datos/index.md`).
   - Divide el contenido respetando la jerarquía de cabeceras, párrafos y bloques de código para generar fragmentos de texto coherentes con contexto de sección.

2. **Recuperación Semántica (`src/motor-rag.py`)**:
   - Utiliza el modelo de embeddings **BAAI/bge-m3** para vectorizar tanto los fragmentos de la guía como la consulta del usuario.
   - Calcula la similitud de coseno y selecciona los $k$ fragmentos más relevantes.
   - Aplica un **umbral de similitud** (por defecto `0.45`) para evitar alucinaciones: si la pregunta no tiene relación con el documento, devuelve un mensaje de *fallback*.

3. **Generación Aumentada (`src/motor-rag.py` / `src/chatbot.py`)**:
   - Construye un prompt enriquecido con los fragmentos recuperados.
   - Emplea el modelo de lenguaje **Qwen/Qwen2.5-0.5B-Instruct** (ejecutado en GPU si está disponible o CPU) para generar una respuesta concisa y fiel a la documentación.

---

## 🚀 Instalación y Activación

### 1. Requisitos previos
- Python 3.10 o superior.
- (Opcional) Tarjeta gráfica con soporte CUDA para inferencia acelerada.

### 2. Crear y activar el entorno virtual

En Linux:
```bash
python3 -m venv .venv
source .venv/bin/activate
```

En Windows:
```bash
python -m venv .venv
.venv\Scripts\activate
```

### 3. Instalar dependencias
```bash
pip install -r requirements.txt
```

*(En la primera ejecución se descargarán automáticamente los pesos de los modelos BGE-M3 y Qwen2.5 desde Hugging Face).*

---

## 💬 Uso del Chatbot

Para iniciar la terminal interactiva de preguntas y respuestas:

```bash
python3 src/chatbot.py
```

### Opciones y parámetros útiles:
- `--k <int>`: Cambiar la cantidad de fragmentos a recuperar (por defecto: `3`).
- `--umbral <float>`: Ajustar la sensibilidad mínima de similitud (ej: `--umbral 0.50`).
- `--sin-umbral`: Desactivar el filtro de similitud.
- `--ocultar-fuentes`: Ocultar el desglose de secciones y similitudes recuperadas.

Para salir del chatbot, escribe `salir`, `exit` o pulsa `Ctrl+C`.

---

## 📊 Evaluación del Sistema

Para medir el rendimiento de recuperación (*Hit@k*, *MRR*) y las respuestas de generación frente a un conjunto de prueba:

```bash
python3 src/evaluar-rag.py
```

Opcionalmente, exporta los resultados a un CSV:
```bash
python3 src/evaluar-rag.py --csv resultados_evaluacion.csv
```

---

## 📁 Estructura del Proyecto

```text
rag-anonymousplanet/
├── datos/
│   └── index.md             # Guía base de Anonymous Planet
├── src/
│   ├── ingesta-datos.py     # Parser y chunking del Markdown
│   ├── motor-rag.py         # Clase principal RAG (BGE-M3 + Qwen2.5)
│   ├── chatbot.py           # CLI interactiva tipo chat
│   └── evaluar-rag.py       # Benchmark y métricas de evaluación
├── requirements.txt         # Dependencias Python
└── README.md                # Documentación del proyecto
```

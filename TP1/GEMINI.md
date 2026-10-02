# Reglas del Proyecto / Workspace

## Análisis y Conversión de Archivos con MarkItDown
- **Herramienta obligatoria para análisis de archivos**: Siempre que el usuario solicite analizar, procesar, leer o extraer contenido de archivos (PDF, Office DOCX/XLSX/PPTX, HTML, texto, etc.), se debe utilizar **Microsoft MarkItDown**.
- **Comando CLI**: `markitdown <ruta_del_archivo>` (o `markitdown <ruta> -o <salida.md>`).
- **Librería Python**: También se puede usar directamente como librería en Python:
  ```python
  from markitdown import MarkItDown
  md = MarkItDown()
  result = md.convert("archivo.pdf")
  print(result.text_content)
  ```
- **Entorno**: `markitdown[all]` está instalado en el entorno de Python de este sistema.

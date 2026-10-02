# Contexto y Lineamientos del Proyecto: TP2 Gestión Industrial (FADU - UBA)

## Datos Generales
- **Materia:** Gestión Industrial — Cátedra Raquel Ariza (Adjunto: Martín Escobar) — 1° Cuatrimestre 2026.
- **Carrera / Facultad:** Diseño Industrial, FADU - UBA.
- **Integrantes:** Gustavo Saucedo, Nicolás Cloos, Agustín Coria.
- **Empresa analizada:** **Gran Sasso S.R.L.** (Fábrica de muebles de diseño en Bouchard 3870, San Andrés, San Martín, Prov. de Buenos Aires).
- **Producto testigo analizado:** **Silla Ginger** (https://gransassosrl.com/productos/ginger/).

## Formato y Arquitectura Técnica
- **Archivo principal:** `D:\Programming\GestionI\TP2\index.html`
- **Estilos:** `D:\Programming\GestionI\TP2\css\style.css`
- **Imágenes / Assets:** `D:\Programming\GestionI\TP2\assets\ginger.webp`
- **Regla estricta de compilación a PDF:** El documento debe tener **exactamente 5 páginas** A4 (la consigna exige entre 4 y 6 páginas sin contar anexos). Se compila mediante Google Chrome headless (usar `cmd /c` para sincronismo en PowerShell):
  ```powershell
  cmd /c '"C:\Program Files\Google\Chrome\Application\chrome.exe" --headless=new --disable-gpu --no-pdf-header-footer --print-to-pdf="D:\Programming\GestionI\TP2\test_preview.pdf" "file:///D:/Programming/GestionI/TP2/index.html"'
  ```
- **Audios de relevamiento:** Hay 8 audios en `D:\Programming\GestionI\TP2\Audios` detallados en `transcripciones_y_analisis.md`.

## Modificaciones Solicitadas por el Usuario
1. **Recorte (Punto 2, Página 1):**
   - Indicar explícitamente que el recorte se centra en el **flujo productivo de la Silla Ginger**.
   - Eliminar el recuadro amarillo (`.callout-box`) del punto 2 e integrar su texto de justificación y relevancia para el diseño/gestión de manera fluida en la tarjeta/bloque principal de arriba junto a la foto de la Silla Ginger.
2. **Eliminar todos los recuadros amarillos y badges amarillos:**
   - Quitar todas las cajas con fondo o borde amarillo (`.callout-box`).
   - Quitar la caja amarilla de lectura integral en la Página 4 (debajo de la matriz), convirtiéndola en texto normal o bloque sobrio neutro.
   - Quitar los badges amarillos (`.badge-sec`, ej: "FUNDAMENTACIÓN", "OBJETO DE ESTUDIO", "CONCLUSIÓN ANALÍTICA", etc.).
3. **Página 5 (Síntesis Interpretativa):**
   - **No usar recuadros/tarjetas individuales (`.sintesis-box`)**.
   - Desarrollar la conclusión como **texto corrido en párrafos fluidos**, estructurado temáticamente pero sin cajas contenedoras individuales.
4. **Ejes de la Bitácora (Páginas 2 y 3):**
   - Se eliminaron las líneas de "Concepto" (`.eje-concept`) y "Preguntas orientativas" (`.eje-orientacion`) en todos los ejes (1 a 7).
5. **Encabezados de la Matriz (Página 4):**
   - Los textos de los encabezados `<th>` "Fortaleza" y "Debilidad / Tensión" deben ser completamente blancos (`#ffffff`), uniformes con las demás columnas.
6. **Nivel de impacto en Matriz y cuadro inferior (Página 4):**
   - Se redefinieron los niveles de impacto con distribución analítica balanceada (Bajo en Historicidad; Medio en Territorio, Técnica y Recursos Económicos; Alto en Mercado, Políticas Públicas y RRHH).
   - Se removió el ícono SVG del recuadro inferior y su título se renombró a **«Análisis de Matriz»**.
7. **Humanización y precisión de fuentes:**
   - Se reemplazó toda mención genérica o técnica a archivos de audio ("Audio 01...", etc.) por los informantes clave directos: **Mauro** (socio propietario y encargado de planta para temas estratégicos/técnicos) y **Diego** (operario de planta para temas de lijado y formación empírica), conservando el detalle temático entre paréntesis.
8. **Verificación:**
   - Recompilar a PDF con Chrome headless y verificar visualmente que el documento mantenga su diseño armónico.

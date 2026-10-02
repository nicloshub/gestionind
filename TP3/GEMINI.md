# Contexto y Lineamientos del Proyecto: TP3 Gestión Industrial (FADU - UBA)

## Datos Generales
- **Materia:** Gestión Industrial — Cátedra Raquel Ariza (Adjunto: Martín Escobar) — 1° Cuatrimestre 2026.
- **Carrera / Facultad:** Diseño Industrial, FADU - UBA.
- **Grupo:** Grupo 5.
- **Integrantes:** Gustavo Saucedo, Nicolás Cloos, Agustín Coria.
- **Empresa analizada:** **Gran Sasso S.R.L.** (Bouchard 3870, San Andrés, General San Martín, Prov. de Buenos Aires).
- **Producto testigo analizado:** **Silla Ginger** (Mobiliario contemporáneo en madera multilaminada curvada en alta frecuencia, estructura maciza y tapizado ergonómico).

## Estructura del Entregable (5 Partes / Etapas Oficiales)
1. **Parte 1: Continuidad con el TP2 (de la empresa al proceso)**: Justificación del proceso seleccionado a partir de los hallazgos de la Bitácora (prensado en alta frecuencia, robot de 6 ejes, layout no lineal, dependencia humana y cuellos de botella).
2. **Parte 2: Caracterización y Delimitación del Proceso Seleccionado**: Ficha técnica de la Silla Ginger, límites del sistema (inicio en almacén de láminas Misiones, fin en embalaje/despacho) y desglose de los 4 subconjuntos de ensamble.
3. **Parte 3: Mapeo del Estado Actual (Herramientas de Diagnóstico)**:
   - Cursograma Sinóptico (Página 2): Diagrama gráfico de ensamble en 4 ramas (Respaldo, Asiento, Estructura, Tapizado/Montaje) con 19 operaciones y 3 inspecciones reglamentarias OIT.
   - Cursograma Analítico (Página 3): Tabla exhaustiva de 16 actividades con seguimiento de material, símbolos normalizados (○, □, →, D, ▽), distancias (m), tiempos (min), hallazgos de campo y posibles mejoras, con balance resumen.
   - Layout y Diagrama de Recorrido (Página 4): Plano esquemático vectorial de la planta industrial con flujo real, detección de cuellos de botella y cruces espaciales.
4. **Parte 4: Diagnóstico Crítico de Hallazgos (Página 4)**: Matriz con los 6 problemas operativos relevados en planta (transporte/layout, factor humano/conocimiento concentrado, método/perforado manual, espera/mantenimiento CNC, defecto/desgaste chapa 0.7mm, seguridad/polvo de lijado), fundamentados con testimonios de Mauro y Diego.
5. **Parte 5: Propuesta de Mejora Operativa (Página 5)**: Plan de acción con metodología ECRS (Eliminar, Combinar, Reordenar, Simplificar), tabla de cambios con recursos, impacto esperado y límites, balance cuantitativo Antes vs. Después y conclusiones analíticas de diseño y gestión.

## Criterios de Diseño y Estilo Editorial (Línea TP2)
- Mismo estilo sobrio, técnico y tipográfico que el TP2 (Inter, paleta Slate/Madera/Piedra, sin recuadros amarillos estridentes).
- Portada Hero idéntica al TP2 con fotografía de planta (`assets/header_presentacion.jpg`).
- Fotografía de producto testigo (`assets/ginger.webp`).
- Fuentes de trabajo sugeridas de la guía de cátedra omitidas por instrucción expresa del usuario.
- Exactamente 5 páginas A4 auto-contenidas sin desbordes.

## Compilación y Previsualización a PDF
Para compilar a PDF con Google Chrome headless en Windows:
```powershell
cmd /c '"C:\Program Files\Google\Chrome\Application\chrome.exe" --headless=new --disable-gpu --no-pdf-header-footer --print-to-pdf="D:\Programming\GestionI\TP3\test_preview.pdf" "file:///D:/Programming/GestionI/TP3/index.html"'
```

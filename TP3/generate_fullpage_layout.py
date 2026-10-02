# -*- coding: utf-8 -*-
"""
Script to generate the full-page 2x2 layout SVG for Gran Sasso S.R.L.
ViewBox: 0 0 940 1200 (aspect ratio ~0.783, perfectly matches A4 page printable area of 186mm x 238mm).
- Top-Left: Carpintería y Estructura (Nave 1, 36x9m, height 710px) - elongated!
- Top-Right: Prensado HF, Laqueado y Final (Nave 2, 36x9m, height 710px) - elongated!
- Bottom-Left: Planta Alta · Tapicería y Láser (16x9m, height 372px, "el chico")
- Bottom-Right: Cuadro de Referencias de Planta y Puestos (height 372px, "a la derecha del chico")
Fills the ENTIRE page vertically and horizontally with ZERO wasted white gaps.
"""

def generate_svg():
    svg = []
    svg_w = 940
    svg_h = 1200
    svg.append(f'<svg viewBox="0 0 {svg_w} {svg_h}" xmlns="http://www.w3.org/2000/svg" font-family="Inter, -apple-system, sans-serif">')
    svg.append('<defs>')
    svg.append('''
      <filter id="shadow" x="-2%" y="-1.5%" width="104%" height="103%">
        <feDropShadow dx="0" dy="1.5" stdDeviation="1.5" flood-opacity="0.06"/>
      </filter>
    ''')
    svg.append('</defs>')

    # Background canvas
    svg.append(f'<rect width="{svg_w}" height="{svg_h}" fill="#ffffff" rx="6"/>')

    # Common horizontal parameters for 2 columns
    col_w = 430
    col1_x = 30
    col2_x = 480

    # Vertical rows
    # Row 1 (Top row · 36m long buildings)
    r1_hdr_y = 10
    r1_y = 36
    r1_h = 712

    # Row 2 (Bottom row · 16m building & References card)
    r2_hdr_y = 780
    r2_y = 806
    r2_h = 372

    # =========================================================================
    # QUADRANT 1: TOP-LEFT · CARPINTERÍA Y ESTRUCTURA (36×9 m)
    # =========================================================================
    # Header
    svg.append(f'''
      <g>
        <rect x="{col1_x}" y="{r1_hdr_y}" width="{col_w}" height="22" rx="3" fill="#1e293b"/>
        <text x="{col1_x + col_w/2}" y="{r1_hdr_y + 15}" fill="#ffffff" font-size="9.5" font-weight="700" text-anchor="middle" letter-spacing="0.5">CARPINTERÍA Y ESTRUCTURA (36×9 m)</text>
      </g>
    ''')

    # Edificio Nave 1
    svg.append(f'''
      <rect x="{col1_x}" y="{r1_y}" width="{col_w}" height="{r1_h}" rx="4" fill="#f8fafc" stroke="#334155" stroke-width="2" filter="url(#shadow)"/>
    ''')

    # Pasillo central franja de circulación Nave 1 (vertical x=col1_x + 155)
    aisle1_x = col1_x + 155
    svg.append(f'''
      <path d="M {aisle1_x} {r1_y + 8} L {aisle1_x} {r1_y + r1_h - 10}" fill="none" stroke="#e2e8f0" stroke-width="18" stroke-linecap="round"/>
      <path d="M {aisle1_x} {r1_y + 8} L {aisle1_x} {r1_y + r1_h - 10}" fill="none" stroke="#94a3b8" stroke-width="1.2" stroke-dasharray="5,4"/>
      
      <!-- Pasillo transversal superior inter-sectores -->
      <path d="M {aisle1_x} {r1_y + 85} L {col1_x + col_w} {r1_y + 85}" fill="none" stroke="#e2e8f0" stroke-width="16"/>
      <path d="M {aisle1_x} {r1_y + 85} L {col1_x + col_w} {r1_y + 85}" fill="none" stroke="#94a3b8" stroke-width="1" stroke-dasharray="4,4"/>

      <!-- Pasillo transversal medio inter-sectores -->
      <path d="M {aisle1_x} {r1_y + 365} L {col1_x + col_w} {r1_y + 365}" fill="none" stroke="#e2e8f0" stroke-width="16"/>
      <path d="M {aisle1_x} {r1_y + 365} L {col1_x + col_w} {r1_y + 365}" fill="none" stroke="#94a3b8" stroke-width="1" stroke-dasharray="4,4"/>
    ''')

    # Puestos Nave 1 (Distribuido verticalmente a lo largo de 712px)
    # 1. Almacén de viruta
    svg.append(f'''
      <rect x="{col1_x + 230}" y="{r1_y + 12}" width="188" height="52" rx="3" fill="#f1f5f9" stroke="#64748b" stroke-width="1.2"/>
      <text x="{col1_x + 324}" y="{r1_y + 35}" font-size="8" font-weight="700" fill="#334155" text-anchor="middle">ALMACÉN DE VIRUTA</text>
      <text x="{col1_x + 324}" y="{r1_y + 50}" font-size="6.5" fill="#64748b" text-anchor="middle">Extracción neumática y silos exteriores</text>
    ''')

    # 2. Lijadora de banda
    svg.append(f'''
      <rect x="{col1_x + 12}" y="{r1_y + 14}" width="125" height="38" rx="2" fill="#fef3c7" stroke="#d97706" stroke-width="1.2"/>
      <text x="{col1_x + 74}" y="{r1_y + 37}" font-size="7.5" font-weight="700" fill="#92400e" text-anchor="middle">LIJADORA DE BANDA</text>
    ''')

    # Almacén MP
    svg.append(f'''
      <rect x="{col1_x + 12}" y="{r1_y + 68}" width="125" height="60" rx="2" fill="#f1f5f9" stroke="#94a3b8" stroke-width="1"/>
      <text x="{col1_x + 74}" y="{r1_y + 96}" font-size="7.5" font-weight="600" fill="#475569" text-anchor="middle">ALMACÉN MP</text>
      <text x="{col1_x + 74}" y="{r1_y + 110}" font-size="6.2" fill="#64748b" text-anchor="middle">Madera noble seleccionada</text>
    ''')

    # 3. Brazo 6 ejes (Robot 4 motores · Fresado 3D)
    svg.append(f'''
      <rect x="{col1_x + 185}" y="{r1_y + 105}" width="135" height="75" rx="3" fill="#e0f2fe" stroke="#0284c7" stroke-width="1.8"/>
      <text x="{col1_x + 252}" y="{r1_y + 138}" font-size="8.5" font-weight="700" fill="#0369a1" text-anchor="middle">BRAZO 6 EJES</text>
      <text x="{col1_x + 252}" y="{r1_y + 154}" font-size="7" fill="#0284c7" text-anchor="middle">(Robot 4 Motores · Fresado 3D)</text>
      <text x="{col1_x + 252}" y="{r1_y + 167}" font-size="6" fill="#0369a1" text-anchor="middle">Mecanizado monocasco Silla Ginger</text>
    ''')

    # Puesto 1: Rectificadora (Badge 1)
    svg.append(f'''
      <rect x="{col1_x + 335}" y="{r1_y + 105}" width="82" height="32" rx="2" fill="#e0f2fe" stroke="#0284c7" stroke-width="1.2"/>
      <circle cx="{col1_x + 352}" cy="{r1_y + 121}" r="7" fill="#0284c7"/>
      <text x="{col1_x + 352}" y="{r1_y + 123.5}" font-size="6.8" font-weight="700" fill="#ffffff" text-anchor="middle">1</text>
      <text x="{col1_x + 384}" y="{r1_y + 123.5}" font-size="6.5" font-weight="600" fill="#0369a1">Rectificadora</text>
    ''')

    # Puesto 2: Cepilladora (Badge 2)
    svg.append(f'''
      <rect x="{col1_x + 335}" y="{r1_y + 145}" width="82" height="35" rx="2" fill="#e0f2fe" stroke="#0284c7" stroke-width="1.2"/>
      <circle cx="{col1_x + 352}" cy="{r1_y + 162}" r="7" fill="#0284c7"/>
      <text x="{col1_x + 352}" y="{r1_y + 164.5}" font-size="6.8" font-weight="700" fill="#ffffff" text-anchor="middle">2</text>
      <text x="{col1_x + 384}" y="{r1_y + 164.5}" font-size="6.5" font-weight="600" fill="#0369a1">Cepilladora</text>
    ''')

    # Puesto 3: Espigadora (Badge 3)
    svg.append(f'''
      <rect x="{col1_x + 12}" y="{r1_y + 145}" width="125" height="35" rx="2" fill="#e0f2fe" stroke="#0284c7" stroke-width="1.2"/>
      <circle cx="{col1_x + 30}" cy="{r1_y + 162}" r="7" fill="#0284c7"/>
      <text x="{col1_x + 30}" y="{r1_y + 164.5}" font-size="6.8" font-weight="700" fill="#ffffff" text-anchor="middle">3</text>
      <text x="{col1_x + 75}" y="{r1_y + 165}" font-size="6.8" font-weight="600" fill="#0369a1">Espigadora</text>
    ''')

    # Almacenamiento intermedio
    svg.append(f'''
      <rect x="{col1_x + 185}" y="{r1_y + 195}" width="135" height="28" rx="2" fill="#f1f5f9" stroke="#94a3b8" stroke-width="1"/>
      <text x="{col1_x + 252}" y="{r1_y + 212}" font-size="6.8" font-weight="600" fill="#475569" text-anchor="middle">Almacenamiento en Proceso</text>
    ''')

    # Puesto 4: Fresadora (Badge 4)
    svg.append(f'''
      <rect x="{col1_x + 12}" y="{r1_y + 195}" width="125" height="35" rx="2" fill="#e0f2fe" stroke="#0284c7" stroke-width="1.2"/>
      <circle cx="{col1_x + 30}" cy="{r1_y + 212}" r="7" fill="#0284c7"/>
      <text x="{col1_x + 30}" y="{r1_y + 214.5}" font-size="6.8" font-weight="700" fill="#ffffff" text-anchor="middle">4</text>
      <text x="{col1_x + 75}" y="{r1_y + 215}" font-size="6.8" font-weight="600" fill="#0369a1">Fresadora tupí</text>
    ''')

    # Puesto 5: Mortajadora (Badge 5)
    svg.append(f'''
      <rect x="{col1_x + 12}" y="{r1_y + 245}" width="125" height="35" rx="2" fill="#e0f2fe" stroke="#0284c7" stroke-width="1.2"/>
      <circle cx="{col1_x + 30}" cy="{r1_y + 262}" r="7" fill="#0284c7"/>
      <text x="{col1_x + 30}" y="{r1_y + 264.5}" font-size="6.8" font-weight="700" fill="#ffffff" text-anchor="middle">5</text>
      <text x="{col1_x + 75}" y="{r1_y + 265}" font-size="6.8" font-weight="600" fill="#0369a1">Mortajadora</text>
    ''')

    # Puesto 6 y 7: Sierras sin fin (Badges 6 y 7)
    svg.append(f'''
      <rect x="{col1_x + 305}" y="{r1_y + 200}" width="112" height="38" rx="2" fill="#e0f2fe" stroke="#0284c7" stroke-width="1.2"/>
      <circle cx="{col1_x + 325}" cy="{r1_y + 219}" r="7" fill="#0284c7"/>
      <text x="{col1_x + 325}" y="{r1_y + 221.5}" font-size="6.8" font-weight="700" fill="#ffffff" text-anchor="middle">6</text>
      <text x="{col1_x + 368}" y="{r1_y + 222}" font-size="6.8" font-weight="600" fill="#0369a1">Sierra sin fin 1</text>

      <rect x="{col1_x + 305}" y="{r1_y + 250}" width="112" height="38" rx="2" fill="#e0f2fe" stroke="#0284c7" stroke-width="1.2"/>
      <circle cx="{col1_x + 325}" cy="{r1_y + 269}" r="7" fill="#0284c7"/>
      <text x="{col1_x + 325}" y="{r1_y + 271.5}" font-size="6.8" font-weight="700" fill="#ffffff" text-anchor="middle">7</text>
      <text x="{col1_x + 368}" y="{r1_y + 272}" font-size="6.8" font-weight="600" fill="#0369a1">Sierra sin fin 2</text>
    ''')

    # Armado Estructura
    svg.append(f'''
      <rect x="{col1_x + 12}" y="{r1_y + 295}" width="125" height="65" rx="3" fill="#dbeafe" stroke="#2563eb" stroke-width="1.5"/>
      <text x="{col1_x + 74}" y="{r1_y + 322}" font-size="8" font-weight="700" fill="#1d4ed8" text-anchor="middle">ARMADO ESTRUCTURA</text>
      <text x="{col1_x + 74}" y="{r1_y + 338}" font-size="6.5" fill="#3b82f6" text-anchor="middle">(Bancos de Encastre y Prensado)</text>
    ''')

    # Sierra Escuadradora
    svg.append(f'''
      <rect x="{col1_x + 205}" y="{r1_y + 380}" width="212" height="65" rx="3" fill="#e0f2fe" stroke="#0284c7" stroke-width="1.5"/>
      <text x="{col1_x + 311}" y="{r1_y + 408}" font-size="8.5" font-weight="700" fill="#0369a1" text-anchor="middle">SIERRA ESCUADRADORA</text>
      <text x="{col1_x + 311}" y="{r1_y + 424}" font-size="6.8" fill="#0284c7" text-anchor="middle">Corte primario de tableros y bastidores</text>
    ''')

    # Almacén madera maciza (lateral largo)
    svg.append(f'''
      <rect x="{col1_x + 12}" y="{r1_y + 380}" width="65" height="175" rx="2" fill="#f1f5f9" stroke="#94a3b8" stroke-width="1"/>
      <text x="{col1_x + 44}" y="{r1_y + 468}" font-size="7.5" font-weight="600" fill="#475569" text-anchor="middle" transform="rotate(-90 {col1_x + 44} {r1_y + 468})">ALMACÉN MADERA MACIZA</text>
    ''')

    # Lijadora plana
    svg.append(f'''
      <rect x="{col1_x + 205}" y="{r1_y + 460}" width="145" height="42" rx="2" fill="#fef3c7" stroke="#d97706" stroke-width="1.2"/>
      <text x="{col1_x + 277}" y="{r1_y + 485}" font-size="7.8" font-weight="700" fill="#92400e" text-anchor="middle">LIJADORA PLANA</text>
    ''')

    # Almacenamiento tablones
    svg.append(f'''
      <rect x="{col1_x + 205}" y="{r1_y + 515}" width="212" height="52" rx="2" fill="#f1f5f9" stroke="#94a3b8" stroke-width="1"/>
      <text x="{col1_x + 311}" y="{r1_y + 538}" font-size="7.8" font-weight="600" fill="#475569" text-anchor="middle">ALMACENAMIENTO DE TABLONES</text>
      <text x="{col1_x + 311}" y="{r1_y + 552}" font-size="6.5" fill="#64748b" text-anchor="middle">Partes pre-mecanizadas listas para armado</text>
    ''')

    # Recepción de materias primas
    svg.append(f'''
      <rect x="{col1_x + 130}" y="{r1_y + 585}" width="288" height="98" rx="3" fill="#e2e8f0" stroke="#64748b" stroke-width="1.4"/>
      <text x="{col1_x + 274}" y="{r1_y + 625}" font-size="9" font-weight="700" fill="#1e293b" text-anchor="middle">RECEPCIÓN DE MATERIAS PRIMAS</text>
      <text x="{col1_x + 274}" y="{r1_y + 642}" font-size="7" fill="#475569" text-anchor="middle">Ingreso Maderas (Misiones) · Descarga, control y pesaje</text>
      <text x="{col1_x + 274}" y="{r1_y + 656}" font-size="6.2" fill="#64748b" text-anchor="middle">Control de humedad y estacionamiento</text>
    ''')

    # Portón Ingreso 1
    svg.append(f'''
      <rect x="{col1_x + 20}" y="{r1_y + r1_h - 18}" width="140" height="18" rx="2" fill="#22c55e"/>
      <text x="{col1_x + 90}" y="{r1_y + r1_h - 5}" font-size="8" font-weight="700" fill="#ffffff" text-anchor="middle">PORTÓN INGRESO 1 ▼</text>
    ''')

    # Cotas 360 y 90
    svg.append(f'''
      <text x="{col1_x - 12}" y="{r1_y + r1_h/2}" font-size="10" font-weight="800" fill="#94a3b8" text-anchor="middle" transform="rotate(-90 {col1_x - 12} {r1_y + r1_h/2})">360 (36 m)</text>
      <text x="{col1_x + col_w/2}" y="{r1_y + r1_h + 15}" font-size="8.5" font-weight="700" fill="#94a3b8" text-anchor="middle">90 (9 m)</text>
    ''')


    # =========================================================================
    # QUADRANT 2: TOP-RIGHT · PRENSADO HF, LAQUEADO Y FINAL (36×9 m)
    # =========================================================================
    # Header
    svg.append(f'''
      <g>
        <rect x="{col2_x}" y="{r1_hdr_y}" width="{col_w}" height="22" rx="3" fill="#1e293b"/>
        <text x="{col2_x + col_w/2}" y="{r1_hdr_y + 15}" fill="#ffffff" font-size="9.5" font-weight="700" text-anchor="middle" letter-spacing="0.5">PRENSADO HF, LAQUEADO Y FINAL (36×9 m)</text>
      </g>
    ''')

    # Edificio Nave 2
    svg.append(f'''
      <rect x="{col2_x}" y="{r1_y}" width="{col_w}" height="{r1_h}" rx="4" fill="#f8fafc" stroke="#334155" stroke-width="2" filter="url(#shadow)"/>
    ''')

    # Pasillo central franja de circulación Nave 2
    aisle2_x = col2_x + 205
    svg.append(f'''
      <path d="M {aisle2_x} {r1_y + 8} L {aisle2_x} {r1_y + r1_h - 10}" fill="none" stroke="#e2e8f0" stroke-width="18" stroke-linecap="round"/>
      <path d="M {aisle2_x} {r1_y + 8} L {aisle2_x} {r1_y + r1_h - 10}" fill="none" stroke="#94a3b8" stroke-width="1.2" stroke-dasharray="5,4"/>
      
      <!-- Pasillo transversal superior inter-sectores -->
      <path d="M {col2_x} {r1_y + 85} L {aisle2_x} {r1_y + 85}" fill="none" stroke="#e2e8f0" stroke-width="16"/>
      <path d="M {col2_x} {r1_y + 85} L {aisle2_x} {r1_y + 85}" fill="none" stroke="#94a3b8" stroke-width="1" stroke-dasharray="4,4"/>

      <!-- Pasillo transversal medio inter-sectores -->
      <path d="M {col2_x} {r1_y + 365} L {aisle2_x} {r1_y + 365}" fill="none" stroke="#e2e8f0" stroke-width="16"/>
      <path d="M {col2_x} {r1_y + 365} L {aisle2_x} {r1_y + 365}" fill="none" stroke="#94a3b8" stroke-width="1" stroke-dasharray="4,4"/>
    ''')

    # Puestos Nave 2 (Distribuido a lo largo de 712px)
    # Curvadoras 1 y 2
    svg.append(f'''
      <rect x="{col2_x + 12}" y="{r1_y + 12}" width="85" height="48" rx="2" fill="#ffedd5" stroke="#ea580c" stroke-width="1.3"/>
      <text x="{col2_x + 54}" y="{r1_y + 40}" font-size="7.5" font-weight="700" fill="#c2410c" text-anchor="middle">Curvadora 1</text>

      <rect x="{col2_x + 12}" y="{r1_y + 68}" width="85" height="48" rx="2" fill="#ffedd5" stroke="#ea580c" stroke-width="1.3"/>
      <text x="{col2_x + 54}" y="{r1_y + 96}" font-size="7.5" font-weight="700" fill="#c2410c" text-anchor="middle">Curvadora 2</text>
    ''')

    # Almacén chapa costurada y racks
    svg.append(f'''
      <rect x="{col2_x + 235}" y="{r1_y + 12}" width="105" height="40" rx="2" fill="#f1f5f9" stroke="#94a3b8" stroke-width="1"/>
      <text x="{col2_x + 287}" y="{r1_y + 30}" font-size="7" font-weight="600" fill="#475569" text-anchor="middle">Almacén Chapa</text>
      <text x="{col2_x + 287}" y="{r1_y + 43}" font-size="6.2" fill="#64748b" text-anchor="middle">Costurada</text>

      <rect x="{col2_x + 352}" y="{r1_y + 12}" width="65" height="75" rx="2" fill="#f1f5f9" stroke="#94a3b8" stroke-width="1"/>
      <text x="{col2_x + 384}" y="{r1_y + 52}" font-size="6.8" font-weight="600" fill="#475569" text-anchor="middle">Racks Chapas</text>
    ''')

    # Puesto 8: Encoladora de rodillos (Badge 8)
    svg.append(f'''
      <rect x="{col2_x + 235}" y="{r1_y + 60}" width="60" height="30" rx="2" fill="#ffedd5" stroke="#ea580c" stroke-width="1.2"/>
      <circle cx="{col2_x + 250}" cy="{r1_y + 75}" r="7" fill="#ea580c"/>
      <text x="{col2_x + 250}" y="{r1_y + 77.5}" font-size="6.8" font-weight="700" fill="#ffffff" text-anchor="middle">8</text>
      <text x="{col2_x + 274}" y="{r1_y + 77.5}" font-size="6.5" font-weight="700" fill="#c2410c">Encol.</text>
    ''')

    # Puesto 9: Aplicador de adhesivo (Badge 9)
    svg.append(f'''
      <rect x="{col2_x + 225}" y="{r1_y + 100}" width="100" height="32" rx="2" fill="#ffedd5" stroke="#ea580c" stroke-width="1.2"/>
      <circle cx="{col2_x + 240}" cy="{r1_y + 116}" r="7" fill="#ea580c"/>
      <text x="{col2_x + 240}" y="{r1_y + 118.5}" font-size="6.8" font-weight="700" fill="#ffffff" text-anchor="middle">9</text>
      <text x="{col2_x + 273}" y="{r1_y + 119}" font-size="6" font-weight="700" fill="#c2410c">Aplicador Adhesivo</text>
    ''')

    # Prensa HF
    svg.append(f'''
      <rect x="{col2_x + 328}" y="{r1_y + 98}" width="90" height="65" rx="3" fill="#ffedd5" stroke="#ea580c" stroke-width="1.8"/>
      <text x="{col2_x + 373}" y="{r1_y + 125}" font-size="8.5" font-weight="700" fill="#c2410c" text-anchor="middle">PRENSA HF</text>
      <text x="{col2_x + 373}" y="{r1_y + 140}" font-size="6.8" font-weight="600" fill="#ea580c" text-anchor="middle">(Curvado 3 min)</text>
      <text x="{col2_x + 373}" y="{r1_y + 152}" font-size="5.8" fill="#c2410c" text-anchor="middle">Dieléctrico alta frecuencia</text>
    ''')

    # Almacén Multilaminados
    svg.append(f'''
      <rect x="{col2_x + 12}" y="{r1_y + 130}" width="165" height="155" rx="3" fill="#f1f5f9" stroke="#94a3b8" stroke-width="1.2"/>
      <text x="{col2_x + 94}" y="{r1_y + 195}" font-size="8.5" font-weight="700" fill="#475569" text-anchor="middle">ALMACÉN</text>
      <text x="{col2_x + 94}" y="{r1_y + 212}" font-size="8.5" font-weight="700" fill="#475569" text-anchor="middle">MULTILAMINADOS</text>
      <text x="{col2_x + 94}" y="{r1_y + 230}" font-size="7" fill="#64748b" text-anchor="middle">Placas Guatambú / Guayica</text>
      <text x="{col2_x + 94}" y="{r1_y + 244}" font-size="6" fill="#94a3b8" text-anchor="middle">Pallets 1,30 × 2,60 m</text>
    ''')

    # Puesto 10: Guillotina de chapa (Badge 10)
    svg.append(f'''
      <rect x="{col2_x + 355}" y="{r1_y + 175}" width="62" height="75" rx="2" fill="#e0f2fe" stroke="#0284c7" stroke-width="1.2"/>
      <circle cx="{col2_x + 374}" cy="{r1_y + 200}" r="7" fill="#0284c7"/>
      <text x="{col2_x + 374}" y="{r1_y + 202.5}" font-size="6.8" font-weight="700" fill="#ffffff" text-anchor="middle">10</text>
      <text x="{col2_x + 386}" y="{r1_y + 225}" font-size="6.5" font-weight="600" fill="#0369a1" text-anchor="middle">Guillotina Madera</text>
    ''')

    # Puesto 11: Costura de chapa (Badge 11)
    svg.append(f'''
      <rect x="{col2_x + 235}" y="{r1_y + 190}" width="112" height="60" rx="2" fill="#e0f2fe" stroke="#0284c7" stroke-width="1.2"/>
      <circle cx="{col2_x + 252}" cy="{r1_y + 215}" r="7" fill="#0284c7"/>
      <text x="{col2_x + 252}" y="{r1_y + 217.5}" font-size="6.8" font-weight="700" fill="#ffffff" text-anchor="middle">11</text>
      <text x="{col2_x + 288}" y="{r1_y + 219}" font-size="6.5" font-weight="600" fill="#0369a1">Costura de Chapa</text>
    ''')

    # Puesto 12: Cabinas Lijado Fino (Badge 12)
    svg.append(f'''
      <rect x="{col2_x + 355}" y="{r1_y + 265}" width="62" height="85" rx="2" fill="#fefce8" stroke="#ca8a04" stroke-width="1.5"/>
      <circle cx="{col2_x + 374}" cy="{r1_y + 290}" r="7" fill="#ca8a04"/>
      <text x="{col2_x + 374}" y="{r1_y + 292.5}" font-size="6.8" font-weight="700" fill="#ffffff" text-anchor="middle">12</text>
      <text x="{col2_x + 386}" y="{r1_y + 312}" font-size="6.5" font-weight="700" fill="#854d0e" text-anchor="middle">Lijado Fino</text>
      <text x="{col2_x + 386}" y="{r1_y + 325}" font-size="5.8" fill="#a16207" text-anchor="middle">(Diego · 0,7 mm)</text>
    ''')

    # Cabina de Pintura y Puesto 13: Montaje Final (Badge 13)
    svg.append(f'''
      <rect x="{col2_x + 12}" y="{r1_y + 300}" width="120" height="90" rx="3" fill="#ede9fe" stroke="#7c3aed" stroke-width="1.6"/>
      <text x="{col2_x + 72}" y="{r1_y + 338}" font-size="8.2" font-weight="700" fill="#5b21b6" text-anchor="middle">CABINA DE PINTURA</text>
      <text x="{col2_x + 72}" y="{r1_y + 354}" font-size="6.5" fill="#7c3aed" text-anchor="middle">(Laca Semimate Soplete)</text>
      <text x="{col2_x + 72}" y="{r1_y + 368}" font-size="5.8" fill="#5b21b6" text-anchor="middle">Cortina y extracción</text>

      <rect x="{col2_x + 138}" y="{r1_y + 300}" width="50" height="55" rx="2" fill="#f0fdf4" stroke="#16a34a" stroke-width="1.4"/>
      <circle cx="{col2_x + 163}" cy="{r1_y + 320}" r="7" fill="#16a34a"/>
      <text x="{col2_x + 163}" y="{r1_y + 322.5}" font-size="6.8" font-weight="700" fill="#ffffff" text-anchor="middle">13</text>
      <text x="{col2_x + 163}" y="{r1_y + 342}" font-size="6.2" font-weight="700" fill="#15803d" text-anchor="middle">Montaje</text>
    ''')

    # Almacenamiento intermedio + ESCALERA
    svg.append(f'''
      <rect x="{col2_x + 235}" y="{r1_y + 365}" width="105" height="55" rx="3" fill="#f1f5f9" stroke="#94a3b8" stroke-width="1"/>
      <text x="{col2_x + 287}" y="{r1_y + 390}" font-size="7.5" font-weight="600" fill="#475569" text-anchor="middle">ALMACENAMIENTO</text>
      <text x="{col2_x + 287}" y="{r1_y + 404}" font-size="6.2" fill="#64748b" text-anchor="middle">Pulido e Insumos</text>

      <rect x="{col2_x + 352}" y="{r1_y + 365}" width="65" height="35" rx="2" fill="#3b82f6"/>
      <text x="{col2_x + 384}" y="{r1_y + 386}" font-size="7.5" font-weight="700" fill="#ffffff" text-anchor="middle">ESCALERA</text>
    ''')

    # Router CNC
    svg.append(f'''
      <rect x="{col2_x + 12}" y="{r1_y + 405}" width="176" height="110" rx="3" fill="#e0f2fe" stroke="#0284c7" stroke-width="1.8"/>
      <text x="{col2_x + 100}" y="{r1_y + 448}" font-size="8.8" font-weight="700" fill="#0369a1" text-anchor="middle">ROUTER CNC (MECANIZADO)</text>
      <text x="{col2_x + 100}" y="{r1_y + 466}" font-size="7.2" fill="#0284c7" text-anchor="middle">Mecanizado Asientos y Piezas Planas</text>
      <text x="{col2_x + 100}" y="{r1_y + 480}" font-size="6.2" fill="#0369a1" text-anchor="middle">Corte de placas curvas y calibración</text>
    ''')

    # Almacenamiento en proceso y Almacén General
    svg.append(f'''
      <rect x="{col2_x + 235}" y="{r1_y + 435}" width="182" height="52" rx="2" fill="#f1f5f9" stroke="#94a3b8" stroke-width="1"/>
      <text x="{col2_x + 326}" y="{r1_y + 462}" font-size="7.5" font-weight="600" fill="#475569" text-anchor="middle">ALMACENAMIENTO EN PROCESO</text>
      <text x="{col2_x + 326}" y="{r1_y + 475}" font-size="6.2" fill="#64748b" text-anchor="middle">Buffer previo a ensamble final</text>

      <rect x="{col2_x + 215}" y="{r1_y + 505}" width="202" height="175" rx="3" fill="#f1f5f9" stroke="#94a3b8" stroke-width="1.2"/>
      <text x="{col2_x + 316}" y="{r1_y + 580}" font-size="9" font-weight="700" fill="#475569" text-anchor="middle">ALMACÉN GENERAL</text>
      <text x="{col2_x + 316}" y="{r1_y + 598}" font-size="7.5" fill="#64748b" text-anchor="middle">Muebles Embalados y Expedición</text>
      <text x="{col2_x + 316}" y="{r1_y + 614}" font-size="6.5" fill="#94a3b8" text-anchor="middle">Control de calidad y embalaje final</text>
    ''')

    # Portones Entrada 2A y 2B
    svg.append(f'''
      <rect x="{col2_x + 15}" y="{r1_y + r1_h - 18}" width="125" height="18" rx="2" fill="#22c55e"/>
      <text x="{col2_x + 77}" y="{r1_y + r1_h - 5}" font-size="8" font-weight="700" fill="#ffffff" text-anchor="middle">PORTÓN 2A ▼</text>

      <rect x="{col2_x + 215}" y="{r1_y + r1_h - 18}" width="145" height="18" rx="2" fill="#22c55e"/>
      <text x="{col2_x + 287}" y="{r1_y + r1_h - 5}" font-size="8" font-weight="700" fill="#ffffff" text-anchor="middle">PORTÓN EXPEDICIÓN 2B ▼</text>
    ''')

    # Cotas 360 y 90 Nave 2
    svg.append(f'''
      <text x="{col2_x + col_w + 12}" y="{r1_y + r1_h/2}" font-size="10" font-weight="800" fill="#94a3b8" text-anchor="middle" transform="rotate(90 {col2_x + col_w + 12} {r1_y + r1_h/2})">360 (36 m)</text>
      <text x="{col2_x + col_w/2}" y="{r1_y + r1_h + 15}" font-size="8.5" font-weight="700" fill="#94a3b8" text-anchor="middle">90 (9 m)</text>
    ''')


    # =========================================================================
    # QUADRANT 3: BOTTOM-LEFT · PLANTA ALTA · TAPICERÍA Y LÁSER (16×9 m)
    # =========================================================================
    # Header
    svg.append(f'''
      <g>
        <rect x="{col1_x}" y="{r2_hdr_y}" width="{col_w}" height="22" rx="3" fill="#1e293b"/>
        <text x="{col1_x + col_w/2}" y="{r2_hdr_y + 15}" fill="#ffffff" font-size="9.5" font-weight="700" text-anchor="middle" letter-spacing="0.5">PLANTA ALTA · TAPICERÍA Y CORTE LÁSER (16×9 m)</text>
      </g>
    ''')

    # Edificio Entrepiso (height = 372px)
    svg.append(f'''
      <rect x="{col1_x}" y="{r2_y}" width="{col_w}" height="{r2_h}" rx="4" fill="#f8fafc" stroke="#334155" stroke-width="2" filter="url(#shadow)"/>
    ''')

    # Pasillo central entrepiso
    aisle3_x = col1_x + 195
    svg.append(f'''
      <path d="M {aisle3_x} {r2_y + 8} L {aisle3_x} {r2_y + r2_h - 45} L {aisle3_x + 130} {r2_y + r2_h - 45} L {aisle3_x + 130} {r2_y + r2_h - 12}" fill="none" stroke="#e2e8f0" stroke-width="18" stroke-linecap="round"/>
      <path d="M {aisle3_x} {r2_y + 8} L {aisle3_x} {r2_y + r2_h - 45} L {aisle3_x + 130} {r2_y + r2_h - 45} L {aisle3_x + 130} {r2_y + r2_h - 12}" fill="none" stroke="#94a3b8" stroke-width="1.2" stroke-dasharray="5,4"/>
    ''')

    # Almacén de telas
    svg.append(f'''
      <rect x="{col1_x + 115}" y="{r2_y + 14}" width="165" height="48" rx="2" fill="#f1f5f9" stroke="#94a3b8" stroke-width="1"/>
      <text x="{col1_x + 197}" y="{r2_y + 36}" font-size="8" font-weight="600" fill="#475569" text-anchor="middle">ALMACÉN DE TELAS</text>
      <text x="{col1_x + 197}" y="{r2_y + 51}" font-size="6.5" fill="#64748b" text-anchor="middle">Bobinas y Rollos Textiles</text>
    ''')

    # Racks espumas lateral derecho
    svg.append(f'''
      <rect x="{col1_x + 355}" y="{r2_y + 14}" width="65" height="190" rx="2" fill="#f1f5f9" stroke="#94a3b8" stroke-width="1"/>
      <text x="{col1_x + 387}" y="{r2_y + 110}" font-size="7.5" font-weight="600" fill="#475569" text-anchor="middle" transform="rotate(90 {col1_x + 387} {r2_y + 110})">RACKS DE ESPUMAS</text>
    ''')

    # Corte Láser y Puesto 15: Mesa Despiece (Badge 15)
    svg.append(f'''
      <rect x="{col1_x + 225}" y="{r2_y + 80}" width="120" height="65" rx="3" fill="#dcfce7" stroke="#16a34a" stroke-width="1.6"/>
      <text x="{col1_x + 285}" y="{r2_y + 108}" font-size="8.2" font-weight="700" fill="#15803d" text-anchor="middle">CORTE LÁSER TEXTIL</text>
      <text x="{col1_x + 285}" y="{r2_y + 125}" font-size="6.5" fill="#16a34a" text-anchor="middle">Mesa CNC Automatizada</text>

      <rect x="{col1_x + 225}" y="{r2_y + 158}" width="120" height="38" rx="2" fill="#f1f5f9" stroke="#94a3b8" stroke-width="1"/>
      <circle cx="{col1_x + 245}" cy="{r2_y + 177}" r="7" fill="#64748b"/>
      <text x="{col1_x + 245}" y="{r2_y + 179.5}" font-size="6.8" font-weight="700" fill="#ffffff" text-anchor="middle">15</text>
      <text x="{col1_x + 292}" y="{r2_y + 180}" font-size="6.8" font-weight="600" fill="#475569">Mesa Despiece</text>
    ''')

    # Puesto 14: Montaje Espuma y Tela (Badge 14)
    svg.append(f'''
      <rect x="{col1_x + 12}" y="{r2_y + 80}" width="168" height="70" rx="2" fill="#dcfce7" stroke="#16a34a" stroke-width="1.4"/>
      <circle cx="{col1_x + 32}" cy="{r2_y + 115}" r="7.5" fill="#16a34a"/>
      <text x="{col1_x + 32}" y="{r2_y + 117.5}" font-size="6.8" font-weight="700" fill="#ffffff" text-anchor="middle">14</text>
      <text x="{col1_x + 105}" y="{r2_y + 108}" font-size="7.5" font-weight="700" fill="#15803d" text-anchor="middle">MONTAJE ESPUMA Y TELA</text>
      <text x="{col1_x + 105}" y="{r2_y + 124}" font-size="6.2" fill="#16a34a" text-anchor="middle">Engrapado y confección de fundas</text>
    ''')

    # Almacén partes tapizadas
    svg.append(f'''
      <rect x="{col1_x + 12}" y="{r2_y + 168}" width="168" height="110" rx="2" fill="#f1f5f9" stroke="#94a3b8" stroke-width="1"/>
      <text x="{col1_x + 96}" y="{r2_y + 215}" font-size="8" font-weight="600" fill="#475569" text-anchor="middle">ALMACÉN PARTES TAPIZADAS</text>
      <text x="{col1_x + 96}" y="{r2_y + 232}" font-size="6.8" fill="#64748b" text-anchor="middle">Asientos y respaldos listos</text>
      <text x="{col1_x + 96}" y="{r2_y + 246}" font-size="6" fill="#94a3b8" text-anchor="middle">Buffer para ensamble final</text>
    ''')

    # Apertura Clark y Escalera Entrepiso
    svg.append(f'''
      <rect x="{col1_x + 165}" y="{r2_y + r2_h - 32}" width="155" height="26" rx="2" fill="#fef3c7" stroke="#f59e0b" stroke-width="1.4" stroke-dasharray="3,3"/>
      <text x="{col1_x + 242}" y="{r2_y + r2_h - 15}" font-size="7.5" font-weight="700" fill="#b45309" text-anchor="middle">APERTURA PARA CLARK / ELEVADOR</text>

      <rect x="{col1_x + 330}" y="{r2_y + r2_h - 32}" width="90" height="26" rx="2" fill="#3b82f6"/>
      <text x="{col1_x + 375}" y="{r2_y + r2_h - 15}" font-size="7.5" font-weight="700" fill="#ffffff" text-anchor="middle">ESCALERA</text>
    ''')

    # Cotas 160 y 90
    svg.append(f'''
      <text x="{col1_x - 12}" y="{r2_y + r2_h/2}" font-size="10" font-weight="800" fill="#94a3b8" text-anchor="middle" transform="rotate(-90 {col1_x - 12} {r2_y + r2_h/2})">160 (16 m)</text>
      <text x="{col1_x + col_w/2}" y="{r2_y + r2_h + 15}" font-size="8.5" font-weight="700" fill="#94a3b8" text-anchor="middle">90 (9 m)</text>
    ''')


    # =========================================================================
    # QUADRANT 4: BOTTOM-RIGHT · CUADRO DE REFERENCIAS DE PLANTA Y PUESTOS
    # =========================================================================
    # Header
    svg.append(f'''
      <g>
        <rect x="{col2_x}" y="{r2_hdr_y}" width="{col_w}" height="22" rx="3" fill="#1e293b"/>
        <text x="{col2_x + col_w/2}" y="{r2_hdr_y + 15}" fill="#ffffff" font-size="9.5" font-weight="700" text-anchor="middle" letter-spacing="0.5">REFERENCIAS DE PLANTA Y PUESTOS</text>
      </g>
    ''')

    # Panel principal de referencias (height = 372px)
    svg.append(f'''
      <rect x="{col2_x}" y="{r2_y}" width="{col_w}" height="{r2_h}" rx="4" fill="#ffffff" stroke="#cbd5e1" stroke-width="1.5" filter="url(#shadow)"/>
    ''')

    # 1. CÓDIGO DE SECTORES (ZONAS) (Parte superior del panel, width = col_w - 28)
    sec_x = col2_x + 14
    sec_y = r2_y + 14
    svg.append(f'''
      <text x="{sec_x}" y="{sec_y + 6}" font-size="8" font-weight="700" fill="#0f172a">1. CÓDIGO DE SECTORES FUNCIONALES:</text>
      
      <g transform="translate({sec_x}, {sec_y + 16})">
        <!-- Fila 1: Prensas HF y Mecanizado -->
        <rect x="0" y="0" width="12" height="12" rx="2" fill="#ffedd5" stroke="#ea580c"/>
        <text x="18" y="10" font-size="7" fill="#334155">Curvado y Prensas Alta Frecuencia (HF)</text>

        <rect x="210" y="0" width="12" height="12" rx="2" fill="#e0f2fe" stroke="#0284c7"/>
        <text x="228" y="10" font-size="7" fill="#334155">Mecanizado CNC / Carpintería</text>

        <!-- Fila 2: Cabina Pintura y Corte Láser -->
        <rect x="0" y="18" width="12" height="12" rx="2" fill="#ede9fe" stroke="#7c3aed"/>
        <text x="18" y="28" font-size="7" fill="#334155">Cabina de Laqueado y Lijado Fino</text>

        <rect x="210" y="18" width="12" height="12" rx="2" fill="#dcfce7" stroke="#16a34a"/>
        <text x="228" y="28" font-size="7" fill="#334155">Corte Láser Textil y Tapicería</text>

        <!-- Fila 3: Almacenamiento -->
        <rect x="0" y="36" width="12" height="12" rx="2" fill="#f1f5f9" stroke="#94a3b8"/>
        <text x="18" y="46" font-size="7" fill="#334155">Almacenamiento e Inventarios en Proceso</text>
      </g>

      <!-- Línea divisoria sobria -->
      <line x1="{sec_x}" y1="{sec_y + 74}" x2="{col2_x + col_w - 14}" y2="{sec_y + 74}" stroke="#e2e8f0" stroke-width="1"/>
    ''')

    # 2. PUESTOS NUMERADOS (1 al 15) (Parte media del panel)
    p2_y = sec_y + 90
    svg.append(f'''
      <text x="{sec_x}" y="{p2_y}" font-size="8" font-weight="700" fill="#0f172a">2. PUESTOS Y MÁQUINAS REFERENCIADAS EN PLANO:</text>
    ''')

    # Subcolumna A (1 al 8) y Subcolumna B (9 al 15)
    colA_x = sec_x + 6
    colB_x = sec_x + 205
    start_p_y = p2_y + 18
    p_gap = 18

    puestos = [
        # Columna A (1 al 8)
        (1, "Rectificadora de cantos", "#0284c7", colA_x, start_p_y + 0*p_gap),
        (2, "Cepilladora mecánica", "#0284c7", colA_x, start_p_y + 1*p_gap),
        (3, "Espigadora de estructura", "#0284c7", colA_x, start_p_y + 2*p_gap),
        (4, "Fresadora tupí vertical", "#0284c7", colA_x, start_p_y + 3*p_gap),
        (5, "Mortajadora de cadena", "#0284c7", colA_x, start_p_y + 4*p_gap),
        (6, "Sierra sin fin 1 (desbaste)", "#0284c7", colA_x, start_p_y + 5*p_gap),
        (7, "Sierra sin fin 2 (corte fino)", "#0284c7", colA_x, start_p_y + 6*p_gap),
        (8, "Encoladora de rodillos", "#ea580c", colA_x, start_p_y + 7*p_gap),

        # Columna B (9 al 15)
        (9, "Aplicador de adhesivo", "#ea580c", colB_x, start_p_y + 0*p_gap),
        (10, "Guillotina de chapas", "#0284c7", colB_x, start_p_y + 1*p_gap),
        (11, "Costura de chapa noble", "#0284c7", colB_x, start_p_y + 2*p_gap),
        (12, "Lijado fino (Diego · 0,7mm)", "#ca8a04", colB_x, start_p_y + 3*p_gap),
        (13, "Montaje y ensamble final", "#16a34a", colB_x, start_p_y + 4*p_gap),
        (14, "Montaje de espuma y tela", "#16a34a", colB_x, start_p_y + 5*p_gap),
        (15, "Mesa de despiece textil", "#64748b", colB_x, start_p_y + 6*p_gap),
    ]

    for num, name, color, px, py in puestos:
        svg.append(f'''
          <circle cx="{px + 6}" cy="{py}" r="6.5" fill="{color}"/>
          <text x="{px + 6}" y="{py + 2.4}" font-size="6.2" font-weight="700" fill="#ffffff" text-anchor="middle">{num}</text>
          <text x="{px + 18}" y="{py + 2.8}" font-size="7" font-weight="600" fill="#334155">{name}</text>
        ''')

    # Ficha Técnica de Síntesis al pie del Cuadro de Referencias
    note_y = start_p_y + 8*p_gap + 8
    svg.append(f'''
      <rect x="{sec_x}" y="{note_y}" width="{col_w - 28}" height="38" rx="3" fill="#f8fafc" stroke="#e2e8f0"/>
      <text x="{sec_x + 10}" y="{note_y + 14}" font-size="7" font-weight="700" fill="#1e293b">FICHA TÉCNICA DE PLANTA (GRAN SASSO S.R.L.):</text>
      <text x="{sec_x + 10}" y="{note_y + 25}" font-size="6.2" fill="#475569">· Bouchard 3870, Villa Lynch · Sup. PB: 648 m² (2 naves 36×9m) · Entrepiso: 144 m² (16×9m)</text>
      <text x="{sec_x + 10}" y="{note_y + 34}" font-size="6.2" font-weight="600" fill="#0284c7">· Superficie total: ~792 m² cubiertos · Relevamiento y planimetría a escala técnica</text>
    ''')

    svg.append('</svg>')
    return '\n'.join(svg)

if __name__ == '__main__':
    content = generate_svg()
    with open('assets/layout_oficial_planta.svg', 'w', encoding='utf-8') as f:
        f.write(content)
    print("assets/layout_oficial_planta.svg full-page 2x2 layout generated successfully!")

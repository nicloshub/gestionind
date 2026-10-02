# -*- coding: utf-8 -*-
"""
Script to generate the 2x2 layout SVG for Gran Sasso S.R.L.:
- Top-Left: Carpintería y Estructura (Nave 1, 36x9m)
- Top-Right: Prensado HF, Laqueado y Final (Nave 2, 36x9m)
- Bottom-Left: Planta Alta · Tapicería y Láser (16x9m, "el chico")
- Bottom-Right: Cuadro de Referencias de Planta y Puestos ("a la derecha del chico")
All elements are significantly larger, wider (425px vs 260px), and perfectly legible.
"""

def generate_svg():
    svg = []
    svg_w = 940
    svg_h = 782
    svg.append(f'<svg viewBox="0 0 {svg_w} {svg_h}" xmlns="http://www.w3.org/2000/svg" font-family="Inter, -apple-system, sans-serif">')
    svg.append('<defs>')
    svg.append('''
      <filter id="shadow" x="-2%" y="-2%" width="104%" height="104%">
        <feDropShadow dx="0" dy="1.5" stdDeviation="1.5" flood-opacity="0.06"/>
      </filter>
    ''')
    svg.append('</defs>')

    # Background canvas
    svg.append(f'<rect width="{svg_w}" height="{svg_h}" fill="#ffffff" rx="6"/>')

    # Common dimensions for 2-column grid
    col_w = 430
    col1_x = 30
    col2_x = 480

    # Row 1 (Top): Height for 36m buildings
    r1_y = 38
    r1_h = 440

    # Row 2 (Bottom): Height for 16m building & References card
    r2_y = 525
    r2_h = 230

    # =========================================================================
    # QUADRANT 1: TOP-LEFT · CARPINTERÍA Y ESTRUCTURA (36×9 m)
    # =========================================================================
    # Header
    svg.append(f'''
      <g>
        <rect x="{col1_x}" y="10" width="{col_w}" height="22" rx="3" fill="#1e293b"/>
        <text x="{col1_x + col_w/2}" y="25" fill="#ffffff" font-size="9.5" font-weight="700" text-anchor="middle" letter-spacing="0.5">CARPINTERÍA Y ESTRUCTURA (36×9 m)</text>
      </g>
    ''')

    # Edificio Nave 1
    svg.append(f'''
      <rect x="{col1_x}" y="{r1_y}" width="{col_w}" height="{r1_h}" rx="4" fill="#f8fafc" stroke="#334155" stroke-width="2" filter="url(#shadow)"/>
    ''')

    # Pasillo central franja de circulación Nave 1 (vertical x=col1_x + 140)
    aisle1_x = col1_x + 130
    svg.append(f'''
      <path d="M {aisle1_x} {r1_y + 8} L {aisle1_x} {r1_y + r1_h - 10}" fill="none" stroke="#e2e8f0" stroke-width="16" stroke-linecap="round"/>
      <path d="M {aisle1_x} {r1_y + 8} L {aisle1_x} {r1_y + r1_h - 10}" fill="none" stroke="#94a3b8" stroke-width="1.2" stroke-dasharray="5,4"/>
      
      <!-- Pasillo transversal superior inter-sectores -->
      <path d="M {aisle1_x} {r1_y + 50} L {col1_x + col_w} {r1_y + 50}" fill="none" stroke="#e2e8f0" stroke-width="14"/>
      <path d="M {aisle1_x} {r1_y + 50} L {col1_x + col_w} {r1_y + 50}" fill="none" stroke="#94a3b8" stroke-width="1" stroke-dasharray="4,4"/>

      <!-- Pasillo transversal medio inter-sectores -->
      <path d="M {aisle1_x} {r1_y + 225} L {col1_x + col_w} {r1_y + 225}" fill="none" stroke="#e2e8f0" stroke-width="14"/>
      <path d="M {aisle1_x} {r1_y + 225} L {col1_x + col_w} {r1_y + 225}" fill="none" stroke="#94a3b8" stroke-width="1" stroke-dasharray="4,4"/>
    ''')

    # Puestos Nave 1
    # 1. Almacén de viruta
    svg.append(f'''
      <rect x="{col1_x + 230}" y="{r1_y + 8}" width="188" height="34" rx="3" fill="#f1f5f9" stroke="#64748b" stroke-width="1.2"/>
      <text x="{col1_x + 324}" y="{r1_y + 24}" font-size="7.5" font-weight="700" fill="#334155" text-anchor="middle">ALMACÉN DE VIRUTA</text>
      <text x="{col1_x + 324}" y="{r1_y + 35}" font-size="6" fill="#64748b" text-anchor="middle">Extracción neumática y silos</text>
    ''')

    # 2. Lijadora de banda
    svg.append(f'''
      <rect x="{col1_x + 10}" y="{r1_y + 12}" width="105" height="24" rx="2" fill="#fef3c7" stroke="#d97706" stroke-width="1.2"/>
      <text x="{col1_x + 62}" y="{r1_y + 27}" font-size="7.2" font-weight="700" fill="#92400e" text-anchor="middle">LIJADORA DE BANDA</text>
    ''')

    # 3. Brazo 6 ejes (Robot 4 motores)
    svg.append(f'''
      <rect x="{col1_x + 155}" y="{r1_y + 60}" width="125" height="48" rx="3" fill="#e0f2fe" stroke="#0284c7" stroke-width="1.8"/>
      <text x="{col1_x + 217}" y="{r1_y + 82}" font-size="8" font-weight="700" fill="#0369a1" text-anchor="middle">BRAZO 6 EJES</text>
      <text x="{col1_x + 217}" y="{r1_y + 95}" font-size="6.5" fill="#0284c7" text-anchor="middle">(Robot 4 Motores · Fresado 3D)</text>
    ''')

    # Puesto 1: Rectificadora (Badge 1)
    svg.append(f'''
      <rect x="{col1_x + 290}" y="{r1_y + 62}" width="75" height="20" rx="2" fill="#e0f2fe" stroke="#0284c7" stroke-width="1.2"/>
      <circle cx="{col1_x + 305}" cy="{r1_y + 72}" r="6.5" fill="#0284c7"/>
      <text x="{col1_x + 305}" y="{r1_y + 74.5}" font-size="6.5" font-weight="700" fill="#ffffff" text-anchor="middle">1</text>
      <text x="{col1_x + 338}" y="{r1_y + 74.5}" font-size="6" font-weight="600" fill="#0369a1">Rectificadora</text>
    ''')

    # Puesto 2: Cepilladora (Badge 2)
    svg.append(f'''
      <rect x="{col1_x + 372}" y="{r1_y + 62}" width="46" height="44" rx="2" fill="#e0f2fe" stroke="#0284c7" stroke-width="1.2"/>
      <circle cx="{col1_x + 395}" cy="{r1_y + 76}" r="6.5" fill="#0284c7"/>
      <text x="{col1_x + 395}" y="{r1_y + 78.5}" font-size="6.5" font-weight="700" fill="#ffffff" text-anchor="middle">2</text>
      <text x="{col1_x + 395}" y="{r1_y + 94}" font-size="5.8" font-weight="600" fill="#0369a1" text-anchor="middle">Cepilladora</text>
    ''')

    # Almacén MP
    svg.append(f'''
      <rect x="{col1_x + 10}" y="{r1_y + 48}" width="105" height="42" rx="2" fill="#f1f5f9" stroke="#94a3b8" stroke-width="1"/>
      <text x="{col1_x + 62}" y="{r1_y + 68}" font-size="6.8" font-weight="600" fill="#475569" text-anchor="middle">Almacén MP</text>
      <text x="{col1_x + 62}" y="{r1_y + 79}" font-size="5.8" fill="#64748b" text-anchor="middle">Madera seleccionada</text>
    ''')

    # Puesto 3: Espigadora (Badge 3)
    svg.append(f'''
      <rect x="{col1_x + 10}" y="{r1_y + 100}" width="85" height="24" rx="2" fill="#e0f2fe" stroke="#0284c7" stroke-width="1.2"/>
      <circle cx="{col1_x + 24}" cy="{r1_y + 112}" r="6.5" fill="#0284c7"/>
      <text x="{col1_x + 24}" y="{r1_y + 114.5}" font-size="6.5" font-weight="700" fill="#ffffff" text-anchor="middle">3</text>
      <text x="{col1_x + 55}" y="{r1_y + 114.5}" font-size="6.2" font-weight="600" fill="#0369a1">Espigadora</text>
    ''')

    # Almacenamiento intermedio
    svg.append(f'''
      <rect x="{col1_x + 155}" y="{r1_y + 120}" width="125" height="18" rx="2" fill="#f1f5f9" stroke="#94a3b8" stroke-width="1"/>
      <text x="{col1_x + 217}" y="{r1_y + 132}" font-size="6.2" font-weight="600" fill="#475569" text-anchor="middle">Almacenamiento en Proceso</text>
    ''')

    # Puesto 4: Fresadora (Badge 4)
    svg.append(f'''
      <rect x="{col1_x + 10}" y="{r1_y + 132}" width="85" height="22" rx="2" fill="#e0f2fe" stroke="#0284c7" stroke-width="1.2"/>
      <circle cx="{col1_x + 24}" cy="{r1_y + 143}" r="6.5" fill="#0284c7"/>
      <text x="{col1_x + 24}" y="{r1_y + 145.5}" font-size="6.5" font-weight="700" fill="#ffffff" text-anchor="middle">4</text>
      <text x="{col1_x + 55}" y="{r1_y + 145.5}" font-size="6.2" font-weight="600" fill="#0369a1">Fresadora tupí</text>
    ''')

    # Puesto 5: Mortajadora (Badge 5)
    svg.append(f'''
      <rect x="{col1_x + 10}" y="{r1_y + 160}" width="85" height="22" rx="2" fill="#e0f2fe" stroke="#0284c7" stroke-width="1.2"/>
      <circle cx="{col1_x + 24}" cy="{r1_y + 171}" r="6.5" fill="#0284c7"/>
      <text x="{col1_x + 24}" y="{r1_y + 173.5}" font-size="6.5" font-weight="700" fill="#ffffff" text-anchor="middle">5</text>
      <text x="{col1_x + 55}" y="{r1_y + 173.5}" font-size="6.2" font-weight="600" fill="#0369a1">Mortajadora</text>
    ''')

    # Puesto 6 y 7: Sierras sin fin (Badges 6 y 7)
    svg.append(f'''
      <rect x="{col1_x + 305}" y="{r1_y + 120}" width="112" height="26" rx="2" fill="#e0f2fe" stroke="#0284c7" stroke-width="1.2"/>
      <circle cx="{col1_x + 322}" cy="{r1_y + 133}" r="6.5" fill="#0284c7"/>
      <text x="{col1_x + 322}" y="{r1_y + 135.5}" font-size="6.5" font-weight="700" fill="#ffffff" text-anchor="middle">6</text>
      <text x="{col1_x + 365}" y="{r1_y + 135.5}" font-size="6.2" font-weight="600" fill="#0369a1">Sierra sin fin 1</text>

      <rect x="{col1_x + 305}" y="{r1_y + 154}" width="112" height="26" rx="2" fill="#e0f2fe" stroke="#0284c7" stroke-width="1.2"/>
      <circle cx="{col1_x + 322}" cy="{r1_y + 167}" r="6.5" fill="#0284c7"/>
      <text x="{col1_x + 322}" y="{r1_y + 169.5}" font-size="6.5" font-weight="700" fill="#ffffff" text-anchor="middle">7</text>
      <text x="{col1_x + 365}" y="{r1_y + 169.5}" font-size="6.2" font-weight="600" fill="#0369a1">Sierra sin fin 2</text>
    ''')

    # Armado Estructura
    svg.append(f'''
      <rect x="{col1_x + 10}" y="{r1_y + 192}" width="105" height="45" rx="3" fill="#dbeafe" stroke="#2563eb" stroke-width="1.5"/>
      <text x="{col1_x + 62}" y="{r1_y + 210}" font-size="7.5" font-weight="700" fill="#1d4ed8" text-anchor="middle">ARMADO ESTRUCTURA</text>
      <text x="{col1_x + 62}" y="{r1_y + 224}" font-size="6.2" fill="#3b82f6" text-anchor="middle">(Bancos de Encastre y Prensado)</text>
    ''')

    # Sierra Escuadradora
    svg.append(f'''
      <rect x="{col1_x + 230}" y="{r1_y + 235}" width="188" height="42" rx="3" fill="#e0f2fe" stroke="#0284c7" stroke-width="1.5"/>
      <text x="{col1_x + 324}" y="{r1_y + 254}" font-size="7.8" font-weight="700" fill="#0369a1" text-anchor="middle">SIERRA ESCUADRADORA</text>
      <text x="{col1_x + 324}" y="{r1_y + 267}" font-size="6.2" fill="#0284c7" text-anchor="middle">Corte primario de tableros y bastidores</text>
    ''')

    # Almacén madera maciza
    svg.append(f'''
      <rect x="{col1_x + 10}" y="{r1_y + 248}" width="50" height="95" rx="2" fill="#f1f5f9" stroke="#94a3b8" stroke-width="1"/>
      <text x="{col1_x + 35}" y="{r1_y + 295}" font-size="6.8" font-weight="600" fill="#475569" text-anchor="middle" transform="rotate(-90 {col1_x + 35} {r1_y + 295})">MADERA MACIZA</text>
    ''')

    # Lijadora plana
    svg.append(f'''
      <rect x="{col1_x + 230}" y="{r1_y + 285}" width="115" height="26" rx="2" fill="#fef3c7" stroke="#d97706" stroke-width="1.2"/>
      <text x="{col1_x + 287}" y="{r1_y + 301}" font-size="7" font-weight="700" fill="#92400e" text-anchor="middle">LIJADORA PLANA</text>
    ''')

    # Almacenamiento tablones
    svg.append(f'''
      <rect x="{col1_x + 230}" y="{r1_y + 318}" width="188" height="38" rx="2" fill="#f1f5f9" stroke="#94a3b8" stroke-width="1"/>
      <text x="{col1_x + 324}" y="{r1_y + 334}" font-size="7.2" font-weight="600" fill="#475569" text-anchor="middle">ALMACENAMIENTO</text>
      <text x="{col1_x + 324}" y="{r1_y + 346}" font-size="6" fill="#64748b" text-anchor="middle">Tablones y Partes Pre-Mecanizadas</text>
    ''')

    # Recepción
    svg.append(f'''
      <rect x="{col1_x + 160}" y="{r1_y + 365}" width="258" height="60" rx="3" fill="#e2e8f0" stroke="#64748b" stroke-width="1.4"/>
      <text x="{col1_x + 289}" y="{r1_y + 392}" font-size="8.5" font-weight="700" fill="#1e293b" text-anchor="middle">RECEPCIÓN DE MATERIAS PRIMAS</text>
      <text x="{col1_x + 289}" y="{r1_y + 406}" font-size="6.5" fill="#475569" text-anchor="middle">Ingreso Maderas · Control de humedad y pesaje</text>
    ''')

    # Portón Entrada 1
    svg.append(f'''
      <rect x="{col1_x + 20}" y="{r1_y + r1_h - 14}" width="120" height="14" rx="2" fill="#22c55e"/>
      <text x="{col1_x + 80}" y="{r1_y + r1_h - 4}" font-size="7.5" font-weight="700" fill="#ffffff" text-anchor="middle">PORTÓN INGRESO 1 ▼</text>
    ''')

    # Cotas 360 y 90
    svg.append(f'''
      <text x="{col1_x - 12}" y="{r1_y + r1_h/2}" font-size="9" font-weight="800" fill="#94a3b8" text-anchor="middle" transform="rotate(-90 {col1_x - 12} {r1_y + r1_h/2})">360 (36 m)</text>
      <text x="{col1_x + col_w/2}" y="{r1_y + r1_h + 14}" font-size="8" font-weight="700" fill="#94a3b8" text-anchor="middle">90 (9 m)</text>
    ''')


    # =========================================================================
    # QUADRANT 2: TOP-RIGHT · PRENSADO HF, LAQUEADO Y FINAL (36×9 m)
    # =========================================================================
    # Header
    svg.append(f'''
      <g>
        <rect x="{col2_x}" y="10" width="{col_w}" height="22" rx="3" fill="#1e293b"/>
        <text x="{col2_x + col_w/2}" y="25" fill="#ffffff" font-size="9.5" font-weight="700" text-anchor="middle" letter-spacing="0.5">PRENSADO HF, LAQUEADO Y FINAL (36×9 m)</text>
      </g>
    ''')

    # Edificio Nave 2
    svg.append(f'''
      <rect x="{col2_x}" y="{r1_y}" width="{col_w}" height="{r1_h}" rx="4" fill="#f8fafc" stroke="#334155" stroke-width="2" filter="url(#shadow)"/>
    ''')

    # Pasillo central franja de circulación Nave 2
    aisle2_x = col2_x + 195
    svg.append(f'''
      <path d="M {aisle2_x} {r1_y + 8} L {aisle2_x} {r1_y + r1_h - 10}" fill="none" stroke="#e2e8f0" stroke-width="16" stroke-linecap="round"/>
      <path d="M {aisle2_x} {r1_y + 8} L {aisle2_x} {r1_y + r1_h - 10}" fill="none" stroke="#94a3b8" stroke-width="1.2" stroke-dasharray="5,4"/>
      
      <!-- Pasillo transversal superior inter-sectores -->
      <path d="M {col2_x} {r1_y + 50} L {aisle2_x} {r1_y + 50}" fill="none" stroke="#e2e8f0" stroke-width="14"/>
      <path d="M {col2_x} {r1_y + 50} L {aisle2_x} {r1_y + 50}" fill="none" stroke="#94a3b8" stroke-width="1" stroke-dasharray="4,4"/>

      <!-- Pasillo transversal medio inter-sectores -->
      <path d="M {col2_x} {r1_y + 225} L {aisle2_x} {r1_y + 225}" fill="none" stroke="#e2e8f0" stroke-width="14"/>
      <path d="M {col2_x} {r1_y + 225} L {aisle2_x} {r1_y + 225}" fill="none" stroke="#94a3b8" stroke-width="1" stroke-dasharray="4,4"/>
    ''')

    # Curvadoras 1 y 2
    svg.append(f'''
      <rect x="{col2_x + 10}" y="{r1_y + 8}" width="65" height="32" rx="2" fill="#ffedd5" stroke="#ea580c" stroke-width="1.3"/>
      <text x="{col2_x + 42}" y="{r1_y + 27}" font-size="6.8" font-weight="700" fill="#c2410c" text-anchor="middle">Curvadora 1</text>

      <rect x="{col2_x + 10}" y="{r1_y + 46}" width="65" height="32" rx="2" fill="#ffedd5" stroke="#ea580c" stroke-width="1.3"/>
      <text x="{col2_x + 42}" y="{r1_y + 65}" font-size="6.8" font-weight="700" fill="#c2410c" text-anchor="middle">Curvadora 2</text>
    ''')

    # Almacén chapa costurada y racks
    svg.append(f'''
      <rect x="{col2_x + 230}" y="{r1_y + 8}" width="105" height="28" rx="2" fill="#f1f5f9" stroke="#94a3b8" stroke-width="1"/>
      <text x="{col2_x + 282}" y="{r1_y + 25}" font-size="6.5" font-weight="600" fill="#475569" text-anchor="middle">Almacén Chapa Costurada</text>

      <rect x="{col2_x + 350}" y="{r1_y + 8}" width="68" height="55" rx="2" fill="#f1f5f9" stroke="#94a3b8" stroke-width="1"/>
      <text x="{col2_x + 384}" y="{r1_y + 38}" font-size="6.5" font-weight="600" fill="#475569" text-anchor="middle">Racks Chapas</text>
    ''')

    # Puesto 8: Encoladora de rodillos (Badge 8)
    svg.append(f'''
      <rect x="{col2_x + 230}" y="{r1_y + 42}" width="54" height="24" rx="2" fill="#ffedd5" stroke="#ea580c" stroke-width="1.2"/>
      <circle cx="{col2_x + 242}" cy="{r1_y + 54}" r="6.5" fill="#ea580c"/>
      <text x="{col2_x + 242}" y="{r1_y + 56.5}" font-size="6.5" font-weight="700" fill="#ffffff" text-anchor="middle">8</text>
      <text x="{col2_x + 262}" y="{r1_y + 56.5}" font-size="5.8" font-weight="700" fill="#c2410c">Encol.</text>
    ''')

    # Puesto 9: Aplicador de adhesivo (Badge 9)
    svg.append(f'''
      <rect x="{col2_x + 215}" y="{r1_y + 72}" width="95" height="22" rx="2" fill="#ffedd5" stroke="#ea580c" stroke-width="1.2"/>
      <circle cx="{col2_x + 230}" cy="{r1_y + 83}" r="6.5" fill="#ea580c"/>
      <text x="{col2_x + 230}" y="{r1_y + 85.5}" font-size="6.5" font-weight="700" fill="#ffffff" text-anchor="middle">9</text>
      <text x="{col2_x + 268}" y="{r1_y + 85.5}" font-size="6" font-weight="700" fill="#c2410c">Aplicador Adhesivo</text>
    ''')

    # Prensa HF
    svg.append(f'''
      <rect x="{col2_x + 318}" y="{r1_y + 70}" width="100" height="42" rx="3" fill="#ffedd5" stroke="#ea580c" stroke-width="1.8"/>
      <text x="{col2_x + 368}" y="{r1_y + 88}" font-size="7.8" font-weight="700" fill="#c2410c" text-anchor="middle">PRENSA HF</text>
      <text x="{col2_x + 368}" y="{r1_y + 101}" font-size="6.2" font-weight="600" fill="#ea580c" text-anchor="middle">(Curvado dieléctrico 3 min)</text>
    ''')

    # Puesto 10: Guillotina de chapa (Badge 10)
    svg.append(f'''
      <rect x="{col2_x + 355}" y="{r1_y + 120}" width="65" height="52" rx="2" fill="#e0f2fe" stroke="#0284c7" stroke-width="1.2"/>
      <circle cx="{col2_x + 372}" cy="{r1_y + 138}" r="7" fill="#0284c7"/>
      <text x="{col2_x + 372}" y="{r1_y + 140.5}" font-size="6.2" font-weight="700" fill="#ffffff" text-anchor="middle">10</text>
      <text x="{col2_x + 372}" y="{r1_y + 158}" font-size="5.8" font-weight="600" fill="#0369a1" text-anchor="middle">Guillotina Madera</text>
    ''')

    # Puesto 11: Costura de chapa (Badge 11)
    svg.append(f'''
      <rect x="{col2_x + 230}" y="{r1_y + 130}" width="95" height="42" rx="2" fill="#e0f2fe" stroke="#0284c7" stroke-width="1.2"/>
      <circle cx="{col2_x + 248}" cy="{r1_y + 148}" r="7" fill="#0284c7"/>
      <text x="{col2_x + 248}" y="{r1_y + 150.5}" font-size="6.2" font-weight="700" fill="#ffffff" text-anchor="middle">11</text>
      <text x="{col2_x + 282}" y="{r1_y + 152}" font-size="6.2" font-weight="600" fill="#0369a1">Costura de Chapa</text>
    ''')

    # Almacén Multilaminados
    svg.append(f'''
      <rect x="{col2_x + 10}" y="{r1_y + 90}" width="155" height="100" rx="3" fill="#f1f5f9" stroke="#94a3b8" stroke-width="1.2"/>
      <text x="{col2_x + 87}" y="{r1_y + 135}" font-size="8" font-weight="700" fill="#475569" text-anchor="middle">ALMACÉN MULTILAMINADOS</text>
      <text x="{col2_x + 87}" y="{r1_y + 149}" font-size="6.8" fill="#64748b" text-anchor="middle">Placas Guatambú / Guayica</text>
    ''')

    # Puesto 12: Cabinas Lijado Fino (Badge 12)
    svg.append(f'''
      <rect x="{col2_x + 355}" y="{r1_y + 180}" width="65" height="48" rx="2" fill="#fefce8" stroke="#ca8a04" stroke-width="1.5"/>
      <circle cx="{col2_x + 372}" cy="{r1_y + 196}" r="7" fill="#ca8a04"/>
      <text x="{col2_x + 372}" y="{r1_y + 198.5}" font-size="6.2" font-weight="700" fill="#ffffff" text-anchor="middle">12</text>
      <text x="{col2_x + 372}" y="{r1_y + 214}" font-size="5.8" font-weight="700" fill="#854d0e" text-anchor="middle">Lijado Diego</text>
    ''')

    # Almacenamiento intermedio + ESCALERA
    svg.append(f'''
      <rect x="{col2_x + 230}" y="{r1_y + 235}" width="115" height="42" rx="3" fill="#f1f5f9" stroke="#94a3b8" stroke-width="1"/>
      <text x="{col2_x + 287}" y="{r1_y + 254}" font-size="7.2" font-weight="600" fill="#475569" text-anchor="middle">ALMACENAMIENTO</text>
      <text x="{col2_x + 287}" y="{r1_y + 266}" font-size="6" fill="#64748b" text-anchor="middle">Pulido e Insumos</text>

      <rect x="{col2_x + 355}" y="{r1_y + 245}" width="65" height="24" rx="2" fill="#3b82f6"/>
      <text x="{col2_x + 387}" y="{r1_y + 260}" font-size="6.8" font-weight="700" fill="#ffffff" text-anchor="middle">ESCALERA</text>
    ''')

    # Cabina de Pintura y Puesto 13: Montaje Final (Badge 13)
    svg.append(f'''
      <rect x="{col2_x + 10}" y="{r1_y + 205}" width="125" height="60" rx="3" fill="#ede9fe" stroke="#7c3aed" stroke-width="1.6"/>
      <text x="{col2_x + 72}" y="{r1_y + 233}" font-size="7.8" font-weight="700" fill="#5b21b6" text-anchor="middle">CABINA DE PINTURA</text>
      <text x="{col2_x + 72}" y="{r1_y + 246}" font-size="6.2" fill="#7c3aed" text-anchor="middle">(Laca Poliuretánica a Soplete)</text>

      <rect x="{col2_x + 142}" y="{r1_y + 205}" width="46" height="42" rx="2" fill="#f0fdf4" stroke="#16a34a" stroke-width="1.4"/>
      <circle cx="{col2_x + 165}" cy="{r1_y + 220}" r="7" fill="#16a34a"/>
      <text x="{col2_x + 165}" y="{r1_y + 222.5}" font-size="6.2" font-weight="700" fill="#ffffff" text-anchor="middle">13</text>
      <text x="{col2_x + 165}" y="{r1_y + 238}" font-size="5.8" font-weight="700" fill="#15803d" text-anchor="middle">Montaje</text>
    ''')

    # Router CNC
    svg.append(f'''
      <rect x="{col2_x + 10}" y="{r1_y + 280}" width="178" height="75" rx="3" fill="#e0f2fe" stroke="#0284c7" stroke-width="1.8"/>
      <text x="{col2_x + 99}" y="{r1_y + 312}" font-size="8" font-weight="700" fill="#0369a1" text-anchor="middle">ROUTER CNC (MECANIZADO)</text>
      <text x="{col2_x + 99}" y="{r1_y + 326}" font-size="6.8" fill="#0284c7" text-anchor="middle">Mecanizado de Asientos y Piezas Planas</text>
    ''')

    # Almacén inferior y Almacén General
    svg.append(f'''
      <rect x="{col2_x + 230}" y="{r1_y + 285}" width="190" height="38" rx="2" fill="#f1f5f9" stroke="#94a3b8" stroke-width="1"/>
      <text x="{col2_x + 325}" y="{r1_y + 308}" font-size="6.8" font-weight="600" fill="#475569" text-anchor="middle">ALMACENAMIENTO EN PROCESO</text>

      <rect x="{col2_x + 215}" y="{r1_y + 332}" width="205" height="88" rx="3" fill="#f1f5f9" stroke="#94a3b8" stroke-width="1.2"/>
      <text x="{col2_x + 317}" y="{r1_y + 368}" font-size="8" font-weight="700" fill="#475569" text-anchor="middle">ALMACÉN GENERAL</text>
      <text x="{col2_x + 317}" y="{r1_y + 382}" font-size="6.8" fill="#64748b" text-anchor="middle">Muebles Embalados y Expedición</text>
    ''')

    # Portones Entrada 2A y 2B
    svg.append(f'''
      <rect x="{col2_x + 15}" y="{r1_y + r1_h - 14}" width="110" height="14" rx="2" fill="#22c55e"/>
      <text x="{col2_x + 70}" y="{r1_y + r1_h - 4}" font-size="7.2" font-weight="700" fill="#ffffff" text-anchor="middle">PORTÓN 2A ▼</text>

      <rect x="{col2_x + 215}" y="{r1_y + r1_h - 14}" width="130" height="14" rx="2" fill="#22c55e"/>
      <text x="{col2_x + 280}" y="{r1_y + r1_h - 4}" font-size="7.2" font-weight="700" fill="#ffffff" text-anchor="middle">PORTÓN EXPEDICIÓN 2B ▼</text>
    ''')

    # Cota 90 Nave 2
    svg.append(f'''
      <text x="{col2_x + col_w + 12}" y="{r1_y + r1_h/2}" font-size="9" font-weight="800" fill="#94a3b8" text-anchor="middle" transform="rotate(90 {col2_x + col_w + 12} {r1_y + r1_h/2})">360 (36 m)</text>
      <text x="{col2_x + col_w/2}" y="{r1_y + r1_h + 14}" font-size="8" font-weight="700" fill="#94a3b8" text-anchor="middle">90 (9 m)</text>
    ''')


    # =========================================================================
    # QUADRANT 3: BOTTOM-LEFT · PLANTA ALTA · TAPICERÍA Y LÁSER (16×9 m)
    # =========================================================================
    # Header
    svg.append(f'''
      <g>
        <rect x="{col1_x}" y="{r2_y - 28}" width="{col_w}" height="22" rx="3" fill="#1e293b"/>
        <text x="{col1_x + col_w/2}" y="{r2_y - 13}" fill="#ffffff" font-size="9.5" font-weight="700" text-anchor="middle" letter-spacing="0.5">PLANTA ALTA · TAPICERÍA Y CORTE LÁSER (16×9 m)</text>
      </g>
    ''')

    # Edificio Entrepiso
    svg.append(f'''
      <rect x="{col1_x}" y="{r2_y}" width="{col_w}" height="{r2_h}" rx="4" fill="#f8fafc" stroke="#334155" stroke-width="2" filter="url(#shadow)"/>
    ''')

    # Pasillo central entrepiso
    aisle3_x = col1_x + 195
    svg.append(f'''
      <path d="M {aisle3_x} {r2_y + 8} L {aisle3_x} {r2_y + r2_h - 35} L {aisle3_x + 120} {r2_y + r2_h - 35} L {aisle3_x + 120} {r2_y + r2_h - 10}" fill="none" stroke="#e2e8f0" stroke-width="14" stroke-linecap="round"/>
      <path d="M {aisle3_x} {r2_y + 8} L {aisle3_x} {r2_y + r2_h - 35} L {aisle3_x + 120} {r2_y + r2_h - 35} L {aisle3_x + 120} {r2_y + r2_h - 10}" fill="none" stroke="#94a3b8" stroke-width="1.2" stroke-dasharray="5,4"/>
    ''')

    # Almacén de telas
    svg.append(f'''
      <rect x="{col1_x + 115}" y="{r2_y + 10}" width="160" height="32" rx="2" fill="#f1f5f9" stroke="#94a3b8" stroke-width="1"/>
      <text x="{col1_x + 195}" y="{r2_y + 25}" font-size="7.2" font-weight="600" fill="#475569" text-anchor="middle">ALMACÉN DE TELAS</text>
      <text x="{col1_x + 195}" y="{r2_y + 36}" font-size="6" fill="#64748b" text-anchor="middle">Bobinas y Rollos Textiles</text>
    ''')

    # Racks espumas lateral derecho
    svg.append(f'''
      <rect x="{col1_x + 360}" y="{r2_y + 10}" width="55" height="120" rx="2" fill="#f1f5f9" stroke="#94a3b8" stroke-width="1"/>
      <text x="{col1_x + 387}" y="{r2_y + 75}" font-size="6.5" font-weight="600" fill="#475569" text-anchor="middle" transform="rotate(90 {col1_x + 387} {r2_y + 75})">Racks Espumas</text>
    ''')

    # Corte Láser y Puesto 15: Mesa Despiece (Badge 15)
    svg.append(f'''
      <rect x="{col1_x + 230}" y="{r2_y + 52}" width="115" height="42" rx="3" fill="#dcfce7" stroke="#16a34a" stroke-width="1.6"/>
      <text x="{col1_x + 287}" y="{r2_y + 72}" font-size="7.5" font-weight="700" fill="#15803d" text-anchor="middle">CORTE LÁSER TEXTIL</text>
      <text x="{col1_x + 287}" y="{r2_y + 85}" font-size="6" fill="#16a34a" text-anchor="middle">Mesa CNC Automatizada</text>

      <rect x="{col1_x + 230}" y="{r2_y + 102}" width="115" height="24" rx="2" fill="#f1f5f9" stroke="#94a3b8" stroke-width="1"/>
      <circle cx="{col1_x + 248}" cy="{r2_y + 114}" r="6.5" fill="#64748b"/>
      <text x="{col1_x + 248}" y="{r2_y + 116.5}" font-size="6.5" font-weight="700" fill="#ffffff" text-anchor="middle">15</text>
      <text x="{col1_x + 287}" y="{r2_y + 116.5}" font-size="6.2" font-weight="600" fill="#475569">Mesa Despiece</text>
    ''')

    # Puesto 14: Montaje Espuma y Tela (Badge 14)
    svg.append(f'''
      <rect x="{col1_x + 12}" y="{r2_y + 52}" width="165" height="45" rx="2" fill="#dcfce7" stroke="#16a34a" stroke-width="1.4"/>
      <circle cx="{col1_x + 30}" cy="{r2_y + 74}" r="7.5" fill="#16a34a"/>
      <text x="{col1_x + 30}" y="{r2_y + 76.5}" font-size="6.5" font-weight="700" fill="#ffffff" text-anchor="middle">14</text>
      <text x="{col1_x + 102}" y="{r2_y + 72}" font-size="7" font-weight="700" fill="#15803d" text-anchor="middle">MONTAJE ESPUMA Y TELA</text>
      <text x="{col1_x + 102}" y="{r2_y + 84}" font-size="5.8" fill="#16a34a" text-anchor="middle">Engrapado y confección de fundas</text>
    ''')

    # Almacén partes tapizadas
    svg.append(f'''
      <rect x="{col1_x + 12}" y="{r2_y + 108}" width="165" height="65" rx="2" fill="#f1f5f9" stroke="#94a3b8" stroke-width="1"/>
      <text x="{col1_x + 94}" y="{r2_y + 138}" font-size="7.5" font-weight="600" fill="#475569" text-anchor="middle">ALMACÉN PARTES TAPIZADAS</text>
      <text x="{col1_x + 94}" y="{r2_y + 152}" font-size="6.2" fill="#64748b" text-anchor="middle">Asientos y respaldos listos para ensamble</text>
    ''')

    # Apertura Clark y Escalera Entrepiso
    svg.append(f'''
      <rect x="{col1_x + 180}" y="{r2_y + r2_h - 24}" width="135" height="20" rx="2" fill="#fef3c7" stroke="#f59e0b" stroke-width="1.4" stroke-dasharray="3,3"/>
      <text x="{col1_x + 247}" y="{r2_y + r2_h - 10}" font-size="6.8" font-weight="700" fill="#b45309" text-anchor="middle">APERTURA PARA CLARK / ELEVADOR</text>

      <rect x="{col1_x + 325}" y="{r2_y + r2_h - 24}" width="85" height="20" rx="2" fill="#3b82f6"/>
      <text x="{col1_x + 367}" y="{r2_y + r2_h - 10}" font-size="6.8" font-weight="700" fill="#ffffff" text-anchor="middle">ESCALERA</text>
    ''')

    # Cotas 160 y 90
    svg.append(f'''
      <text x="{col1_x - 12}" y="{r2_y + r2_h/2}" font-size="9" font-weight="800" fill="#94a3b8" text-anchor="middle" transform="rotate(-90 {col1_x - 12} {r2_y + r2_h/2})">160 (16 m)</text>
      <text x="{col1_x + col_w/2}" y="{r2_y + r2_h + 14}" font-size="8" font-weight="700" fill="#94a3b8" text-anchor="middle">90 (9 m)</text>
    ''')


    # =========================================================================
    # QUADRANT 4: BOTTOM-RIGHT · CUADRO DE REFERENCIAS DE PLANTA Y PUESTOS
    # =========================================================================
    # Header
    svg.append(f'''
      <g>
        <rect x="{col2_x}" y="{r2_y - 28}" width="{col_w}" height="22" rx="3" fill="#1e293b"/>
        <text x="{col2_x + col_w/2}" y="{r2_y - 13}" fill="#ffffff" font-size="9.5" font-weight="700" text-anchor="middle" letter-spacing="0.5">REFERENCIAS DE PLANTA Y PUESTOS</text>
      </g>
    ''')

    # Panel principal de referencias
    svg.append(f'''
      <rect x="{col2_x}" y="{r2_y}" width="{col_w}" height="{r2_h}" rx="4" fill="#ffffff" stroke="#cbd5e1" stroke-width="1.5" filter="url(#shadow)"/>
    ''')

    # Mitad Izquierda del Panel: 1. CÓDIGO DE SECTORES (ZONAS)
    p1_x = col2_x + 14
    p1_w = 175
    svg.append(f'''
      <text x="{p1_x}" y="{r2_y + 18}" font-size="7.5" font-weight="700" fill="#0f172a">1. CÓDIGO DE SECTORES (ZONAS):</text>
      
      <rect x="{p1_x}" y="{r2_y + 28}" width="12" height="12" rx="2" fill="#ffedd5" stroke="#ea580c"/>
      <text x="{p1_x + 18}" y="{r2_y + 37}" font-size="6.5" fill="#334155">Curvado y Prensas Alta Frecuencia</text>

      <rect x="{p1_x}" y="{r2_y + 46}" width="12" height="12" rx="2" fill="#e0f2fe" stroke="#0284c7"/>
      <text x="{p1_x + 18}" y="{r2_y + 55}" font-size="6.5" fill="#334155">Mecanizado CNC / Carpintería</text>

      <rect x="{p1_x}" y="{r2_y + 64}" width="12" height="12" rx="2" fill="#ede9fe" stroke="#7c3aed"/>
      <text x="{p1_x + 18}" y="{r2_y + 73}" font-size="6.5" fill="#334155">Cabina de Laqueado y Lijado</text>

      <rect x="{p1_x}" y="{r2_y + 82}" width="12" height="12" rx="2" fill="#dcfce7" stroke="#16a34a"/>
      <text x="{p1_x + 18}" y="{r2_y + 91}" font-size="6.5" fill="#334155">Corte Láser Textil y Tapicería</text>

      <rect x="{p1_x}" y="{r2_y + 100}" width="12" height="12" rx="2" fill="#f1f5f9" stroke="#94a3b8"/>
      <text x="{p1_x + 18}" y="{r2_y + 109}" font-size="6.5" fill="#334155">Almacenes y Logística Interna</text>

      <!-- Resumen de Planta -->
      <rect x="{p1_x}" y="{r2_y + 128}" width="{p1_w}" height="84" rx="3" fill="#f8fafc" stroke="#e2e8f0"/>
      <text x="{p1_x + 10}" y="{r2_y + 144}" font-size="6.8" font-weight="700" fill="#1e293b">RESUMEN TÉCNICO DE PLANTA:</text>
      <text x="{p1_x + 10}" y="{r2_y + 158}" font-size="6" fill="#475569">· Ubicación: Bouchard 3870, Villa Lynch</text>
      <text x="{p1_x + 10}" y="{r2_y + 170}" font-size="6" fill="#475569">· Sup. PB: 2 Sectores de 36×9 m (648 m²)</text>
      <text x="{p1_x + 10}" y="{r2_y + 182}" font-size="6" fill="#475569">· Sup. Entrepiso: 16×9 m (144 m²)</text>
      <text x="{p1_x + 10}" y="{r2_y + 194}" font-size="6" fill="#475569">· Superficie total: ~792 m² cubiertos</text>
      <text x="{p1_x + 10}" y="{r2_y + 204}" font-size="5.8" font-weight="600" fill="#0284c7">· Layout industrial relevado a escala</text>
    ''')

    # Línea vertical divisoria interior
    svg.append(f'''
      <line x1="{col2_x + 198}" y1="{r2_y + 12}" x2="{col2_x + 198}" y2="{r2_y + r2_h - 12}" stroke="#e2e8f0" stroke-width="1.2"/>
    ''')

    # Mitad Derecha del Panel: 2. PUESTOS NUMERADOS (1 al 15)
    p2_x = col2_x + 210
    svg.append(f'''
      <text x="{p2_x}" y="{r2_y + 18}" font-size="7.5" font-weight="700" fill="#0f172a">2. PUESTOS NUMERADOS EN PLANO:</text>
    ''')

    # Subcolumna A (1 al 8) y Subcolumna B (9 al 15)
    subA_x = p2_x
    subB_x = p2_x + 105
    start_y = r2_y + 36
    rg = 23

    puestos = [
        # Columna A (1 al 8)
        (1, "Rectificadora", "#0284c7", subA_x, start_y + 0*rg),
        (2, "Cepilladora", "#0284c7", subA_x, start_y + 1*rg),
        (3, "Espigadora", "#0284c7", subA_x, start_y + 2*rg),
        (4, "Fresadora tupí", "#0284c7", subA_x, start_y + 3*rg),
        (5, "Mortajadora", "#0284c7", subA_x, start_y + 4*rg),
        (6, "Sierra sin fin 1", "#0284c7", subA_x, start_y + 5*rg),
        (7, "Sierra sin fin 2", "#0284c7", subA_x, start_y + 6*rg),
        (8, "Encoladora rod.", "#ea580c", subA_x, start_y + 7*rg),

        # Columna B (9 al 15)
        (9, "Aplicador adh.", "#ea580c", subB_x, start_y + 0*rg),
        (10, "Guillotina chapa", "#0284c7", subB_x, start_y + 1*rg),
        (11, "Costura de chapa", "#0284c7", subB_x, start_y + 2*rg),
        (12, "Lijado Diego", "#ca8a04", subB_x, start_y + 3*rg),
        (13, "Montaje final", "#16a34a", subB_x, start_y + 4*rg),
        (14, "Montaje espuma", "#16a34a", subB_x, start_y + 5*rg),
        (15, "Mesa despiece", "#64748b", subB_x, start_y + 6*rg),
    ]

    for num, name, color, px, py in puestos:
        svg.append(f'''
          <circle cx="{px + 6}" cy="{py}" r="6.5" fill="{color}"/>
          <text x="{px + 6}" y="{py + 2.4}" font-size="6" font-weight="700" fill="#ffffff" text-anchor="middle">{num}</text>
          <text x="{px + 16}" y="{py + 2.8}" font-size="6.5" font-weight="600" fill="#334155">{name}</text>
        ''')

    svg.append('</svg>')
    return '\n'.join(svg)

if __name__ == '__main__':
    content = generate_svg()
    with open('assets/layout_oficial_planta.svg', 'w', encoding='utf-8') as f:
        f.write(content)
    print("assets/layout_oficial_planta.svg successfully updated to 2x2 grid layout!")

# -*- coding: utf-8 -*-
"""
Script to generate the updated official plant layout of Gran Sasso S.R.L.
- Removed 'Nave 1/2' prefixes from sector headers.
- Removed all flow polyline layers.
- Replaced cramped/small machine labels with numbered badges (1 to 15).
- Redesigned the right panel with:
  1. Código de sectores (zonas funcionales).
  2. Referencias completas de los 15 puestos numerados.
  Removed old point 3 (hallazgos críticos).
"""

def generate_svg():
    svg = []
    svg.append('<svg viewBox="0 0 940 782" xmlns="http://www.w3.org/2000/svg" font-family="Inter, -apple-system, sans-serif">')
    svg.append('<defs>')
    svg.append('''
      <filter id="shadow" x="-3%" y="-3%" width="106%" height="106%">
        <feDropShadow dx="0" dy="1.5" stdDeviation="1.5" flood-opacity="0.06"/>
      </filter>
    ''')
    svg.append('</defs>')

    # Background canvas
    svg.append('<rect width="940" height="782" fill="#ffffff" rx="6"/>')

    # =========================================================================
    # COLUMNA 1: CARPINTERÍA TRADICIONAL, MECANIZADO Y ESTRUCTURA (36×9 m)
    # =========================================================================
    col1_x = 25
    col1_y = 42
    col1_w = 260
    col1_h = 715

    # Header Columna 1 (sin texto "Nave 1")
    svg.append(f'''
      <g>
        <rect x="{col1_x}" y="12" width="{col1_w}" height="24" rx="3" fill="#1e293b"/>
        <text x="{col1_x + col1_w/2}" y="28" fill="#ffffff" font-size="9" font-weight="700" text-anchor="middle" letter-spacing="0.5">CARPINTERÍA Y ESTRUCTURA (36×9 m)</text>
      </g>
    ''')

    # Edificio Columna 1
    svg.append(f'''
      <rect x="{col1_x}" y="{col1_y}" width="{col1_w}" height="{col1_h}" rx="4" fill="#f8fafc" stroke="#334155" stroke-width="2" filter="url(#shadow)"/>
    ''')

    # Pasillo central franja de circulación
    svg.append(f'''
      <path d="M {col1_x + 85} {col1_y + 10} L {col1_x + 85} {col1_y + 700}" fill="none" stroke="#e2e8f0" stroke-width="14" stroke-linecap="round"/>
      <path d="M {col1_x + 85} {col1_y + 10} L {col1_x + 85} {col1_y + 700}" fill="none" stroke="#94a3b8" stroke-width="1.2" stroke-dasharray="5,4"/>
      
      <!-- Pasillo transversal inter-sectores superior -->
      <path d="M {col1_x + 85} {col1_y + 70} L {col1_x + col1_w} {col1_y + 70}" fill="none" stroke="#e2e8f0" stroke-width="12"/>
      <path d="M {col1_x + 85} {col1_y + 70} L {col1_x + col1_w} {col1_y + 70}" fill="none" stroke="#94a3b8" stroke-width="1" stroke-dasharray="4,4"/>

      <!-- Pasillo transversal inter-sectores medio -->
      <path d="M {col1_x + 85} {col1_y + 365} L {col1_x + col1_w} {col1_y + 365}" fill="none" stroke="#e2e8f0" stroke-width="12"/>
      <path d="M {col1_x + 85} {col1_y + 365} L {col1_x + col1_w} {col1_y + 365}" fill="none" stroke="#94a3b8" stroke-width="1" stroke-dasharray="4,4"/>
    ''')

    # Puestos Columna 1
    # Almacén de viruta
    svg.append(f'''
      <rect x="{col1_x + 155}" y="{col1_y + 8}" width="97" height="54" rx="3" fill="#f1f5f9" stroke="#64748b" stroke-width="1.2"/>
      <text x="{col1_x + 203}" y="{col1_y + 31}" font-size="7.5" font-weight="700" fill="#334155" text-anchor="middle">ALMACÉN DE</text>
      <text x="{col1_x + 203}" y="{col1_y + 43}" font-size="7.5" font-weight="700" fill="#334155" text-anchor="middle">VIRUTA</text>
    ''')

    # Lijadora de banda
    svg.append(f'''
      <rect x="{col1_x + 8}" y="{col1_y + 24}" width="138" height="28" rx="3" fill="#fef3c7" stroke="#d97706" stroke-width="1.2"/>
      <text x="{col1_x + 77}" y="{col1_y + 42}" font-size="8" font-weight="700" fill="#92400e" text-anchor="middle">LIJADORA DE BANDA</text>
    ''')

    # Brazo 6 ejes (Robot)
    svg.append(f'''
      <rect x="{col1_x + 115}" y="{col1_y + 86}" width="65" height="58" rx="3" fill="#e0f2fe" stroke="#0284c7" stroke-width="1.8"/>
      <text x="{col1_x + 147}" y="{col1_y + 111}" font-size="7.5" font-weight="700" fill="#0369a1" text-anchor="middle">BRAZO 6 EJES</text>
      <text x="{col1_x + 147}" y="{col1_y + 124}" font-size="6.5" fill="#0284c7" text-anchor="middle">(Robot 4 Motores)</text>
    ''')

    # Puesto 1: Rectificadora (Badge 1)
    svg.append(f'''
      <rect x="{col1_x + 188}" y="{col1_y + 100}" width="42" height="18" rx="2" fill="#e0f2fe" stroke="#0284c7" stroke-width="1.2"/>
      <circle cx="{col1_x + 209}" cy="{col1_y + 109}" r="6.5" fill="#0284c7"/>
      <text x="{col1_x + 209}" y="{col1_y + 111.5}" font-size="6.5" font-weight="700" fill="#ffffff" text-anchor="middle">1</text>
    ''')

    # Puesto 2: Cepilladora (Badge 2)
    svg.append(f'''
      <rect x="{col1_x + 236}" y="{col1_y + 96}" width="16" height="28" rx="2" fill="#e0f2fe" stroke="#0284c7" stroke-width="1.2"/>
      <circle cx="{col1_x + 244}" cy="{col1_y + 110}" r="6.5" fill="#0284c7"/>
      <text x="{col1_x + 244}" y="{col1_y + 112.5}" font-size="6.5" font-weight="700" fill="#ffffff" text-anchor="middle">2</text>
    ''')

    # Almacén MP
    svg.append(f'''
      <rect x="{col1_x + 8}" y="{col1_y + 100}" width="48" height="58" rx="2" fill="#f1f5f9" stroke="#94a3b8" stroke-width="1"/>
      <text x="{col1_x + 32}" y="{col1_y + 130}" font-size="6.5" font-weight="600" fill="#475569" text-anchor="middle">Almacén MP</text>
    ''')

    # Puesto 3: Espigadora (Badge 3)
    svg.append(f'''
      <rect x="{col1_x + 8}" y="{col1_y + 182}" width="44" height="28" rx="2" fill="#e0f2fe" stroke="#0284c7" stroke-width="1.2"/>
      <circle cx="{col1_x + 30}" cy="{col1_y + 196}" r="6.5" fill="#0284c7"/>
      <text x="{col1_x + 30}" y="{col1_y + 198.5}" font-size="6.5" font-weight="700" fill="#ffffff" text-anchor="middle">3</text>
    ''')

    # Almacenamiento intermedio
    svg.append(f'''
      <rect x="{col1_x + 115}" y="{col1_y + 192}" width="65" height="18" rx="2" fill="#f1f5f9" stroke="#94a3b8" stroke-width="1"/>
      <text x="{col1_x + 147}" y="{col1_y + 204}" font-size="6.2" font-weight="600" fill="#475569" text-anchor="middle">Almacenamiento</text>
    ''')

    # Puesto 4: Fresadora (Badge 4)
    svg.append(f'''
      <rect x="{col1_x + 20}" y="{col1_y + 222}" width="30" height="20" rx="2" fill="#e0f2fe" stroke="#0284c7" stroke-width="1.2"/>
      <circle cx="{col1_x + 35}" cy="{col1_y + 232}" r="6.5" fill="#0284c7"/>
      <text x="{col1_x + 35}" y="{col1_y + 234.5}" font-size="6.5" font-weight="700" fill="#ffffff" text-anchor="middle">4</text>
    ''')

    # Puesto 5: Mortajadora (Badge 5)
    svg.append(f'''
      <rect x="{col1_x + 18}" y="{col1_y + 250}" width="34" height="18" rx="2" fill="#e0f2fe" stroke="#0284c7" stroke-width="1.2"/>
      <circle cx="{col1_x + 35}" cy="{col1_y + 259}" r="6.5" fill="#0284c7"/>
      <text x="{col1_x + 35}" y="{col1_y + 261.5}" font-size="6.5" font-weight="700" fill="#ffffff" text-anchor="middle">5</text>
    ''')

    # Puesto 6 y 7: Sierras sin fin (Badges 6 y 7)
    svg.append(f'''
      <rect x="{col1_x + 190}" y="{col1_y + 225}" width="38" height="26" rx="2" fill="#e0f2fe" stroke="#0284c7" stroke-width="1.2"/>
      <circle cx="{col1_x + 209}" cy="{col1_y + 238}" r="6.5" fill="#0284c7"/>
      <text x="{col1_x + 209}" y="{col1_y + 240.5}" font-size="6.5" font-weight="700" fill="#ffffff" text-anchor="middle">6</text>

      <rect x="{col1_x + 190}" y="{col1_y + 260}" width="38" height="26" rx="2" fill="#e0f2fe" stroke="#0284c7" stroke-width="1.2"/>
      <circle cx="{col1_x + 209}" cy="{col1_y + 273}" r="6.5" fill="#0284c7"/>
      <text x="{col1_x + 209}" y="{col1_y + 275.5}" font-size="6.5" font-weight="700" fill="#ffffff" text-anchor="middle">7</text>
    ''')

    # Armado Estructura
    svg.append(f'''
      <rect x="{col1_x + 8}" y="{col1_y + 288}" width="65" height="52" rx="3" fill="#dbeafe" stroke="#2563eb" stroke-width="1.5"/>
      <text x="{col1_x + 40}" y="{col1_y + 307}" font-size="7" font-weight="700" fill="#1d4ed8" text-anchor="middle">ARMADO</text>
      <text x="{col1_x + 40}" y="{col1_y + 320}" font-size="7" font-weight="700" fill="#1d4ed8" text-anchor="middle">ESTRUCTURA</text>
      <text x="{col1_x + 40}" y="{col1_y + 332}" font-size="5.8" fill="#3b82f6" text-anchor="middle">(Bancos Encastre)</text>
    ''')

    # Sierra Escuadradora
    svg.append(f'''
      <rect x="{col1_x + 165}" y="{col1_y + 385}" width="82" height="58" rx="3" fill="#e0f2fe" stroke="#0284c7" stroke-width="1.4"/>
      <text x="{col1_x + 206}" y="{col1_y + 412}" font-size="7.2" font-weight="700" fill="#0369a1" text-anchor="middle">SIERRA</text>
      <text x="{col1_x + 206}" y="{col1_y + 425}" font-size="7.2" font-weight="700" fill="#0369a1" text-anchor="middle">ESCUADRADORA</text>
    ''')

    # Almacén madera maciza
    svg.append(f'''
      <rect x="{col1_x + 8}" y="{col1_y + 355}" width="26" height="150" rx="2" fill="#f1f5f9" stroke="#94a3b8" stroke-width="1"/>
      <text x="{col1_x + 21}" y="{col1_y + 430}" font-size="6.8" font-weight="600" fill="#475569" text-anchor="middle" transform="rotate(-90 {col1_x + 21} {col1_y + 430})">ALMACÉN MADERA MACIZA</text>
    ''')

    # Lijadora plana
    svg.append(f'''
      <rect x="{col1_x + 145}" y="{col1_y + 450}" width="52" height="34" rx="2" fill="#fef3c7" stroke="#d97706" stroke-width="1.2"/>
      <text x="{col1_x + 171}" y="{col1_y + 468}" font-size="6.8" font-weight="700" fill="#92400e" text-anchor="middle">LIJADORA</text>
      <text x="{col1_x + 171}" y="{col1_y + 479}" font-size="6.2" font-weight="600" fill="#92400e" text-anchor="middle">PLANA</text>
    ''')

    # Almacenamiento tablones
    svg.append(f'''
      <rect x="{col1_x + 168}" y="{col1_y + 490}" width="82" height="68" rx="3" fill="#f1f5f9" stroke="#94a3b8" stroke-width="1"/>
      <text x="{col1_x + 209}" y="{col1_y + 524}" font-size="7.2" font-weight="600" fill="#475569" text-anchor="middle">ALMACENAMIENTO</text>
      <text x="{col1_x + 209}" y="{col1_y + 536}" font-size="6.2" fill="#64748b" text-anchor="middle">Tablones y Partes</text>
    ''')

    # Recepción
    svg.append(f'''
      <rect x="{col1_x + 140}" y="{col1_y + 570}" width="112" height="135" rx="3" fill="#e2e8f0" stroke="#64748b" stroke-width="1.4"/>
      <text x="{col1_x + 196}" y="{col1_y + 635}" font-size="8.5" font-weight="700" fill="#1e293b" text-anchor="middle">RECEPCIÓN</text>
      <text x="{col1_x + 196}" y="{col1_y + 650}" font-size="6.8" fill="#475569" text-anchor="middle">Ingreso Maderas</text>
      <text x="{col1_x + 196}" y="{col1_y + 662}" font-size="6.2" fill="#64748b" text-anchor="middle">Descarga y pesaje</text>
    ''')

    # Portón Entrada
    svg.append(f'''
      <rect x="{col1_x + 20}" y="{col1_y + col1_h - 12}" width="95" height="12" rx="2" fill="#22c55e"/>
      <text x="{col1_x + 67}" y="{col1_y + col1_h - 3}" font-size="7.5" font-weight="700" fill="#ffffff" text-anchor="middle">ENTRADA 1 ▼</text>
    ''')

    # Cotas 360 y 90
    svg.append(f'''
      <text x="{col1_x - 10}" y="{col1_y + col1_h/2}" font-size="10" font-weight="800" fill="#94a3b8" text-anchor="middle" transform="rotate(-90 {col1_x - 10} {col1_y + col1_h/2})">360 (36 m)</text>
      <text x="{col1_x + col1_w/2}" y="{col1_y + col1_h + 15}" font-size="8.5" font-weight="700" fill="#94a3b8" text-anchor="middle">90 (9 m)</text>
    ''')


    # =========================================================================
    # COLUMNA 2: PRENSADO HF, LAQUEADO Y FINAL (36×9 m)
    # =========================================================================
    col2_x = 320
    col2_y = 42
    col2_w = 260
    col2_h = 715

    # Header Columna 2 (sin texto "Nave 2")
    svg.append(f'''
      <g>
        <rect x="{col2_x}" y="12" width="{col2_w}" height="24" rx="3" fill="#1e293b"/>
        <text x="{col2_x + col2_w/2}" y="28" fill="#ffffff" font-size="9" font-weight="700" text-anchor="middle" letter-spacing="0.5">PRENSADO HF, LAQUEADO Y FINAL (36×9 m)</text>
      </g>
    ''')

    # Edificio Columna 2
    svg.append(f'''
      <rect x="{col2_x}" y="{col2_y}" width="{col2_w}" height="{col2_h}" rx="4" fill="#f8fafc" stroke="#334155" stroke-width="2" filter="url(#shadow)"/>
    ''')

    # Pasillo central
    svg.append(f'''
      <path d="M {col2_x + 125} {col2_y + 10} L {col2_x + 125} {col2_y + 700}" fill="none" stroke="#e2e8f0" stroke-width="14" stroke-linecap="round"/>
      <path d="M {col2_x + 125} {col2_y + 10} L {col2_x + 125} {col2_y + 700}" fill="none" stroke="#94a3b8" stroke-width="1.2" stroke-dasharray="5,4"/>
      
      <!-- Pasillo transversal superior -->
      <path d="M {col2_x} {col2_y + 70} L {col2_x + 125} {col2_y + 70}" fill="none" stroke="#e2e8f0" stroke-width="12"/>
      <path d="M {col2_x} {col2_y + 70} L {col2_x + 125} {col2_y + 70}" fill="none" stroke="#94a3b8" stroke-width="1" stroke-dasharray="4,4"/>

      <!-- Pasillo transversal medio -->
      <path d="M {col2_x} {col2_y + 365} L {col2_x + 125} {col2_y + 365}" fill="none" stroke="#e2e8f0" stroke-width="12"/>
      <path d="M {col2_x} {col2_y + 365} L {col2_x + 125} {col2_y + 365}" fill="none" stroke="#94a3b8" stroke-width="1" stroke-dasharray="4,4"/>
    ''')

    # Curvadoras 1 y 2
    svg.append(f'''
      <rect x="{col2_x + 8}" y="{col2_y + 12}" width="36" height="42" rx="2" fill="#ffedd5" stroke="#ea580c" stroke-width="1.3"/>
      <text x="{col2_x + 26}" y="{col2_y + 35}" font-size="6.5" font-weight="700" fill="#c2410c" text-anchor="middle">Curvadora 1</text>
      <rect x="{col2_x + 15}" y="{col2_y + 57}" width="22" height="14" rx="1.5" fill="#f1f5f9" stroke="#94a3b8" stroke-width="1"/>

      <rect x="{col2_x + 8}" y="{col2_y + 78}" width="36" height="42" rx="2" fill="#ffedd5" stroke="#ea580c" stroke-width="1.3"/>
      <text x="{col2_x + 26}" y="{col2_y + 101}" font-size="6.5" font-weight="700" fill="#c2410c" text-anchor="middle">Curvadora 2</text>
      <rect x="{col2_x + 15}" y="{col2_y + 123}" width="22" height="14" rx="1.5" fill="#f1f5f9" stroke="#94a3b8" stroke-width="1"/>
    ''')

    # Almacén chapa costurada y racks
    svg.append(f'''
      <rect x="{col2_x + 145}" y="{col2_y + 10}" width="58" height="32" rx="2" fill="#f1f5f9" stroke="#94a3b8" stroke-width="1"/>
      <text x="{col2_x + 174}" y="{col2_y + 24}" font-size="6" font-weight="600" fill="#475569" text-anchor="middle">Almacén Chapa</text>
      <text x="{col2_x + 174}" y="{col2_y + 34}" font-size="5.8" fill="#64748b" text-anchor="middle">Costurada</text>

      <rect x="{col2_x + 210}" y="{col2_y + 10}" width="42" height="65" rx="2" fill="#f1f5f9" stroke="#94a3b8" stroke-width="1"/>
      <text x="{col2_x + 231}" y="{col2_y + 45}" font-size="6" font-weight="600" fill="#475569" text-anchor="middle" transform="rotate(-90 {col2_x + 231} {col2_y + 45})">Racks Chapas</text>
    ''')

    # Puesto 8: Encoladora de rodillos (Badge 8)
    svg.append(f'''
      <rect x="{col2_x + 145}" y="{col2_y + 48}" width="26" height="20" rx="2" fill="#ffedd5" stroke="#ea580c" stroke-width="1.2"/>
      <circle cx="{col2_x + 158}" cy="{col2_y + 58}" r="6.5" fill="#ea580c"/>
      <text x="{col2_x + 158}" y="{col2_y + 60.5}" font-size="6.5" font-weight="700" fill="#ffffff" text-anchor="middle">8</text>
    ''')

    # Puesto 9: Aplicador de adhesivo (Badge 9)
    svg.append(f'''
      <rect x="{col2_x + 130}" y="{col2_y + 74}" width="52" height="24" rx="2" fill="#ffedd5" stroke="#ea580c" stroke-width="1.2"/>
      <circle cx="{col2_x + 156}" cy="{col2_y + 86}" r="6.5" fill="#ea580c"/>
      <text x="{col2_x + 156}" y="{col2_y + 88.5}" font-size="6.5" font-weight="700" fill="#ffffff" text-anchor="middle">9</text>
    ''')

    # Prensa HF
    svg.append(f'''
      <rect x="{col2_x + 188}" y="{col2_y + 82}" width="62" height="52" rx="3" fill="#ffedd5" stroke="#ea580c" stroke-width="1.8"/>
      <text x="{col2_x + 219}" y="{col2_y + 105}" font-size="7.5" font-weight="700" fill="#c2410c" text-anchor="middle">PRENSA HF</text>
      <text x="{col2_x + 219}" y="{col2_y + 118}" font-size="6.2" font-weight="600" fill="#ea580c" text-anchor="middle">(Curvado 3 min)</text>
    ''')

    # Puesto 10: Guillotina de chapa (Badge 10)
    svg.append(f'''
      <rect x="{col2_x + 215}" y="{col2_y + 155}" width="37" height="75" rx="2" fill="#e0f2fe" stroke="#0284c7" stroke-width="1.2"/>
      <circle cx="{col2_x + 233}" cy="{col2_y + 192}" r="7.5" fill="#0284c7"/>
      <text x="{col2_x + 233}" y="{col2_y + 194.5}" font-size="6.5" font-weight="700" fill="#ffffff" text-anchor="middle">10</text>
    ''')

    # Puesto 11: Costura de chapa (Badge 11)
    svg.append(f'''
      <rect x="{col2_x + 165}" y="{col2_y + 225}" width="44" height="55" rx="2" fill="#e0f2fe" stroke="#0284c7" stroke-width="1.2"/>
      <circle cx="{col2_x + 187}" cy="{col2_y + 252}" r="7.5" fill="#0284c7"/>
      <text x="{col2_x + 187}" y="{col2_y + 254.5}" font-size="6.5" font-weight="700" fill="#ffffff" text-anchor="middle">11</text>
    ''')

    # Almacén Multilaminados
    svg.append(f'''
      <rect x="{col2_x + 8}" y="{col2_y + 150}" width="98" height="150" rx="3" fill="#f1f5f9" stroke="#94a3b8" stroke-width="1.2"/>
      <text x="{col2_x + 57}" y="{col2_y + 225}" font-size="7.8" font-weight="700" fill="#475569" text-anchor="middle">ALMACÉN</text>
      <text x="{col2_x + 57}" y="{col2_y + 238}" font-size="7.8" font-weight="700" fill="#475569" text-anchor="middle">MULTILAMINADOS</text>
      <text x="{col2_x + 57}" y="{col2_y + 252}" font-size="6.5" fill="#64748b" text-anchor="middle">Placas Guatambú</text>
    ''')

    # Puesto 12: Cabinas Lijado Fino (Badge 12)
    svg.append(f'''
      <rect x="{col2_x + 226}" y="{col2_y + 305}" width="26" height="70" rx="2" fill="#fefce8" stroke="#ca8a04" stroke-width="1.5"/>
      <circle cx="{col2_x + 239}" cy="{col2_y + 340}" r="7.5" fill="#ca8a04"/>
      <text x="{col2_x + 239}" y="{col2_y + 342.5}" font-size="6.5" font-weight="700" fill="#ffffff" text-anchor="middle">12</text>
    ''')

    # Almacenamiento intermedio + ESCALERA
    svg.append(f'''
      <rect x="{col2_x + 145}" y="{col2_y + 385}" width="98" height="75" rx="3" fill="#f1f5f9" stroke="#94a3b8" stroke-width="1"/>
      <text x="{col2_x + 194}" y="{col2_y + 420}" font-size="7.2" font-weight="600" fill="#475569" text-anchor="middle">ALMACENAMIENTO</text>
      <text x="{col2_x + 194}" y="{col2_y + 432}" font-size="6.2" fill="#64748b" text-anchor="middle">Pulido e Insumos</text>

      <rect x="{col2_x + 215}" y="{col2_y + 465}" width="38" height="18" rx="2" fill="#3b82f6"/>
      <text x="{col2_x + 234}" y="{col2_y + 477}" font-size="6.8" font-weight="700" fill="#ffffff" text-anchor="middle">ESCALERA</text>
    ''')

    # Cabina de Pintura y Puesto 13: Montaje Final (Badge 13)
    svg.append(f'''
      <rect x="{col2_x + 8}" y="{col2_y + 385}" width="88" height="98" rx="3" fill="#ede9fe" stroke="#7c3aed" stroke-width="1.6"/>
      <text x="{col2_x + 52}" y="{col2_y + 430}" font-size="7.8" font-weight="700" fill="#5b21b6" text-anchor="middle">CABINA DE</text>
      <text x="{col2_x + 52}" y="{col2_y + 443}" font-size="7.8" font-weight="700" fill="#5b21b6" text-anchor="middle">PINTURA</text>
      <text x="{col2_x + 52}" y="{col2_y + 456}" font-size="6.2" fill="#7c3aed" text-anchor="middle">(Laca Soplete)</text>

      <rect x="{col2_x + 98}" y="{col2_y + 385}" width="30" height="38" rx="2" fill="#f0fdf4" stroke="#16a34a" stroke-width="1.4"/>
      <circle cx="{col2_x + 113}" cy="{col2_y + 404}" r="7.5" fill="#16a34a"/>
      <text x="{col2_x + 113}" y="{col2_y + 406.5}" font-size="6.5" font-weight="700" fill="#ffffff" text-anchor="middle">13</text>
    ''')

    # Router CNC
    svg.append(f'''
      <rect x="{col2_x + 8}" y="{col2_y + 500}" width="98" height="120" rx="3" fill="#e0f2fe" stroke="#0284c7" stroke-width="1.8"/>
      <text x="{col2_x + 57}" y="{col2_y + 555}" font-size="8" font-weight="700" fill="#0369a1" text-anchor="middle">ROUTER CNC</text>
      <text x="{col2_x + 57}" y="{col2_y + 570}" font-size="6.8" fill="#0284c7" text-anchor="middle">Mecanizado Tableros</text>
      <text x="{col2_x + 57}" y="{col2_y + 582}" font-size="6.2" fill="#0369a1" text-anchor="middle">Asientos y Piezas Planas</text>
    ''')

    # Almacén inferior y Almacén General
    svg.append(f'''
      <rect x="{col2_x + 145}" y="{col2_y + 490}" width="107" height="60" rx="2" fill="#f1f5f9" stroke="#94a3b8" stroke-width="1"/>
      <text x="{col2_x + 198}" y="{col2_y + 525}" font-size="6.8" font-weight="600" fill="#475569" text-anchor="middle">ALMACENAMIENTO</text>

      <rect x="{col2_x + 145}" y="{col2_y + 558}" width="107" height="145" rx="3" fill="#f1f5f9" stroke="#94a3b8" stroke-width="1.2"/>
      <text x="{col2_x + 198}" y="{col2_y + 630}" font-size="7.8" font-weight="700" fill="#475569" text-anchor="middle">ALMACÉN GENERAL</text>
      <text x="{col2_x + 198}" y="{col2_y + 645}" font-size="6.8" fill="#64748b" text-anchor="middle">Muebles Embalados</text>
      <text x="{col2_x + 198}" y="{col2_y + 658}" font-size="6.2" fill="#64748b" text-anchor="middle">y Producto Terminado</text>
    ''')

    # Portones Entrada 2A y 2B
    svg.append(f'''
      <rect x="{col2_x + 10}" y="{col2_y + col2_h - 12}" width="70" height="12" rx="2" fill="#22c55e"/>
      <text x="{col2_x + 45}" y="{col2_y + col2_h - 3}" font-size="7.2" font-weight="700" fill="#ffffff" text-anchor="middle">ENTRADA 2A ▼</text>

      <rect x="{col2_x + 145}" y="{col2_y + col2_h - 12}" width="85" height="12" rx="2" fill="#22c55e"/>
      <text x="{col2_x + 187}" y="{col2_y + col2_h - 3}" font-size="7.2" font-weight="700" fill="#ffffff" text-anchor="middle">ENTRADA 2B ▼</text>
    ''')

    # Cota 90 Nave 2
    svg.append(f'''
      <text x="{col2_x + col2_w/2}" y="{col2_y + col2_h + 15}" font-size="8.5" font-weight="700" fill="#94a3b8" text-anchor="middle">90 (9 m)</text>
    ''')


    # =========================================================================
    # COLUMNA 3 ARRIBA: PLANTA ALTA · TAPICERÍA Y CORTE LÁSER (16×9 m)
    # =========================================================================
    col3_x = 615
    col3_y = 42
    col3_w = 260
    col3_h = 320

    # Header Columna 3
    svg.append(f'''
      <g>
        <rect x="{col3_x}" y="12" width="{col3_w}" height="24" rx="3" fill="#1e293b"/>
        <text x="{col3_x + col3_w/2}" y="28" fill="#ffffff" font-size="9" font-weight="700" text-anchor="middle" letter-spacing="0.5">PLANTA ALTA · TAPICERÍA Y LÁSER (16×9 m)</text>
      </g>
    ''')

    # Edificio Entrepiso
    svg.append(f'''
      <rect x="{col3_x}" y="{col3_y}" width="{col3_w}" height="{col3_h}" rx="4" fill="#f8fafc" stroke="#334155" stroke-width="2" filter="url(#shadow)"/>
    ''')

    # Pasillo central entrepiso
    svg.append(f'''
      <path d="M {col3_x + 115} {col3_y + 10} L {col3_x + 115} {col3_y + 270} L {col3_x + 200} {col3_y + 270} L {col3_x + 200} {col3_y + 310}" fill="none" stroke="#e2e8f0" stroke-width="12" stroke-linecap="round"/>
      <path d="M {col3_x + 115} {col3_y + 10} L {col3_x + 115} {col3_y + 270} L {col3_x + 200} {col3_y + 270} L {col3_x + 200} {col3_y + 310}" fill="none" stroke="#94a3b8" stroke-width="1.2" stroke-dasharray="5,4"/>
    ''')

    # Almacén de telas
    svg.append(f'''
      <rect x="{col3_x + 75}" y="{col3_y + 12}" width="95" height="32" rx="2" fill="#f1f5f9" stroke="#94a3b8" stroke-width="1"/>
      <text x="{col3_x + 122}" y="{col3_y + 26}" font-size="6.8" font-weight="600" fill="#475569" text-anchor="middle">ALMACÉN DE TELAS</text>
      <text x="{col3_x + 122}" y="{col3_y + 37}" font-size="5.8" fill="#64748b" text-anchor="middle">Bobinas y Rollos</text>
    ''')

    # Racks espumas lateral derecho
    svg.append(f'''
      <rect x="{col3_x + 238}" y="{col3_y + 12}" width="14" height="55" rx="1.5" fill="#f1f5f9" stroke="#94a3b8" stroke-width="1"/>
      <rect x="{col3_x + 224}" y="{col3_y + 80}" width="28" height="75" rx="2" fill="#f1f5f9" stroke="#94a3b8" stroke-width="1"/>
      <text x="{col3_x + 238}" y="{col3_y + 120}" font-size="6" font-weight="600" fill="#475569" text-anchor="middle" transform="rotate(-90 {col3_x + 238} {col3_y + 120})">Racks Espumas</text>
    ''')

    # Corte Láser y Puesto 15: Mesa Despiece (Badge 15)
    svg.append(f'''
      <rect x="{col3_x + 168}" y="{col3_y + 60}" width="50" height="42" rx="3" fill="#dcfce7" stroke="#16a34a" stroke-width="1.6"/>
      <text x="{col3_x + 193}" y="{col3_y + 81}" font-size="7.2" font-weight="700" fill="#15803d" text-anchor="middle">CORTE</text>
      <text x="{col3_x + 193}" y="{col3_y + 92}" font-size="7.2" font-weight="700" fill="#15803d" text-anchor="middle">LÁSER</text>

      <rect x="{col3_x + 148}" y="{col3_y + 110}" width="50" height="18" rx="2" fill="#f1f5f9" stroke="#94a3b8" stroke-width="1"/>
      <circle cx="{col3_x + 173}" cy="{col3_y + 119}" r="6.5" fill="#64748b"/>
      <text x="{col3_x + 173}" y="{col3_y + 121.5}" font-size="6.5" font-weight="700" fill="#ffffff" text-anchor="middle">15</text>
    ''')

    # Puesto 14: Montaje Espuma y Tela (Badge 14)
    svg.append(f'''
      <rect x="{col3_x + 8}" y="{col3_y + 65}" width="24" height="68" rx="2" fill="#dcfce7" stroke="#16a34a" stroke-width="1.4"/>
      <circle cx="{col3_x + 20}" cy="{col3_y + 99}" r="7.5" fill="#16a34a"/>
      <text x="{col3_x + 20}" y="{col3_y + 101.5}" font-size="6.5" font-weight="700" fill="#ffffff" text-anchor="middle">14</text>

      <rect x="{col3_x + 8}" y="{col3_y + 10}" width="28" height="45" rx="2" fill="#f1f5f9" stroke="#94a3b8" stroke-width="1"/>
    ''')

    # Almacén partes tapizadas
    svg.append(f'''
      <rect x="{col3_x + 10}" y="{col3_y + 155}" width="75" height="58" rx="2" fill="#f1f5f9" stroke="#94a3b8" stroke-width="1"/>
      <text x="{col3_x + 47}" y="{col3_y + 185}" font-size="6.8" font-weight="600" fill="#475569" text-anchor="middle">ALMACÉN PARTES</text>
      <text x="{col3_x + 47}" y="{col3_y + 196}" font-size="5.8" fill="#64748b" text-anchor="middle">Tapizadas Listas</text>
    ''')

    # Apertura Clark y Escalera Entrepiso
    svg.append(f'''
      <rect x="{col3_x + 105}" y="{col3_y + col3_h - 18}" width="88" height="18" rx="2" fill="#fef3c7" stroke="#f59e0b" stroke-width="1.4" stroke-dasharray="3,3"/>
      <text x="{col3_x + 149}" y="{col3_y + col3_h - 6}" font-size="6.5" font-weight="700" fill="#b45309" text-anchor="middle">APERTURA CLARK</text>

      <rect x="{col3_x + 202}" y="{col3_y + col3_h - 18}" width="50" height="18" rx="2" fill="#3b82f6"/>
      <text x="{col3_x + 227}" y="{col3_y + col3_h - 6}" font-size="6.5" font-weight="700" fill="#ffffff" text-anchor="middle">ESCALERA</text>
    ''')

    # Cota exterior 160
    svg.append(f'''
      <text x="{col3_x + col3_w + 14}" y="{col3_y + col3_h/2}" font-size="9" font-weight="800" fill="#94a3b8" text-anchor="middle" transform="rotate(90 {col3_x + col3_w + 14} {col3_y + col3_h/2})">160 (16 m)</text>
    ''')


    # =========================================================================
    # COLUMNA 3 ABAJO: PANEL DE REFERENCIAS Y PUESTOS NUMERADOS
    # =========================================================================
    leg_y = 388
    leg_h = 369
    svg.append(f'''
      <g>
        <rect x="{col3_x}" y="{leg_y}" width="{col3_w}" height="{leg_h}" rx="4" fill="#ffffff" stroke="#cbd5e1" stroke-width="1.5" filter="url(#shadow)"/>
        
        <!-- Header de la tarjeta de leyendas -->
        <path d="M {col3_x} {leg_y + 4} a 4 4 0 0 1 4 -4 h {col3_w - 8} a 4 4 0 0 1 4 4 v 24 h -{col3_w} z" fill="#1e293b"/>
        <text x="{col3_x + col3_w/2}" y="{leg_y + 19}" fill="#ffffff" font-size="8.5" font-weight="700" text-anchor="middle">REFERENCIAS DE PLANTA Y PUESTOS</text>
      </g>
    ''')

    # 1. CÓDIGO FUNCIONAL DE SECTORES (ZONAS)
    ly_sec = leg_y + 38
    svg.append(f'''
      <text x="{col3_x + 12}" y="{ly_sec}" font-size="7.5" font-weight="700" fill="#0f172a">1. CÓDIGO DE SECTORES (ZONAS):</text>
      
      <rect x="{col3_x + 14}" y="{ly_sec + 8}" width="12" height="12" rx="2" fill="#ffedd5" stroke="#ea580c"/>
      <text x="{col3_x + 32}" y="{ly_sec + 17}" font-size="6.5" fill="#334155">Curvado y Prensas de Alta Frecuencia (HF)</text>

      <rect x="{col3_x + 14}" y="{ly_sec + 24}" width="12" height="12" rx="2" fill="#e0f2fe" stroke="#0284c7"/>
      <text x="{col3_x + 32}" y="{ly_sec + 33}" font-size="6.5" fill="#334155">Mecanizado CNC / Carpintería Tradicional</text>

      <rect x="{col3_x + 14}" y="{ly_sec + 40}" width="12" height="12" rx="2" fill="#ede9fe" stroke="#7c3aed"/>
      <text x="{col3_x + 32}" y="{ly_sec + 49}" font-size="6.5" fill="#334155">Cabina de Laqueado y Lijado Fino</text>

      <rect x="{col3_x + 14}" y="{ly_sec + 56}" width="12" height="12" rx="2" fill="#dcfce7" stroke="#16a34a"/>
      <text x="{col3_x + 32}" y="{ly_sec + 65}" font-size="6.5" fill="#334155">Corte Láser Textil y Tapicería</text>

      <rect x="{col3_x + 14}" y="{ly_sec + 72}" width="12" height="12" rx="2" fill="#f1f5f9" stroke="#94a3b8"/>
      <text x="{col3_x + 32}" y="{ly_sec + 81}" font-size="6.5" fill="#334155">Almacenamiento e Inventarios en Proceso</text>

      <!-- Línea divisoria sobria -->
      <line x1="{col3_x + 12}" y1="{ly_sec + 92}" x2="{col3_x + col3_w - 12}" y2="{ly_sec + 92}" stroke="#e2e8f0" stroke-width="1"/>
    ''')

    # 2. PUESTOS Y MAQUINARIAS REFERENCIADAS (N.º)
    ly_puestos = ly_sec + 106
    svg.append(f'''
      <text x="{col3_x + 12}" y="{ly_puestos}" font-size="7.5" font-weight="700" fill="#0f172a">2. PUESTOS REFERENCIADOS EN PLANO:</text>
    ''')

    # 15 puestos divididos en 2 columnas:
    # Columna Izquierda: Puestos 1 a 8
    # Columna Derecha: Puestos 9 a 15
    col_left_x = col3_x + 14
    col_right_x = col3_x + 134
    start_y = ly_puestos + 12
    row_gap = 18

    puestos = [
        # Columna 1 (1 a 8)
        (1, "Rectificadora", "#0284c7", col_left_x, start_y + 0*row_gap),
        (2, "Cepilladora", "#0284c7", col_left_x, start_y + 1*row_gap),
        (3, "Espigadora", "#0284c7", col_left_x, start_y + 2*row_gap),
        (4, "Fresadora tupí", "#0284c7", col_left_x, start_y + 3*row_gap),
        (5, "Mortajadora", "#0284c7", col_left_x, start_y + 4*row_gap),
        (6, "Sierra sin fin 1", "#0284c7", col_left_x, start_y + 5*row_gap),
        (7, "Sierra sin fin 2", "#0284c7", col_left_x, start_y + 6*row_gap),
        (8, "Encoladora rodillos", "#ea580c", col_left_x, start_y + 7*row_gap),

        # Columna 2 (9 a 15)
        (9, "Aplicador adhesivo", "#ea580c", col_right_x, start_y + 0*row_gap),
        (10, "Guillotina chapa", "#0284c7", col_right_x, start_y + 1*row_gap),
        (11, "Costura de chapa", "#0284c7", col_right_x, start_y + 2*row_gap),
        (12, "Lijado fino (Diego)", "#ca8a04", col_right_x, start_y + 3*row_gap),
        (13, "Montaje y ensamble", "#16a34a", col_right_x, start_y + 4*row_gap),
        (14, "Montaje espuma/tela", "#16a34a", col_right_x, start_y + 5*row_gap),
        (15, "Mesa de despiece", "#64748b", col_right_x, start_y + 6*row_gap),
    ]

    for num, name, color, px, py in puestos:
        svg.append(f'''
          <circle cx="{px + 6}" cy="{py}" r="6" fill="{color}"/>
          <text x="{px + 6}" y="{py + 2.2}" font-size="6" font-weight="700" fill="#ffffff" text-anchor="middle">{num}</text>
          <text x="{px + 16}" y="{py + 2.8}" font-size="6.5" font-weight="600" fill="#334155">{name}</text>
        ''')

    # Pie de tarjeta con nota técnica
    svg.append(f'''
      <rect x="{col3_x + 12}" y="{start_y + 8*row_gap + 4}" width="{col3_w - 24}" height="20" rx="2" fill="#f8fafc" stroke="#e2e8f0"/>
      <text x="{col3_x + col3_w/2}" y="{start_y + 8*row_gap + 17}" font-size="5.8" fill="#64748b" text-anchor="middle">Plano general a escala · Puestos mayores identificados en plano</text>
    ''')

    svg.append('</svg>')
    return '\n'.join(svg)

if __name__ == '__main__':
    content = generate_svg()
    with open('assets/layout_oficial_planta.svg', 'w', encoding='utf-8') as f:
        f.write(content)
    print("assets/layout_oficial_planta.svg generated successfully with clean badges and references!")

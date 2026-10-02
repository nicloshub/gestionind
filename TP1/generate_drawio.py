import xml.etree.ElementTree as ET
import html

def build_drawio():
    root = ET.Element("mxfile", host="app.diagrams.net", version="24.0.0", type="device")
    diagram = ET.SubElement(root, "diagram", id="cadena_valor_film_stretch", name="Cadena de Valor - Film Stretch")
    graph_model = ET.SubElement(diagram, "mxGraphModel", 
                                dx="2800", dy="1800", grid="1", gridSize="10", 
                                guides="1", tooltips="1", connect="1", arrows="1", 
                                fold="1", page="1", pageScale="1", pageWidth="2600", 
                                pageHeight="1850", background="#F8FAFC", math="0", shadow="0")
    
    root_cell = ET.SubElement(graph_model, "root")
    
    cell_id_counter = 0
    def new_id():
        nonlocal cell_id_counter
        cid = str(cell_id_counter)
        cell_id_counter += 1
        return cid

    # Default cells 0 and 1
    c0 = ET.SubElement(root_cell, "mxCell", id=new_id())
    c1 = ET.SubElement(root_cell, "mxCell", id=new_id(), parent="0")

    def add_cell(value, style, x, y, w, h, parent="1", is_vertex=True):
        cid = new_id()
        cell = ET.SubElement(root_cell, "mxCell", id=cid, value=value, style=style, parent=parent)
        if is_vertex:
            cell.set("vertex", "1")
            geo = ET.SubElement(cell, "mxGeometry", x=str(x), y=str(y), width=str(w), height=str(h))
            geo.set("as", "geometry")
        return cid

    def add_edge(value, style, source_id, target_id, points=None, parent="1"):
        cid = new_id()
        cell = ET.SubElement(root_cell, "mxCell", id=cid, value=value, style=style, parent=parent, edge="1")
        if source_id:
            cell.set("source", source_id)
        if target_id:
            cell.set("target", target_id)
        geo = ET.SubElement(cell, "mxGeometry", relative="1")
        geo.set("as", "geometry")
        if points:
            arr = ET.SubElement(geo, "Array")
            arr.set("as", "points")
            for px, py in points:
                pt = ET.SubElement(arr, "mxPoint", x=str(px), y=str(py))
        return cid

    # ----------------------------------------------------
    # 1. HEADER SECTION
    # ----------------------------------------------------
    # Main Title Box
    title_html = (
        "<div style='text-align: left; font-family: Inter, Arial, sans-serif;'>"
        "<div style='font-size: 26px; font-weight: 800; color: #0F172A; letter-spacing: -0.5px;'>"
        "CADENA DE VALOR DEL FILM STRETCH PARA PALLETS (PEBDL / LLDPE)"
        "</div>"
        "<div style='font-size: 15px; font-weight: 600; color: #1E3A8A; margin-top: 4px;'>"
        "Desde la extracción de hidrocarburos hasta el postconsumo logístico B2B y su recirculación circular"
        "</div>"
        "<div style='font-size: 12px; color: #475569; margin-top: 3px;'>"
        "Análisis integral de etapas, actores, entradas, procesos industriales, salidas, pérdidas de valor y estrategias de circularidad 4.0"
        "</div>"
        "</div>"
    )
    add_cell(title_html, "text;html=1;align=left;verticalAlign=middle;resizable=0;points=[];autosize=0;strokeColor=none;fillColor=none;", 50, 25, 1300, 75)

    # Product Overview Card
    prod_html = (
        "<div style='font-family: Inter, Arial, sans-serif; text-align: left;'>"
        "<div style='font-size: 11px; font-weight: 800; color: #1E3A8A; text-transform: uppercase; letter-spacing: 0.5px;'>Producto Representativo</div>"
        "<div style='font-size: 13px; font-weight: 700; color: #0F172A; margin-top: 2px;'>Film Stretch para Pallets (PEBDL / LLDPE)</div>"
        "<div style='font-size: 11px; color: #334155; margin-top: 4px; line-height: 1.3;'>"
        "• <b>Aplicación:</b> Flexible logístico para unitización y contención.<br>"
        "• <b>Resina:</b> Polietileno lineal de baja densidad (Monomaterial).<br>"
        "• <b>Vida útil:</b> Muy corta (Uso único por pallet / Alta rotación B2B).<br>"
        "• <b>Normas clave:</b> ASTM D4649, ASTM D2103, ISO 17855, EUMOS 40509."
        "</div>"
        "</div>"
    )
    add_cell(prod_html, "rounded=1;whiteSpace=wrap;html=1;fillColor=#EFF6FF;strokeColor=#BFDBFE;strokeWidth=1.5;arcSize=8;align=left;spacing=10;", 1400, 20, 520, 85)

    # Legend Card
    legend_html = (
        "<div style='font-family: Inter, Arial, sans-serif; font-size: 10.5px; text-align: left; line-height: 1.4; color: #1E293B;'>"
        "<div style='font-weight: 800; color: #0F172A; margin-bottom: 2px;'>LEYENDA DE FLUJOS Y CIRCULARIDAD</div>"
        "<div><span style='color:#2563EB; font-weight:bold;'>━━━</span> Flujo Principal de Material (Lineal / Productivo)</div>"
        "<div><span style='color:#16A34A; font-weight:bold;'>- - -</span> Flujo de Reciclaje Mecánico B2B / PCR</div>"
        "<div><span style='color:#9333EA; font-weight:bold;'>- - -</span> Bucle Scrap Pre-consumo (Refilado / Planta)</div>"
        "<div><span style='color:#DC2626; font-weight:bold;'>- - -</span> Mermas, Emisiones y Descarte Residual</div>"
        "<div style='margin-top:2px;'><b>Niveles:</b> <span style='color:#16A34A;'>●</span> Alto (PCR cerrada) &nbsp; <span style='color:#EAB308;'>●</span> Medio (Downcycling) &nbsp; <span style='color:#DC2626;'>●</span> Pérdida</div>"
        "</div>"
    )
    add_cell(legend_html, "rounded=1;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#CBD5E1;strokeWidth=1;arcSize=8;align=left;spacing=8;", 1940, 20, 510, 85)

    # ----------------------------------------------------
    # 2. TOP CIRCULARITY ARCS (Banner / Loops)
    # ----------------------------------------------------
    loop_banner_html = (
        "<div style='font-family: Inter, Arial, sans-serif; font-size: 12px; font-weight: 700; color: #166534; text-align: center; letter-spacing: 0.5px;'>"
        "⟳ BUCLES DE RETORNO Y RECIRCULACIÓN CIRCULAR (RECUPERACIÓN DE RESINAS Y MATERIALES) ⟲"
        "</div>"
    )
    add_cell(loop_banner_html, "rounded=1;whiteSpace=wrap;html=1;fillColor=#DCFCE7;strokeColor=#86EFAC;strokeWidth=1;arcSize=20;align=center;", 750, 115, 1000, 26)

    # ----------------------------------------------------
    # 3. THE 8 MAIN STAGES
    # ----------------------------------------------------
    stages_data = [
        {
            "num": "1",
            "title": "SECTOR PRIMARIO\n(Extracción)",
            "header_color": "#1E3A8A",
            "bg_color": "#F8FAFC",
            "border_color": "#CBD5E1",
            "badge_color": "#1E40AF",
            "icon": "⛽ 🛢️",
            "actores": "• Empresas energéticas y gasíferas (YPF, Pampa Energía, Tecpetrol)\n• Cuenca Neuquina (Vaca Muerta)\n• Transporte por gasoducto (TGS)",
            "entradas": "• Yacimientos de gas natural y petróleo crudo\n• Agua de proceso e insumos químicos\n• Energía térmica y eléctrica",
            "procesos": "• Perforación y extracción de gas natural húmedo\n• Separación primaria y fraccionamiento\n• Acondicionamiento de etano en Planta Mega",
            "salidas": "• Corriente rica en Etano (líquido/gas)\n• Gas metano a red (CH₄)\n• Emisiones fugitivas y barros de perforación",
            "escala": "Nacional / Global",
            "escala_bg": "#DBEAFE",
            "escala_fg": "#1E40AF"
        },
        {
            "num": "2",
            "title": "PETROQUÍMICA BASE\n(Cracking y Resina)",
            "header_color": "#0284C7",
            "bg_color": "#F8FAFC",
            "border_color": "#CBD5E1",
            "badge_color": "#0369A1",
            "icon": "🏭 🔬",
            "actores": "• Dow Argentina (Polo Petroquímico Bahía Blanca)\n• PBB Polisur\n• Proveedores de comonómeros y catalizadores",
            "entradas": "• Etano por gasoducto dedicado\n• Catalizadores Ziegler-Natta o metalocenos\n• Comonómeros (1-buteno, 1-hexeno, 1-octeno)\n• Energía eléctrica y vapor a alta presión",
            "procesos": "• Craqueo térmico de etano (pirólisis a 800°C)\n• Purificación y fraccionamiento criogénico\n• Polimerización en fase gaseosa / solución\n• Granulado en pellets vírgenes de PEBDL (LLDPE)",
            "salidas": "• Pellets vírgenes de PEBDL (MFI ~1.5 - 3.5 g/10min)\n• Subproductos: Hidrógeno (H₂), etileno residual\n• Emisiones de CO₂ y calor residual",
            "escala": "Nacional / Regional",
            "escala_bg": "#E0F2FE",
            "escala_fg": "#0369A1"
        },
        {
            "num": "3",
            "title": "COMPOUND Y\nFORMULACIÓN",
            "header_color": "#0D9488",
            "bg_color": "#F8FAFC",
            "border_color": "#CBD5E1",
            "badge_color": "#0F766E",
            "icon": "🧪 📦",
            "actores": "• Formuladores de aditivos (Clariant, Masterbatchers)\n• Extrusores integrados\n• Proveedores de resina reciclada PCR",
            "entradas": "• Pellets vírgenes de PEBDL / mLLDPE\n• Aditivos tackificantes (PIB - poliisobutileno para cling)\n• Resina reciclada postconsumo (R-PEBDL 20-50%)\n• Deslizantes internos, estabilizantes UV, antioxidantes",
            "procesos": "• Dosificación gravimétrica de alta precisión\n• Mezcla seca y extrusión de masterbatch\n• Calibración de índice de fluidez (MFI) y elasticidad\n• Ensayos reológicos de compatibilización",
            "salidas": "• Mezcla formulada lista para tolva de extrusión\n• Mermas de purga y polvo de aditivos",
            "escala": "Nacional",
            "escala_bg": "#CCFBF1",
            "escala_fg": "#0F766E"
        },
        {
            "num": "4",
            "title": "TRANSFORMACIÓN\n(Extrusión Cast Film)",
            "header_color": "#7C3AED",
            "bg_color": "#F8FAFC",
            "border_color": "#CBD5E1",
            "badge_color": "#6D28D9",
            "icon": "⚙️ 🎞️",
            "actores": "• Fabricantes / extrusores de film stretch\n  (Rok Stretch, SonFuertes, Embafor, AMBA)\n• Operadores técnicos y control de calidad",
            "entradas": "• Mezcla de PEBDL virgen + PCR + aditivos\n• Scrap pre-consumo triturado (bucle interno)\n• Tubos de cartón/plástico (mandriles/cores)\n• Energía eléctrica y agua de enfriamiento (chiller)",
            "procesos": "• Extrusión plana multicapa (Cast film 3 a 55 capas)\n• Salida de labio plano sobre rodillos enfriadores\n• Enfriamiento rápido (quench roll) para transparencia\n• Refilado lateral y bobinado automático",
            "salidas": "• Bobinas de film stretch manual (10-15 µm)\n• Bobinas de film stretch automático (17-30 µm)\n• Scrap de refilado y despunte (Scrap pre-consumo)\n• Pérdidas térmicas",
            "escala": "Nacional / AMBA",
            "escala_bg": "#EDE9FE",
            "escala_fg": "#6D28D9"
        },
        {
            "num": "5",
            "title": "APLICACIÓN Y\nENFARDADO LOGÍSTICO",
            "header_color": "#2563EB",
            "bg_color": "#F8FAFC",
            "border_color": "#CBD5E1",
            "badge_color": "#1D4ED8",
            "icon": "📦 🔄",
            "actores": "• Titular de la carga / Empresas envasadoras\n  (Consumo masivo, bebidas, alimentos, retail)\n• Operarios de almacén y enfardadoras automáticas\n• Responsables de seguridad y embalaje (REP)",
            "entradas": "• Pallets con mercadería unitizada (cajas, bidones)\n• Bobinas de film stretch de PEBDL\n• Energía eléctrica para máquinas envolvedoras",
            "procesos": "• Aplicación manual con aplicador o enfardadora de plato\n• Pre-estiramiento motorizado (150% a 300% según film)\n• Cantidad de vueltas de refuerzo en base y corona\n• Corte y sellado del extremo final\n• Validación de sujeción dinámica (EUMOS 40509)",
            "salidas": "• Pallet unitizado y estabilizado listo para transporte\n• Mandriles de cartón vacíos (scrap reciclable)\n• Despunte de film de inicio/fin de bobina",
            "escala": "Nacional / Regional",
            "escala_bg": "#DBEAFE",
            "escala_fg": "#1D4ED8"
        },
        {
            "num": "6",
            "title": "DISTRIBUCIÓN Y\nTRANSPORTE B2B",
            "header_color": "#475569",
            "bg_color": "#F8FAFC",
            "border_color": "#CBD5E1",
            "badge_color": "#334155",
            "icon": "🚛 🏢",
            "actores": "• Empresas de transporte de carga y logística B2B\n• Operadores 3PL / Depósitos fiscales\n• Choferes y supervisores de ruta",
            "entradas": "• Pallets enfardados en camiones semirremolque\n• Combustible diésel y energía logística",
            "procesos": "• Traslado interprovincial e interurbano (50 a 1500 km)\n• Sometimiento a vibraciones, aceleración y frenadas\n• Transbordo en centros de cross-docking\n• Control de integridad del film protector contra humedad y polvo",
            "salidas": "• Cargas intactas entregadas en destino\n• Emisiones de transporte (GEI: CO₂, NOx)\n• Casos de rotura o enganche de film (merma en tránsito)",
            "escala": "Provincial / Nacional",
            "escala_bg": "#F1F5F9",
            "escala_fg": "#334155"
        },
        {
            "num": "7",
            "title": "USO Y DESPALETIZADO\n(Recepción y Quitado)",
            "header_color": "#D97706",
            "bg_color": "#F8FAFC",
            "border_color": "#CBD5E1",
            "badge_color": "#B45309",
            "icon": "🏬 ✂️",
            "actores": "• Centros de distribución mayoristas y supermercados\n  (Grandes generadores B2B: Coto, Carrefour, etc.)\n• Operarios de despaletizado y recepción",
            "entradas": "• Pallets arribados a muelle de descarga\n• Herramientas de corte seguro (cutters protegidos)",
            "procesos": "• Corte vertical del film stretch envolvente\n• Retiro manual del film y desenrollado\n• Despaletizado y acomodo de mercadería en racks\n• Acopio inmediato en jaulas o bolsones dedicados",
            "salidas": "• Mercadería lista para reposición o venta\n• Film stretch sucio o descartado (Residuo B2B concentrado)\n• Contaminación accidental con cintas adhesivas y etiquetas",
            "escala": "Local / Urbano",
            "escala_bg": "#FEF3C7",
            "escala_fg": "#B45309"
        },
        {
            "num": "8",
            "title": "POSTCONSUMO, GESTIÓN\nY RECICLAJE B2B",
            "header_color": "#16A34A",
            "bg_color": "#F8FAFC",
            "border_color": "#CBD5E1",
            "badge_color": "#15803D",
            "icon": "♻️ 🔄",
            "actores": "• Recuperadores urbanos y cooperativas de reciclaje\n• Empresas recicladoras de plásticos (B2B)\n• Fabricantes de pellets reciclados de PEBDL",
            "entradas": "• Film stretch descartado en grandes fardos limpios\n• Agua de lavado y detergentes industriales\n• Energía eléctrica en líneas de reciclado mecánico",
            "procesos": "• Clasificación manual (separación de PVC, etiquetas y flejes)\n• Lavado intensivo en balsa de flotación (PE flota)\n• Secado centrífugo y trituración a escamas (flakes)\n• Extrusión con desgasificado al vacío y re-peletizado",
            "salidas": "• Pellets de PEBDL reciclado (R-LLDPE / PCR)\n• Efluentes líquidos (aguas de lavado tratadas)\n• Rechazos no reciclables a disposición final",
            "escala": "Regional / Nacional",
            "escala_bg": "#DCFCE7",
            "escala_fg": "#15803D"
        }
    ]

    col_w = 285
    col_gap = 25
    start_x = 50
    start_y = 160
    card_h = 670

    stage_node_ids = []

    for i, s in enumerate(stages_data):
        cur_x = start_x + i * (col_w + col_gap)
        
        # Outer Card Container
        card_style = (
            f"rounded=1;whiteSpace=wrap;html=1;fillColor={s['bg_color']};strokeColor={s['border_color']};"
            f"strokeWidth=1.5;arcSize=4;shadow=0;"
        )
        card_id = add_cell("", card_style, cur_x, start_y, col_w, card_h)
        stage_node_ids.append(card_id)

        # Header Box with Number and Title
        header_html = (
            f"<div style='font-family: Inter, Arial, sans-serif; text-align: center;'>"
            f"<span style='background-color: {s['badge_color']}; color: #FFFFFF; font-size: 11px; font-weight: 800; "
            f"padding: 2px 7px; border-radius: 10px; display: inline-block; margin-bottom: 4px;'>ETAPA {s['num']}</span>"
            f"<div style='font-size: 12.5px; font-weight: 800; color: #FFFFFF; line-height: 1.2; text-transform: uppercase;'>"
            f"{s['title'].replace(chr(10), '<br>')}"
            f"</div>"
            f"</div>"
        )
        add_cell(header_html, f"rounded=1;whiteSpace=wrap;html=1;fillColor={s['header_color']};strokeColor=none;arcSize=6;align=center;spacing=6;", cur_x + 6, start_y + 6, col_w - 12, 60)

        # Icon Box
        icon_html = f"<div style='font-size: 24px; text-align: center; line-height: 32px;'>{s['icon']}</div>"
        add_cell(icon_html, "rounded=1;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#E2E8F0;strokeWidth=1;align=center;", cur_x + 12, start_y + 72, col_w - 24, 34)

        # Content Section Boxes inside Card
        curr_y = start_y + 112
        
        def make_section(title, text, color_title, fill_c, height_box):
            nonlocal curr_y
            sec_html = (
                f"<div style='font-family: Inter, Arial, sans-serif; font-size: 10px; text-align: left; line-height: 1.35;'>"
                f"<div style='font-weight: 800; color: {color_title}; text-transform: uppercase; font-size: 9.5px; margin-bottom: 2px;'>"
                f"{title}</div>"
                f"<div style='color: #1E293B;'>{text.replace(chr(10), '<br>')}</div>"
                f"</div>"
            )
            add_cell(sec_html, f"rounded=1;whiteSpace=wrap;html=1;fillColor={fill_c};strokeColor=#E2E8F0;strokeWidth=1;arcSize=4;align=left;spacing=6;", 
                     cur_x + 10, curr_y, col_w - 20, height_box)
            curr_y += height_box + 6

        make_section("Actores Clave", s['actores'], "#1E40AF", "#FFFFFF", 95)
        make_section("Entradas (Insumos/Energía)", s['entradas'], "#0369A1", "#F0F9FF", 110)
        make_section("Procesos Principales", s['procesos'], "#4338CA", "#FFFFFF", 125)
        make_section("Salidas (Productos/Mermas)", s['salidas'], "#B91C1C", "#FFF1F2", 110)

        # Escala Territorial Badge at Bottom
        escala_html = (
            f"<div style='font-family: Inter, Arial, sans-serif; font-size: 9.5px; font-weight: 700; color: {s['escala_fg']}; text-align: center;'>"
            f"📍 Escala: {s['escala']}</div>"
        )
        add_cell(escala_html, f"rounded=1;whiteSpace=wrap;html=1;fillColor={s['escala_bg']};strokeColor=none;arcSize=8;align=center;", 
                 cur_x + 12, start_y + card_h - 32, col_w - 24, 22)

    # ----------------------------------------------------
    # 4. HORIZONTAL FORWARD ARROWS BETWEEN STAGES
    # ----------------------------------------------------
    for i in range(len(stage_node_ids) - 1):
        add_edge("", "edgeStyle=orthogonalEdgeStyle;rounded=1;orthogonalLoop=1;jettySize=auto;html=1;strokeColor=#2563EB;strokeWidth=3;endArrow=block;endFill=1;", 
                 stage_node_ids[i], stage_node_ids[i+1])

    # ----------------------------------------------------
    # 5. CIRCULARITY RECIRCULATION BUFFERS / LOOPS (MIDDLE)
    # ----------------------------------------------------
    mid_y = 855

    # 5.1 Scrap Pre-Consumo (under stage 4)
    pre_scrap_html = (
        "<div style='font-family: Inter, Arial, sans-serif; text-align: center;'>"
        "<span style='background-color: #7C3AED; color: #FFF; font-size: 9px; font-weight: 800; padding: 2px 6px; border-radius: 8px;'>BUCLE PRE-CONSUMO</span>"
        "<div style='font-size: 11.5px; font-weight: 800; color: #4C1D95; margin-top: 3px;'>SCRAP INDUSTRIAL INTERNO</div>"
        "<div style='font-size: 10px; color: #334155; margin-top: 2px; line-height: 1.25;'>"
        "Refilado de bordes, recortes y bobinas falladas se muelen en línea y retornan <b>100% a tolva</b> sin perder calidad."
        "</div>"
        "</div>"
    )
    pre_scrap_id = add_cell(pre_scrap_html, "rounded=1;whiteSpace=wrap;html=1;fillColor=#F3E8FF;strokeColor=#C084FC;strokeWidth=1.5;arcSize=6;align=center;spacing=6;", 
                            start_x + 3 * (col_w + col_gap), mid_y, col_w, 75)

    # 5.2 Reciclaje Mecánico B2B (between stage 7 & 8)
    mec_scrap_html = (
        "<div style='font-family: Inter, Arial, sans-serif; text-align: center;'>"
        "<span style='background-color: #16A34A; color: #FFF; font-size: 9px; font-weight: 800; padding: 2px 6px; border-radius: 8px;'>BUCLE POST-CONSUMO PRINCIPAL</span>"
        "<div style='font-size: 11.5px; font-weight: 800; color: #14532D; margin-top: 3px;'>RECICLAJE MECÁNICO B2B (R-PEBDL)</div>"
        "<div style='font-size: 10px; color: #334155; margin-top: 2px; line-height: 1.25;'>"
        "Acopio limpio en centros logísticos ➔ Lavado y secado ➔ Peletizado de resina reciclada (PCR) de alta pureza."
        "</div>"
        "</div>"
    )
    mec_scrap_id = add_cell(mec_scrap_html, "rounded=1;whiteSpace=wrap;html=1;fillColor=#DCFCE7;strokeColor=#86EFAC;strokeWidth=1.5;arcSize=6;align=center;spacing=6;", 
                            start_x + 6 * (col_w + col_gap) - 140, mid_y, col_w + 140, 75)

    # 5.3 Mercado de Reincorporación (R-PEBDL)
    mercado_pcr_html = (
        "<div style='font-family: Inter, Arial, sans-serif; text-align: center;'>"
        "<span style='background-color: #0284C7; color: #FFF; font-size: 9px; font-weight: 800; padding: 2px 6px; border-radius: 8px;'>MERCADO DEL MATERIAL RECUPERADO</span>"
        "<div style='font-size: 11.5px; font-weight: 800; color: #0C4A6E; margin-top: 3px;'>APLICACIONES DE PEBDL RECICLADO</div>"
        "<div style='font-size: 10px; color: #334155; margin-top: 2px; line-height: 1.25;'>"
        "• <b>Nuevo Film Stretch con PCR (30-50%)</b> | Bolsas de consorcio e industriales | Madera plástica y tarimas | Caños y tubos."
        "</div>"
        "</div>"
    )
    mercado_pcr_id = add_cell(mercado_pcr_html, "rounded=1;whiteSpace=wrap;html=1;fillColor=#E0F2FE;strokeColor=#7DD3FC;strokeWidth=1.5;arcSize=6;align=center;spacing=6;", 
                              start_x + 2 * (col_w + col_gap), mid_y, col_w + 20, 75)

    # 5.4 Disposición Final / Downcycling
    disp_html = (
        "<div style='font-family: Inter, Arial, sans-serif; text-align: center;'>"
        "<span style='background-color: #64748B; color: #FFF; font-size: 9px; font-weight: 800; padding: 2px 6px; border-radius: 8px;'>FIN DE CICLO</span>"
        "<div style='font-size: 11.5px; font-weight: 800; color: #334155; margin-top: 3px;'>DISPOSICIÓN RESIDUAL</div>"
        "<div style='font-size: 10px; color: #475569; margin-top: 2px; line-height: 1.25;'>"
        "Relleno sanitario controlado o valorización energética para fracciones altamente contaminadas."
        "</div>"
        "</div>"
    )
    disp_id = add_cell(disp_html, "rounded=1;whiteSpace=wrap;html=1;fillColor=#F1F5F9;strokeColor=#CBD5E1;strokeWidth=1;arcSize=6;align=center;spacing=6;", 
                       start_x + 7 * (col_w + col_gap), mid_y, col_w, 75)

    # Connecting loop edges
    # Top curved arrow from stage 8 back to stage 4 (Extrusion)
    add_edge("Retorno de Resina Reciclada (PCR)", 
             "edgeStyle=curved;html=1;strokeColor=#16A34A;strokeWidth=2.5;strokeFactor=1;dashed=1;dashPattern=6 4;endArrow=block;endFill=1;fontSize=10;fontColor=#15803D;fontStyle=1;align=center;", 
             stage_node_ids[7], stage_node_ids[3], 
             points=[(start_x + 7 * (col_w + col_gap) + 140, 140), (start_x + 5 * (col_w + col_gap), 125), (start_x + 3 * (col_w + col_gap) + 140, 140)])

    # Top curved arrow from stage 8 back to stage 3 (Compound)
    add_edge("Inclusión en Formulación", 
             "edgeStyle=curved;html=1;strokeColor=#0D9488;strokeWidth=2;dashed=1;dashPattern=4 4;endArrow=block;endFill=1;fontSize=9;fontColor=#0F766E;align=center;", 
             stage_node_ids[7], stage_node_ids[2], 
             points=[(start_x + 7 * (col_w + col_gap) + 140, 130), (start_x + 4 * (col_w + col_gap), 115), (start_x + 2 * (col_w + col_gap) + 140, 130)])

    # Pre-consumo loop on stage 4
    add_edge("100% Reincorporación In-situ", 
             "edgeStyle=curved;html=1;strokeColor=#7C3AED;strokeWidth=2.5;dashed=1;dashPattern=4 3;endArrow=block;endFill=1;fontSize=9.5;fontColor=#6D28D9;fontStyle=1;", 
             stage_node_ids[3], pre_scrap_id, 
             points=[(start_x + 3 * (col_w + col_gap) + 70, start_y + card_h + 10)])
    
    add_edge("", 
             "edgeStyle=curved;html=1;strokeColor=#7C3AED;strokeWidth=2.5;dashed=1;dashPattern=4 3;endArrow=block;endFill=1;", 
             pre_scrap_id, stage_node_ids[3], 
             points=[(start_x + 3 * (col_w + col_gap) + 210, start_y + card_h + 10)])

    # Edge from Stage 8 to Mecánico
    add_edge("", "edgeStyle=orthogonalEdgeStyle;rounded=1;html=1;strokeColor=#16A34A;strokeWidth=2;dashed=1;endArrow=block;endFill=1;", 
             stage_node_ids[7], mec_scrap_id)
    # Edge from Mecánico to Mercado PCR
    add_edge("Pellets PCR R-PEBDL", "edgeStyle=orthogonalEdgeStyle;rounded=1;html=1;strokeColor=#16A34A;strokeWidth=2;dashed=1;endArrow=block;endFill=1;fontSize=10;fontColor=#15803D;fontStyle=1;", 
             mec_scrap_id, mercado_pcr_id)
    # Edge from Mercado PCR to Stage 4
    add_edge("Alimentación a Extrusión", "edgeStyle=orthogonalEdgeStyle;rounded=1;html=1;strokeColor=#0284C7;strokeWidth=2;dashed=1;endArrow=block;endFill=1;fontSize=9.5;fontColor=#0369A1;", 
             mercado_pcr_id, stage_node_ids[3])
    # Edge to Disposición
    add_edge("Rechazos no reciclables", "edgeStyle=orthogonalEdgeStyle;rounded=1;html=1;strokeColor=#94A3B8;strokeWidth=1.5;dashed=1;endArrow=block;endFill=1;fontSize=9;fontColor=#64748B;", 
             stage_node_ids[7], disp_id)

    # ----------------------------------------------------
    # 6. LOWER PANELS: PUNTOS CRÍTICOS, ESTRATEGIAS, JERARQUÍA
    # ----------------------------------------------------
    low_y = 960

    # Panel 1: Puntos Críticos de la Cadena (Width: 620)
    crit_w = 600
    crit_html = (
        "<div style='font-family: Inter, Arial, sans-serif; text-align: left;'>"
        "<div style='background-color: #FEE2E2; border-left: 4px solid #EF4444; padding: 6px 10px; border-radius: 4px;'>"
        "<span style='font-size: 13px; font-weight: 800; color: #991B1B;'>⚠️ PUNTOS CRÍTICOS Y CUELLOS DE BOTELLA</span>"
        "</div>"
        "<div style='margin-top: 10px; font-size: 10.5px; line-height: 1.4; color: #1E293B;'>"
        
        "<div style='margin-bottom: 8px; background: #FFF; padding: 8px; border-radius: 6px; border: 1px solid #FECACA;'>"
        "<b style='color: #B91C1C;'>1. Vida Útil Ultracorta y Escala Masiva:</b><br>"
        "Se usa solo una vez por pallet (horas o días en tránsito). Se genera como desecho masivo en cada descarga de mercadería en centros logísticos y supermercados."
        "</div>"

        "<div style='margin-bottom: 8px; background: #FFF; padding: 8px; border-radius: 6px; border: 1px solid #FECACA;'>"
        "<b style='color: #B91C1C;'>2. Contaminación en Segregación B2B:</b><br>"
        "La mezcla con cintas adhesivas (BOPP/adhesivo acrílico), etiquetas de papel y polvo en depósitos altera drásticamente el índice de fluidez (MFI) e introduce infusibles en el reproceso."
        "</div>"

        "<div style='margin-bottom: 8px; background: #FFF; padding: 8px; border-radius: 6px; border: 1px solid #FECACA;'>"
        "<b style='color: #B91C1C;'>3. Pérdida de Propiedades Mecánicas (EUMOS 40509):</b><br>"
        "La reincorporación de PCR puede reducir la elongación y resistencia a la punción si no se controla rigurosamente, poniendo en riesgo la estabilidad del pallet en camión."
        "</div>"

        "<div style='background: #FFF; padding: 8px; border-radius: 6px; border: 1px solid #FECACA;'>"
        "<b style='color: #B91C1C;'>4. Trazabilidad y Homogeneidad de Lotes:</b><br>"
        "Variabilidad entre lotes de recuperadores informales. Dificultad para garantizar trazabilidad por segregación física frente a esquemas de balance de masa."
        "</div>"

        "</div>"
        "</div>"
    )
    add_cell(crit_html, "rounded=1;whiteSpace=wrap;html=1;fillColor=#FFF5F5;strokeColor=#FCA5A5;strokeWidth=1.5;arcSize=4;align=left;spacing=10;", 
             start_x, low_y, crit_w, 350)

    # Panel 2: Estrategias de Economía Circular 4.0 (Width: 1100)
    strat_w = 1140
    strat_x = start_x + crit_w + 30
    strat_html = (
        "<div style='font-family: Inter, Arial, sans-serif; text-align: left;'>"
        "<div style='background-color: #DCFCE7; border-left: 4px solid #16A34A; padding: 6px 10px; border-radius: 4px;'>"
        "<span style='font-size: 13px; font-weight: 800; color: #14532D;'>💡 ESTRATEGIAS DE ECONOMÍA CIRCULAR 4.0 E INTERVENCIÓN PRIORITARIA</span>"
        "</div>"
        "<div style='display: flex; gap: 12px; margin-top: 10px; font-size: 10.5px; line-height: 1.4; color: #1E293B;'>"
        
        # Col A
        "<div style='background: #FFF; padding: 10px; border-radius: 6px; border: 1px solid #BBF7D0; width: 48%;'>"
        "<div style='font-size: 11.5px; font-weight: 800; color: #15803D; margin-bottom: 4px;'>A. REDISEÑO Y NANO-EXTRUSIÓN (REDUCCIÓN EN ORIGEN)</div>"
        "• <b>Tecnología Nano-Layer (33 a 55 capas):</b> Estructuras micro-estratificadas que combinan capas de rigidez y tenacidad, permitiendo reducir espesor de <b>23 µm a 12-15 µm</b>.<br>"
        "• <b>Ahorro de material:</b> Hasta <b>40% menos de resina PEBDL por pallet</b>, manteniendo idéntica fuerza de retención de carga.<br>"
        "• <b>Pre-estiramiento en máquina (>300%):</b> Enfardadoras automáticas motorizadas que multiplican la longitud del film antes de envolver el pallet.<br>"
        "• <b>Sensorización IoT:</b> Medición del par y tensión para calibrar número exacto de vueltas según peso y centro de gravedad."
        "</div>"

        # Col B
        "<div style='background: #FFF; padding: 10px; border-radius: 6px; border: 1px solid #BBF7D0; width: 48%;'>"
        "<div style='font-size: 11.5px; font-weight: 800; color: #15803D; margin-bottom: 4px;'>B. CIERRE DE CIRCUITO B2B Y REINCORPORACIÓN DE PCR</div>"
        "• <b>Convenios de Logística Inversa Limpia:</b> Retiro programado de fardos de stretch limpio directamente en centros de distribución de supermercados.<br>"
        "• <b>Film Co-extruido con PCR (Core/Skin):</b> Estructura A-B-A donde la capa central (B) contiene 30% a 50% de PEBDL reciclado (PCR) y las capas exteriores (A) resina virgen para retener adhesividad (cling).<br>"
        "• <b>Ensayos dinámicos rigurosos (EUMOS 40509 / ASTM D4649):</b> Verificación de deformación elástica y retención de carga sin comprometer seguridad vial.<br>"
        "• <b>Trazabilidad Digital:</b> Registro de lotes de material recuperado bajo esquemas de Balance de Masa y certificación de contenido reciclado."
        "</div>"

        "</div>"
        "</div>"
    )
    add_cell(strat_html, "rounded=1;whiteSpace=wrap;html=1;fillColor=#F0FDF4;strokeColor=#86EFAC;strokeWidth=1.5;arcSize=4;align=left;spacing=10;", 
             strat_x, low_y, strat_w, 350)

    # Panel 3: Jerarquía de Recuperación (Width: 620)
    hier_w = 640
    hier_x = strat_x + strat_w + 30
    hier_html = (
        "<div style='font-family: Inter, Arial, sans-serif; text-align: left;'>"
        "<div style='background-color: #EDE9FE; border-left: 4px solid #7C3AED; padding: 6px 10px; border-radius: 4px;'>"
        "<span style='font-size: 13px; font-weight: 800; color: #5B21B6;'>📊 JERARQUÍA DE CIRCULARIDAD (PEBDL)</span>"
        "</div>"
        "<div style='margin-top: 10px; font-size: 10.5px; line-height: 1.35; color: #1E293B;'>"
        
        "<div style='background: #FFF; padding: 6px 8px; border-radius: 4px; margin-bottom: 5px; border-left: 4px solid #16A34A;'>"
        "<b>1. REDUCIR (Prioridad Máxima):</b> Nano-films ultradelgados (12 µm) y cálculo optimizado de vueltas por pallet."
        "</div>"

        "<div style='background: #FFF; padding: 6px 8px; border-radius: 4px; margin-bottom: 5px; border-left: 4px solid #22C55E;'>"
        "<b>2. REUTILIZAR:</b> Fundas elásticas reutilizables y cinchas para distribución en bucle cautivo interno."
        "</div>"

        "<div style='background: #FFF; padding: 6px 8px; border-radius: 4px; margin-bottom: 5px; border-left: 4px solid #EAB308;'>"
        "<b>3. RECICLAJE MECÁNICO CERRADO (B2B):</b> Reprocesado a pellets R-PEBDL para nuevo film stretch con PCR."
        "</div>"

        "<div style='background: #FFF; padding: 6px 8px; border-radius: 4px; margin-bottom: 5px; border-left: 4px solid #F97316;'>"
        "<b>4. RECICLAJE ABIERTO (Downcycling):</b> Bolsas de residuos industriales, caños de polietileno, tarimas y madera plástica."
        "</div>"

        "<div style='background: #FFF; padding: 6px 8px; border-radius: 4px; margin-bottom: 5px; border-left: 4px solid #8B5CF6;'>"
        "<b>5. RECICLAJE QUÍMICO:</b> Pirólisis de fracciones mezcladas/contaminadas para obtener nafta química."
        "</div>"

        "<div style='background: #FFF; padding: 6px 8px; border-radius: 4px; border-left: 4px solid #64748B;'>"
        "<b>6. DISPOSICIÓN FINAL:</b> Relleno sanitario exclusivo para mermas no valorizables."
        "</div>"

        "</div>"
        "</div>"
    )
    add_cell(hier_html, "rounded=1;whiteSpace=wrap;html=1;fillColor=#FAF5FF;strokeColor=#D8B4FE;strokeWidth=1.5;arcSize=4;align=left;spacing=10;", 
             hier_x, low_y, hier_w, 350)

    # ----------------------------------------------------
    # 7. BOTTOM BANNER: MENSAJE CENTRAL Y CONCLUSIÓN
    # ----------------------------------------------------
    banner_y = 1335
    banner_html = (
        "<div style='font-family: Inter, Arial, sans-serif; text-align: center; color: #0F172A;'>"
        "<div style='font-size: 15px; font-weight: 800; color: #1E3A8A; letter-spacing: 0.5px; text-transform: uppercase;'>"
        "🌱 MENSAJE CENTRAL: LA CIRCULARIDAD EN LOGÍSTICA COMIENZA EN EL ECO-DISEÑO Y SE SOSTIENE EN LA SEGREGACIÓN B2B 🌱"
        "</div>"
        "<div style='font-size: 12px; font-weight: 500; color: #334155; margin-top: 6px; max-width: 2200px; margin-left: auto; margin-right: auto; line-height: 1.4;'>"
        "El film stretch de PEBDL es un monomaterial logístico de consumo masivo y vida útil efímera. "
        "La mayor oportunidad de circularidad radica en <b>reducir el consumo en origen</b> mediante tecnologías nano-layer y pre-estiramiento inteligente (hasta 40% de ahorro), "
        "combinado con la <b>segregación limpia en centros logísticos mayoristas</b> para alimentar un <b>reciclaje mecánico B2B de alta pureza</b> que permita reincorporar resina reciclada (PCR) "
        "en nuevos embalajes sin comprometer la estabilidad mecánica de la carga exigida por las normas internacionales (ASTM D4649 / EUMOS 40509)."
        "</div>"
        "<div style='font-size: 10px; color: #64748B; margin-top: 8px;'>"
        "Trabajo Práctico N° 1 - Gestión Industrial | Cátedra Raquel Ariza (INTI - Industria 4.0 / IHOBE) | Archivo nativo para Draw.io / diagrams.net"
        "</div>"
        "</div>"
    )
    add_cell(banner_html, "rounded=1;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#1E3A8A;strokeWidth=2;arcSize=6;align=center;spacing=12;", 
             start_x, banner_y, 2450, 110)

    # Write out XML
    tree = ET.ElementTree(root)
    ET.indent(tree, space="  ", level=0)
    output_path = r"d:\Programming\GestionI\Cadena_de_Valor_Film_Stretch.drawio"
    tree.write(output_path, encoding="utf-8", xml_declaration=True)
    print(f"Generated draw.io diagram successfully at: {output_path}")

if __name__ == "__main__":
    build_drawio()

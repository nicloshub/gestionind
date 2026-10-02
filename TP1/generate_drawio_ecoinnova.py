import xml.etree.ElementTree as ET
import base64
import os

def load_icon_b64(name):
    path = os.path.join("icons", f"{name}.png")
    if os.path.exists(path):
        with open(path, "rb") as f:
            data = f.read()
            # En Draw.io/mxGraph, el formato data URL DEBE ser data:image/png,{base64} (sin ';base64')
            return f"data:image/png,{base64.b64encode(data).decode('utf-8')}"
    print(f"Warning: icon {name} not found!")
    return ""

def build_drawio_ecoinnova():
    root = ET.Element("mxfile", host="app.diagrams.net", version="24.0.0", type="device")
    diagram = ET.SubElement(root, "diagram", id="cadena_valor_ecoinnova_film_stretch", name="Cadena de Valor - Film Stretch (EcoInnova)")
    
    # Compact, balanced canvas dimensions (3100 x 1460 px)
    graph_model = ET.SubElement(diagram, "mxGraphModel", 
                                dx="3100", dy="1460", grid="1", gridSize="10", 
                                guides="1", tooltips="1", connect="1", arrows="1", 
                                fold="1", page="1", pageScale="1", pageWidth="3100", 
                                pageHeight="1460", background="#FAFAFC", math="0", shadow="0")
    
    root_cell = ET.SubElement(graph_model, "root")
    
    cell_id_counter = 0
    def new_id():
        nonlocal cell_id_counter
        cid = str(cell_id_counter)
        cell_id_counter += 1
        return cid

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

    def add_icon(icon_name, x, y, w=50, h=58, parent="1"):
        b64 = load_icon_b64(icon_name)
        if not b64:
            return None
        style = f"shape=image;aspect=fixed;image={b64};verticalLabelPosition=bottom;verticalAlign=top;imageAspect=1;"
        return add_cell("", style, x, y, w, h, parent)

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
    # HEADER SECTION (Y: 20 to 105)
    # ----------------------------------------------------
    header_html = (
        "<div style='font-family: Inter, Arial, sans-serif; text-align: left;'>"
        "<div style='font-size: 26px; font-weight: 800; color: #2E1065; letter-spacing: -0.5px;'>"
        "CADENA DE VALOR | FILM STRETCH PARA PALLETS (PEBDL / LLDPE)"
        "</div>"
        "<div style='font-size: 14.5px; font-weight: 600; color: #4338CA; margin-top: 3px;'>"
        "Mapeo de Ciclo de Vida y Circularidad según Metodología EcoInnova - Cátedra Raquel Ariza (INTI - Industria 4.0)"
        "</div>"
        "<div style='font-size: 11.5px; color: #64748B; margin-top: 2px;'>"
        "Grupo 5 | Flexible Logístico Monomaterial (PEBDL) | Unitización y Contención de Cargas Paletizadas"
        "</div>"
        "</div>"
    )
    add_cell(header_html, "text;html=1;align=left;verticalAlign=middle;resizable=0;points=[];autosize=0;strokeColor=none;fillColor=none;", 45, 20, 1350, 75)

    # Technical Specs Card
    specs_html = (
        "<div style='font-family: Inter, Arial, sans-serif; font-size: 10px; line-height: 1.35; color: #1E293B;'>"
        "<b style='color: #4338CA; font-size: 11px; text-transform: uppercase;'>Ficha Técnica:</b><br>"
        "• <b>Resina:</b> Monomaterial PEBDL (Polietileno lineal de baja densidad).<br>"
        "• <b>Vida Útil:</b> Muy corta (Monouso logístico / Alta generación B2B).<br>"
        "• <b>Normas:</b> ASTM D4649 (Paletizado), ASTM D2103 (Film), EUMOS 40509 (Retención dinámica)."
        "</div>"
    )
    add_cell(specs_html, "rounded=1;whiteSpace=wrap;html=1;fillColor=#F5F3FF;strokeColor=#DDD6FE;strokeWidth=1.5;arcSize=6;align=left;spacing=8;", 1450, 18, 500, 80)

    # Distances & Legend Card
    dist_html = (
        "<div style='font-family: Inter, Arial, sans-serif; font-size: 9.5px; line-height: 1.4; color: #1E293B;'>"
        "<b style='color: #0F172A;'>CÓDIGO DE DISTANCIAS Y FLUJOS:</b><br>"
        "<span style='display:inline-block; width:10px; height:10px; background:#4C1D95; border-radius:2px; vertical-align:middle;'></span> <b>GLOBAL:</b> +2000 km &nbsp;&nbsp;"
        "<span style='display:inline-block; width:10px; height:10px; background:#1E40AF; border-radius:2px; vertical-align:middle;'></span> <b>NACIONAL:</b> +500 km &nbsp;&nbsp;"
        "<span style='display:inline-block; width:10px; height:10px; background:#059669; border-radius:2px; vertical-align:middle;'></span> <b>PROVINCIAL:</b> 100-500 km &nbsp;&nbsp;"
        "<span style='display:inline-block; width:10px; height:10px; background:#D97706; border-radius:2px; vertical-align:middle;'></span> <b>CIUDAD:</b> &lt;100 km<br>"
        "<div style='margin-top:2px;'>"
        "<span style='color:#2563EB; font-weight:bold;'>━━━</span> Flujo Principal &nbsp;|&nbsp; "
        "<span style='color:#16A34A; font-weight:bold;'>- - -</span> Reciclaje PCR &nbsp;|&nbsp; "
        "<span style='color:#7C3AED; font-weight:bold;'>- - -</span> Scrap Pre-consumo"
        "</div>"
        "</div>"
    )
    add_cell(dist_html, "rounded=1;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#CBD5E1;strokeWidth=1;arcSize=6;align=left;spacing=8;", 1970, 18, 510, 80)

    # EcoInnova Logo Badge
    add_cell("<div style='font-family: Inter, Arial, sans-serif; font-weight: 800; font-size: 15px; color: #0284C7;'>eco<span style='color:#1E1B4B;'>innova.</span></div><div style='font-size: 8.5px; color:#64748B;'>Por Raquel Ariza</div>", 
             "rounded=1;whiteSpace=wrap;html=1;fillColor=#E0F2FE;strokeColor=#BAE6FD;align=center;", 2500, 22, 110, 42)

    # ----------------------------------------------------
    # 5 LANES SETUP (COMPACT & BALANCED)
    # ----------------------------------------------------
    stage_w = 580
    lane_gap = 18
    start_x = 45
    lane_top_y = 110
    lane_h = 880  # Compacted from 1450 to 880 (no dead space!)

    lanes_info = [
        {
            "num": "1",
            "title": "ETAPA EXTRACTIVA\n(Sector Primario)",
            "subtitle": "¿Cómo se obtienen las materias primas? ¿Renovables o no?",
            "color": "#4C1D95",
            "bg": "#FBFBFF",
            "border": "#DDD6FE"
        },
        {
            "num": "2",
            "title": "INDUSTRIALIZACIÓN DE COMPONENTES Y PRODUCTOS",
            "subtitle": "Transformaciones petroquímicas (Dow) y extrusión de film (Cast)",
            "color": "#1E3A8A",
            "bg": "#F8FAFF",
            "border": "#BFDBFE"
        },
        {
            "num": "3",
            "title": "SERVICIOS, COMERCIO Y DISTRIBUCIÓN",
            "subtitle": "Logística B2B para que el producto llegue al usuario",
            "color": "#0F766E",
            "bg": "#F0FDFA",
            "border": "#99F6E4"
        },
        {
            "num": "4",
            "title": "PRODUCTO EN USO\n(Paletizado / Enfardado)",
            "subtitle": "¿Qué necesita para funcionar? ¿Se mantiene? ¿Se degrada?",
            "color": "#D97706",
            "bg": "#FFFBEB",
            "border": "#FDE68A"
        },
        {
            "num": "5",
            "title": "GESTIÓN DE RESIDUOS / GIRSU Y RECICLAJE B2B",
            "subtitle": "Puntos de acopio, lavado, peletizado y retorno",
            "color": "#15803D",
            "bg": "#F0FDF4",
            "border": "#BBF7D0"
        }
    ]

    lane_ids = []
    for i, l in enumerate(lanes_info):
        lx = start_x + i * (stage_w + lane_gap)
        lid = add_cell("", f"rounded=1;whiteSpace=wrap;html=1;fillColor={l['bg']};strokeColor={l['border']};strokeWidth=1.5;arcSize=3;", lx, lane_top_y, stage_w, lane_h)
        lane_ids.append(lid)

        header_val = (
            f"<div style='font-family: Inter, Arial, sans-serif; text-align: center; color: #FFF;'>"
            f"<div style='font-size: 10px; font-weight: 800; opacity: 0.9; text-transform: uppercase; letter-spacing: 0.5px;'>ETAPA {l['num']}</div>"
            f"<div style='font-size: 13px; font-weight: 800; line-height: 1.2;'>{l['title'].replace(chr(10), '<br>')}</div>"
            f"<div style='font-size: 9px; font-weight: 500; opacity: 0.85; margin-top: 2px;'>{l['subtitle']}</div>"
            f"</div>"
        )
        add_cell(header_val, f"rounded=1;whiteSpace=wrap;html=1;fillColor={l['color']};strokeColor=none;arcSize=4;align=center;spacing=5;", lx + 6, lane_top_y + 6, stage_w - 12, 54)

    # Helper node builders filling the lane width (Process Node: w=320, IO/Problem: w=160, Icon: 50x58)
    def add_process_node(title, desc, x, y, w=320, h=72, bg="#FFFFFF", border="#CBD5E1"):
        val = (
            f"<div style='font-family: Inter, Arial, sans-serif; text-align: left; line-height: 1.25; padding-left: 4px;'>"
            f"<div style='font-size: 11.5px; font-weight: 800; color: #0F172A;'>{title}</div>"
            f"<div style='font-size: 10px; color: #475569; margin-top: 3px;'>{desc}</div>"
            f"</div>"
        )
        return add_cell(val, f"rounded=1;whiteSpace=wrap;html=1;fillColor={bg};strokeColor={border};strokeWidth=1.5;arcSize=5;align=left;spacing=6;", x, y, w, h)

    def add_io_circle(is_entry, text_items, x, y, r=85):
        if is_entry:
            color = "#D97706"
            bg = "#FFFBEB"
            title = "ENTRADAS"
        else:
            color = "#7C3AED"
            bg = "#F5F3FF"
            title = "SALIDAS"
        val = (
            f"<div style='font-family: Inter, Arial, sans-serif; text-align: center; font-size: 8.5px; line-height: 1.25; color: #1E293B;'>"
            f"<b style='color: {color}; font-size: 9.5px;'>{title}</b><br>"
            + "<br>".join(text_items) +
            f"</div>"
        )
        return add_cell(val, f"ellipse;whiteSpace=wrap;html=1;fillColor={bg};strokeColor={color};strokeWidth=1.5;align=center;spacing=2;", x, y, r, r)

    def add_problem_cloud(text, x, y, w=150, h=65):
        val = f"<div style='font-family: Inter, Arial, sans-serif; font-size: 9px; font-weight: 700; color: #B91C1C; text-align: center; line-height: 1.2;'>⚠️ {text}</div>"
        return add_cell(val, "ellipse;shape=cloud;whiteSpace=wrap;html=1;fillColor=#FEF2F2;strokeColor=#EF4444;strokeWidth=1.5;align=center;spacing=3;", x, y, w, h)

    def add_dist_badge(dist_name, km, bg_col, x, y):
        val = f"<div style='font-family: Inter, Arial, sans-serif; font-size: 9px; font-weight: 800; color: #FFFFFF; text-align: center;'>{dist_name} ({km})</div>"
        return add_cell(val, f"rounded=1;whiteSpace=wrap;html=1;fillColor={bg_col};strokeColor=none;arcSize=8;align=center;", x, y, 150, 22)

    # ----------------------------------------------------
    # LANE 1: ETAPA EXTRACTIVA
    # ----------------------------------------------------
    l1_x = start_x + 12
    y_cur = lane_top_y + 68

    # Top Icons Row
    add_icon("materias_primas_no_renovables", l1_x + 60, y_cur)
    add_icon("materia_prima", l1_x + 150, y_cur)
    add_icon("produccion_materias_primas_1", l1_x + 240, y_cur)
    add_icon("insumo", l1_x + 330, y_cur)

    y_cur += 68
    # Actors Card (full width of lane)
    act1_val = (
        "<div style='font-family: Inter, Arial, sans-serif; font-size: 9.5px; text-align: left; line-height: 1.35;'>"
        "<b style='color: #4C1D95; font-size: 10px;'>ACTORES CLAVE:</b><br>"
        "• Empresas energéticas y gasíferas (YPF, Pampa Energía, Tecpetrol)<br>"
        "• Cuenca Neuquina (Vaca Muerta) | Compañía MEGA S.A. (Loma La Lata)"
        "</div>"
    )
    add_cell(act1_val, "rounded=1;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#E2E8F0;strokeWidth=1;arcSize=4;align=left;spacing=6;", l1_x + 6, y_cur, stage_w - 24, 52)

    y_cur += 64
    # Step 1
    p1 = add_process_node("1. Exploración y Perforación", "Extracción no convencional (Shale Gas)<br>Perforación horizontal y fractura hidráulica", l1_x + 10, y_cur)
    add_icon("materias_primas_no_renovables", l1_x + 340, y_cur + 6)
    add_io_circle(True, ["Yacimientos de gas", "Agua / Químicos", "Energía térmica"], l1_x + 410, y_cur - 6, 85)

    y_cur += 92
    # Step 2
    p2 = add_process_node("2. Separación Primaria de Gas", "Separación en boca de pozo de gas seco (CH₄)<br>y condensados líquidos ricos en etano", l1_x + 10, y_cur)
    add_icon("materia_prima", l1_x + 340, y_cur + 6)
    add_problem_cloud("Emisiones fugitivas de metano y consumo de agua", l1_x + 400, y_cur, 155, 68)

    y_cur += 92
    # Step 3
    p3 = add_process_node("3. Fraccionamiento Criogénico", "Planta Mega (Loma La Lata): Fraccionamiento<br>y recuperación de Etano líquido", l1_x + 10, y_cur)
    add_icon("produccion_materias_primas_1", l1_x + 340, y_cur + 6)
    add_io_circle(False, ["Etano líquido", "Gas metano a red", "Barros y lodos"], l1_x + 410, y_cur - 6, 85)

    y_cur += 92
    # Step 4
    add_dist_badge("TRANSPORTE NACIONAL", "+600 km", "#1E40AF", l1_x + 400, y_cur + 25)
    p4 = add_process_node("4. Transporte por Poliducto", "Poliducto dedicado de Mega hacia el Polo<br>Petroquímico de Bahía Blanca (Pcias. Bs. As.)", l1_x + 10, y_cur)
    add_icon("insumo", l1_x + 340, y_cur + 6)

    # ----------------------------------------------------
    # LANE 2: INDUSTRIALIZACIÓN (DOW + EXTRUSIÓN CAST)
    # ----------------------------------------------------
    l2_x = start_x + (stage_w + lane_gap) + 12
    y_cur = lane_top_y + 68

    # Top Icons Row
    add_icon("produccion_materias_primas_2", l2_x + 30, y_cur)
    add_icon("insumo", l2_x + 105, y_cur)
    add_icon("produccion_componentes_modulos", l2_x + 180, y_cur)
    add_icon("material_secundario_pre_consumo", l2_x + 255, y_cur)
    add_icon("produccion_productos_finales", l2_x + 330, y_cur)

    y_cur += 68
    act2_val = (
        "<div style='font-family: Inter, Arial, sans-serif; font-size: 9.5px; text-align: left; line-height: 1.35;'>"
        "<b style='color: #1E3A8A; font-size: 10px;'>ACTORES CLAVE:</b><br>"
        "• Petroquímica base: Dow Argentina / PBB Polisur (Bahía Blanca)<br>"
        "• Fabricantes de film: Rok Stretch, SonFuertes, Embafor (AMBA)"
        "</div>"
    )
    add_cell(act2_val, "rounded=1;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#E2E8F0;strokeWidth=1;arcSize=4;align=left;spacing=6;", l2_x + 6, y_cur, stage_w - 24, 52)

    y_cur += 60
    # Step 5
    p5 = add_process_node("5. Cracking Térmico de Etano", "Hornos de pirólisis (800°C): Rotura térmica<br>de enlace molecular de Etano a Etileno", l2_x + 10, y_cur, 310, 68)
    add_icon("produccion_materias_primas_1", l2_x + 330, y_cur + 4)
    add_problem_cloud("Emisiones de CO₂, calor y gases de combustión", l2_x + 395, y_cur, 155, 62)

    y_cur += 78
    # Step 6
    p6 = add_process_node("6. Polimerización de PEBDL", "Reactor con catalizador Ziegler-Natta / metaloceno<br>y comonómero (1-buteno / 1-hexeno)", l2_x + 10, y_cur, 310, 68)
    add_icon("produccion_materias_primas_2", l2_x + 330, y_cur + 4)
    add_io_circle(True, ["Etileno monómero", "Catalizador", "Comonómero"], l2_x + 405, y_cur - 6, 80)

    y_cur += 78
    # Step 7
    p7 = add_process_node("7. Granulado y Peletizado", "Pellets vírgenes de PEBDL (LLDPE)<br>Control de MFI (1.8 a 2.8 g/10 min) y densidad", l2_x + 10, y_cur, 310, 68)
    add_icon("producto", l2_x + 330, y_cur + 4)
    add_io_circle(False, ["Pellets PEBDL", "Hidrógeno (H₂)", "Calor residual"], l2_x + 405, y_cur - 6, 80)

    y_cur += 78
    # Transport badge
    add_dist_badge("TRANSPORTE PROVINCIAL", "Bahía Blanca ➔ AMBA (650 km)", "#059669", l2_x + 395, y_cur + 20)
    # Step 8
    p8 = add_process_node("8. Dosificación y Formulación", "Mezcla de PEBDL virgen + PIB (tackificante cling)<br>+ aditivos UV + Resina reciclada PCR", l2_x + 10, y_cur, 310, 68)
    add_icon("insumo", l2_x + 330, y_cur + 4)

    y_cur += 78
    # Step 9
    p9 = add_process_node("9. Extrusión Cast (Plana)", "Línea cast multicapa (3 a 55 nano-layers)<br>Enfriamiento ultra-rápido sobre chill rolls", l2_x + 10, y_cur, 310, 68)
    add_icon("produccion_componentes_modulos", l2_x + 330, y_cur + 4)

    y_cur += 78
    # Step 10 & Scrap Box
    p10 = add_process_node("10. Bobinado y Refilado", "Corte lateral y bobinado en rollos manuales<br>(10-15 µm) o automáticos de alto rendimiento", l2_x + 10, y_cur, 310, 68)
    add_icon("produccion_productos_finales", l2_x + 330, y_cur + 4)

    scrap_box = add_cell(
        "<div style='font-family:Inter; font-size:9px; text-align:center; line-height:1.2;'>"
        "<b style='color:#7C3AED;'>BUCLE PRE-CONSUMO:</b><br>"
        "Refilado de bordes y descartes se muelen in-situ y retornan <b>100% a tolva</b>."
        "</div>",
        "rounded=1;whiteSpace=wrap;html=1;fillColor=#F3E8FF;strokeColor=#C084FC;strokeWidth=1.5;align=center;spacing=3;",
        l2_x + 395, y_cur - 2, 160, 66
    )

    # ----------------------------------------------------
    # LANE 3: SERVICIOS Y DISTRIBUCIÓN
    # ----------------------------------------------------
    l3_x = start_x + 2 * (stage_w + lane_gap) + 12
    y_cur = lane_top_y + 68

    add_icon("comercio_distribuidor", l3_x + 80, y_cur)
    add_icon("logistica_ultima_milla", l3_x + 180, y_cur)
    add_icon("prestador_servicios", l3_x + 280, y_cur)

    y_cur += 68
    act3_val = (
        "<div style='font-family: Inter, Arial, sans-serif; font-size: 9.5px; text-align: left; line-height: 1.35;'>"
        "<b style='color: #0F766E; font-size: 10px;'>ACTORES CLAVE:</b><br>"
        "• Distribuidores y mayoristas de insumos de packaging<br>"
        "• Operadores logísticos 3PL y transporte carretero B2B"
        "</div>"
    )
    add_cell(act3_val, "rounded=1;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#E2E8F0;strokeWidth=1;arcSize=4;align=left;spacing=6;", l3_x + 6, y_cur, stage_w - 24, 52)

    y_cur += 64
    # Step 11
    p11 = add_process_node("11. Embalaje y Paletizado de Bobinas", "Acondicionamiento en cajas y pallets de madera<br>para protección durante despacho comercial", l3_x + 10, y_cur)
    add_icon("comercio_distribuidor", l3_x + 340, y_cur + 6)
    add_io_circle(False, ["Bobinas listas", "Mandriles cartón", "Pallets madera"], l3_x + 410, y_cur - 6, 85)

    y_cur += 92
    # Step 12
    p12 = add_process_node("12. Distribución Mayorista B2B", "Comercialización directa a industrias de bebidas,<br>alimentos, logística y centros de distribución", l3_x + 10, y_cur)
    add_icon("logistica_ultima_milla", l3_x + 340, y_cur + 6)
    add_dist_badge("TRANSPORTE REGIONAL", "100 a 400 km", "#059669", l3_x + 400, y_cur + 25)

    y_cur += 92
    # Step 13
    p13 = add_process_node("13. Logística de Última Milla B2B", "Abastecimiento 'Just-in-Time' a plantas<br>embotelladoras, farmacéuticas y depósitos", l3_x + 10, y_cur)
    add_icon("prestador_servicios", l3_x + 340, y_cur + 6)
    add_problem_cloud("Emisiones de CO₂ en flotas de camiones diésel", l3_x + 400, y_cur, 155, 68)

    y_cur += 92
    # Commercial Servitization Box (fills the lane!)
    add_cell(
        "<div style='font-family:Inter; font-size:9.5px; text-align:left; color:#065F46; line-height:1.35;'>"
        "<b>ESTRATEGIA DE SERVITIZACIÓN LOGÍSTICA:</b><br>"
        "• Venta por pallet asegurado en lugar de por kilo de film.<br>"
        "• Provisión de enfardadoras en comodato con mantenimiento.<br>"
        "• Asesoramiento técnico para calibrar pre-estiramiento."
        "</div>",
        "rounded=1;whiteSpace=wrap;html=1;fillColor=#CCFBF1;strokeColor=#5EEAD4;strokeWidth=1;align=left;spacing=8;",
        l3_x + 10, y_cur, stage_w - 24, 75
    )

    # ----------------------------------------------------
    # LANE 4: PRODUCTO EN USO (PALETIZADO)
    # ----------------------------------------------------
    l4_x = start_x + 3 * (stage_w + lane_gap) + 12
    y_cur = lane_top_y + 68

    add_icon("producto_en_uso", l4_x + 30, y_cur - 5, 58, 66)
    add_icon("reutilizable", l4_x + 110, y_cur)
    add_icon("durabilidad", l4_x + 180, y_cur)
    add_icon("reparable", l4_x + 250, y_cur)
    add_icon("desmontable", l4_x + 320, y_cur)

    y_cur += 68
    act4_val = (
        "<div style='font-family: Inter, Arial, sans-serif; font-size: 9.5px; text-align: left; line-height: 1.35;'>"
        "<b style='color: #D97706; font-size: 10px;'>ACTORES Y USUARIOS EN USO:</b><br>"
        "• Operarios de almacén y enfardadoras automáticas<br>"
        "• Responsables de expedición (Norma EUMOS 40509) | Centros de retail"
        "</div>"
    )
    add_cell(act4_val, "rounded=1;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#E2E8F0;strokeWidth=1;arcSize=4;align=left;spacing=6;", l4_x + 6, y_cur, stage_w - 24, 52)

    y_cur += 64
    # Step 14
    p14 = add_process_node("14. Enfardado y Paletizado", "Envoltura manual con aplicador o automática<br>con pre-estiramiento motorizado (150% - 300%)", l4_x + 10, y_cur)
    add_icon("producto_en_uso", l4_x + 340, y_cur + 2, 54, 62)
    add_io_circle(True, ["Pallets con carga", "Bobina PEBDL", "Electricidad"], l4_x + 410, y_cur - 6, 85)

    y_cur += 92
    # Step 15
    p15 = add_process_node("15. Estabilización de Carga", "Contención mecánica por memoria elástica.<br>Ensayos dinámicos según EUMOS 40509", l4_x + 10, y_cur)
    add_icon("durabilidad", l4_x + 340, y_cur + 6)
    add_problem_cloud("SOBRE-EMBALAJE: Exceso de vueltas por falta de sensorización", l4_x + 400, y_cur, 160, 68)

    y_cur += 92
    # Step 16
    p16 = add_process_node("16. Transporte de Pallet Enfardado", "Vida útil muy corta (1 a 15 días en tránsito):<br>Protección contra humedad, suciedad y vuelcos", l4_x + 10, y_cur)
    add_icon("reutilizable", l4_x + 340, y_cur + 6)
    add_dist_badge("TRANSPORTE INTERURBANO", "50 a 1500 km", "#1E40AF", l4_x + 400, y_cur + 25)

    y_cur += 92
    # Step 17
    p17 = add_process_node("17. Despaletizado y Quitado", "Descarga en muelle de supermercado:<br>Corte del film con cutter de seguridad", l4_x + 10, y_cur)
    add_icon("desmontable", l4_x + 340, y_cur + 6)

    # Use features card (fills the lane!)
    add_cell(
        "<div style='font-family:Inter; font-size:9.5px; text-align:left; color:#78350F; line-height:1.3;'>"
        "<b>CARACTERÍSTICAS EN USO:</b><br>"
        "• <b>Función:</b> Pasiva (sin energía en reposo).<br>"
        "• <b>Monouso:</b> No reutilizable directamente.<br>"
        "• <b>Generación:</b> Masiva y concentrada en muelle."
        "</div>",
        "rounded=1;whiteSpace=wrap;html=1;fillColor=#FEF3C7;strokeColor=#FCD34D;strokeWidth=1;align=left;spacing=6;",
        l4_x + 400, y_cur - 2, 160, 75
    )

    # ----------------------------------------------------
    # LANE 5: GESTIÓN DE RESIDUOS Y RECICLAJE
    # ----------------------------------------------------
    l5_x = start_x + 4 * (stage_w + lane_gap) + 12
    y_cur = lane_top_y + 68

    add_icon("punto_limpio", l5_x + 30, y_cur)
    add_icon("centro_reciclaje", l5_x + 105, y_cur)
    add_icon("recuperacion_materiales", l5_x + 180, y_cur)
    add_icon("recuperacion_materias_primas", l5_x + 255, y_cur)
    add_icon("material_secundario_post_consumo", l5_x + 330, y_cur)

    y_cur += 68
    act5_val = (
        "<div style='font-family: Inter, Arial, sans-serif; font-size: 9.5px; text-align: left; line-height: 1.35;'>"
        "<b style='color: #15803D; font-size: 10px;'>ACTORES DE GESTIÓN Y RECICLADO:</b><br>"
        "• Grandes generadores (Supermercados, centros logísticos 3PL)<br>"
        "• Cooperativas de recuperadores | Plantas recicladoras de film B2B"
        "</div>"
    )
    add_cell(act5_val, "rounded=1;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#E2E8F0;strokeWidth=1;arcSize=4;align=left;spacing=6;", l5_x + 6, y_cur, stage_w - 24, 52)

    y_cur += 64
    # Step 18
    p18 = add_process_node("18. Segregación en Grandes Generadores", "Acopio limpio inmediato de film transparente en jaulas<br>o bolsones y enfardado a alta presión in-situ", l5_x + 10, y_cur)
    add_icon("punto_limpio", l5_x + 340, y_cur + 6)
    add_problem_cloud("CONTAMINACIÓN: Cintas adhesivas, etiquetas de papel y polvo", l5_x + 400, y_cur, 160, 68)

    y_cur += 92
    # Step 19
    p19 = add_process_node("19. Transporte y Clasificación", "Recepción en planta de reciclado B2B:<br>Separación manual de cintas, flejes y etiquetas", l5_x + 10, y_cur)
    add_icon("centro_reciclaje", l5_x + 340, y_cur + 6)
    add_dist_badge("TRANSPORTE LOCAL", "20 a 80 km", "#D97706", l5_x + 400, y_cur + 25)

    y_cur += 92
    # Step 20
    p20 = add_process_node("20. Lavado Intensivo y Molienda", "Balsa de flotación (PEBDL flota, suciedad cae al fondo)<br>Triturado a escamas (flakes) y secado centrífugo", l5_x + 10, y_cur)
    add_icon("recuperacion_materiales", l5_x + 340, y_cur + 6)
    add_io_circle(True, ["Film enfardado", "Agua / Detergentes", "Energía mecánica"], l5_x + 410, y_cur - 6, 85)

    y_cur += 92
    # Step 21
    p21 = add_process_node("21. Extrusión y Re-peletizado", "Extrusora con desgasificado al vacío y doble filtro.<br>Obtención de pellets reciclados R-PEBDL (PCR)", l5_x + 10, y_cur)
    add_icon("recuperacion_materias_primas", l5_x + 340, y_cur + 6)
    add_io_circle(False, ["Pellets R-PEBDL", "Aguas residuales", "Rechazos no recicl."], l5_x + 410, y_cur - 6, 85)

    y_cur += 92
    # Step 22
    p22 = add_process_node("22. Reincorporación Circular", "<b>Aplicaciones de R-PEBDL (PCR):</b><br>• Nuevo film stretch (capa central PCR 30-50%)<br>• Bolsas de residuos e industriales | Madera plástica", l5_x + 10, y_cur, 320, 72)
    add_icon("material_secundario_post_consumo", l5_x + 340, y_cur + 6)
    add_icon("materiales_reciclables", l5_x + 410, y_cur + 6)

    # ----------------------------------------------------
    # LOWER PANELS: ANÁLISIS ESTRATÉGICO Y CIRCULARIDAD
    # Positioned right at bottom_y = 1010 (immediately below lanes!)
    # ----------------------------------------------------
    bottom_y = lane_top_y + lane_h + 20

    # Panel 1: Cuellos de botella y Puntos Críticos (Width: 700)
    crit_html = (
        "<div style='font-family: Inter, Arial, sans-serif; text-align: left;'>"
        "<div style='background-color: #FEE2E2; border-left: 4px solid #DC2626; padding: 5px 10px; border-radius: 4px;'>"
        "<span style='font-size: 12px; font-weight: 800; color: #991B1B;'>⚠️ PUNTOS CRÍTICOS Y CUELLOS DE BOTELLA DEL CASO</span>"
        "</div>"
        "<div style='margin-top: 8px; font-size: 10px; line-height: 1.4; color: #1E293B;'>"
        "<b>1. Monouso y Gran Volumen Concentrado:</b> Vida útil de pocos días; cada descarga genera fardos masivos de residuo flexible.<br>"
        "<b>2. Contaminación en Segregación:</b> Cintas adhesivas (BOPP/acrílico) y etiquetas de papel carbonizan y taponan filtros.<br>"
        "<b>3. Exigencia Mecánica (EUMOS 40509):</b> La reincorporación de PCR degrada elongación si no se formula con co-extrusión A-B-A.<br>"
        "<b>4. Trazabilidad:</b> Necesidad de esquemas de Balance de Masa (Mass Balance) para certificar origen y calidad de PCR."
        "</div>"
        "</div>"
    )
    add_cell(crit_html, "rounded=1;whiteSpace=wrap;html=1;fillColor=#FFF5F5;strokeColor=#FCA5A5;strokeWidth=1.5;align=left;spacing=8;", start_x, bottom_y, 700, 150)

    # Panel 2: Estrategias de Economía Circular 4.0 (Width: 1380)
    strat_html = (
        "<div style='font-family: Inter, Arial, sans-serif; text-align: left;'>"
        "<div style='background-color: #DCFCE7; border-left: 4px solid #16A34A; padding: 5px 10px; border-radius: 4px;'>"
        "<span style='font-size: 12px; font-weight: 800; color: #14532D;'>💡 ESTRATEGIAS CIRCULARES 4.0 E INTERVENCIÓN PRIORITARIA (INTI / ECOINNOVA)</span>"
        "</div>"
        "<div style='display:flex; gap:10px; margin-top:8px; font-size: 10px; line-height: 1.35; color: #1E293B;'>"
        "<div style='flex:1; background:#FFF; padding:8px; border-radius:4px; border:1px solid #BBF7D0;'>"
        "<b style='color:#15803D;'>A. REDISEÑO Y NANO-EXTRUSIÓN (REDUCCIÓN EN ORIGEN):</b><br>"
        "• <b>Nano-Layers (33-55 capas):</b> Reducción de espesor de <b>23 µm a 12-15 µm</b> manteniendo rigidez.<br>"
        "• <b>Ahorro de hasta 40% de resina virgen</b> por pallet embalado.<br>"
        "• <b>Pre-estiramiento motorizado (>300%):</b> Enfardadoras automáticas que multiplican rendimiento.<br>"
        "• <b>Sensorización IoT:</b> Calibración de vueltas y tensión según peso y altura de carga."
        "</div>"
        "<div style='flex:1; background:#FFF; padding:8px; border-radius:4px; border:1px solid #BBF7D0;'>"
        "<b style='color:#15803D;'>B. CIRCUITO CERRADO B2B Y REINCORPORACIÓN DE PCR:</b><br>"
        "• <b>Convenios 'Take-Back' B2B:</b> Retiro de fardos limpios en grandes supermercados directamente por extrusores.<br>"
        "• <b>Film Co-extruido A-B-A:</b> Capa central (B) con 30-50% PCR y capas externas (A) vírgenes para cling.<br>"
        "• <b>Ensayos dinámicos rigurosos:</b> Garantizar estabilidad vial sin comprometer seguridad (ASTM D4649).<br>"
        "• <b>Logística inversa colaborativa:</b> Retorno de fardos en camiones vacíos de distribución."
        "</div>"
        "</div>"
        "</div>"
    )
    add_cell(strat_html, "rounded=1;whiteSpace=wrap;html=1;fillColor=#F0FDF4;strokeColor=#86EFAC;strokeWidth=1.5;align=left;spacing=8;", start_x + 718, bottom_y, 1380, 150)

    # Panel 3: Jerarquía de Recuperación (Width: 860)
    hier_html = (
        "<div style='font-family: Inter, Arial, sans-serif; text-align: left;'>"
        "<div style='background-color: #EDE9FE; border-left: 4px solid #7C3AED; padding: 5px 10px; border-radius: 4px;'>"
        "<span style='font-size: 12px; font-weight: 800; color: #5B21B6;'>📊 JERARQUÍA DE VALOR (PEBDL)</span>"
        "</div>"
        "<div style='margin-top: 8px; font-size: 9.5px; line-height: 1.35; color: #1E293B;'>"
        "🟢 <b>1. REDUCIR (Prioridad 1):</b> Nano-films ultradelgados (12 µm) y ajuste de pre-estiramiento.<br>"
        "🟡 <b>2. REUTILIZAR:</b> Fundas elásticas retornables para circuitos logísticos cerrados.<br>"
        "🟠 <b>3. RECICLAJE MECÁNICO CERRADO (B2B):</b> Reprocesado a pellets PCR para nuevo film.<br>"
        "🟤 <b>4. RECICLAJE ABIERTO (Downcycling):</b> Bolsas de residuos, madera plástica y tarimas.<br>"
        "🟣 <b>5. RECICLAJE QUÍMICO:</b> Pirólisis para fracciones mezcladas o contaminadas.<br>"
        "⚫ <b>6. DISPOSICIÓN:</b> Relleno sanitario controlado exclusivo para rechazos."
        "</div>"
        "</div>"
    )
    add_cell(hier_html, "rounded=1;whiteSpace=wrap;html=1;fillColor=#FAF5FF;strokeColor=#D8B4FE;strokeWidth=1.5;align=left;spacing=8;", start_x + 2116, bottom_y, 856, 150)

    # ----------------------------------------------------
    # FINAL FOOTER BANNER: MENSAJE CENTRAL
    # ----------------------------------------------------
    footer_y = bottom_y + 165
    msg_html = (
        "<div style='font-family: Inter, Arial, sans-serif; text-align: center; color: #0F172A;'>"
        "<div style='font-size: 13.5px; font-weight: 800; color: #2E1065; text-transform: uppercase;'>"
        "🌱 MENSAJE CENTRAL: LA CIRCULARIDAD EN PLÁSTICOS LOGÍSTICOS NACE EN EL ECO-DISEÑO Y SE SOSTIENE EN LA SEGREGACIÓN B2B 🌱"
        "</div>"
        "<div style='font-size: 11px; font-weight: 500; color: #334155; margin-top: 4px; max-width: 2800px; margin-left: auto; margin-right: auto; line-height: 1.4;'>"
        "El film stretch de PEBDL es un monomaterial logístico de vida útil efímera y consumo masivo. "
        "La máxima rentabilidad ambiental y económica se obtiene mediante la <b>reducción en origen</b> (films multicapa nano-stretch de 12 µm con pre-estiramiento inteligente, logrando hasta 40% de ahorro) "
        "combinada con un <b>circuito cerrado de logística inversa B2B</b> que capture el film limpio en grandes depósitos y lo reincorpore como resina reciclada (PCR) "
        "validando su resistencia dinámica bajo normas internacionales (ASTM D4649 / EUMOS 40509)."
        "</div>"
        "</div>"
    )
    add_cell(msg_html, "rounded=1;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#4338CA;strokeWidth=2;arcSize=6;align=center;spacing=8;", start_x, footer_y, stage_w * 5 + lane_gap * 4, 75)

    # Write out XML
    tree = ET.ElementTree(root)
    ET.indent(tree, space="  ", level=0)
    output_path = r"d:\Programming\GestionI\Cadena_de_Valor_Film_Stretch.drawio"
    tree.write(output_path, encoding="utf-8", xml_declaration=True)
    print(f"Generated compact draw.io diagram successfully at: {output_path}")

if __name__ == "__main__":
    build_drawio_ecoinnova()

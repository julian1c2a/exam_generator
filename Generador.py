import os
import random
from typing import List, Tuple, Any, Dict

from docx import Document
from docx.shared import Pt, Cm, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT

# --- CONSTANTES GLOBALES ---
N_BITS = 8
FILENAME_BASE = 'Examen_Electronica_Digital.docx'

# --- FUNCIONES AUXILIARES DE CONVERSIÓN ---

def int_to_bin_str(val: int, bits: int) -> str:
    """Convierte un entero a string binario de N bits."""
    return format(val if val >= 0 else (1 << bits) + val, f'0{bits}b')

def int_to_bcd_str(val: int) -> str:
    """Convierte un entero (0-99) a su representación BCD de 8 bits."""
    if not (0 <= val <= 99): return "NR"
    tens = val // 10
    units = val % 10
    return f"{tens:04b} {units:04b}"

def int_to_sm_str(val: int, bits: int) -> str:
    """Convierte un entero a Signo-Magnitud."""
    if val >= 0:
        return format(val, f'0{bits}b')  # Bit de signo 0
    else:
        abs_val = abs(val)
        bin_abs = format(abs_val, f'0{bits - 1}b')
        return '1' + bin_abs

# --- CONFIGURACIÓN DEL DOCUMENTO ---

def configurar_estilos(doc: Document):
    """Configura la fuente y estilos base del documento."""
    style = doc.styles['Normal']
    font = style.font
    font.name = 'Calibri'
    font.size = Pt(11)

    # Crear estilo para Código/ASCII Art
    try:
        style_code = doc.styles.add_style('CodeStyle', 1) # 1 = Paragraph Style
        style_code.font.name = 'Courier New'
        style_code.font.size = Pt(9)
        style_code.paragraph_format.space_after = Pt(0)
        style_code.paragraph_format.space_before = Pt(0)
        style_code.paragraph_format.line_spacing = 1
        style_code.paragraph_format.keep_with_next = True
    except:
        pass # Si ya existe, ignoramos

def agregar_ascii_art(doc: Document, art: str):
    """Agrega un bloque de texto ASCII monoespaciado."""
    p = doc.add_paragraph(art, style='CodeStyle')
    p.alignment = WD_ALIGN_PARAGRAPH.LEFT

def agregar_encabezado(doc: Document):
    """Genera el título y el área de nombre del alumno."""
    titulo = doc.add_heading('Fundamentos de Electrónica', 0)
    titulo.alignment = WD_ALIGN_PARAGRAPH.CENTER

    subtitulo = doc.add_paragraph('Parte I: Electrónica Digital')
    subtitulo.alignment = WD_ALIGN_PARAGRAPH.CENTER
    subtitulo.runs[0].bold = True
    subtitulo.runs[0].font.size = Pt(14)

    doc.add_paragraph('_' * 85)
    doc.add_paragraph('Nombre: __________________________________________________  Fecha: ____________')
    doc.add_paragraph('\n')

# --- GENERACIÓN DE EJERCICIOS INDIVIDUALES ---

def generar_ejercicio_1(doc: Document) -> List[Tuple[str, int]]:
    """Genera el Ejercicio 1 (Tabla de conversión)."""
    doc.add_heading(f'Ejercicio 1: Sistemas de Representación (N = {N_BITS} bits)', level=1)

    p = doc.add_paragraph()
    p.add_run('a) Complete la tabla. ').bold = True
    p.add_run(f'El registro es de {N_BITS} bits. Si el número no es representable, escriba "NR".')

    headers = ['Id', 'Decimal', 'Binario Nat.', 'C2', 'Signo-Magnitud', 'BCD']
    table = doc.add_table(rows=5, cols=6)
    table.style = 'Table Grid'
    table.alignment = WD_TABLE_ALIGNMENT.CENTER

    hdr_cells = table.rows[0].cells
    for i, text in enumerate(headers):
        run = hdr_cells[i].paragraphs[0].add_run(text)
        run.bold = True
        run.font.size = Pt(9)
        hdr_cells[i].paragraphs[0].alignment = WD_ALIGN_PARAGRAPH.CENTER
        hdr_cells[i].width = Cm(2.5)

    filas_labels = ['a', 'b', 'c', 'd']
    valores_generados = []

    for i, label in enumerate(filas_labels):
        row_cells = table.rows[i + 1].cells
        row_cells[0].text = f"{label})"
        row_cells[0].paragraphs[0].alignment = WD_ALIGN_PARAGRAPH.CENTER

        opciones_columna = [1, 1, 2, 3, 3, 4, 4, 5]
        col_idx = random.choice(opciones_columna)
        val = 0
        text_val = ""

        es_signed_col = col_idx in [1, 3, 4]
        signo = -1 if (es_signed_col and random.random() < 0.7) else 1

        if col_idx == 1: magnitud = random.randint(0, 200); val = signo * magnitud; text_val = str(val)
        elif col_idx == 2: val = random.randint(0, 255); text_val = int_to_bin_str(val, N_BITS)
        elif col_idx == 3: limit = 128 if signo == -1 else 127; magnitud = random.randint(0, limit); val = signo * magnitud; text_val = int_to_bin_str(val, N_BITS)
        elif col_idx == 4: magnitud = random.randint(0, 127); val = signo * magnitud; text_val = int_to_sm_str(val, N_BITS)
        elif col_idx == 5: val = random.randint(0, 99); text_val = int_to_bcd_str(val)

        cell = row_cells[col_idx]
        cell.text = text_val
        cell.paragraphs[0].alignment = WD_ALIGN_PARAGRAPH.CENTER
        valores_generados.append((label, val))

    doc.add_paragraph('\n')
    return valores_generados

def generar_ejercicio_1_parte_b(doc: Document, valores: List[Tuple[str, int]]):
    """Genera la parte B del Ejercicio 1."""
    if len(valores) < 2: return

    p_b = doc.add_paragraph()
    p_b.add_run('b) Realice las siguientes operaciones aritméticas ').bold = True
    p_b.add_run('utilizando los valores de la tabla anterior. Indique el resultado binario y marque las casillas correspondientes.')

    for i in range(1, 3):
        fila1 = random.choice(valores)
        fila2 = random.choice([x for x in valores if x != fila1])
        es_suma = random.choice([True, False])
        sistema = random.choice(['Binario Natural (Unsigned)', 'Complemento a 2'])
        op_texto = "Suma" if es_suma else "Resta"
        signo = "+" if es_suma else "-"

        p_preg = doc.add_paragraph()
        p_preg.add_run(f'   {i}) {op_texto} en {sistema}: ').bold = True
        p_preg.add_run(f'Fila {fila1[0]} {signo} Fila {fila2[0]}')

        doc.add_paragraph('       Resultado Binario (N bits): __________________________')
        p_estado = doc.add_paragraph()
        p_estado.paragraph_format.left_indent = Cm(1.5)
        run = p_estado.add_run('¿Overflow? [   ]    ¿Underflow? [   ]    ¿Resultado Correcto? [   ]')
        run.italic = True
        doc.add_paragraph('')

def generar_ejercicio_2(doc: Document) -> Dict[str, Any]:
    """Genera el Ejercicio 2: K-Map 7x7."""
    doc.add_heading('Ejercicio 2: Diseño y Simplificación Lógica', level=1)

    es_minterms = random.choice([True, False])
    tipo_canonico = "Minitérminos (Suma de Productos)" if es_minterms else "Maxitérminos (Producto de Sumas)"
    tipo_puerta = "NAND" if es_minterms else "NOR"
    target_val = 1 if es_minterms else 0
    default_val = 0 if es_minterms else 1
    outputs = [default_val] * 16

    num_grupos = random.randint(3, 6)
    for _ in range(num_grupos):
        idx1 = random.randint(0, 15)
        bit_diff = random.randint(0, 3)
        idx2 = idx1 ^ (1 << bit_diff)
        outputs[idx1] = target_val
        outputs[idx2] = target_val

    doc.add_paragraph(f'Dada la función lógica F(A, B, C, D) definida por la siguiente tabla de verdad:')

    table_tv = doc.add_table(rows=17, cols=5)
    table_tv.style = 'Table Grid'
    table_tv.alignment = WD_TABLE_ALIGNMENT.CENTER
    headers_tv = ['A', 'B', 'C', 'D', 'F']
    for idx, text in enumerate(headers_tv):
        cell = table_tv.rows[0].cells[idx]
        cell.text = text
        cell.paragraphs[0].alignment = WD_ALIGN_PARAGRAPH.CENTER
        cell.paragraphs[0].runs[0].bold = True

    for i in range(16):
        row_cells = table_tv.rows[i+1].cells
        bin_vals = f"{i:04b}"
        for j in range(4):
            row_cells[j].text = bin_vals[j]
            row_cells[j].paragraphs[0].alignment = WD_ALIGN_PARAGRAPH.CENTER
        row_cells[4].text = str(outputs[i])
        row_cells[4].paragraphs[0].alignment = WD_ALIGN_PARAGRAPH.CENTER
        row_cells[4].paragraphs[0].runs[0].bold = True

    doc.add_paragraph('\nUtilice el siguiente esquema para simplificar la función. (Nota: La numeración incluye opciones correctas e incorrectas, táchese la que no proceda).')

    table_k = doc.add_table(rows=7, cols=7)
    table_k.style = 'Table Grid'
    table_k.alignment = WD_TABLE_ALIGNMENT.CENTER

    cell_f = table_k.cell(0, 0)
    cell_f.merge(table_k.cell(2, 2))
    cell_f.text = "F"
    cell_f.paragraphs[0].alignment = WD_ALIGN_PARAGRAPH.CENTER
    cell_f.paragraphs[0].runs[0].bold = True
    cell_f.paragraphs[0].runs[0].font.size = Pt(24)
    cell_f.vertical_alignment = WD_ALIGN_PARAGRAPH.CENTER

    cell_cd = table_k.cell(0, 3)
    cell_cd.merge(table_k.cell(0, 6))
    cell_cd.text = "CD ="
    cell_cd.paragraphs[0].alignment = WD_ALIGN_PARAGRAPH.CENTER
    cell_cd.paragraphs[0].runs[0].bold = True

    cell_ab = table_k.cell(3, 0)
    cell_ab.merge(table_k.cell(6, 0))
    cell_ab.text = "AB ="
    cell_ab.vertical_alignment = WD_ALIGN_PARAGRAPH.CENTER
    cell_ab.paragraphs[0].alignment = WD_ALIGN_PARAGRAPH.CENTER
    cell_ab.paragraphs[0].runs[0].bold = True

    gray_code = ["00", "01", "11", "10"]
    bin_code = ["00", "01", "10", "11"]

    for i in range(4):
        table_k.cell(1, i+3).text = bin_code[i]
        table_k.cell(1, i+3).paragraphs[0].alignment = WD_ALIGN_PARAGRAPH.CENTER
        table_k.cell(2, i+3).text = gray_code[i]
        table_k.cell(2, i+3).paragraphs[0].alignment = WD_ALIGN_PARAGRAPH.CENTER

    for i in range(4):
        table_k.cell(i+3, 1).text = bin_code[i]
        table_k.cell(i+3, 1).paragraphs[0].alignment = WD_ALIGN_PARAGRAPH.CENTER
        table_k.cell(i+3, 2).text = gray_code[i]
        table_k.cell(i+3, 2).paragraphs[0].alignment = WD_ALIGN_PARAGRAPH.CENTER

    for i in range(3, 7):
        table_k.rows[i].height = Cm(1.2)

    doc.add_paragraph('\nSe pide:')
    doc.add_paragraph(f'a) Obtener la expresión canónica mediante {tipo_canonico}.', style='List Number')
    doc.add_paragraph('b) Identificar la numeración correcta del mapa (tachando la incorrecta) y simplificar.', style='List Number')
    doc.add_paragraph(f'c) Implementar el circuito simplificado utilizando EXCLUSIVAMENTE puertas {tipo_puerta}.', style='List Number')
    doc.add_paragraph('\n' * 2)
    return {"outputs": outputs}

def generar_ejercicio_3(doc: Document) -> Dict[str, Any]:
    """Genera el Ejercicio 3."""
    doc.add_heading('Ejercicio 3: Problema de Diseño Lógico (Alta Puntuación)', level=1)

    escenarios = [
        {"titulo": "Sistema de Seguridad de Bóveda Bancaria", "vars": ["A: Sensor Reloj (1=Laboral)", "B: Llave Director (1=Si)", "C: Llave Gerente (1=Si)", "D: Código (1=OK)"], "salida": "Z: Apertura", "logicas": ["Se abre SI (Horario Y Código) O (Fuera Horario Y LlaveDirector Y LlaveGerente)."]},
        {"titulo": "Reactor Químico", "vars": ["P: Presión (1=Alta)", "T: Temp (1=Alta)", "N: Nivel (1=Alto)", "M: Manual (1=ON)"], "salida": "E: Escape", "logicas": ["Se abre SI M=1 O (P=1 Y (T=1 O N=1))."]}
    ]
    escenario = random.choice(escenarios)
    logica_texto = random.choice(escenario["logicas"])

    doc.add_paragraph(f"Contexto: {escenario['titulo']}").bold = True
    for var in escenario["vars"]: doc.add_paragraph(var, style='List Bullet')
    doc.add_paragraph(f"Lógica: {logica_texto}").italic = True

    doc.add_paragraph('\nSe pide: Tabla de Verdad, Karnaugh y Esquema Lógico.')
    doc.add_paragraph('\n' * 3)
    return {"escenario": escenario}

def generar_ejercicio_4(doc: Document) -> Dict[str, Any]:
    """Genera el Ejercicio 4: Análisis de Bloques MSI (ASCII Art)."""
    doc.add_heading('Ejercicio 4: Análisis de Bloques MSI', level=1)

    tipo_bloque = random.choice(['MUX', 'COMPARADOR', 'SUMADOR'])
    datos_retorno = {"tipo": tipo_bloque}

    doc.add_paragraph(f'Dado el siguiente componente: {tipo_bloque}').bold = True

    if tipo_bloque == 'MUX':
        inputs_mux = [random.randint(0, 1) for _ in range(16)]
        inputs_str = [str(x) for x in inputs_mux]
        col1 = inputs_str[:8]; col2 = inputs_str[8:]

        ascii_art = (
            f"          +-----------------------+\n"
            f" I0 ={col1[0]} ---|                       |--- Y (Salida)\n"
            f" I1 ={col1[1]} ---|                       |--- Y_neg\n"
            f" ...      |       MUX 16:1        |\n"
            f" I7 ={col1[7]} ---|                       |\n"
            f"          |                       |\n"
            f" I8 ={col2[0]} ---|                       |\n"
            f" ...      |                       |\n"
            f" I15={col2[7]} ---|                       |\n"
            f"          +-----------------------+\n"
            f"             |   |   |   |     |\n"
            f"             S3  S2  S1  S0    E (Activo L)\n"
        )
        agregar_ascii_art(doc, ascii_art)
        doc.add_paragraph(f'Tabla de entradas: {inputs_mux}')

        doc.add_paragraph('\nDetermine la salida Y y Y_neg para los siguientes casos:')
        for i in range(1, 4):
            addr_val = random.randint(0, 15)
            enable = random.choice([0, 1])
            enable_str = "0 (Activo)" if enable == 0 else "1 (Inactivo)"
            doc.add_paragraph(f'{i}) Enable={enable_str}, Dir={addr_val:04b}.', style='List Number')

    elif tipo_bloque == 'COMPARADOR':
        val_a = random.randint(0, 15); val_b = random.randint(0, 15)
        cascada = [random.choice([0, 1]) for _ in range(3)]

        ascii_art = (
            f"             +-------------------+\n"
            f"  A = {val_a:04b}  --|                   |--- A > B\n"
            f"             |    COMPARADOR     |\n"
            f"  B = {val_b:04b}  --|      4 BITS       |--- A = B\n"
            f"             |                   |\n"
            f"  I(A>B)={cascada[0]} --|                   |--- A < B\n"
            f"  I(A=B)={cascada[1]} --|                   |\n"
            f"  I(A<B)={cascada[2]} --|                   |\n"
            f"             +-------------------+\n"
        )
        agregar_ascii_art(doc, ascii_art)
        doc.add_paragraph('Determine el estado de las 3 salidas > = <.')

    elif tipo_bloque == 'SUMADOR':
        val_a = random.randint(0, 15); val_b = random.randint(0, 15); c_in = random.choice([0, 1])
        ascii_art = (
            f"             +-------------------+\n"
            f"  A = {val_a:04b}  --|                   |--- S (Suma)\n"
            f"             |      SUMADOR      |\n"
            f"  B = {val_b:04b}  --|      4 BITS       |--- Cout\n"
            f"             |                   |\n"
            f"  Cin = {c_in}  ---|                   |\n"
            f"             +-------------------+\n"
        )
        agregar_ascii_art(doc, ascii_art)
        doc.add_paragraph('Determine S (binario), Cout y si hay Overflow.')

    doc.add_paragraph('\n' * 2)
    return datos_retorno

def generar_ejercicio_5(doc: Document) -> Dict[str, Any]:
    """
    Genera el Ejercicio 5: Sistemas Secuenciales.
    Configura biestables, lógica, dibuja esquema y cronograma.
    """
    doc.add_heading('Ejercicio 5: Análisis de Sistemas Secuenciales', level=1)

    # 1. CONFIGURACIÓN DEL SISTEMA
    ff_type = random.choice(['JK', 'D', 'T'])
    edge = random.choice(['Subida', 'Bajada'])
    has_async = random.choice([True, False])

    async_cfg = {}
    if has_async:
        async_cfg['type'] = random.choice(['Preset', 'Clear'])
        async_cfg['level'] = random.choice(['Alto (1)', 'Bajo (0)'])
        async_text = f"Entrada asíncrona de {async_cfg['type']} activa a Nivel {async_cfg['level']}."
    else:
        async_text = "Sin entradas asíncronas."

    # 2. SELECCIÓN DE LÓGICA (Simplificada y Compatible)
    # Elegimos entre "Registro de Desplazamiento" o "Contador" según lo que mejor encaje con el FF
    logic_options = []

    # Opción A: Registro de Desplazamiento (Ideal para D, posible para JK)
    if ff_type == 'D':
        logic_options.append('SHIFT')
    elif ff_type == 'JK':
        logic_options.append('COUNTER')
    else: # T
        logic_options.append('COUNTER')

    logic_type = random.choice(logic_options)

    doc.add_paragraph(f"Analice el siguiente sistema secuencial síncrono por flanco de {edge}.")
    doc.add_paragraph(f"Datos: Biestables tipo {ff_type}. {async_text}")

    # 3. GENERACIÓN DEL ESQUEMA (ASCII ART)
    ascii_ckt = ""
    clock_sym = "> " if edge == 'Subida' else "o>"

    if logic_type == 'SHIFT':
        doc.add_paragraph("Lógica: Registro de Desplazamiento de 2 bits (Entrada Serie 'E').")
        # Esquema simplificado para D
        ascii_ckt = (
            f"        Async                               Async\n"
            f"          |                                   |\n"
            f"      +-------+                           +-------+\n"
            f"      |       |                           |       |\n"
            f" E ---|D    Q |---------- Q0 -------------|D    Q |------- Q1\n"
            f"      |       |             |             |       |\n"
            f"CLK --|{clock_sym}    Q'|             +-------------|{clock_sym}    Q'|\n"
            f"      +-------+                           +-------+\n"
        )

    elif logic_type == 'COUNTER':
        doc.add_paragraph("Lógica: Contador Binario Ascendente de 2 bits (Entrada Enable 'E').")
        if ff_type == 'JK':
            ascii_ckt = (
                f"      +-------+                           +-------+\n"
                f" E ---|J    Q |---------- Q0 -------------|J    Q |------- Q1\n"
                f" E ---|K      |      |              Q0 ---|K      |\n"
                f"      |       |      |                    |       |\n"
                f"CLK --|{clock_sym}    Q'|      +--------------------|{clock_sym}    Q'|\n"
                f"      +-------+                           +-------+\n"
                f"      (Async conectada a ambos)           (Async conectada a ambos)\n"
            )
        elif ff_type == 'T':
            ascii_ckt = (
                f"      +-------+                           +-------+\n"
                f" E ---|T    Q |---------- Q0 -------------|T    Q |------- Q1\n"
                f"      |       |      |              Q0 ---|       |\n"
                f"      |       |      |                    |       |\n"
                f"CLK --|{clock_sym}    Q'|      +--------------------|{clock_sym}    Q'|\n"
                f"      +-------+                           +-------+\n"
            )

    agregar_ascii_art(doc, ascii_ckt)

    # 4. GENERACIÓN DEL CRONOGRAMA
    doc.add_paragraph('\nComplete el cronograma (Q0 y Q1). Nota: La señal asíncrona solo actúa al inicio.')

    # Generar señales aleatorias
    # CLK: 6 ciclos. Representación visual: _|-|_|-
    cycles = 6
    clk_wave =  "__|--|__|--|__|--|__|--|__|--|__|--"

    # Async: Activa solo al principio (digamos, durante el primer medio ciclo)
    # Longitud total visual aprox 3 chars por medio ciclo -> 6 chars por ciclo -> 36 chars
    async_wave = "___________________________________"
    if has_async:
        # Si es activa en alto, ponemos 'High' al principio. Si bajo, 'Low' (visual inverted?)
        # Simplificación visual: Mostramos cuando está ACTIVA visualmente diferente
        is_high_active = 'Alto' in async_cfg['level']
        # Dibujamos la activación:
        if is_high_active:
            async_wave = "~~~~~______________________________" # Pulse High
        else:
            async_wave = "_____~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~" # Pulse Low (active) then High

    # Input E: Aleatoria
    input_bits = [random.randint(0,1) for _ in range(cycles*2)] # Cambios cada medio ciclo
    input_wave = ""
    for bit in input_bits:
        input_wave += "~~~" if bit == 1 else "___"

    # Salidas vacías (punteadas)
    q_empty = "..................................."

    crono_art = (
        f"       t0 t1 t2 t3 t4 t5 t6 ...\n"
        f" CLK:  {clk_wave}\n"
        f" ASY:  {async_wave} ({'CLR/PRE' if has_async else 'N/A'})\n"
        f"  E :  {input_wave}\n"
        f" Q0 :  {q_empty}\n"
        f" Q1 :  {q_empty}\n"
    )

    agregar_ascii_art(doc, crono_art)

    doc.add_paragraph('Se pide:')
    doc.add_paragraph('a) Identificar las ecuaciones de entrada de los biestables.', style='List Number')
    doc.add_paragraph('b) Completar el cronograma basándose en la señal de reloj y las entradas.', style='List Number')

    return {
        "ff": ff_type,
        "edge": edge,
        "logic": logic_type
    }

# --- GUARDADO Y EJECUCIÓN ---

def guardar_documento(doc: Document):
    """Intenta guardar el documento, manejando errores de bloqueo."""
    nombre_final = FILENAME_BASE

    try:
        doc.save(nombre_final)
        print(f"\n✅ ¡ÉXITO! Examen generado correctamente.")
        print(f"📂 Archivo: {os.path.abspath(nombre_final)}")
    except PermissionError:
        print(f"\n⚠️ AVISO: El archivo '{nombre_final}' está abierto en Word y no se puede sobrescribir.")
        nuevo_nombre = f'Examen_Electronica_Digital_{random.randint(100, 999)}.docx'
        doc.save(nuevo_nombre)
        print(f"✅ ¡GUARDADO! Se ha creado una copia nueva: {nuevo_nombre}")
        print(f"📂 Archivo: {os.path.abspath(nuevo_nombre)}")

def main():
    doc = Document()
    configurar_estilos(doc)
    agregar_encabezado(doc)

    generar_ejercicio_1(doc)
    valores_ej1 = generar_ejercicio_1(doc) # Bug fix: call once. Actually generate returns values.
    # Fixed logic: generate_ejercicio_1 calls add_heading. Don't call twice.
    # Re-structure main properly:

    # Corrected Main flow
    doc = Document() # Reset
    configurar_estilos(doc)
    agregar_encabezado(doc)

    valores_ej1 = generar_ejercicio_1(doc)
    generar_ejercicio_1_parte_b(doc, valores_ej1)

    generar_ejercicio_2(doc)
    generar_ejercicio_3(doc)
    generar_ejercicio_4(doc)
    generar_ejercicio_5(doc)

    guardar_documento(doc)

if __name__ == "__main__":
    main()
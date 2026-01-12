from exam_generator import ExamGenerator
from latex_renderer import LatexRenderer
from docx_renderer import DocxRenderer

def main():
    # 1. Configuración
    # Asegúrate de que 'scenarios.json' exista, si no, el generador fallará.
    try:
        generator = ExamGenerator('scenarios.json')
    except FileNotFoundError:
        print("❌ Error: No se encontró 'scenarios.json'. Asegúrate de que el archivo exista.")
        return

    latex_renderer = LatexRenderer()
    docx_renderer = DocxRenderer()

    # 2. Generación de Modelos (Lógica Pura - Única fuente de verdad)
    data_ej1 = generator.generate_ej1()
    data_ej2 = generator.generate_ej2()
    data_ej3 = generator.generate_ej3()
    data_ej4 = generator.generate_ej4()
    data_ej5 = generator.generate_ej5()

    # 3. Renderizado LaTeX
    print("--- Generando LaTeX ---")
    latex_content = latex_renderer.get_preamble()
    latex_content += latex_renderer.render_ej1(data_ej1)
    latex_content += latex_renderer.render_ej2(data_ej2)
    latex_content += latex_renderer.render_ej3(data_ej3)
    latex_content += latex_renderer.render_ej4(data_ej4)
    latex_content += latex_renderer.render_ej5(data_ej5)
    latex_content += latex_renderer.get_footer()

    with open("Examen_Final.tex", "w", encoding="utf-8") as f:
        f.write(latex_content)
    print("✅ Examen LaTeX generado: Examen_Final.tex")

    # 4. Renderizado Word
    print("\n--- Generando Word ---")
    docx_renderer.render_examen(data_ej1, data_ej2, data_ej3, data_ej4, data_ej5, "Examen_Final.docx")

if __name__ == "__main__":
    main()
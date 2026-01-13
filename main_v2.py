import os
import argparse
from core.exam_builder import ExamBuilder
from renderers.latex.main_renderer import LatexExamRenderer

def main():
    # Configuración por defecto para pruebas
    default_config = os.path.join("config", "test_exam.json")
    
    print("🚀 Iniciando Generador de Exámenes V2...")
    
    # 1. Construcción
    try:
        builder = ExamBuilder(default_config)
        exercises = builder.build()
    except Exception as e:
        print(f"❌ Error al construir el examen: {e}")
        return
    
    if not exercises:
        print("❌ No se generaron ejercicios. Revisa la configuración.")
        return

    # 2. Renderizado
    print("🎨 Renderizando a LaTeX...")
    try:
        renderer = LatexExamRenderer()
        latex_code = renderer.render(exercises)
    except Exception as e:
        print(f"❌ Error al renderizar: {e}")
        import traceback
        traceback.print_exc()
        return
    
    # 3. Guardado en build/latex
    output_dir = os.path.join("build", "latex")
    os.makedirs(output_dir, exist_ok=True)
    
    output_file = os.path.join(output_dir, "Examen_V2.tex")
    
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(latex_code)
        
    print(f"✅ ¡Éxito! Archivo generado: {os.path.abspath(output_file)}")
    print(f"📂 Componentes generados en: {os.path.abspath(os.path.join(output_dir, 'components'))}")

if __name__ == "__main__":
    main()
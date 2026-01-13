import os
from typing import Callable

class LatexAssetManager:
    def __init__(self, base_build_path="build/latex"):
        self.base_path = base_build_path
        self.components_path = os.path.join(base_build_path, "components")
        self.resources_path = "resources/latex" # Ruta relativa desde la raíz del proyecto
        
        # Asegurar que existe el directorio de componentes generados
        os.makedirs(self.components_path, exist_ok=True)

    def get_component(self, name_id: str, content_generator_func: Callable[[], str]) -> str:
        r"""
        Gestiona un componente LaTeX (ej: un diagrama TikZ).
        
        1. Busca si existe un archivo fijo en /resources/latex/{name_id}.tex
        2. Si existe, devuelve el \input a ese archivo.
        3. Si no, ejecuta content_generator_func(), guarda el resultado en 
           build/latex/components/{name_id}.tex y devuelve el \input a ese archivo.
        """
        
        # Nombre del archivo esperado
        filename = f"{name_id}.tex"
        
        # 1. Chequear recurso fijo (Fixed)
        # La ruta física para comprobar existencia
        fixed_file_path = os.path.join(self.resources_path, filename)
        
        if os.path.exists(fixed_file_path):
            # Ruta relativa para el \input desde el archivo Examen_Final.tex (que está en build/latex/)
            # Necesitamos subir 2 niveles (../../) para salir de build/latex/ y entrar a resources/latex/
            relative_input_path = f"../../{self.resources_path}/{filename}".replace("\\", "/")
            
            return fr"% [RECURSO FIJO DETECTADO: {filename}]" + "\n" + fr"\input{{{relative_input_path}}}" + "\n"

        # 2. Generar borrador (Draft)
        content = content_generator_func()
        
        # Añadir cabecera para identificarlo fácil y facilitar la edición manual
        header = f"% --- COMPONENTE GENERADO: {name_id} ---\n"
        header += f"% ID: {name_id}\n"
        header += f"% Si quieres fijar este diseño, copia este archivo a '{self.resources_path}/{filename}' y edítalo.\n"
        
        full_content = header + content
        
        # Guardar en build/latex/components/
        draft_path = os.path.join(self.components_path, filename)
        with open(draft_path, "w", encoding="utf-8") as f:
            f.write(full_content)
            
        # Ruta relativa para el \input (desde build/latex/ hacia build/latex/components/)
        return fr"\input{{components/{filename}}}" + "\n"

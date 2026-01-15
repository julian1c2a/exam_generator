"""
FastAPI Web Interface for Exam Generator
==========================================

RESTful API + HTML Dashboard for managing exam problems.
Supports File and SQLite backends.
"""

from fastapi import FastAPI, HTTPException, Query, UploadFile, File
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse, FileResponse, JSONResponse, StreamingResponse
from pathlib import Path
import json
import csv
import io
from datetime import datetime
from typing import Optional, List, Dict, Any
import tempfile

# Importar repositorio y modelos
from database.file_repo import FileProblemRepository
from database.sqlite_repo import SQLiteProblemRepository
from models.problem import Problem, ProblemType

# Crear app FastAPI
app = FastAPI(
    title="Exam Generator",
    description="Web interface for managing exam problems",
    version="1.0.0"
)

# Montar archivos estáticos
static_dir = Path(__file__).parent / "static"
templates_dir = Path(__file__).parent / "templates"
static_dir.mkdir(exist_ok=True)
templates_dir.mkdir(exist_ok=True)

app.mount("/static", StaticFiles(directory=static_dir), name="static")

# Repositorio global (File por defecto)
REPO = None

def get_repo():
    """Obtener repositorio actual"""
    global REPO
    if REPO is None:
        REPO = FileProblemRepository("./problems_db")
    return REPO

def set_repo(repo_path: str, backend: str = "file"):
    """Configurar repositorio"""
    global REPO
    if backend == "sqlite":
        REPO = SQLiteProblemRepository(repo_path)
    else:
        REPO = FileProblemRepository(repo_path)

# ==================== RUTAS HTML ====================

@app.get("/", response_class=HTMLResponse)
async def dashboard():
    """Dashboard principal"""
    html_path = templates_dir / "index.html"
    if html_path.exists():
        return html_path.read_text()
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Exam Generator</title>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <link rel="stylesheet" href="/static/style.css">
    </head>
    <body>
        <nav class="navbar">
            <div class="container">
                <h1>Exam Generator</h1>
                <ul>
                    <li><a href="#" onclick="showTab('list')">Listar</a></li>
                    <li><a href="#" onclick="showTab('search')">Buscar</a></li>
                    <li><a href="#" onclick="showTab('stats')">Estadísticas</a></li>
                    <li><a href="#" onclick="showTab('export')">Exportar</a></li>
                    <li><a href="#" onclick="showTab('import')">Importar</a></li>
                </ul>
            </div>
        </nav>
        <div class="container">
            <div id="list-tab" class="tab">
                <h2>Problemas</h2>
                <div id="problems-list"></div>
            </div>
            <div id="search-tab" class="tab" style="display:none;">
                <h2>Buscar Problemas</h2>
                <input type="text" id="search-input" placeholder="Buscar...">
                <button onclick="search()">Buscar</button>
                <div id="search-results"></div>
            </div>
            <div id="stats-tab" class="tab" style="display:none;">
                <h2>Estadísticas</h2>
                <div id="stats-content"></div>
            </div>
            <div id="export-tab" class="tab" style="display:none;">
                <h2>Exportar</h2>
                <button onclick="exportJSON()">JSON</button>
                <button onclick="exportCSV()">CSV</button>
            </div>
            <div id="import-tab" class="tab" style="display:none;">
                <h2>Importar</h2>
                <input type="file" id="import-file">
                <button onclick="importFile()">Importar</button>
            </div>
        </div>
        <script src="/static/app.js"></script>
    </body>
    </html>
    """

# ==================== API: PROBLEMAS ====================

@app.get("/api/problems")
async def list_problems(
    problem_type: Optional[str] = None,
    difficulty: Optional[int] = None,
    limit: int = 50,
    offset: int = 0
):
    """Listar problemas con filtros opcionales"""
    repo = get_repo()
    filters = {}
    if problem_type:
        filters['problem_type'] = problem_type
    if difficulty is not None:
        filters['difficulty'] = difficulty
    filters['limit'] = limit
    filters['offset'] = offset
    
    try:
        problems = repo.list(filters)
        return {
            "success": True,
            "count": len(problems),
            "problems": [p.to_dict() for p in problems]
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/api/problems/{problem_id}")
async def get_problem(problem_id: str):
    """Obtener problema por ID"""
    repo = get_repo()
    try:
        problem = repo.load(problem_id)
        if not problem:
            raise HTTPException(status_code=404, detail="Problema no encontrado")
        return {
            "success": True,
            "problem": problem.to_dict()
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/api/problems")
async def create_problem(problem_data: Dict[str, Any]):
    """Crear nuevo problema"""
    repo = get_repo()
    try:
        problem = Problem.from_dict(problem_data)
        problem_id = repo.save(problem)
        return {
            "success": True,
            "problem_id": problem_id,
            "message": "Problema creado exitosamente"
        }
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error al crear: {str(e)}")

@app.put("/api/problems/{problem_id}")
async def update_problem(problem_id: str, problem_data: Dict[str, Any]):
    """Actualizar problema"""
    repo = get_repo()
    try:
        problem = Problem.from_dict(problem_data)
        problem.id = problem_id
        repo.save(problem)
        return {
            "success": True,
            "message": "Problema actualizado"
        }
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.delete("/api/problems/{problem_id}")
async def delete_problem(problem_id: str, confirm: bool = False):
    """Eliminar problema"""
    if not confirm:
        raise HTTPException(status_code=400, detail="Confirmación requerida")
    
    repo = get_repo()
    try:
        if repo.exists(problem_id):
            repo.delete(problem_id)
            return {"success": True, "message": "Problema eliminado"}
        else:
            raise HTTPException(status_code=404, detail="Problema no encontrado")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# ==================== API: BÚSQUEDA ====================

@app.get("/api/search")
async def search_problems(q: str, limit: int = 20):
    """Buscar problemas por texto"""
    repo = get_repo()
    try:
        all_problems = repo.list({'limit': 1000})
        results = []
        q_lower = q.lower()
        
        for p in all_problems:
            if q_lower in str(p.metadata.title).lower() or \
               q_lower in str(p.metadata.topic).lower() or \
               q_lower in str(p.metadata.tags).lower():
                results.append(p)
                if len(results) >= limit:
                    break
        
        return {
            "success": True,
            "count": len(results),
            "results": [p.to_dict() for p in results]
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# ==================== API: ESTADÍSTICAS ====================

@app.get("/api/stats")
async def get_stats():
    """Obtener estadísticas"""
    repo = get_repo()
    try:
        info = repo.info()
        return {
            "success": True,
            "stats": info
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# ==================== API: EXPORTAR ====================

@app.get("/api/export/json")
async def export_json(problem_type: Optional[str] = None):
    """Exportar a JSON"""
    repo = get_repo()
    try:
        filters = {}
        if problem_type:
            filters['problem_type'] = problem_type
        problems = repo.list(filters)
        
        data = [p.to_dict() for p in problems]
        json_str = json.dumps(data, indent=2)
        
        return StreamingResponse(
            iter([json_str]),
            media_type="application/json",
            headers={"Content-Disposition": f"attachment; filename=problems_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"}
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/api/export/csv")
async def export_csv(problem_type: Optional[str] = None):
    """Exportar a CSV"""
    repo = get_repo()
    try:
        filters = {}
        if problem_type:
            filters['problem_type'] = problem_type
        problems = repo.list(filters)
        
        output = io.StringIO()
        if problems:
            writer = csv.DictWriter(output, fieldnames=['id', 'type', 'title', 'difficulty', 'topic'])
            writer.writeheader()
            for p in problems:
                writer.writerow({
                    'id': p.id,
                    'type': p.type.value,
                    'title': p.metadata.title,
                    'difficulty': p.metadata.difficulty,
                    'topic': p.metadata.topic
                })
        
        csv_str = output.getvalue()
        return StreamingResponse(
            iter([csv_str]),
            media_type="text/csv",
            headers={"Content-Disposition": f"attachment; filename=problems_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"}
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# ==================== API: IMPORTAR ====================

@app.post("/api/import")
async def import_file(
    file: UploadFile = File(...),
    skip_duplicates: bool = False
):
    """Importar archivo JSON"""
    repo = get_repo()
    try:
        content = await file.read()
        data = json.loads(content.decode())
        
        if not isinstance(data, list):
            data = [data]
        
        imported_count = 0
        skipped_count = 0
        
        for item in data:
            try:
                problem = Problem.from_dict(item)
                if skip_duplicates and repo.exists(problem.id):
                    skipped_count += 1
                else:
                    repo.save(problem)
                    imported_count += 1
            except Exception as e:
                skipped_count += 1
        
        return {
            "success": True,
            "imported": imported_count,
            "skipped": skipped_count
        }
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

# ==================== API: CONFIGURACIÓN ====================

@app.post("/api/config/repo")
async def configure_repo(repo_path: str, backend: str = "file"):
    """Configurar repositorio (file o sqlite)"""
    try:
        set_repo(repo_path, backend)
        return {
            "success": True,
            "message": f"Repositorio configurado: {backend} - {repo_path}"
        }
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.get("/api/health")
async def health_check():
    """Health check"""
    try:
        repo = get_repo()
        info = repo.info()
        return {
            "status": "healthy",
            "backend": repo.__class__.__name__,
            "problems_count": info.get('total', 0)
        }
    except Exception as e:
        return {"status": "unhealthy", "error": str(e)}, 503

# ==================== INICIALIZACIÓN ====================

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

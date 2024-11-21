from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional

# Crear una instancia 
app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Welcome to my API!"}

@app.get("/favicon.ico")
async def favicon():
    return {"message": "No favicon available"}

#Creamos la clase alumno por medio del BeseModel
class Alumno(BaseModel):
    id: int
    nombre: str
    semestre: int
    carrera: Optional[str] = None
    estado: Optional[str] = None 

# Generamos una lista para dichos alumnos:
alumnos: List[Alumno] = []

# Lista de alumnos inicial
alumnos = [
    Alumno(id=1, nombre="Erick Santiago Díaz", semestre="4", carrera="Mecatronica", estado="Inscrito"),
    Alumno(id=2, nombre="Diana Velazques Romero", semestre="6", carrera="Telematica", estado="Egresado"),
    Alumno(id=3, nombre="Ramon Lopez Estrada", semestre="2", carrera="Bionica", estado="Inscrito")

]
# Ruta para añadir un alumno
@app.post("/alumnos/", response_model=Alumno)
def crear_alumno(alumno: Alumno):
    for a in alumnos:
        if a.id == alumno.id:
            raise HTTPException(status_code=400, detail="El alumno con ese ID ya existe.")
    alumnos.append(alumno)
    return alumno

# Ruta para obtener todos los alumnos
@app.get("/alumnos/", response_model=List[Alumno])
def obtener_alumnos():
    return alumnos

# Ruta para buscar un alumno por ID
@app.get("/alumnos/{alumno_id}", response_model=Alumno)
def obtener_alumno(alumno_id: int):
    for alumno in alumnos:
        if alumno.id == alumno_id:
            return alumno
    raise HTTPException(status_code=404, detail="Alumno no encontrado.")

# Ruta para eliminar un alumno por ID
@app.delete("/alumnos/{alumno_id}")
def eliminar_alumno(alumno_id: int):
    for index, alumno in enumerate(alumnos):
        if alumno.id == alumno_id:
            del alumnos[index]
            return {"message": "Alumno eliminado correctamente"}
    raise HTTPException(status_code=404, detail="Alumno no encontrado.")

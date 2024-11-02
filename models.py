from pydantic import BaseModel

# Definir un esquema de salida con Pydantic
class JuegosRecomendados(BaseModel):
    pregunta: str
    respuesta: str
    
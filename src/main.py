from fastapi import FastAPI
from src.core.config import settings
from src.api.routes import maquinas
from fastapi.middleware.cors import CORSMiddleware  # Importa el middleware CORS

app = FastAPI(title = settings.PROJECT_NAME, version = settings.PROJECT_VERSION)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # URL de tu frontend (React)
    allow_methods=["GET", "POST", "PUT", "DELETE"],  # Métodos permitidos
    allow_headers=["*"],  # Cabeceras permitidas
    allow_credentials=True,  # Si usas cookies o autenticación
)

app.include_router(maquinas.router, prefix = '/maquinas', tags = ['Maquinasss']) #CON ESTA LINEA ESTOY TRAYENDO TODOS LOS ENDPOINT DE MAQUINAS

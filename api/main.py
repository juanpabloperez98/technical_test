from fastapi import FastAPI
from dotenv import load_dotenv
from routes.auth import auth_routes
from routes.procesos import procesos_route
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth_routes, prefix="/api")
app.include_router(procesos_route, prefix="/api")


load_dotenv()
from fastapi import FastAPI
from app.routes import taskroutes


from contextlib import asynccontextmanager
from app.db.session import init_db
async def lifespan(app: FastAPI):
    init_db()
    yield
    





app = FastAPI(lifespan=lifespan)

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


origins = [
    "http://localhost:3000", 
    "http://127.0.0.1:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,           
    allow_credentials=True,
    allow_methods=["*"],             
    allow_headers=["*"],             
)

app.include_router(taskroutes.router)


@app.get('/')
def root():
    return {"message": "Welcome to the Task Management API",
            "docs": "/docs",
            "health": "/health",
            "tasks": "/tasks"}
@app.get('/health')
def api_health():
    return {"status":"ok"}



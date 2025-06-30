from fastapi import FastAPI
from app.routes import taskroutes


from contextlib import asynccontextmanager
from app.db.session import init_db
async def lifespan(app: FastAPI):
    init_db()
    yield
    





app = FastAPI(lifespan=lifespan)


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



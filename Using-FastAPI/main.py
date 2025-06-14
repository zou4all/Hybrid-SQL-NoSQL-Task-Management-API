
from fastapi import FastAPI
from app.api.endpoints import users, tasks

app = FastAPI()

# Include routers
app.include_router(users.router, prefix="/users", tags=["Users"])
app.include_router(tasks.router, prefix="/tasks", tags=["Tasks"])

# To run: uvicorn main:app --reload
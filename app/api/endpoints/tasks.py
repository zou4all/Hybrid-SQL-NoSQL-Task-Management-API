
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.core.database import get_sql_db, get_mongo_db
from app.crud import sql_crud, mongo_crud
from app.models.mongo_models import TaskDetails
from bson import ObjectId
from app.models.sql_models import Task

router = APIRouter()







def clean_objectids(doc):
    if isinstance(doc, list):
        return [clean_objectids(i) for i in doc]
    elif isinstance(doc, dict):
        return {
            k: clean_objectids(str(v)) if isinstance(v, ObjectId) else clean_objectids(v)
            for k, v in doc.items()
        }
    return doc


@router.post("/")
def create_task(title: str, status: str, user_id: int, db: Session = Depends(get_sql_db)):
    return sql_crud.create_task(db, title, status, user_id)

@router.post("/{task_id}/details")
async def add_task_details(task_id: int, details: TaskDetails, mongo_db = Depends(get_mongo_db)):
    await mongo_crud.create_task_details(mongo_db, details)
    return {"message": "Task details added."}


@router.get("/tasks/{task_id}")
async def get_task(task_id: int, db: Session = Depends(get_sql_db), mongo_db=Depends(get_mongo_db)):
    task = db.query(Task).filter(Task.id == task_id).first()
    mongo_details = await mongo_db.task_details.find_one({"task_id": task_id})
    
    if mongo_details:
        mongo_details = clean_objectids(mongo_details)

    return {
        "task": task,
        "details": mongo_details
    }



@router.get("/hybrid/tasks/{task_id}")
async def get_hybrid_task(task_id: int, db: Session = Depends(get_sql_db), mongo_db=Depends(get_mongo_db)):
    task = db.query(Task).filter(Task.id == task_id).first()
    mongo_details = await mongo_db.task_details.find_one({"task_id": task_id})
    
    if mongo_details:
        mongo_details = clean_objectids(mongo_details)

    return {
        "task": {
            "id": task.id,
            "title": task.title,
            "status": task.status
        } if task else None,
        "details": mongo_details
    }

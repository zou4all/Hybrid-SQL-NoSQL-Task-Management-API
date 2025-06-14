
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.core.database import get_sql_db
from app.crud import sql_crud

router = APIRouter()

@router.post("/")
def create_user(username: str, email: str, db: Session = Depends(get_sql_db)):
    return sql_crud.create_user(db, username, email)

@router.get("/{user_id}")
def read_user(user_id: int, db: Session = Depends(get_sql_db)):
    return sql_crud.get_user(db, user_id)

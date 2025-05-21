
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from motor.motor_asyncio import AsyncIOMotorClient
from app.core.config import DATABASE_URL, MONGO_URI

# SQLAlchemy setup
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_sql_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# MongoDB setup
mongo_client = AsyncIOMotorClient(MONGO_URI)
mongo_db = mongo_client.hybrid_app

def get_mongo_db():
    return mongo_db

from app.models.mongo_models import TaskDetails
from motor.motor_asyncio import AsyncIOMotorDatabase

async def create_task_details(db: AsyncIOMotorDatabase, task_details: TaskDetails):
    await db.task_details.insert_one(task_details.dict())

async def get_task_details(db: AsyncIOMotorDatabase, task_id: int):
    return await db.task_details.find_one({"task_id": task_id})

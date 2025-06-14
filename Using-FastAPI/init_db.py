from app.models.sql_models import Base
from app.core.database import engine

Base.metadata.create_all(bind=engine)
print("Tables créées avec succès.")

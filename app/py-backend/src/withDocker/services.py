import models
from database import engine, SessionLocal
from fastapi import Depends
from sqlalchemy.orm import Session
from fastapi.params import Annotated

# Crie todas as tabelas novamente
models.Base.metadata.create_all(bind=engine)

def get_db():
  db = SessionLocal()
  try:
    yield db
  finally:
    db.close()
    
db_dependency = Annotated[Session, Depends(get_db)]
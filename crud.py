from sqlalchemy.orm import Sessionfrom . import models, schemas

def create_cooperative(db: Session, cooperative: schemas.CooperativeCreate):    db_cooperative = models.Cooperative(**cooperative.dict())
    db.add(db_cooperative)    db.commit()
    db.refresh(db_cooperative)  
  return db_cooperative

def get_cooperative(db: Session, cooperative_id: int): 
   return db.query(models.Cooperative).filter(models.Cooperative.CooperativeID == cooperative_id).first()

def get_cooperatives(db: Session, skip: int = 0, limit: int = 10): 
   return db.query(models.Cooperative).offset(skip).limit(limit).all()


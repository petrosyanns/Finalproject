from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
import models, schemas, crud
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app=FastApi()



def get_db():
   db = SessionLocal()
   try:
       yield db
   finally:
     db.close()


@app.post("/cooperatives/", response_model=schemas.Cooperative)
def create_cooperative(cooperative: schemas.CooperativeCreate, db: Session = Depends(get_db)):
    return crud.create_cooperative(db=db, cooperative=cooperative)


@app.get("/cooperatives/", response_model=list[schemas.Cooperative])
def read_cooperatives(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud.get_cooperatives(db=db, skip=skip, limit=limit)



@app.get("/cooperatives/{cooperative_id}", response_model=schemas.Cooperative)
def read_cooperative(cooperative_id: int, db: Session = Depends(get_db)):
    db_cooperative = crud.get_cooperative(db=db, cooperative_id=cooperative_id)
    if db_cooperative is None:
        raise HTTPException(status_code=404, detail="Cooperative not found")
    return db_cooperative


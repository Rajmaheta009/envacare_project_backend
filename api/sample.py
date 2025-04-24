from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from Schema.sample import SampleCreate, SampleUpdate, SampleOut
from model.sample import Sample
from typing import List

router = APIRouter()


@router.post("/", response_model=SampleOut)
def create_sample(sample: SampleCreate, db: Session = Depends(get_db)):
    db_sample = Sample(**sample.dict())
    db.add(db_sample)
    db.commit()
    db.refresh(db_sample)
    return db_sample


@router.get("/get_sample", response_model=List[SampleOut])
def get_all_samples(db: Session = Depends(get_db)):
    return db.query(Sample).filter(Sample.is_delete == False).all()


@router.get("/{sample_id}", response_model=SampleOut)
def get_sample(sample_id: int, db: Session = Depends(get_db)):
    sample = db.query(Sample).filter(Sample.id == sample_id, Sample.is_delete == False).first()
    if not sample:
        raise HTTPException(status_code=404, detail="Sample not found")
    return sample


@router.put("/{sample_id}", response_model=SampleOut)
def update_sample(sample_id: int, updated_data: SampleUpdate, db: Session = Depends(get_db)):
    sample = db.query(Sample).filter(Sample.id == sample_id).first()
    if not sample:
        raise HTTPException(status_code=404, detail="Sample not found")

    for key, value in updated_data.dict().items():
        setattr(sample, key, value)

    db.commit()
    db.refresh(sample)
    return sample


@router.delete("/{sample_id}")
def delete_sample(sample_id: int, db: Session = Depends(get_db)):
    sample = db.query(Sample).filter(Sample.id == sample_id).first()
    if not sample:
        raise HTTPException(status_code=404, detail="Sample not found")

    sample.is_delete = True
    db.commit()
    return {"detail": "Sample soft-deleted"}

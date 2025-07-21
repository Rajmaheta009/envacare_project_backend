from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from model.quick_result import QuickResult
from Schema.quick_result import QuickResultCreate, QuickResultOut

router = APIRouter()

# Create a new quick result
@router.post("/re", response_model=QuickResultOut)
def create_quick_result(payload: QuickResultCreate, db: Session = Depends(get_db)):
    quick_result = QuickResult(**payload.dict())
    db.add(quick_result)
    db.commit()
    db.refresh(quick_result)
    return quick_result

# Get all quick results (not deleted)
@router.get("/", response_model=list[QuickResultOut])
def get_all_quick_results(db: Session = Depends(get_db)):
    results = db.query(QuickResult).filter(QuickResult.is_delete == False).all()
    return results

# Soft delete by ID
@router.put("/{id}/delete", response_model=QuickResultOut)
def soft_delete_quick_result(id: int, db: Session = Depends(get_db)):
    result = db.query(QuickResult).filter(QuickResult.id == id).first()
    if not result:
        raise HTTPException(status_code=404, detail="Result not found")

    result.is_delete = True
    db.commit()
    db.refresh(result)
    return result

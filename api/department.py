from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from database import get_db
from model import department as models
from Schema import department as schemas

router = APIRouter()

# Create Department
@router.post("/", response_model=schemas.DepartmentOut)
def create_department(dept: schemas.DepartmentCreate, db: Session = Depends(get_db)):
    new_dept = models.Department(**dept.dict())
    db.add(new_dept)
    db.commit()
    db.refresh(new_dept)
    return new_dept

# Get All Departments
@router.get("/", response_model=list[schemas.DepartmentOut])
def get_departments(db: Session = Depends(get_db)):
    return db.query(models.Department).filter(models.Department.is_deleted == False).all()

# Get Single Department by ID
@router.get("/{dept_id}", response_model=schemas.DepartmentOut)
def get_department(dept_id: int, db: Session = Depends(get_db)):
    dept = db.query(models.Department).filter(models.Department.id == dept_id, models.Department.is_deleted == False).first()
    if not dept:
        raise HTTPException(status_code=404, detail="Department not found")
    return dept

# Update Department
@router.put("/{dept_id}", response_model=schemas.DepartmentOut)
def update_department(dept_id: int, updated: schemas.DepartmentUpdate, db: Session = Depends(get_db)):
    dept = db.query(models.Department).filter(models.Department.id == dept_id).first()
    if not dept:
        raise HTTPException(status_code=404, detail="Department not found")
    for key, value in updated.dict(exclude_unset=True).items():
        setattr(dept, key, value)
    db.commit()
    db.refresh(dept)
    return dept

# Soft Delete Department
@router.delete("/{dept_id}")
def delete_department(dept_id: int, db: Session = Depends(get_db)):
    dept = db.query(models.Department).filter(models.Department.id == dept_id).first()
    if not dept:
        raise HTTPException(status_code=404, detail="Department not found")
    dept.is_deleted = True
    db.commit()
    return {"detail": "Department deleted successfully"}

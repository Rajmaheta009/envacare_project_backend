from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from database import get_db
from model import employee as models
from Schema import employee as schemas

router = APIRouter(
    prefix="/employees",
    tags=["Employees"]
)

# Create Employee
@router.post("/", response_model=schemas.EmployeeOut)
def create_employee(emp: schemas.EmployeeCreate, db: Session = Depends(get_db)):
    db_emp = db.query(models.Employee).filter(models.Employee.email == emp.email).first()
    if db_emp:
        raise HTTPException(status_code=400, detail="Email already registered")
    new_emp = models.Employee(**emp.dict())
    db.add(new_emp)
    db.commit()
    db.refresh(new_emp)
    return new_emp

# Get All Employees
@router.get("/", response_model=list[schemas.EmployeeOut])
def get_employees(db: Session = Depends(get_db)):
    return db.query(models.Employee).filter(models.Employee.is_deleted == False).all()

# Get Single Employee
@router.get("/{emp_id}", response_model=schemas.EmployeeOut)
def get_employee(emp_id: int, db: Session = Depends(get_db)):
    emp = db.query(models.Employee).filter(models.Employee.id == emp_id, models.Employee.is_deleted == False).first()
    if not emp:
        raise HTTPException(status_code=404, detail="Employee not found")
    return emp

# Update Employee
@router.put("/{emp_id}", response_model=schemas.EmployeeOut)
def update_employee(emp_id: int, updated: schemas.EmployeeUpdate, db: Session = Depends(get_db)):
    emp = db.query(models.Employee).filter(models.Employee.id == emp_id).first()
    if not emp:
        raise HTTPException(status_code=404, detail="Employee not found")
    for key, value in updated.dict(exclude_unset=True).items():
        setattr(emp, key, value)
    db.commit()
    db.refresh(emp)
    return emp

# Soft Delete Employee
@router.delete("/{emp_id}")
def delete_employee(emp_id: int, db: Session = Depends(get_db)):
    emp = db.query(models.Employee).filter(models.Employee.id == emp_id).first()
    if not emp:
        raise HTTPException(status_code=404, detail="Employee not found")
    emp.is_deleted = True
    db.commit()
    return {"detail": "Employee deleted successfully"}
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from model.order_parameter import OrderParameter
from Schema.order_parameter import OrderParameterCreate, OrderParameterOut

router = APIRouter()

@router.post("/", response_model=OrderParameterOut)
def create_quotation_parameter(payload: OrderParameterCreate, db: Session = Depends(get_db)):
    new_qp = OrderParameter(**payload.dict())
    db.add(new_qp)
    db.commit()
    db.refresh(new_qp)
    return new_qp


@router.get("/op_id/{quotation_id}")
def get_quotation_parameter(quotation_id: int, db: Session = Depends(get_db)):
    qp = db.query(OrderParameter).filter(
        OrderParameter.quotation_id == quotation_id,
        OrderParameter.is_delete == False
    ).all()

    if not qp:
        raise HTTPException(status_code=405, detail="Quotation Parameter not found")
    return qp


@router.get("/")
def get_quotation_parameter(db: Session = Depends(get_db)):
    qp = db.query(OrderParameter).all()
    if not qp:
        raise HTTPException(status_code=404, detail="Quotation Parameter not found")
    return qp

@router.put("/{id}", response_model=OrderParameterOut)
def update_quotation_parameter(id: int, payload: OrderParameterCreate, db: Session = Depends(get_db)):
    qp = db.query(OrderParameter).filter(OrderParameter.id == id).first()
    if not qp:
        raise HTTPException(status_code=404, detail="Quotation Parameter not found")
    for key, value in payload.dict(exclude_unset=True).items():
        setattr(qp, key, value)
    db.commit()
    db.refresh(qp)
    return qp

@router.delete("/{id}")
def delete_quotation_parameter(id: int, db: Session = Depends(get_db)):
    qp = db.query(OrderParameter).filter(OrderParameter.id == id).first()
    if not qp:
        raise HTTPException(status_code=404, detail="Quotation Parameter not found")
    qp.is_delete = True
    db.commit()
    return {"message": "Quotation Parameter soft-deleted"}

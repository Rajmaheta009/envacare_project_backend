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


@router.get("/op_id/{quot_id}")
def get_quotation_parameter(quot_id: int, db: Session = Depends(get_db)):
    qp = db.query(OrderParameter).filter(
        OrderParameter.quotation_id == quot_id,
        OrderParameter.is_delete == False
    ).all()

    if not qp:
        raise HTTPException(status_code=405, detail="Quotation Parameter not found")
    return qp


@router.get("/submitted_results/{quotation_id}")
def get_submitted_results(quotation_id: int, db: Session = Depends(get_db)):
    results = db.query(OrderParameter).filter(
        OrderParameter.quotation_id == quotation_id,
        OrderParameter.result.isnot(None),
        OrderParameter.is_delete == False
    ).all()

    if not results:
        raise HTTPException(status_code=404, detail="No submitted results found")
    return results


@router.get("/")
def get_quotation_parameter(db: Session = Depends(get_db)):
    qp = db.query(OrderParameter).all()
    if not qp:
        raise HTTPException(status_code=404, detail="Quotation Parameter not found")
    return qp

@router.put("/{p_id}", response_model=OrderParameterOut)
def update_quotation_parameter(p_id: int, payload: OrderParameterCreate, db: Session = Depends(get_db)):
    qp = db.query(OrderParameter).filter(OrderParameter.parameter_id == p_id).first()
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


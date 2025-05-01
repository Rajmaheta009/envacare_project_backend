from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from model.quotation import Quotation
from Schema.quotation import QuotationCreate, QuotationResponse

router = APIRouter()

# ✅ Create quotation
@router.post("/", response_model=QuotationResponse)
def create_quotation(quotation: QuotationCreate, db: Session = Depends(get_db)):
    new_quotation = Quotation(order_id=quotation.order_id, pdf_url=quotation.pdf_url)
    db.add(new_quotation)
    db.commit()
    db.refresh(new_quotation)
    return new_quotation

# ✅ Get single quotation
@router.get("/{order_id}", response_model=QuotationResponse)
def get_quotation(order_id: int, db: Session = Depends(get_db)):
    quotation = db.query(Quotation).filter(
        Quotation.order_id == order_id,
        Quotation.is_delete == False
    ).first()
    if not quotation:
        raise HTTPException(status_code=404, detail="Quotation not found")
    return quotation

# ✅ Get all quotations
@router.get("/", response_model=list[QuotationResponse])
def get_all_quotations(db: Session = Depends(get_db)):
    quotations = db.query(Quotation).filter(Quotation.is_delete == False).all()
    return quotations

# ✅ Update quotation
@router.put("/quotation/{quotation_id}", response_model=QuotationResponse)
def update_quotation(quotation_id: int, updated_data: QuotationCreate, db: Session = Depends(get_db)):
    quotation = db.query(Quotation).filter(Quotation.id == quotation_id, Quotation.is_delete == False).first()
    if not quotation:
        raise HTTPException(status_code=404, detail="Quotation not found")

    quotation.order_id = updated_data.order_id
    quotation.pdf_url = updated_data.pdf_url
    db.commit()
    db.refresh(quotation)
    return quotation

# ✅ Delete quotation (soft delete)
@router.delete("/{quotation_id}")
def delete_quotation(quotation_id: int, db: Session = Depends(get_db)):
    quotation = db.query(Quotation).filter(Quotation.id == quotation_id).first()
    if not quotation:
        raise HTTPException(status_code=404, detail="Quotation not found")

    quotation.is_active = False
    quotation.is_delete = True
    db.commit()
    return {"message": "Quotation deleted successfully"}

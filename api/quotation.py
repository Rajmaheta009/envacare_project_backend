# --- api/quotation.py ---
import shutil
import uuid
import os
from fastapi import APIRouter, Depends, HTTPException, Body
from sqlalchemy.orm import Session
from database import get_db
from model.quotation import Quotation, get_next_id
from Schema.quotation import QuotationCreate, QuotationResponse
from utility.quotation_pdf_generater.qoutation_invoice_maker import quotation_pdf_create
from dotenv import load_dotenv

load_dotenv()

BASE_URL = os.getenv('BASE_URL')
UPLOAD_DIR = "static/Quotation/"

router = APIRouter()

@router.post("/", response_model=dict)
def create_quotation(payload: QuotationCreate, db: Session = Depends(get_db)):
    # Step 1: Get next quotation ID manually
    next_id = get_next_id(db)

    # Step 2: Generate PDF
    quotation_pdf_path = quotation_pdf_create(payload.customer_id, payload.parameter_info)

    # Step 3: Save PDF as static/Quotation/<id>.pdf
    os.makedirs("static/Quotation", exist_ok=True)
    filename = f"{next_id}.pdf"
    output_pdf_path = os.path.join("static/Quotation", filename)

    with open(quotation_pdf_path, "rb") as pdf_file:
        with open(output_pdf_path, "wb") as f:
            f.write(pdf_file.read())

    # Step 4: Insert quotation record with fixed ID and filename
    quotation = Quotation(
        id=next_id,
        order_id=payload.order_id,
        pdf_url=filename,
        is_active=True,
        is_delete=False
    )
    db.add(quotation)
    db.commit()

    return {
        "message": "Quotation PDF generated successfully",
        "pdf_url": filename,
        "quotation_id": next_id
    }

@router.get("/{order_id}", response_model=QuotationResponse)
def get_quotation(order_id: int, db: Session = Depends(get_db)):
    quotation = db.query(Quotation).filter(
        Quotation.order_id == order_id,
        Quotation.is_delete == False
    ).first()
    if not quotation:
        raise HTTPException(status_code=404, detail="Quotation not found")
    return quotation

@router.get("/", response_model=list[QuotationResponse])
def get_all_quotations(db: Session = Depends(get_db)):
    return db.query(Quotation).filter(Quotation.is_delete == False).all()

@router.put("/quotation/{quotation_id}", response_model=QuotationResponse)
def update_quotation(quotation_id: int, updated_data: QuotationCreate, db: Session = Depends(get_db)):
    quotation = db.query(Quotation).filter(Quotation.id == quotation_id, Quotation.is_delete == False).first()
    if not quotation:
        raise HTTPException(status_code=404, detail="Quotation not found")
    quotation.order_id = updated_data.order_id
    db.commit()
    db.refresh(quotation)
    return quotation

@router.delete("/{quotation_id}")
def delete_quotation(quotation_id: int, db: Session = Depends(get_db)):
    quotation = db.query(Quotation).filter(Quotation.id == quotation_id).first()
    if not quotation:
        raise HTTPException(status_code=404, detail="Quotation not found")
    quotation.is_active = False
    quotation.is_delete = True
    db.commit()
    return {"message": "Quotation deleted successfully"}

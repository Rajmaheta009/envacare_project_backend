import shutil
from fastapi import APIRouter, Depends, HTTPException,UploadFile,File,Form
from typing import Optional
from sqlalchemy.orm import Session
from database import get_db
from model.quotation import Quotation ,get_next_id
from Schema.quotation import QuotationCreate, QuotationResponse
import os
from dotenv import load_dotenv
load_dotenv()
BASE_URL = os.getenv('BASE_URL')

router = APIRouter()

UPLOAD_DIR = "static/Quotation/"

def append_filename(quotation):
    """ Add file URL to order output """
    file_url = f"{BASE_URL}{UPLOAD_DIR}/{quotation.pdf}" if quotation.pdf != "No document uploaded" else "No document uploaded"

    return {
        "id": quotation.id,
        "pdf": file_url,
    }

# # ✅ Create quotation
# @router.post("/", response_model=QuotationResponse)
# def create_quotation(order_id:int,
#                      pdf:Optional[UploadFile] = File()
#                      , db: Session = Depends(get_db)):
#     if pdf != "":
#         next_id = get_next_id(db)
#         filename = pdf.filename
#         file_extension = '.' + filename.split('.')[-1] if '.' in filename else ''
#
#         new_filename = f"{next_id+1}{file_extension}"
#
#         image_path = os.path.join(UPLOAD_DIR, new_filename)
#
#         # ✔️ Save the file
#         with open(image_path, "wb") as f:
#             shutil.copyfileobj(pdf.file, f)
#
#     # raise HTTPException(status_code=400,detail=f"{file_extension}")
#     # return f"{file_extension}"
#     else:
#         new_filename="that is not work"
#
#     new_quotation = Quotation(order_id=order_id, pdf_url=new_filename)
#     db.add(new_quotation)
#     db.commit()
#     db.refresh(new_quotation)
#     return new_quotation

@router.post("/", response_model=dict)
def create_quotation(
    order_id: int = Form(...),
    pdf_url: Optional[UploadFile] = File(None),
    db: Session = Depends(get_db)
):
    if pdf_url:
        next_id = get_next_id(db)  # Assuming you have this helper
        file_extension = os.path.splitext(pdf_url.filename)[-1]
        new_filename = f"{next_id + 1}{file_extension}"
        image_path = os.path.join(UPLOAD_DIR, new_filename)

        # Save the file
        with open(image_path, "wb") as f:
            shutil.copyfileobj(pdf_url.file, f)
    else:
        new_filename = "No document uploaded"
        image_path = new_filename

    # Save to database
    new_quotation = Quotation(order_id=order_id, pdf_url=image_path)
    db.add(new_quotation)
    db.commit()
    db.refresh(new_quotation)

    return {"id": new_quotation.id}

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

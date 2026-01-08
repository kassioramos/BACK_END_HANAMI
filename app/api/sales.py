from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List
from datetime import datetime

router = APIRouter(prefix="/sales", tags=["Vendas"])

# ---------- MODELO ----------
class Sale(BaseModel):
    id: int
    product_id: int
    quantity: int
    total_value: float
    date: datetime

# ---------- BANCO EM MEMÓRIA ----------
sales_db: List[Sale] = []

# ---------- ENDPOINTS ----------
@router.post("/", response_model=Sale)
def create_sale(sale: Sale):
    sales_db.append(sale)
    return sale


@router.get("/", response_model=List[Sale])
def list_sales():
    return sales_db

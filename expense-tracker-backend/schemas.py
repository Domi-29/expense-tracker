from pydantic import BaseModel
from datetime import date
from typing import Optional

# spoločný základ
class ExpenseBase(BaseModel):
    title: str
    amount: float
    category: str
    date: Optional[date] = None


# CREATE
class ExpenseCreate(ExpenseBase):
    pass


# UPDATE (partial update → bezpečné)
class ExpenseUpdate(BaseModel):
    title: Optional[str] = None
    amount: Optional[float] = None
    category: Optional[str] = None
    date: Optional[date] = None
    type: Optional[str] = None



# RESPONSE
class ExpenseResponse(ExpenseBase):
    id: int

    class Config:
        from_attributes = True
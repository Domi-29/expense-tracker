from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from datetime import date
from fastapi.middleware.cors import CORSMiddleware

from database import SessionLocal, engine
import models

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# CREATE (FIXED)
@app.post("/expenses")
def create_expense(expense: dict, db: Session = Depends(get_db)):

    print("RECEIVED:", expense)

    if "date" not in expense or not expense["date"]:
        expense["date"] = date.today()

    new_expense = models.Expense(**expense)

    db.add(new_expense)
    db.commit()        # 🔥 toto MUSÍ byť
    db.refresh(new_expense)

    print("SAVED:", new_expense)

    return new_expense


# READ
@app.get("/expenses")
def get_expenses(db: Session = Depends(get_db)):
    return db.query(models.Expense).all()


# DELETE
@app.delete("/expenses/{expense_id}")
def delete_expense(expense_id: int, db: Session = Depends(get_db)):
    expense = db.query(models.Expense).filter(models.Expense.id == expense_id).first()

    if not expense:
        raise HTTPException(status_code=404, detail="Not found")

    db.delete(expense)
    db.commit()

    return {"message": "deleted"}
from sqlalchemy import Column, Integer, String, Float, Date
from database import Base
from datetime import date

class Expense(Base):
    __tablename__ = "expenses"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    amount = Column(Float, nullable=False)
    category = Column(String, nullable=False)
    type = Column(String, nullable=False)  # income / expense
    date = Column(Date, nullable=False, default=date.today)
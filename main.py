from datetime import datetime

from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel


app = FastAPI(title="Transaction Processing API")

transactions = []


class Schema(BaseModel):
    user_id: str
    amount: float
    type: str
    timestamp: datetime


@app.post("/transactions", status_code=status.HTTP_201_CREATED)
def create(transaction: Schema):
    if transaction.amount <= 0:
        raise HTTPException(
            status_code=400,
            detail="Amount must be greater than 0"
        )
    if transaction.type not in ["credit", "debit"]:
        raise HTTPException(
            status_code=400,
            detail="Transaction type must be credit or debit"
        )
    transactions.append(transaction)
    return {
        "message": "Transaction created successfully",
        "transaction": transaction,
        "status": status.HTTP_201_CREATED
    }


@app.get("/transactions/{user_id}", status_code=status.HTTP_200_OK)
def get(user_id: str):
    user_transactions = []
    for transaction in transactions:
        if transaction.user_id == user_id:
            user_transactions.append(transaction)
    if not user_transactions:
        raise HTTPException(
            status_code=404,
            detail="No transactions found for this user"
        )
    return user_transactions

@app.get("/transactions/{user_id}/summary", status_code=status.HTTP_200_OK)
def get_summary(user_id: str):
    if user_id not in transactions:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="No transactions found for this user"
        )
    total_credit = 0
    total_debit = 0
    for transaction in transactions[user_id]:
        if transaction.type == "credit":
            total_credit += transaction.amount
        else:
            total_debit += transaction.amount
    return {
        "total_credit": total_credit,
        "total_debit": total_debit,
        "balance": total_credit - total_debit
    }
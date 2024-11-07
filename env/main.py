from fastapi import FastAPI

app = FastAPI()
from pydantic import BaseModel
from fastapi import HTTPException

# Define a data model for customer registration (Creating columns of table for a database)
class Customer(BaseModel):
    id: int
    name: str
    email: str
    phone: str

# Create a dictionary to store customer data
customers = {}

@app.post("/register/")
def register_customer(customer: Customer):
    if customer.id in customers:
        raise HTTPException(status_code=400, detail="Customer already exists")
    
    # Save the customer in the dictionary
    customers[customer.id] = customer
    return {"message": "Customer registered successfully", "customer": customer}

# Retrieve Customer Info based on their ID
@app.get("/customer/{customer_id}")
def get_customer(customer_id: int):
    customer = customers.get(customer_id)
    if not customer:
        raise HTTPException(status_code=404, detail="Customer not found")
    return customer

#Loan Application (Allows customer to apply for a loan)
class LoanApplication(BaseModel): 
    customer_id: int
    amount: float
    purpose: str

loans = {}

@app.post("/apply-loan/")
def apply_loan(application: LoanApplication):
    if application.customer_id not in customers:
        raise HTTPException(status_code=404, detail="Customer not found")
    
    loan_id = len(loans) + 1
    loans[loan_id] = {"customer_id": application.customer_id, "amount": application.amount, "purpose": application.purpose, "status": "pending"}
    return {"message": "Loan application submitted successfully", "loan_id": loan_id}


# Loan Status Endpoint 
@app.get("/loan-status/{loan_id}")
def loan_status(loan_id: int):
    loan = loans.get(loan_id)
    if not loan:
        raise HTTPException(status_code=404, detail="Loan not found")
    return loan

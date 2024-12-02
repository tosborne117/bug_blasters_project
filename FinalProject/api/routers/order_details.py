from fastapi import APIRouter, Depends, FastAPI, status, Response
from sqlalchemy.orm import Session
from ..controllers import order_details as controller
from ..schemas import order_details as schema
from ..dependencies.database import engine, get_db

router = APIRouter(
    tags=['Order Details'],
    prefix="/orderdetails"
)


@router.post("/", response_model=schema.OrderDetail)
def create(request: schema.OrderDetailCreate, db: Session = Depends(get_db)):
    return controller.create(db=db, request=request)


@router.get("/", response_model=list[schema.OrderDetail])
def read_all(db: Session = Depends(get_db)):
    return controller.read_all(db)


@router.get("/{item_id}", response_model=schema.OrderDetail)
def read_one(item_id: int, db: Session = Depends(get_db)):
    return controller.read_one(db, item_id=item_id)


@router.put("/{item_id}", response_model=schema.OrderDetail)
def update(item_id: int, request: schema.OrderDetailUpdate, db: Session = Depends(get_db)):
    return controller.update(db=db, request=request, item_id=item_id)


@router.delete("/{item_id}")
def delete(item_id: int, db: Session = Depends(get_db)):
    return controller.delete(db=db, item_id=item_id)

# PaymentDetail Endpoints (Nested)
@router.post("/{order_id}/paymentdetails", response_model=schema.PaymentDetail)
def create_payment(order_id: int, request: schema.PaymentDetailCreate, db: Session = Depends(get_db)):
    return controller.create_payment(db=db, order_id=order_id, request=request)


@router.get("/{order_id}/paymentdetails", response_model=list[schema.PaymentDetail])
def read_payments(order_id: int, db: Session = Depends(get_db)):
    return controller.read_payments_by_order(db=db, order_id=order_id)


@router.delete("/paymentdetails/{payment_id}")
def delete_payment(payment_id: int, db: Session = Depends(get_db)):
    return controller.delete_payment(db=db, payment_id=payment_id)
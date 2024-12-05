from sqlalchemy.orm import Session, joinedload
from fastapi import HTTPException, status, Response, Depends
from ..models import orders as order_model
from ..models import orderstatus as status_model
from sqlalchemy.exc import SQLAlchemyError



def create(db: Session, request):
    new_order = order_model.Order(
        customer_id=request.customer_id,
        customer_name=request.customer_name,
        description=request.description,
        order_date=request.order_date,
        payment_type=request.payment_type,
        promotion_key=request.promotion_key,
        order_status=request.order_status
    )

    try:
        db.add(new_order)
        db.commit()
        db.refresh(new_order)
        return{
            "order_id": new_order.order_id,
            "customer_name": new_order.customer_name,
            "order_date": new_order.order_date,
            "description": new_order.description,
            "payment_type": new_order.payment_type,
            "promotion_key": new_order.promotion_key,
            "order_status": new_order.order_status
        }
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)

def read_all(db: Session):
    try:
        orders = db.query(order_model.Order).options(joinedload(order_model.Order.orderstatus)).all()
        result = []
        for order in orders:
            result.append({
                "order_id": order.order_id,
                "customer_name": order.customer_name,
                "order_date": order.order_date,
                "description": order.description,
                "payment_type": order.payment_type,
                "promotion_key": order.promotion_key,
                "order_status": order.order_status
            })
        return result
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)


def read_one(db: Session, order_id: int):
    try:
        order = db.query(order_model.Order).all()
        #order = db.query(order_model.Order).options(joinedload(order_model.Order.orderstatus)).filter(order_model.Order.order_id == order_id).first()
        if not order:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Id not found!")
        return {
            "order_id": order.order_id,
                "customer_name": order.customer_name,
                "order_date": order.order_date,
                "description": order.description,
                "payment_type": order.payment_type,
                "promotion_key": order.promotion_key,
                "order_status": order.order_status
        }
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)


def update(db: Session, order_id: int, request):
    try:
        order = db.query(order_model.Order).filter(order_model.Order.order_id == order_id)
        if not order.first():
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Id not found!")

        order.update(request.dict(exclude_unset=True), synchronize_session=False)
        db.commit()
        return order.first()
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)


def delete(db: Session, order_id: int):
    try:
        order = db.query(order_model.Order).filter(order_model.Order.order_id == order_id).first()
        if not order:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Id not found!")
        db.delete(order)
        db.commit()
        return Response(status_code=status.HTTP_204_NO_CONTENT)
    except SQLAlchemyError as e:
        error = str(e.__dict__.get('orig', str(e)))
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)

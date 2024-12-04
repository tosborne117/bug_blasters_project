from sqlalchemy.orm import Session
from fastapi import HTTPException, status, Response, Depends
from ..models import orderstatus as status_model
from ..models import orders as order_model
from sqlalchemy.exc import SQLAlchemyError


def create(db: Session, order_id: int, status: str):
    try:
        order = db.query(order_model.Order).filter(order_model.Order.order_id == order_id).first()
        if not order:
            raise HTTPException(status_code=404, detail="Order wasn't fount")

        new_status = status_model.OrderStatus(
        order_id  = order_id,
        order_status = status
        )

        db.add(new_status)
        db.commit()
        db.refresh(new_status)
        return {"order_id": order_id, "status": new_status.order_status}
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)

def read_all(db: Session):
    try:
        all_status = db.query(status_model.OrderStatus).all()
        result = []

        for status in all_status:
            result.append({
                "tracking_num": status.tracking_num,
                "order_id": status.order_id,
                "status": status.order_status
            })
        return result
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)

def read_one(db: Session, order_id: int):
    try:
        status = db.query(status_model.OrderStatus).filter(status_model.OrderStatus.order_id == order_id).first()
        if not status:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Id not found!")
        return {"order_id": status.order_id, "status": status.order_status}
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)


def update(db: Session, order_id: int, new_status: str):
    try:
        status = db.query(status_model.OrderStatus).filter(status_model.OrderStatus.order_id == order_id).first()
        if not status:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Status wasn't found!")

        status.order_status = new_status
        db.commit()
        db.refresh(status)
        return {"order_id": status.order_id, "updated_status": status.order_status}
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)


def delete(db: Session, order_id: int):
    try:
        status = db.query(status_model.OrderStatus).filter(status_model.OrderStatus.order_id == order_id).first()
        if not status:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="stauts was not found!")
        db.delete(status)
        db.commit()
        return {"message": f"Status for order {order_id} deleted successfully"}
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)

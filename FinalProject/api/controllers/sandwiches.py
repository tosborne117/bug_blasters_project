from sqlalchemy import func
from sqlalchemy.orm import Session
from fastapi import HTTPException, status, Response, Depends
from ..models import sandwiches as model
from ..models import resources as model
from ..models import recipes as model
from sqlalchemy.exc import SQLAlchemyError

def create(db: Session, request):
    new_item = model.Sandwich(
        sandwich_name=request.sandwich_name,
        price=request.price,
        calories=request.calories,
        category=request.category,
        availability_status=request.availability_status
    )

    try:
        db.add(new_item)
        db.commit()
        db.refresh(new_item)
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)

    return new_item

def read_all(db: Session):
    try:
        # result = db.query(model.Sandwich).all()
        result = []
        for sandwich in db.query(model.Sandwich).all():
            result.append({
                "id": sandwich.id,
                "sandwich_name": sandwich.sandwich_name,
                "price": sandwich.price,
                "category": sandwich.category,
                "calories": sandwich.calories,
                "availability_status": sandwich.availability_status
            })
        return result
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)




def read_one(db: Session, item_id):
    try:
        item = db.query(model.Sandwich).filter(model.Sandwich.id == item_id).first()
        if not item:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Id not found!")
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)
    return item


def update(db: Session, item_id, request):
    try:
        item = db.query(model.Sandwich).filter(model.Sandwich.id == item_id)
        if not item.first():
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Id not found!")
        update_data = request.dict(exclude_unset=True)
        item.update(update_data, synchronize_session=False)
        db.commit()
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)
    return item.first()


def delete(db: Session, item_id):
    try:
        item = db.query(model.Sandwich).filter(model.Sandwich.id == item_id)
        if not item.first():
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Id not found!")
        item.delete(synchronize_session=False)
        db.commit()
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)
    return Response(status_code=status.HTTP_204_NO_CONTENT)

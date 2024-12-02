from fastapi import APIRouter, Depends, FastAPI, status, Response
from sqlalchemy.orm import Session
from ..controllers import orderstatus as controller
from ..schemas import orderstatus as schema
from ..dependencies.database import engine, get_db

router = APIRouter(
    tags=['OrderStatus'],
    prefix="/orderstatus"
)


@router.post("/", response_model=schema.OrderStatus)
def create(request: schema.OrderStatusCreate, db: Session = Depends(get_db)):
    return controller.create(db=db, request=request)


@router.get("/", response_model=list[schema.OrderStatus])
def read_all(db: Session = Depends(get_db)):
    return controller.read_all(db)


@router.get("/{item_id}", response_model=schema.OrderStatus)
def read_one(item_id: int, db: Session = Depends(get_db)):
    return controller.read_one(db, item_id=item_id)


@router.put("/{item_id}", response_model=schema.OrderStatus)
def update(item_id: int, request: schema.OrderStatus, db: Session = Depends(get_db)):
    return controller.update(db=db, request=request, item_id=item_id)


@router.delete("/{item_id}")
def delete(item_id: int, db: Session = Depends(get_db)):
    return controller.delete(db=db, item_id=item_id)

from fastapi import APIRouter, Depends, Body, HTTPException, status
from sqlalchemy.orm import Session
import models
from Database import engine, SessionLocal
from auth import get_current_user, get_user_exceptions
from schemas import InfoOut


def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


router = APIRouter(prefix="/crud",
                   tags=['crud'],
                   responses={404: {'description': "Not Found"}}, )
models.Base.metadata.create_all(bind=engine)


@router.get("/list/")
async def info_list(db: Session = Depends(get_db),
                    user: dict = Depends(get_current_user)
                    ):
    if user is None:
        raise get_user_exceptions()
    query = db.query(models.UserInfo).all()

    return query


@router.post("/create/")
async def post_client_info(name: str = Body(...),
                           course: str = Body(...),
                           phone_number: str = Body(...),
                           db: Session = Depends(get_db),
                           # user: dict = Depends(get_current_user)
                           ):
    result = []
    # if user is None:
    #     raise get_user_exceptions()

    model = models.UserInfo()

    model.name = name
    model.course = course
    model.phone_number = phone_number
    #
    # if model.name or model.course or model.phone_number i:
    #     raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Validation Error")

    result.append(model)

    db.add(model)
    db.commit()

    return InfoOut(name=result[0].name, course=result[0].course,
                   phone_number=result[0].phone_number)


@router.delete("/info/{info_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_clients_info(info_id: int,
                              db: Session = Depends(get_db),
                              user: dict = Depends(get_current_user)):
    if user is None:
        raise get_user_exceptions()

    info_model = db.query(models.UserInfo) \
        .filter(models.UserInfo.id == info_id).first()

    if not info_model:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No information")

    info_model = db.query(models.UserInfo) \
        .filter(models.UserInfo.id == info_id).delete()

    db.commit()

    return info_model

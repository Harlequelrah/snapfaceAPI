from sqlalchemy.orm import Session
from .schema import *
from settings.database import get_db
from settings.secret import authentication
import snapfaceapi.crud as crud
from fastapi import Depends, APIRouter
from typing import List

# get_curent_user=authentication.get_current_user
app_facesnap = APIRouter(prefix="/facesnaps", tags=["facesnaps"])

@app_facesnap.get("/", response_model=List[SnapFace])
async def get_facesnaps(db: Session = Depends(get_db)):
    return await crud.get_facesnaps(db)

@app_facesnap.get("/get-face-snap/{snapface_id}",response_model=SnapFace)
async def get_facesnap(snapface_id:int,db:Session = Depends(get_db)):
    return await crud.get_facesnap(db,snapface_id)


@app_facesnap.post('/create-face-snap',response_model=SnapFace)
async def create_facesnap(snapface_create:SnapFaceCreate,db:Session = Depends(get_db)):
    return await crud.create_facesnap(db,snapface_create)

@app_facesnap.delete('/delete-face-snap/{snapface_id}')
async def delete_facesnap(snapface_id:int,db:Session=Depends(get_db)):
    return await crud.delete_facesnap(db,snapface_id)

@app_facesnap.put('/update-face-snap/{snapface_id}',response_model=SnapFace)
async def update_facesnap(snapface_id:int,snapface:SnapFaceUpdate,db:Session=Depends(get_db)):
    return await crud.update_facesnap(db,snapface_id,snapface)

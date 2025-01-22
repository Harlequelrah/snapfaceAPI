from sqlalchemy.sql import func
from fastapi import HTTPException, status, Depends, Response
from fastapi.responses import JSONResponse
from .model import SnapFace
from .schema import SnapFaceCreate,SnapFaceUpdate
from  settings.database import get_db
from sqlalchemy.orm import Session
from elrahapi.utility.utils import update_entity


async def create_facesnap(db:Session,snapface_create:SnapFaceCreate):
    snapface= SnapFace(**snapface_create.dict())
    db.add(snapface)
    db.commit()
    db.refresh(snapface)
    return JSONResponse(status_code=status.HTTP_200_OK,content={"message":'FaceSnape créee avec succès.'})

async def get_facesnap(db:Session,snapface_id:int):
    face_snap=db.query(SnapFace).filter(SnapFace.id==snapface_id).first()
    if not face_snap: raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail='FaceSnap non trouvée.')
    return face_snap


async def get_facesnaps(db: Session,skip:int=0, limit:int=None):
    face_snaps = db.query(SnapFace).offset(skip).limit(limit).all()
    if not face_snaps:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="FaceSnaps non trouvées."
        )
    return face_snaps


async def delete_facesnap(db:Session,snapface_id:int):
    snapface=await get_facesnap(db,snapface_id)
    db.delete(snapface)
    db.commit()
    return JSONResponse(status_code=status.HTTP_200_OK ,content={"message":'FaceSnap supprimée avec succès'})

async def update_facesnap(db:Session,snapface_id:int,snapface_update:SnapFaceUpdate):
    face_snap= await get_facesnap(db,snapface_id)
    update_entity(face_snap,snapface_update)
    db.commit()
    db.refresh(face_snap)
    return face_snap

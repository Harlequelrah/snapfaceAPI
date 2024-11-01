from pydantic import BaseModel, Field
from typing import List, Optional
from datetime import datetime
from decimal import Decimal
from fastapi import Form

class SnapFaceBase(BaseModel):
    title:str=Field(example='Archibald à la plage')
    description:str=Field(example='Picnic à la plage')
class SnapFaceCreate(SnapFaceBase):
    imageUrl:str=Field(example='assets/images/archibald_plate.jpg')

class SnapFaceUpdate(SnapFaceBase):
    title:Optional[str]=None
    description:Optional[str]=None
    imageUrl:Optional[str]=None
    snaps:Optional[int]=None
    createAt:Optional[datetime]=None

class SnapFace(SnapFaceCreate):
    id:int
    createdAt:datetime
    snaps:int

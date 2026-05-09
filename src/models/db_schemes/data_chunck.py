from pydantic import BaseModel, Field, validator
from bson import ObjectId
from typing import Optional


class DataChunk(BaseModel):
    _id: Optional[ObjectId]
    chunk_project_id: ObjectId
    chunk_text: str = Field(..., min_length=1)
    chunk_metadata: dict
    chunk_order: int=Field(..., gt=0)

    @validator('project_id', 'chunk_id')
    def validate_ids(cls, value):
        if not value.isalnum():
            raise ValueError('IDs can only contain alphanumeric characters')
        return value

    class Config:
        arbitrary_types_allowed = True
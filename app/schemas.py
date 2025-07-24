from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime

current_year = datetime.now().year

class BookBase(BaseModel):
    title: str
    author: str
    published_year: int = Field(..., ge=0, le=current_year + 1, description="Must be a realistic year")
    summary: Optional[str] = None

class BookCreate(BookBase):
    """ Schema for creating a new book. """
    pass

class BookUpdate(BaseModel):
    """ Schema for updating an existing book. """
    title: Optional[str] = None
    author: Optional[str] = None
    published_year: Optional[int] = Field(None, ge=0, le=current_year + 1)
    summary: Optional[str] = None

class Book(BookBase):
    """ Schema for responses including book ID. """
    id: int

    class Config:
        orm_mode = True

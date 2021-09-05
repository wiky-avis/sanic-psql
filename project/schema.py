from pydantic import BaseModel


class Book(BaseModel):
    title: str
    author: str

    class Config:
        orm_mode = True

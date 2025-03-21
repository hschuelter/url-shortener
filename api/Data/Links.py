from pydantic import BaseModel


class Links(BaseModel):
    short_code: str
    long_url: str

    class Config:
        orm_mode = True


class CreatePost(Links):
    class Config:
        orm_mode = True
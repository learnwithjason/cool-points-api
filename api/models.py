import typing
from sqlmodel import SQLModel, Field

class CoolPeople(SQLModel, table=True):
    id: typing.Optional[int] = Field(default=None, primary_key=True)
    name: str
    cool_points: int = 0

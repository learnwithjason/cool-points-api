from fastapi import FastAPI
from sqlmodel import SQLModel, Session, create_engine, select
from .models import CoolPeople

app = FastAPI()

engine = create_engine("sqlite:///coolpeopledata.db")
SQLModel.metadata.create_all(engine)
session = Session(engine)

# @app.on_event("startup")
# def create_session():
#     Session(engine)

@app.get("/")
def hello_world():
    """
    # WHAT
    outputs hello world
    """
    return { "message": "hello world" }

@app.post('/people')
def add_people(coolPerson: CoolPeople):
    """
    Adds a people
    """

    session.add(coolPerson)
    session.commit()

    return {
        "message": "success",
        "person": coolPerson
    }

@app.get('/people')
def get_people():
    query = select(CoolPeople)
    items = session.exec(query).all()
    return { "people": items }

@app.put("/people/{item_id}")
def update_people(item_id: int, cool_points: int):
    item = session.get(CoolPeople, item_id)
    item.cool_points = cool_points
    session.commit()
    return { "updated": item }

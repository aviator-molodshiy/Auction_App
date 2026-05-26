from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from database import SessionLocal, engine
from models import Base, Container, Item


app = FastAPI()


Base.metadata.create_all(bind=engine)



def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()



@app.get("/")
def hello():
    return {"message": "Привіт, Оресте! Твій сервер працює з PostgreSQL!"}



@app.get("/containers")
def get_containers(db: Session = Depends(get_db)):
    containers = db.query(Container).all()
    result = []
    for c in containers:
        result.append({
            "name": c.name,
            "items": {item.name: item.price for item in c.items}
        })
    return {"containers": result}




@app.post("/containers/{container_name}/items")
def add_item(container_name: str, item_name: str, item_price: float, db: Session = Depends(get_db)):
    container = db.query(Container).filter(Container.name == container_name).first()



    if not container:
        container = Container(name=container_name)
        db.add(container)
        db.commit()
        db.refresh(container)



    item = Item(name=item_name, price=item_price, container_id=container.id)
    db.add(item)
    db.commit()



    return {"message": f"{item_name} додано в {container_name} за ${item_price}"}

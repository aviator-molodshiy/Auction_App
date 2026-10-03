# containers = [
#     {"name": "Container A", "items": {"Chair": 100, "Table": 300}},
#     {"name": "Container B", "items": {"Lamp": 50, "Vase": 80}},
# ]
#
# def show_all_containers(data):
#     for container in data:
#         print(f"=== {container['name']} ===")
#         for item_name, item_price in container['items'].items():
#             print(f"{item_name}: ${item_price}")
#
#         print("")
#
# show_all_containers(containers)


# import json
#
#
# def save_to_json(data, filename):
#     with open(filename, 'w') as file:
#         json.dump(data, file)
#
# def load_from_json(filename):
#     with open(filename, 'r') as file:
#         return json.load(file)
#
#
# test_data = {"name": "Container A", "items": {"Chair": 100, "Table": 300}}
#
# save_to_json(test_data, "test.json")
# loaded_data = load_from_json("test.json")
# print(loaded_data)



from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from database import Base




class Container(Base):
    __tablename__ = "containers"


    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, nullable=False)


    items = relationship("Item", back_populates="container")



class Item(Base):
    __tablename__ = "items"


    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    price = Column(Float, nullable=False)
    container_id = Column(Integer, ForeignKey("containers.id"))


    container = relationship("Container", back_populates="items")
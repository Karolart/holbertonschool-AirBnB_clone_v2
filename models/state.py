#!/usr/bin/python3
""" State Module for HBNB project """
import models
from models.base_model import Base, BaseModel
from models.city import City
from os import getenv
from sqlalchemy import Column, String
from sqlalchemy import relationship


class State(BaseModel, Base):
    """ State class """
    if models.storage_t == "db":
        __tablename__ = 'states'
        name = Column(String(128), nullable = False)
        cities = relationship("City", backref = "state")
    else:
        name = ""

    def __init__(self, *args, **kwargs):
        """state initialization"""
        super().__init__(*args, **kwargs)

    if models.storage_t != "db":
        @property
        def cities(self):
            """getter of city instances state list"""
            city_list = []
            all_cities = models.storage.all(City)
            for city in all_cities.values():
                if city.state_id == self.id:
                    city_list.append(city)
            return city_list

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
"""
This module contains a schema for database hbtn_0e_6_usa
"""

Base = declarative_base()


class State(Base):
    """
    This class is a schema
    of the states table
    """
    __tablename__ = 'states'

    id = Column(Integer, autoincrement=True,
                nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)

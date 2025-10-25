#!/usr/bin/python3
"""
This module contain query to add a new
instance of a class State to db
"""
import sys
from model_state import Base
from model_city import City
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1],
        sys.argv[2],
        sys.argv[3]),
        pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()  # creation d'une sessions

res = session.query(City).order_by(City.id)
if res:
    for instance in res:
        print((f"{instance.state.name}: ({instance.id}) {instance.name}"))

session.close()
engine.dispose()

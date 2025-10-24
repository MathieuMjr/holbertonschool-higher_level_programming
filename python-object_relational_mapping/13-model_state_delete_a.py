#!/usr/bin/python3
"""
This module contain query to add a new
instance of a class State to db
"""
import sys
from model_state import Base, State
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

    # on appelle l'objet à modifier
    states_del = session.query(State).filter(State.name.like('%a%'))
    for instance in states_del:
        session.delete(instance)
    session.commit()

    session.close()
    engine.dispose()

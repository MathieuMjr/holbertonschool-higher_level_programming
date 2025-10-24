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
    state_to_updt = session.query(State).filter(State.id == 2).first()
    # On modifie l'attribut souhaiter
    state_to_updt.name = 'New Mexico'
    # On renvoie l'objet modifié
    session.add(state_to_updt)
    # Le commit part
    session.commit()

    session.close()
    engine.dispose()

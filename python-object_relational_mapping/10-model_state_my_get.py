#!/usr/bin/python3
"""
This module contain query for getting all
instances of a class State
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

    state_name = sys.argv[4]
    # réalisation d'une query Select id, name from state order by id où id =1
    # sans first, res est un objet Query à parcourir pour accéder aux instances
    res = session.query(State).filter(
        State.name.ilike(f"{state_name}")).order_by(State.id)
    if res:
        for instance in res:
            print(f"{instance.id}")
    else:
        print("Not found")

    session.close()
    engine.dispose()

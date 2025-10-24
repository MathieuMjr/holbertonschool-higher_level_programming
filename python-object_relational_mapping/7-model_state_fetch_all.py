#!/usr/bin/env python3
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

    # réalisation d'une query Select id, name from state order by id
    for instance in session.query(State).order_by(State.id):
        print(f"{instance.id}: {instance.name}")

    session.close()
    engine.dispose()

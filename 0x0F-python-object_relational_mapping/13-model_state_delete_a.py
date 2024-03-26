#!/usr/bin/python3
"""List all states"""

from sqlalchemy import create_engine, select, delete
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from sys import argv

if __name__ == '__main__':
    db_url = "mysql://{}:{}@localhost:3306/{}".format(
            argv[1],
            argv[2],
            argv[3])
    engine = create_engine(db_url)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    Session.configure(bind=engine)
    session = Session()

    query = delete(State).where(State.name.like('%a%'))
    result = session.execute(query)
    session.commit()
    session.close()

#!/usr/bin/python3
"""List all states"""

from sqlalchemy import create_engine, select
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from model_state import State

if __name__ == '__main__':
    db_url = "mysql://root:root@localhost:3306/hbtn_0e_6_usa"
    engine = create_engine(db_url)
    Base = declarative_base()
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    Session.configure(bind=engine)
    session = Session()

    query = select(
            State.id.label('id'),
            State.name.label('name')).order_by(State.id).limit(5)
    result = session.execute(query).fetchall()
    for row in result:
        print('{}: {}'.format(row.id, row.name))
    session.close()

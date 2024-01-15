#!/usr/bin/python3
"""List all states"""

from sqlalchemy import create_engine, select
from sqlalchemy.orm import Session
from model_state import Base, State

if __name__ == '__main__':
    db_url = "mysql://root:root@localhost:3306/hbtn_0e_6_usa"
    engine = create_engine(db_url)
    Base.metadata.create_all(engine)
    session = Session(engine)
    query = select(State.id.label('id'), State.name.label('name')).order_by(State.id)
    result = session.execute(query).fetchall()
    for row in result:
        print(row.id, row.name)
    session.close()

#!/usr/bin/python3
"""define class state to db"""
from sqlalchemy import create_engine, MetaData, Table, String, Column, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.engine.url import URL

Base = declarative_base()


class State(Base):
    """class to define states table"""
    __tablename__ = 'states'
    id = Column(
            Integer,
            primary_key=True,
            nullable=False,
            unique=True,
            autoincrement=True)
    name = Column(String(128), nullable=False)

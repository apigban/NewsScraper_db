# !/usr/bin/env python3.7

from datetime import datetime as dt

from sqlalchemy.orm import sessionmaker
import log.log as log

from db_base import Base, engine, URLs, RapplerURLs

dbLogger = log.get_logger(__name__)

dateFormat = "%Y-%m-%d"

Base.metadata.create_all(engine, checkfirst=True)
DBSession = sessionmaker(bind=engine)
session = DBSession()

def create(table, content):
    """
         search db table for dynamic column, return max 1000
         'recentResult' is a list
         if no table is present from db, return an empty list
         ###SQL QUERY:
         SELECT composite FROM table
         ORDER BY id DESC
         """

    object_to_commit = table(content)

    session.add(object_to_commit)
    session.commit()
    dbLogger.info(f'Commit Done.')
    session.close()
    dbLogger.info(f'Session Closed')

    return link

def testquery():
    q = session.query(URLs).all()



testquery()

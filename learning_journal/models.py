from sqlalchemy import (
    CheckConstraint,
    Column,
    DateTime,
    desc,
    func,
    Index,
    Integer,
    String,
    Text
    )

from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy.orm import (
    scoped_session,
    sessionmaker,
    )

from zope.sqlalchemy import ZopeTransactionExtension

DBSession = scoped_session(sessionmaker(extension=ZopeTransactionExtension()))
Base = declarative_base()
query = DBSession.query_property()

# class MyModel(Base):
#     __tablename__ = 'models'
#     id = Column(Integer, primary_key=True)
#     name = Column(Text)
#     value = Column(Integer)

# Index('my_index', MyModel.name, unique=True, mysql_length=255)


class Entry(Base):
    __tablename__ = 'entries'
    id = Column(Integer, primary_key=True)
    title = Column(String(255), CheckConstraint('title!=""'), unique=True)
    body = Column(Text, default='')
    created = Column(DateTime, default=func.utcnow)
    edited = Column(DateTime, onupdate=func.utcnow)

    @classmethod
    def all(cls):
        all_entries = cls.query(Entry).order_by(desc(Entry.id))
        return [(entry.title) for entry in all_entries]

    @classmethod
    def by_id(cls, requested_id):
        return cls.query(Entry).get(requested_id)

Index('my_index', Entry.title, unique=True, mysql_length=255)

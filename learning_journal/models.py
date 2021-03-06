from datetime import datetime, timedelta

from passlib.context import CryptContext

from sqlalchemy import (
    Column,
    DateTime,
    desc,
    Index,
    Integer,
    Unicode,
    UnicodeText
    )

from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy.orm import (
    scoped_session,
    sessionmaker,
    )

from zope.sqlalchemy import ZopeTransactionExtension

DBSession = scoped_session(sessionmaker(extension=ZopeTransactionExtension()))
Base = declarative_base()

password_context = CryptContext(schemes=['pbkdf2_sha512'])


class Entry(Base):
    __tablename__ = 'entries'
    id = Column(Integer, primary_key=True)
    title = Column(Unicode(length=255), nullable=False, unique=True)
    body = Column(UnicodeText)
    created = Column(DateTime, default=datetime.utcnow)
    edited = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    @classmethod
    def all(cls, session=None):
        """Returns all the entries in the database, with the most recent entry first."""
        if session is None:
            session = DBSession
        all_entries = session.query(cls).order_by(desc(cls.id))
        return all_entries

    @classmethod
    def by_id(cls, requested_id, session=None):
        """Returns a single entry, given an id."""
        if session is None:
            session = DBSession
        return session.query(cls).get(requested_id)

    @property
    def is_edited(self):
        delta = timedelta(seconds=30)
        actual = self.edited - self.created
        return actual > delta
# Index('my_index', Entry.title, unique=True, mysql_length=255)


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(Unicode(length=255), nullable=False, unique=True, index=True)
    password = Column(Unicode, nullable=False)

    @classmethod
    def get_user(cls, username, session=None):
        """Returns user information, given a username"""
        if session is None:
            session = DBSession
        return session.query(cls).filter(cls.username == username).first()

    def verify_password(self, password):
        return password_context.verify(password, self.password)

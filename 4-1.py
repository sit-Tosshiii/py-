from sqlalchemy import create_engine, Column, String, Integer, DATETIME
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session

engine = create_engine('sqlite:///app.db')
Base = declarative_base()


class User(Base):
    __tablename__ = 'users'
    name = Column(String,primary_key=True,unique=True)
    passw = Column(String)

    def __repr__(self):
        return "User<{},{},{}>".format(self.name)

class Content(Base):
    __tablename__='contents'
    id=Column(Integer,primary_key=True)
    name=Column(String)
    content=Column(String)
    timestamp=Column(DATETIME)

    def __repr__(self):
        return "Content<{},{},{},{}>".format(self.id,self.name,self.content,self.timestamp)

Base.metadata.create_all(engine)
SessionMaker = sessionmaker(bind=engine)
session = scoped_session(SessionMaker)


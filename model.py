from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Date
from sqlalchemy import create_engine

engine = create_engine('postgresql://postgres:admin@localhost/lsi')
Base = declarative_base()


class Document(Base):

    __tablename__ = 'documents'
    id = Column(Integer, primary_key=True)
    title = Column(String)
    url = Column(String)
    created_at = Column(Date)
    updated_at = Column(Date)

    def __repr__(self):
       return self.title
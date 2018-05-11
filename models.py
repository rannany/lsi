from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Date, Table
from sqlalchemy import create_engine
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

engine = create_engine('postgresql://postgres:admin@localhost/lsi')
Base = declarative_base()


class DocumentTerm(Base):

    __tablename__ = 'document_term'
    id = Column(Integer, primary_key=True, unique=True)
    term_id = Column(Integer, ForeignKey('terms.id'), primary_key=True),
    document_id = Column(Integer, ForeignKey('documents.id'), primary_key=True),
    Column('frequency', Integer)
    term = relationship("Document", back_populates="terms")
    document = relationship("Term", back_populates="documents")


class Term(Base):

    __tablename__ = 'terms'
    id = Column(Integer, unique=True, primary_key=True)
    term = Column(String, unique=True)
    frequency = Column(Integer)
    document = relationship("DocumentTerm", back_populates="terms")

    def __repr__(self):
        return self.term


class Document(Base):

    __tablename__ = 'documents'
    id = Column(Integer, primary_key=True)
    title = Column(String)
    url = Column(String)
    created_at = Column(Date)
    updated_at = Column(Date)
    term = relationship("DocumentTerm", back_populates="documents")

    def __repr__(self):
       return self.title


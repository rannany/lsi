from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Date
from sqlalchemy import create_engine
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

engine = create_engine('postgresql://postgres:admin@localhost/lsi')
Base = declarative_base()


class Document(Base):

    __tablename__ = 'documents'
    id = Column(Integer, primary_key=True)
    title = Column(String)
    url = Column(String)
    created_at = Column(Date)
    updated_at = Column(Date)
    words = relationship("Word", order_by=Word.id, back_populates="document")

    def __repr__(self):
       return self.title


class Word(Base):

    __tablename__ = 'words'
    id = Column(Integer, primary_key=True)
    word = Column(String)
    document_id = Column(Integer, ForeignKey('documents.id'))
    document = relationship("Document", back_populates="documents")

    def __repr__(self):
        return self.word


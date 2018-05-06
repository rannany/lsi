from sqlalchemy.orm import sessionmaker
from models import Document, Word
from document import Document
from sqlalchemy import create_engine
import datetime


class DocumentController:

    def __init__(self):
        self.doc = Document()
        self.connect()

    def connect(self):
        engine = create_engine('postgresql://postgres:admin@localhost/lsi')
        Session = sessionmaker(bind=engine)
        self.session = Session()

    def getAll(self):
        doc = []
        for instances in self.session.query(Document).order_by(Document.id):
            doc.append(Document(
                title=instances.title,
                url=instances.url,
                words=instances.words
            ))
        return doc

    def store(self, payload):
        self.doc.title = payload.title
        self.doc.url = payload.url
        self.doc.created_at = datetime.date.today().strftime("%Y-%m-%d")
        self.doc.updated_at = datetime.date.today().strftime("%Y-%m-%d")
        self.doc.words = payload.words
        self.session.add(self.doc)
        self.session.commit()





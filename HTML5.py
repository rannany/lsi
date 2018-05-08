from bs4 import BeautifulSoup
import os
from document import Document
import nltk
import codecs

from lsi import DocumentAbstract
from models import Word
from controllers import DocumentController

class Docx(DocumentAbstract):
    soup=None

    def __init__(self, path):
        with codecs.open(path, 'r') as arq:
            html = arq.read()
            self.soup = BeautifulSoup(html, 'lxml')

    def get_words(self):
        tokens = nltk.word_tokenize(self.soup.get_text())
        return list(map(lambda word: Word(word=str(word)), tokens))

    def get_title(self):
        return self.soup.title.string


"""def html(arq):

    with codecs.open(arq, 'r') as arq:
        html = arq.read()
        soup = BeautifulSoup(html, 'lxml')
        tokens = nltk.word_tokenize(soup.get_text())
        doc = Document(
            title=soup.title.string,
            url=os.path.abspath(arq.name),
            words=list(map(lambda word: Word(word=str(word)), tokens))
        )
        controller = DocumentController()
        controller.store(doc)"""
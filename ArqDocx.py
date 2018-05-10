import codecs
import zipfile

import nltk
from bs4 import BeautifulSoup

from lsi import DocumentAbstract
from models import Word

class Docx(DocumentAbstract):
    soup=None

    def __init__(self, path):
        with codecs.open(path, 'r') as arq:
            with zipfile.ZipFile(arq.name, 'r') as zfp:
                doc=codecs.open('word/document.xml', 'r')
                self.soup= BeautifulSoup(doc.read(), 'xml')

    def get_words(self):
        tokens = nltk.word_tokenize(self.soup.get_text())
        return list(map(lambda word: Word(word=str(word)), tokens))

    def get_title(self):
        return self.soup.title.string if self.soup.title is not None else 'sem titulo'

''''with codecs.open('doc.docx', 'r') as arq:
    with zipfile.ZipFile(arq.name, 'r') as zfp:
        with zfp.open('word/document.xml') as fp:
            soup = BeautifulSoup(fp.read(), 'xml')
            tokens = nltk.word_tokenize(soup.get_text())
            doc = Document(
                title=soup.title.string if soup.title is not None else 'teste',
                url=os.path.abspath(arq.name),
                words=list(map(lambda word: Word(word=str(word)), tokens))
            )
            controller = DocumentController()
            controller.store(doc)'''
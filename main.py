from bs4 import BeautifulSoup
import os
from document import Document
import nltk
import codecs
from models import Word
from controllers import DocumentController

with codecs.open('index.html', 'r') as arq:
    html = arq.read()
    soup = BeautifulSoup(html, 'lxml')
    tokens = nltk.word_tokenize(soup.get_text())
    doc = Document(
        title=soup.title.string,
        url=os.path.abspath(arq.name),
        words=list(map(lambda word: Word(word=str(word)), tokens))
    )
    controller = DocumentController()
    controller.store(doc)

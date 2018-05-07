import codecs
import zipfile

import nltk
from bs4 import BeautifulSoup
import os

from controllers import DocumentController
from document import Document
from models import Word

with codecs.open('doc.docx', 'r') as arq:
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
            controller.store(doc)
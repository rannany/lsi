from tika import parser
import nltk
import codecs
from lsi import DocumentAbstract
from models import Word


class PDF(DocumentAbstract):
    raw = None

    def __init__(self, path):
        with codecs.open(path, 'r') as arq:
            self.raw = parser.from_file(arq)

    def get_words(self):
        tokens = nltk.word_tokenize(self.raw.get_text())
        return list(map(lambda word: Word(word=str(word)), tokens))

    def get_title(self):
        return self.raw.title.string if self.raw.title is not None else 'sem titulo'


"""import PyPDF2
from tika import parser

import os
from document import Document
import nltk
import codecs
from models import Word
from controllers import DocumentController


def pdf(arq)
	with codecs.open(arq, 'r') as arq:

		raw = parser.from_file(arq)
		tokens = nltk.word_tokenize(raw.get_text())
	        doc = Document(
	            title=raw.title.string,
	            url=os.path.abspath(arq.name),
	            words=list(map(lambda word: Word(word=str(word)), tokens))
	        )
	        controller = DocumentController()
	        controller.store(doc)"""
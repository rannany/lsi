#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os

import nltk
from PIL import Image  # Importando o módulo Pillow para abrir a imagem no script
import pytesseract     # Módulo para a utilização da tecnologia OCR
from models import Word
from bs4 import BeautifulSoup

from lsi import DocumentAbstract


class Docx(DocumentAbstract):
    img=None

    def __init__(self, path):
        self.img=Image.open('download.jpg')

    def get_words(self):
        texto = pytesseract.image_to_string(self.img,lang='por')  # eng = english and por = portuguese
        return list(map(lambda word: Word(word=str(word)), texto))

    def get_title(self):
        return 'sem titulo'
from bs4 import BeautifulSoup
import nltk
import codecs


with codecs.open('index.html', 'r') as arq:
    html = arq.read()
    soup = BeautifulSoup(html, 'lxml')
    tokens = nltk.word_tokenize(soup.get_text())
    print(tokens)


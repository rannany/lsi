import nltk
with open('texto.txt', 'r') as arq:
    tokens = nltk.word_tokenize(arq.read())
    print(tokens)


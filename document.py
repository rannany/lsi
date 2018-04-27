class Document:
    def __init__(self, title, url, words):
        self.title = title
        self.url = url
        self.words = words

    def __str__(self):
        return "title: " + self.title + "\nurl: " + self.url + "\nwords: " + str(self.words)

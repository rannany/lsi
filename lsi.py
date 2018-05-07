from abc import ABCMeta, abstractmethod


class DocumentAbstract(metaclass=ABCMeta):

    """recebe path, que é o caminha para o documento """
    def __init__(self, path):
        pass

    """ deve retornar um lista com todas as palavras encontradas"""
    @abstractmethod
    def get_words(self):
        return []

    """deve retorna uma string com o titulo do documento caso exista"""
    @abstractmethod
    def get_title(self):
        return u''

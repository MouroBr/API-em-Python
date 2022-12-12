import json
from json import JSONEncoder

class Book:
    def __init__(self, id, autor, titulo, anoPublicacao, pais):
        self.id = str(id)
        self.autor = autor
        self.titulo = titulo
        self.anoPublicacao = anoPublicacao
        self.pais = pais
        self.leitura = 0

    def toJSON(self):
       return json.loads(json.dumps(self, cls=json.BookEncoder, indent=4))
    
    def emprestimo(self):
        self.leitura = self.leitura + 1 
import json

class Book:
    def __init__(self, id, autor, titulo, anoPublicacao, pais):
        self.id = id
        self.autor = autor
        self.titulo = titulo
        self.anoPublicacao = anoPublicacao
        self.pais = pais
        self.leitura = 0

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, 
            sort_keys=True, indent=4)
    
    def emprestimo(self):
        self.leitura = self.leitura + 1 
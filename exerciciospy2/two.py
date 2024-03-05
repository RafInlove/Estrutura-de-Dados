'''Crie uma classe chamada “Livro” que tenha atributos “titulo” e “autor”. Implemente um método
chamado “detalhes” que retorna uma string com as informações do livro.'''

class Livro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor

    def detalhes(self, titulo, autor):
        return print("Título: " +titulo+ "\nAutor: " +autor)
    
l1 = Livro("Projeto Banco de Dados", "Carlos Alberto Heuser")

l1.detalhes(l1.titulo, l1.autor)
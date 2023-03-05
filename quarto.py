from tabuleiro import Tabuleiro
from pecas import Peca

class Quarto():

    tabuleiro = None

    def __init__(self):
        self.tabuleiro = Tabuleiro()
        
    
    def turno(self):
        """
        Retorna de quem é o turno.
        """
        if len(self.pecas)%2 == 0:
            return 1
        else:
            return 2

    def trocaTurno(self):
        """ 
        Muda de quem é o turno.
        """
        if len(self.pecas)%2 == 0:
            return 2
        else:
            return 1
    
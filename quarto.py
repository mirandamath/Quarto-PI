from tabuleiro import Tabuleiro

VITORIA = "V"
EMJOGO = "I"
DERROTA = "D"
EMPATE = "E"

class Quarto():

    tabuleiro = None

    def __init__(self):
        self.tabuleiro = Tabuleiro()
        
    
    # def turno(self):
    #     """
    #     Retorna de quem é o turno.
    #     """
    #     if len(self.tabuleiro.pecas)%2 == 0:
    #         return 1
    #     else:
    #         return 2

    # def trocaTurno(self):
    #     """ 
    #     Muda de quem é o turno.
    #     """
    #     if len(self.tabuleiro.pecas)%2 == 0:
    #         return 2
    #     else:
    #         return 1
        
    def checkEstado(self):

        if(self.tabuleiro.winLinha() or self.tabuleiro.winColuna() or self.tabuleiro.winDiagonal()):
            return VITORIA
        
        if len(self.tabuleiro.pecas) == 0:
            return EMPATE
        
        return EMJOGO
    
    def copy(self):
        """
        Retorna uma cópia do jogo.
        """
        q = Quarto()
        q.tabuleiro = self.tabuleiro.copy()

        return q


from pecas import Peca
class Tabuleiro():
    pecas = []
    numCol = 4
    numLine = 4
    tabuleiro = None

    def __init__(self):
        self.tabuleiro = [[None for  x in range(self.numCol)] for y in range(self.numLine)]
        self.pecas.append(Peca("GPCO"))
        self.pecas.append(Peca("GPCM"))
        self.pecas.append(Peca("GPQO"))
        self.pecas.append(Peca("GPQM"))
        self.pecas.append(Peca("GBCO"))
        self.pecas.append(Peca("GBCM"))
        self.pecas.append(Peca("GBQO"))
        self.pecas.append(Peca("GBQM"))
        self.pecas.append(Peca("PPCO"))
        self.pecas.append(Peca("PPCM"))
        self.pecas.append(Peca("PPQO"))
        self.pecas.append(Peca("PPQM"))
        self.pecas.append(Peca("PBCO"))
        self.pecas.append(Peca("PBCM"))
        self.pecas.append(Peca("PBQO"))
        self.pecas.append(Peca("PBQM"))


    def imprimeTabuleiro(self):
        """
        Prints the board.
        """
        print("Coluna     1     2     3      4")
        i = 1 # contador de linhas
        for linha in self.tabuleiro:
            linhaP = []
            for peca in linha:
                if peca:
                    linhaP.append(peca.getAbreviacao())
                else:
                    linhaP.append(None)
            print("Linha: " + str(i),linhaP)
            i+=1
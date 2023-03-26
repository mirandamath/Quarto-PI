from pecas import Peca
import copy
class Tabuleiro():
    pecas = []
    numCol = 4
    numLine = 4
    tabuleiro = None

    def __init__(self):
        # Filling self.tabuleiro with None
        self.pecas = []
        self.tabuleiro = [[None for x in range(self.numCol)] for y in range(self.numLine)]
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

    def copy(self):
        """
        Retorna uma cópia do tabuleiro.
        """
        t = Tabuleiro()
        t.tabuleiro = copy.deepcopy(self.tabuleiro)
        return t
    
    def getPecas(self):
        return self.pecas

    def pecasRestantes(self):
        nomes = []

        for i in range(len(self.pecas)):
            nome = ""
            for j in range(len(self.pecas[i].getNome())):
                nome = nome + " " + self.pecas[i].getNome()[j]
            nomes.append(nome)
            
        return ["(" + str(i) + "): " + nomes[i] for i in range(len(self.pecas))]

    def getLinhas(self):
        return self.tabuleiro
    
    def getColunas(self):
        colunas = []
        for i in range(self.numCol):
            coluna = []
            for linha in self.tabuleiro:
                coluna.append(linha[i])
            colunas.append(coluna)
        return colunas
    
    def getDiagonais(self):
        diagonais = []
        diagonal1 = []
        diagonal2 = []
        for i in range(self.numCol):
            diagonal1.append(self.tabuleiro[i][i])
            diagonal2.append(self.tabuleiro[i][self.numCol - i - 1])
        diagonais.append(diagonal1)
        diagonais.append(diagonal2)
        return diagonais

    def imprimeTabuleiro(self):
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
    
    def jogarPeca(self, peca, linha, coluna):
        # Checkar se tem uma peca na mesma posicao no tabuleiro
        if not self.tabuleiro[linha][coluna]:
            if peca in self.pecas:
                self.tabuleiro[linha][coluna] = peca
                self.pecas.remove(peca)
                return True
            else:
                print("Peça não disponivel/inexistente")
                return False
        else:
            print("Posição já ocupada")
            return False
    #funçao que checa se há caracteristicas em comum entre 4 peças de uma lista que pode ser formada por uma linha coluna ou diagonal
    def emComum(self, lista):
        i = 0
        j = 0
        for j in range(4):
            if len(lista) == 4:
                if(lista[i][j] == lista[i+1][j] and lista[i][j] == lista[i+2][j] and lista[i][j] == lista[i+3][j]):
                    return True
        return False
    
    def winLinha(self):
        abreviacoes = []
        for linha in self.getLinhas():
            abrLinha = []
            for elemento in linha:
                if elemento:
                    abrLinha.append(elemento.getAbreviacao())
            abreviacoes.append(abrLinha)

        for lista in abreviacoes:
            if self.emComum(lista):
                return True
        return False


    def winColuna(self):
        abreviacoes = []
        colunas = [[linha[i] for linha in self.getLinhas()] for i in range(self.numLine)]

        for coluna in colunas:
            lstCol = []
            for elemento in coluna:
                if elemento:
                    lstCol.append(elemento.getAbreviacao())
            abreviacoes.append(lstCol)

        for lista in abreviacoes:
            if self.emComum(lista):
                return True
        return False

    def winDiagonal(self):

        diagonalDE = []
        diagonalED = []
        abreviacoesDE = []
        abreviacoesED = []

        i, j = 0, 3
        for linha in self.tabuleiro:
            diagonalDE.append(linha[i])
            diagonalED.append(linha[j])
            i+=1
            j-=1

        for elemento in diagonalDE:
            if elemento:
                abreviacoesDE.append(elemento.getAbreviacao())
            
        for elemento in diagonalED:
            if elemento:
                abreviacoesED.append(elemento.getAbreviacao())
            
        if(self.emComum(abreviacoesDE) or self.emComum(abreviacoesED)):
            return True
        return False
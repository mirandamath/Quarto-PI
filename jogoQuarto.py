from jogo import Jogo, JogadorHumano, JogadorAgente, Jogada, Jogador
from quarto import Quarto
from minimax import minimax, minimax_alfabeta
import copy

class ValidaPosicaoQuarto(Jogada):
    def __init__(self, posicao : tuple[int, int]):
        self.posicao = posicao

    def e_valida(self, jogo : Jogo):
        # Verifica se a peça que quer jogar está fora do tabuleiro, se a posição que quer jogar é válida (esta dentro do tabuleiro) e se a posição que quer jogar não está ocupada
        return self.posicao != None and self.posicao[0] >= 0 and self.posicao[0] <= 3 and self.posicao[1] >= 0 and self.posicao[1] <=3 and jogo.estado.tabuleiro.tabuleiro[self.posicao[0]][self.posicao[1]] == None

class ValidaEscolhaQuarto(Jogada):
    def __init__(self, peca):
        self.peca = peca

    def e_valida(self, jogo : Jogo):
        # Verifica se a peça que quer jogar está fora do tabuleiro, se a posição que quer jogar é válida (esta dentro do tabuleiro) e se a posição que quer jogar não está ocupada
        return self.peca in jogo.estado.tabuleiro.pecas and self.peca not in jogo.estado.tabuleiro.getLinhas()
    
class JogadaQuarto(Jogada):
    def __init__(self, posicao, escolha):
        self.posicao = posicao
        self.escolha = escolha

class JogadorHumanoQuarto(JogadorHumano):
    
    def escolha(self, jogo : Jogo):   
        escolha = ValidaEscolhaQuarto(None)
        while not escolha.e_valida(jogo):
            print("Pecas disponiveis: " + str(jogo.estado.tabuleiro.pecasRestantes()))
            print("Jogador humano, escolha uma peça: (index)")
            
            ipeca = input()
            escolha.peca = jogo.estado.tabuleiro.getPecas()[int(ipeca)]
        return escolha

    def jogar(self, jogo : Jogo):
        escolha = jogo.turno().proximo_turno().escolha(jogo)
        posicao = ValidaPosicaoQuarto(None)
        jogada = JogadaQuarto(None, escolha)
        while not posicao.e_valida(jogo):
            print(f"Jogador {jogo.turno().identificador}, escolha uma posição: (linha coluna)")
            # posicao onde o humano quer jogar a peça escolhida pelo agente
            posicao.posicao = tuple(map(int, input().split()))

        jogada.posicao = posicao.posicao
        return jogada

class JogadorAgenteQuarto(JogadorAgente):

    def escolha(self, jogo : Jogo):
        profundidade_maxima = 2
        pior_valor = float("inf")
        melhor_jogada = JogadaQuarto(None, None)
        jogadas_validas = jogo.gerar_jogadas_validas()
        # print(len(jogadas_validas))
        count = 0
        for proximo_jogo in jogadas_validas:
            count += 1
            utilidade = minimax_alfabeta(jogo.jogar(proximo_jogo), jogo.turno(), profundidade_maxima)
            if utilidade < pior_valor:
                pior_valor = utilidade
                melhor_jogada = proximo_jogo
        print(count)
        print(melhor_jogada.escolha.abreviacao)
        return melhor_jogada.escolha

    # Calcular uma utilidade para cada estado sucessor e o max ira escolher o melhor
    def jogar(self, jogo : Jogo):
        escolha = jogo.turno().proximo_turno().escolha(jogo)
        profundidade_maxima = 2
        melhor_valor = float("-inf")
        melhor_jogada = JogadaQuarto(None, escolha)
        count = 0
        jogadas_validas = jogo.gerar_posicoes_validas(escolha)
        for proximo_jogo in jogadas_validas:
            count += 1
            utilidade = minimax_alfabeta(jogo.jogar(proximo_jogo), jogo.turno(), profundidade_maxima)
            if utilidade > melhor_valor:
                melhor_valor = utilidade
                melhor_jogada = proximo_jogo
        print(count)
        return melhor_jogada
    

class JogoQuarto(Jogo):

    def __init__(self, estado : Quarto = Quarto(), jogador_turno = None):
        super().__init__(estado, jogador_turno)

    def inicializar_jogadores(self):
        (humano, agente) = (JogadorHumanoQuarto("Humano"), JogadorAgenteQuarto("Agente"))
        humano.define_proximo_turno(agente)
        agente.define_proximo_turno(humano)

        # Quem joga primeiro
        self.jogador_turno = agente

        return (humano, agente)

    def turno(self):
        return self.jogador_turno

    def jogar(self, jogada : JogadaQuarto):
        novo_estado : Quarto = copy.deepcopy(self.estado)
        for peca in novo_estado.tabuleiro.pecas:
            if jogada.escolha != None:
                if peca.abreviacao == jogada.escolha.abreviacao:
                    jogada.escolha = peca
        novo_estado.tabuleiro.jogarPeca(jogada.escolha, jogada.posicao[0], jogada.posicao[1])

        return JogoQuarto(novo_estado, self.turno().proximo_turno())
    
    def gerar_posicoes_validas(self, escolha):
        jogadas_validas = []
        escolha_real = escolha.peca
        for linha in range(len(self.estado.tabuleiro.tabuleiro)):
            for coluna in range(len(self.estado.tabuleiro.tabuleiro[linha])):
                if self.estado.tabuleiro.tabuleiro[linha][coluna] == None:
                    jogadas_validas.append(JogadaQuarto((linha, coluna), escolha_real))
        return jogadas_validas
    
    '''
    This function generates a list of valid moves for a game. It iterates over a list of pieces and checks for every empty spot on the board if the piece can be placed there. If it's a valid move, a tuple is appended to the list. The tuple contains the piece and the position to place it in.
    '''
    def gerar_jogadas_validas(self):
        jogadas_validas = []
        for peca in self.estado.tabuleiro.pecas:
            for linha in range(len(self.estado.tabuleiro.tabuleiro)):
                for coluna in range(len(self.estado.tabuleiro.tabuleiro[linha])):
                    if self.estado.tabuleiro.tabuleiro[linha][coluna] == None:
                        jogadas_validas.append(JogadaQuarto((linha, coluna), peca))
        return jogadas_validas
    
    def venceu(self):
        return self.winLinha(self.estado) or self.winColuna(self.estado) or self.winDiagonal(self.estado)
    
    def calcular_utilidade(self, jogo : Jogo, jogador):

        utilidade = 0

        # Checar quantas pecas em comum tem na vertical, horizontal e diagonal

        # Se tiver apenas uma peca da menos pontos, se tiver duas pecas com algum atributo em comum da mais pontos, se tiver tres com algum atributo em comum da o maximo de pontos

        # Checar quantas pecas tem na linha se elas tem algo em comum em peca.nome

        # Horizontal
        def emComumLinha(q : Quarto):

            tempUtilidade = 0

            pecasNoTabuleiro = []
            for linha in q.tabuleiro.getLinhas():
                pecasLinha = []
                for peca in linha:
                    if peca:
                        pecasLinha.append(peca.nome)
                pecasNoTabuleiro.append(pecasLinha)

            lstCount = []
            for linha in pecasNoTabuleiro:
                countLinha = {}
                jaContei = []
                
                for i in range(len(linha)):
                    # iteramos sobre cada elemento da linha
                    for elemento in linha[i]:
                        # countElemento comeca como 1 pq ja temos um elemento contado (o proprio)
                        countElemento = 1
                        if elemento not in jaContei:
                            jaContei.append(elemento)
                            for j in range(i+1, len(linha)):
                                if elemento in linha[j]:
                                    countElemento += 1
                            countLinha[elemento] = countElemento 
                    
                lstCount.append(countLinha)

            for linha in lstCount:
                for elemento in linha:
                    if linha[elemento] == 2:
                        tempUtilidade += 10
                    if linha[elemento] == 3:
                        tempUtilidade += 20

            return tempUtilidade
        

        # Vertical
        def emComumColuna(q : Quarto):

            tempUtilidade = 0

            pecasNoTabuleiro = []
            for coluna in q.tabuleiro.getColunas():
                pecasColuna = []
                for peca in coluna:
                    if peca:
                        pecasColuna.append(peca.nome)
                pecasNoTabuleiro.append(pecasColuna)

            lstCount = []
            for coluna in pecasNoTabuleiro:
                countColuna = {}
                jaContei = []
                
                for i in range(len(coluna)):
                    # iteramos sobre cada elemento da linha
                    for elemento in coluna[i]:
                        # countElemento comeca como 1 pq ja temos um elemento contado (o proprio)
                        countElemento = 1
                        if elemento not in jaContei:
                            jaContei.append(elemento)
                            for j in range(i+1, len(coluna)):
                                if elemento in coluna[j]:
                                    countElemento += 1
                            countColuna[elemento] = countElemento 
                    
                lstCount.append(countColuna)

            for coluna in lstCount:
                for elemento in coluna:
                    if coluna[elemento] == 2:
                        tempUtilidade += 10
                    if coluna[elemento] == 3:
                        tempUtilidade += 20

            return tempUtilidade
        
        # Diagonal
        def emComumDiagonal(q : Quarto):
    
            tempUtilidade = 0
        
            pecasNoTabuleiro = []
            for diagonal in q.tabuleiro.getDiagonais():
                pecasDiagonal = []
                for peca in diagonal:
                    if peca:
                        pecasDiagonal.append(peca.nome)
                pecasNoTabuleiro.append(pecasDiagonal)
        
            lstCount = []
            for diagonal in pecasNoTabuleiro:
                countDiagonal = {}
                jaContei = []
                
                for i in range(len(diagonal)):
                    # iteramos sobre cada elemento da linha
                    for elemento in diagonal[i]:
                        # countElemento comeca como 1 pq ja temos um elemento contado (o proprio)
                        countElemento = 1
                        if elemento not in jaContei:
                            jaContei.append(elemento)
                            for j in range(i+1, len(diagonal)):
                                if elemento in diagonal[j]:
                                    countElemento += 1
                            countDiagonal[elemento] = countElemento 
                    
                lstCount.append(countDiagonal)
        
            for diagonal in lstCount:
                for elemento in diagonal:
                    if diagonal[elemento] == 2:
                        tempUtilidade += 10
                    if diagonal[elemento] == 3:
                        tempUtilidade += 20
        
            return tempUtilidade

        utilidade += emComumLinha(self.estado)
        utilidade += emComumColuna(self.estado)
        utilidade += emComumDiagonal(self.estado)
        # Checar quantas pecas tem na vertical se elas tem algo em comum em peca.nome

        # Checar quantas pecas tem na diagonal se elas tem algo em comum em peca.nome


        if self.venceu() and jogador.e_min():
            # Se eh min sempre negativo
            return utilidade * -1
        elif self.venceu() and jogador.e_max():
            # Se eh max sempre positivo
            return utilidade
        else:
            return utilidade
    
    def winLinha(self, e : Quarto):
        abreviacoes = []
        for linha in e.tabuleiro.tabuleiro:
            abrLinha = []
            for elemento in linha:
                if elemento:
                    abrLinha.append(elemento.getAbreviacao())
            abreviacoes.append(abrLinha)

        for lista in abreviacoes:

            if e.tabuleiro.emComum(lista):
                return True
        return False
    
    def winColuna(self, e : Quarto):
        abreviacoes = []
        colunas = [[linha[i] for linha in e.tabuleiro.getLinhas()] for i in range(e.tabuleiro.numLine)]

        for coluna in colunas:
            lstCol = []
            for elemento in coluna:
                if elemento:
                    lstCol.append(elemento.getAbreviacao())
            abreviacoes.append(lstCol)

        for lista in abreviacoes:
            if e.tabuleiro.emComum(lista):
                return True
        return False
    
    def winDiagonal(self, e : Quarto):

        diagonalDE = []
        diagonalED = []
        abreviacoesDE = []
        abreviacoesED = []

        i, j = 0, 3
        for linha in e.tabuleiro.tabuleiro:
            diagonalDE.append(linha[i])
            diagonalED.append(linha[j])
            i += 1
            j -= 1

        for elemento in diagonalDE:
            if elemento:
                abreviacoesDE.append(elemento.getAbreviacao())
        
        for elemento in diagonalED:
            if elemento:
                abreviacoesED.append(elemento.getAbreviacao())

        if(e.tabuleiro.emComum(abreviacoesDE) or e.tabuleiro.emComum(abreviacoesED)):
            return True
        return False
    
    def empate(self):
        return len(self.estado.tabuleiro.getPecas()) == 0 and not self.venceu()
    
    def imprimir(self):
        print("Coluna     0     1     2      3")
        i = 0 # contador de linhas
        for linha in self.estado.tabuleiro.tabuleiro:
            linhaP = []
            for peca in linha:
                if peca:
                    linhaP.append(peca.getAbreviacao())
                else:
                    linhaP.append(None)
            print("Linha: " + str(i),linhaP)
            i+=1
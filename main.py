from quarto import Quarto



if __name__ == "__main__":
    # peca = Peca("")
    jogo = Quarto()

    jogo.tabuleiro.imprimeTabuleiro()

    jogo.tabuleiro.jogarPeca(jogo.tabuleiro.pecas[0], 0,0)

    jogo.tabuleiro.imprimeTabuleiro()

    jogo.tabuleiro.jogarPeca(jogo.tabuleiro.pecas[0], 0,1)

    jogo.tabuleiro.imprimeTabuleiro()

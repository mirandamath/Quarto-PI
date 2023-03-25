from jogoQuarto import JogoQuarto

if __name__ == '__main__':
    jogo = JogoQuarto()
    
    (jogador_humano, jogador_agente) = jogo.inicializar_jogadores()

    print("QUARTO")
    jogo.imprimir()

    while jogo.estado.checkEstado() == "I":

        jogada_humano = jogador_humano.jogar(jogo)
        jogo = jogo.jogar(jogada_humano)

        print(jogo.estado.tabuleiro.tabuleiro)

        jogada_agente = jogador_agente.jogar(jogo)
        jogo = jogo.jogar(jogada_agente)

        jogo.imprimir()
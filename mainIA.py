from jogoQuarto import JogoQuarto

if __name__ == '__main__':
    jogo = JogoQuarto()
    
    (jogador_humano, jogador_agente) = jogo.inicializar_jogadores()

    print("QUARTO")
    jogo.imprimir()

    ganhou = "I"
    while ganhou == "I":

        jogada_agente = jogador_agente.jogar(jogo)
        jogo = jogo.jogar(jogada_agente)


        jogo.imprimir()
        if jogo.estado.checkEstado() == "V":
            print(f"{jogo.turno().proximo_turno().identificador} GANHOU!")
            jogo.imprimir()
            break

        jogada_humano = jogador_humano.jogar(jogo)
        jogo = jogo.jogar(jogada_humano)

        if jogo.estado.checkEstado() == "V":
            print(f"{jogo.turno().proximo_turno()} GANHOU!")
            jogo.imprimir()
            break
        jogo.imprimir()
        ganhou = jogo.estado.checkEstado()

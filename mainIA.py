from jogoQuarto import JogoQuarto
import random

if __name__ == '__main__':
    jogo = JogoQuarto()
    
    (jogador_humano, jogador_agente) = jogo.inicializar_jogadores()

    print("QUARTO")
    jogo.imprimir()

    quantidade_jogadas_randomicas = 10

    ganhou = "I"
    while ganhou == "I":
        while quantidade_jogadas_randomicas > 0:
            jogadas_validas = jogo.gerar_jogadas_validas()
            jogada_agente = random.choice(jogadas_validas)
            tempJogo = jogo.jogar(jogada_agente)
            if tempJogo.estado.checkEstado() != "V":
                jogo = jogo.jogar(jogada_agente)
                quantidade_jogadas_randomicas -= 1
        jogo.imprimir()

        jogada_humano = jogador_humano.jogar(jogo)
        jogo = jogo.jogar(jogada_humano)

        jogo.imprimir()
        if jogo.estado.checkEstado() == "V":

            print(f"{jogo.turno().proximo_turno().identificador} GANHOU!")
            jogo.imprimir()
            break

        jogada_agente = jogador_agente.jogar(jogo)
        jogo = jogo.jogar(jogada_agente)

        if jogo.estado.checkEstado() == "V":
            print(f"{jogo.turno().proximo_turno()} GANHOU!")
            jogo.imprimir()
            break
        jogo.imprimir()
        ganhou = jogo.estado.checkEstado()

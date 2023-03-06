from quarto import Quarto

if __name__ == "__main__":
    # peca = Peca("")
    quarto = Quarto()

    print("QUARTO")

    tabuleiro = quarto.tabuleiro
    
    while True:
        print("-----------------")
        print("Vez do jogador:", quarto.turno())

        print("Tabuleiro Atual:\n")
        tabuleiro.imprimeTabuleiro()

        print("Peças Disponíveis\n")
        print(tabuleiro.pecasRestantes(),"\n")

        ipeca = input("Jogador " + str(quarto.trocaTurno()) + " escolha a peca para que o jogador " + str(quarto.turno()) + " coloque no tabuleiro (Indice da peça):")
        peca = tabuleiro.getPecas()[int(ipeca)]
        print("Jogador " + str(quarto.turno()) + " escolha posição para colocar a peça " + peca.getAbreviacao() + ":")
        linha = input("Linha(1-4): ")
        coluna = input("Coluna(1-4): ")
        
        tabuleiro.jogarPeca(peca,int(linha)-1,int(coluna)-1)

        if quarto.checkEstado() == "V":
            tabuleiro.imprimeTabuleiro()
            print("Jogador: ", quarto.trocaTurno(), " venceu!")
            break
        else:
            print("Estado: " + quarto.checkEstado() + "\n")
        

        

    





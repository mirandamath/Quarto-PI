## Minimax sem poda
def minimax(jogo, jogador, profundidade_maxima = 8):
  # se o jogo acabou ou se a profundidade é máxima
  if jogo.venceu() or jogo.empate() or profundidade_maxima == 0:
    return jogo.calcular_utilidade(jogador)

  if jogador.e_max(): # turno do MAX
    melhor_valor = float("-inf") # Menos infinito é o menor valor

    # busca todos os possíveis jogos
    for proximo_jogo in jogo.gerar_jogadas_validas():
      utilidade = minimax(jogo.jogar(proximo_jogo), jogador.proximo_turno(), profundidade_maxima - 1)
      melhor_valor = max(utilidade, melhor_valor) # proximo_jogo com o maior valor
    return melhor_valor
  else: # turno no MIN
    pior_valor = float("inf") # Mais infinito é o maior valor

    # busca todos os possíveis jogos
    for proximo_jogo in jogo.gerar_jogadas_validas():
      utilidade = minimax(jogo.jogar(proximo_jogo), jogador.proximo_turno(), profundidade_maxima - 1)
      pior_valor = min(utilidade, pior_valor) # proximo_jogo com o menor valor
    return pior_valor

## Minimax com poda
def minimax_alfabeta(jogo, jogador, profundidade_maxima = 8, alfa = float("-inf"), beta = float("inf")):
  # se o jogo acabou ou se a profundidade é máxima
  if jogo.venceu() or jogo.empate() or profundidade_maxima == 0:
    return jogo.calcular_utilidade(jogador)

  if jogador.e_max(): # turno do MAX
    # busca todos os possíveis jogos
    for proximo_jogo in jogo.gerar_jogadas_validas():
      utilidade = minimax_alfabeta(jogo.jogar(proximo_jogo), jogador.proximo_turno(), profundidade_maxima - 1, alfa, beta)
      alfa = max(utilidade, alfa)
      if alfa >= beta: break
    return alfa
  
  else: # turno no MIN
    # busca todos os possíveis jogos
    for proximo_jogo in jogo.gerar_jogadas_validas():
      utilidade = minimax_alfabeta(jogo.jogar(proximo_jogo), jogador.proximo_turno(), profundidade_maxima - 1, alfa, beta)
      beta = min(utilidade, beta)
      if alfa >= beta: break
    return beta
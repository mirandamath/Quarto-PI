from minimax import minimax, minimax_alfabeta

class Jogada:
  def e_valida(self):
    raise NotImplementedError("Deve ser implementado")

class Jogador:
  def __init__(self, identificador, min_max = None):
    self.identificador = identificador
    self.min_max = min_max

  def define_proximo_turno(self, proximo_turno):
    self.jogador_proximo_turno = proximo_turno

  def imprimir(self):
    return self.identificador
  
  def jogar(self, jogo):
    raise NotImplementedError("Deve ser implementado")
  
  def e_min(self):
    return self.min_max == "min"
  
  def e_max(self):
    return self.min_max == "max"
  
  def proximo_turno(self):
    return self.jogador_proximo_turno

class JogadorHumano(Jogador):
  def __init__(self, identificador):
    super().__init__(identificador, "min")

class JogadorAgente(Jogador):
  def __init__(self, identificador):
    super().__init__(identificador, "max")

class Jogo():
  def __init__(self, estado = None, jogador_turno = None):
    self.estado = estado
    self.jogador_turno = jogador_turno

  def turno(self):
    raise NotImplementedError("Deve ser implementado")

  def jogar(self, jogada):
    raise NotImplementedError("Deve ser implementado")

  def gerar_jogadas_validas(self):
    raise NotImplementedError("Deve ser implementado")

  def venceu(self):
    raise NotImplementedError("Deve ser implementado")

  def empate(self):
    return (not self.venceu()) and (len(self.gerar_jogadas_validas()) == 0)

  def calcular_utilidade(self, jogador):
    raise NotImplementedError("Deve ser implementado")

  def imprimir(self):
    raise NotImplementedError("Deve ser implementado")

  def imprimir_jogada(self, turno, jogada):
    raise NotImplementedError("Deve ser implementado")
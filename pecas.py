VITORIA = "V"
INDECISO = "I"
DERROTA = "D"
EMAPTE = "E"

class Peca():

    caracteristicas = None
    nome = ""
    abreviacao = ""

    def __init__(self, caracteristicas):
        """
        G = Grande
        P = Pequeno
        P = Plack/preto
        B = Bite/Pranco
        C = circulo
        Q = quadrado
        O = oco
        M = maciço
        """
        
        self.caracteristicas = caracteristicas
        if caracteristicas == "GPCO":
            self.nome = ["Grande" , "Preto", "Circular", "Oco"]
            self.abreviacao = "GPCO"

        if caracteristicas == "GPCM":
            self.nome = ["Grande", "Preto", "Circular", "Macico"]
            self.abreviacao = "GPCM"
        if caracteristicas == "GPQO":
            self.nome = ["Grande", "Preto", "Circular", "Oco"]
            self.abreviacao = "GPQO"
        if caracteristicas == "GPQM":
            self.nome = ["Grande", "Preto", "Quadrado", "Macico"]
            self.abreviacao = "GPQM"
        
        if caracteristicas == "GBCO":
            self.nome = ["Grande", "Branco", "Circular", "Oco"]
            self.abreviacao = "GBCO"
        
        if caracteristicas == "GBCM":
            self.nome = ["Grande", "Branco", "Circular", "Macico"]
            self.abreviacao = "GBCM"
        
        if caracteristicas == "GBQO":
            self.nome = ["Grande","Branco" "Quadrado", "Oco"]
            self.abreviacao = "GBQO"
        
        if caracteristicas == "GBQM":
            self.nome = ["Grande","Branco" "Quadrado", "Macico"]
            self.abreviacao = "GBQM"
        
        if caracteristicas == "PPCO":
            self.nome = ["Pequeno", "Preto", "Circular", "Oco"]
            self.abreviacao = "PPCO"
        
        if caracteristicas == "PPCM":
            self.nome = ["Pequeno", "Preto", "Circular", "Macico"]
            self.abreviacao = "PPCM"
        
        if caracteristicas == "PPQO":
            self.nome = ["Pequeno", "Preto", "Quadrado", "Oco"]
            self.abreviacao = "PPQO"
        
        if caracteristicas == "PPQM":
            self.nome = ["Pequeno", "Preto", "Quadrado", "Macico"]
            self.abreviacao = "PPQM"
        
        if caracteristicas == "PBCO":
            self.nome = ["Pequeno", "Branco", "Circular", "Oco"]
            self.abreviacao = "PBCO"
        
        if caracteristicas == "PBCM":
            self.nome = ["Pequeno", "Branco", "Circular", "Macico"]
            self.abreviacao = "PBCM"
        
        if caracteristicas == "PBQO":
            self.nome = ["Pequeno", "Branco", "Quadrado", "Oco"]
            self.abreviacao = "PBQO"
        
        if caracteristicas == "PBQM":
            self.nome = ["Pequeno", "Branco", "Quadrado", "Macico"]
            self.abreviacao = "PBQM"

    # APENAS PARA DEBUG
    def getCaracteristicas(self):
        return self.caracteristicas
    
    def getNome(self):
        return self.nome
    
    def getAbreviacao(self):
        return self.abreviacao
    
    
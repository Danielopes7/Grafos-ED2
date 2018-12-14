class ListaAdj:
    def __init__ (self,vertice,dados=None):
        self.vertice=vertice
        self.aresta=dados

    def __str__(self):
        string=[]
        string=str(self.vertice)
        string += str(self.aresta)

        return string

    def getVertice(self):
        return self.vertice

    def getAresta(self):
        return self.aresta

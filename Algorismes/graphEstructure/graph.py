
class Graph:
    def __init__(self, llista_vertex):
        self.llista_vertex = llista_vertex


    def insertVertex(self, vertex):
        self.llista_vertex.append(vertex)

    def insertEdge (self, origen, desti):
        self.origen.addEdge(origen, desti)

    def searchCityIndex(self, name):
        i = 0
        for vertex in self.llista_vertex:
            if(vertex.nom == name):
                return i
            else:
                i = i + 1


#Marc: quin tipus de representacio de graph es?, tal com ens donen les dades, fent la representació en forma de matriu seria molt lit
class Graph:
    def __init__(self, llista_vertex):
        self.llista_vertex = llista_vertex


    def insertVertex(self, vertex):
        self.llista_vertex.append(vertex)

    def insertEdge (self, origen, desti):
        self.origen.addEdge(origen, desti)

    def searchCityIndex(self, name):    #Marc: això amb una array podria ser cost 1, pensar com si fos un hashmap
        i = 0
        for vertex in self.llista_vertex:
            if(vertex.nom == name):
                return i
            else:
                i = i + 1


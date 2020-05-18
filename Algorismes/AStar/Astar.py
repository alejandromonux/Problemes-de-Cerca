#comentari per Marc - el comentari comença amb Marc:
#Marc: Disclaymer: elguns comentaris/codi afegit per la meva persona, poden ser incorrectes ja que em trobo sota els afectes de substancies psicotropiques com, la falta de son, o el cansament

#TODO: canvair a distancia total, no per nodes recorreguts

class Astar():

    true = 1
    false = 0
    def getCostTotal(n):
        return n.costAcumulat

    def __init__(self):
        pass

    #g(n)   -> cost (pes) del node actual
    #h'(n)  -> cost (pes) de la aresta en cuestió
    def  AStarAlgorithm(self, nodeOrigen, nodeDesti):

        nodesLliures = []
        nodesOcupats = []
        #Alternativamente, si monto yo el graph puedo poner un campo de visitado
        fi = self.false
        n = nodeOrigen
        while ((nodesLliures != nodesOcupats)):
            nodesOcupats.append(n)
            if (n.nom == nodeDesti.nom):
                #fi = self.true #Marc: no fa falta posar a true, si despres fem un return, ja surts del bucle directe, sino podries fer un brake
                n.trace.append(n)
                return n

            else:
                nodesTotals = nodesLliures + nodesOcupats
                rangLliures = len(nodesLliures)
                rangOcupats = len(nodesOcupats)
                for cami in n.camins:
                    esta = self.false
                    nodeIndex = 0
                    #comprovem que el node no estigui en la llista de nodes visitats
                    for node in nodesTotals:
                        if node.nom == cami.desti.nom:
                            esta = self.true
                            nodeIndex = node.index()

                    if esta == self.false:
                        # Insertem el camí del inici fins al node
                        n.trace.append(n)
                        cami.desti.trace = n.trace ##Este destino tendrá el camino del inicio hasta n (siendo n su padre)
                        # Actualitzem el cost
                        cami.desti.costAcumulat = n.costAcumulat + cami.cost
                        nodesLliures.append(cami.desti)
                    else:
                        if 0 <= nodeIndex <= rangLliures:
                            #forma part dels lliures
                            #Reconstruir el camí entre n2 i I pel camí existent i pel nou camí. Guardar el més curt.
                            if(n.trace.len >= nodesTotals[nodeIndex].trace.len):
                                 nodesLliures[nodeIndex].trace = n.trace
                            else:
                                n.trace = nodesLliures[nodeIndex].trace

                        else:
                            #Reconstruir el camí entre n2 i I pel camí existent i pel nou camí. Guardar el més curt.
                            #forma part dels ocupats
                            if (n.trace.len >= nodesTotals[nodeIndex].trace.len):
                                nodesOcupats[nodeIndex-rangLliures].trace = n.trace
                            else:
                                n.trace = nodesOcupats[nodeIndex-rangLliures].trace

                #Ordenem els nodes del array de nodes disponibles
                nodesLliures.sort(key=self.getCostTotal)
                n = nodesLliures.pop(0)

        if fi == self.false:
            print("No s'ha trobat un camí al buscarutes")


from Algorismes.AStar.SolutionASTAR import SolutionASTAR

#comentari per Marc - el comentari comença amb Marc:
#Marc: Disclaymer: elguns comentaris/codi afegit per la meva persona, poden ser incorrectes ja que em trobo sota els afectes de substancies psicotropiques com, la falta de son, o el cansament

class Astar():

    true = 1
    false = 0
    def getCostTotal(n):
        return n.costAcumulat

    def __init__(self, solucio : SolutionASTAR ):
        self.solucio = solucio
        pass

    #g(n)   -> cost (pes) de la aresta
    #h'(n)  -> 
    def  AStarAlgorithm(self, nodeOrigen, nodeDesti):

        nodesLliures = []
        nodesOcupats = []
        #Alternativamente, si monto yo el graph puedo poner un campo de visitado
        fi = self.false
        n = nodeOrigen
        while ((nodesLliures != nodesOcupats) & fi):
            nodesOcupats.append(n)
            if (n.nom == nodeDesti.nom):
                fi = self.true
                n.trace.append(n)           #Marc: no fa falta posar a true, si despres fem un return, ja surts del bucle directe, sino podries fer un brake
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
                        cami.desti.trace = n.trace
                        # Actualitzem el cost
                        cami.desti.costAcumulat = n.costAcumulat + cami.cost
                        nodesLliures.append(cami.desti)
                    else:
                        if 0 <= nodeIndex <= rangLliures:
                            #forma part dels lliures
                            #TODO: Reconstruir el camí entre n2 i I pel camí existent i pel nou camí. Guardar el més curt.
                            min(n.trace.len nodesTotals[nodeIndex].trace.len)
                            pass
                        else:
                            # TODO: Reconstruir el camí entre n2 i I pel camí existent i pel nou camí. Guardar el més curt.
                            #forma part dels ocupats
                            pass

                #Ordenem els nodes del array de nodes disponibles
                nodesLliures.sort(nodesLliures, key=self.getCostTotal)
                n = nodesLliures.pop(0)

        if fi == self.false:
            print("No s'ha trobat un camí al buscarutes")


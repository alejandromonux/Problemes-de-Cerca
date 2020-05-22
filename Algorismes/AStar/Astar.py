# comentari per Marc - el comentari comença amb Marc:
# Marc: Disclaymer: elguns comentaris/codi afegit per la meva persona, poden ser incorrectes ja que em trobo sota els afectes de substancies psicotropiques com, la falta de son, o el cansament
import sys


def getCostTotal(n):
    return n.costAcumulat


# g(n)   -> cost (pes) del node actual
# h'(n)  -> cost (pes) de la aresta en cuestió
def AStarAlgorithm(nodeOrigen, nodeDesti, graphLen):
    nodesLliures = []
    nodesOcupats = []
    # Alternativamente, si monto yo el graph puedo poner un campo de visitado
    fi = 0
    n = nodeOrigen
    while ((len(nodesOcupats) != graphLen)):
        nodesOcupats.append(n)
        if (n.nom == nodeDesti.nom):
            n.trace.append(n)
            return n
        else:
            nodesTotals = nodesLliures + nodesOcupats
            rangLliures = len(nodesLliures)
            for cami in n.camins:
                esta = 0
                nodeIndex = 0
                # comprovem que el node no estigui en la llista de nodes guardats
                for node in nodesTotals:
                    if (node.nom == cami.desti.nom):
                        esta = 1
                        break
                    nodeIndex += 1

                if esta == 0:
                    go = 1
                    if len(n.trace) != 0:
                        if n.trace[len(n.trace)-1].nom == n.nom:
                            go = 0

                    if go:
                        n.trace.append(n)
                    cami.desti.trace = n.trace  ##Este destino tendrá el camino del inicio hasta n (siendo n su padre)
                    # Actualitzem el cost
                    cami.desti.costAcumulat = n.costAcumulat + cami.cost
                    nodesLliures.append(cami.desti)
                else:
                    if 0 <= nodeIndex <  rangLliures:
                        # forma part dels lliures
                        # Reconstruir el camí entre n2 i I pel camí existent i pel nou camí. Guardar el més curt.
                        if (getCostTotal(n) + cami.cost < getCostTotal(nodesTotals[nodeIndex])):
                            if not n.isInTrace(n.nom):
                                n.trace.append(n)
                            nodesLliures[nodeIndex].trace = n.trace
                            nodesLliures[nodeIndex].costAcumulat = getCostTotal(n) + cami.cost
                        else:
                            n.trace = nodesLliures[nodeIndex].trace
                            n.costAcumulat = getCostTotal(nodesLliures[nodeIndex])

                    else:
                        # Reconstruir el camí entre n2 i I pel camí existent i pel nou camí. Guardar el més curt.
                        # forma part dels ocupats
                        if (getCostTotal(n) + cami.cost < getCostTotal(nodesTotals[nodeIndex])):
                            if not n.isInTrace(n.nom):
                                n.trace.append(n)
                            nodesOcupats[nodeIndex - rangLliures].trace = n.trace
                            nodesOcupats[nodeIndex - rangLliures].costAcumulat = getCostTotal(n) + cami.cost
                        else:
                            n.trace = nodesOcupats[nodeIndex - rangLliures].trace
                            n.costAcumulat = getCostTotal(nodesOcupats[nodeIndex - rangLliures])

            if (n.nom == nodeOrigen.nom):
                n.costAcumulat = sys.float_info.max
            # Ordenem els nodes del array de nodes disponibles
            nodesLliures.sort(key=getCostTotal)
            n = nodesLliures.pop(0)

    if fi == 0:
        print("No s'ha trobat un camí al buscarutes")

# comentari per Marc - el comentari comença amb Marc:
# Marc: Disclaymer: elguns comentaris/codi afegit per la meva persona, poden ser incorrectes ja que em trobo sota els afectes de substancies psicotropiques com, la falta de son, o el cansament



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
            rangOcupats = len(nodesOcupats)
            for cami in n.camins:
                esta = 0
                nodeIndex = 0
                # comprovem que el node no estigui en la llista de nodes visitats
                for node in nodesTotals:
                    if (node.nom == cami.desti.nom):
                        esta = 1
                        break
                    nodeIndex += 1

                if esta == 0:
                    #TODO: ENTRA AQUÍ A CADA CAMINO CON LA MISMA N Y POR ESO SE REPITE TANTAS VECES LA MISMA CIUDAD EN EL TRACE. SE HA DE ARREGLAR

                    # Insertem el camí del inici fins al node
                    n.trace.append(n)
                    cami.desti.costAcumulat = n.costAcumulat + cami.cost
                    cami.desti.trace = n.trace  ##Este destino tendrá el camino del inicio hasta n (siendo n su padre)
                    # Actualitzem el cost
                    cami.desti.costAcumulat = n.costAcumulat + cami.cost
                    nodesLliures.append(cami.desti)
                else:
                    if 0 <= nodeIndex <  rangLliures:
                        # forma part dels lliures
                        # Reconstruir el camí entre n2 i I pel camí existent i pel nou camí. Guardar el més curt.
                        if (getCostTotal(n) >= getCostTotal(nodesTotals[nodeIndex])):
                            nodesLliures[nodeIndex].trace = n.trace
                        else:
                            n.trace = nodesLliures[nodeIndex].trace

                    else:
                        # Reconstruir el camí entre n2 i I pel camí existent i pel nou camí. Guardar el més curt.
                        # forma part dels ocupats
                        if (getCostTotal(n) >= getCostTotal(nodesTotals[nodeIndex])):
                            nodesOcupats[nodeIndex - rangLliures].trace = n.trace
                            nodesOcupats[nodeIndex - rangLliures].costAcumulat = getCostTotal(n)
                        else:
                            n.trace = nodesOcupats[nodeIndex - rangLliures].trace
                            n.costAcumulat = getCostTotal(n)

            # Ordenem els nodes del array de nodes disponibles
            nodesLliures.sort(key=getCostTotal)
            n = nodesLliures.pop(0)

    if fi == 0:
        print("No s'ha trobat un camí al buscarutes")

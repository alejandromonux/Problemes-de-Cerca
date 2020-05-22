#Marc: Notes
#ALEX: EL CAMINO MÁS CORTO NO ES EL QUE TIENE MENOS ELEMENTOS SI NO EL QUE TIENE MENOR COSTE TOTAL???
#-------------------------------------------------------------------------------------------------------------------------------------------
#h'1 = escollir variable més restringida -> La que té menys cost
#------------------------------------------------------------------------------------------------------------------------------------------

"""
1. Estat inicial: cap variable té un valor assignat.
2. S'assigna un dels possibles valors a una de les variables seguint un esquema determinat.
3. Es comprova la satisfacció de les restriccions.
4. Es comprova si la solució està completament construïda.
5. Es torna al pas 2 si cal.
"""

def getCostTotal(n):
    return n.costAcumulat

def getCostCami(n):
    return len(n.desti.camins)

def CSP(nodeOrigen, nodeDesti):
    acabar = 0
    n = nodeOrigen
    while acabar == 0:
        #Busquem si podem arribar ja al destí desde aqui
        for cami in n.camins:
            if nodeDesti.nom == cami.desti.nom:
                n.trace.append(cami.desti)
                cami.desti.trace = n.trace
                cami.desti.costAcumulat = n.costAcumulat + cami.cost
                return cami.desti


        #caminsOrdenats = n.camins
        #caminsOrdenats.sort(key = getCostCami)
        #següentCiutat = caminsOrdenats.pop(0)
        
        #Agafem la següent ciutat amb cost menor i avançem per allà
        següentCiutat = n.camins.sort(key = getCostCami).pop(0)
        n.trace.append(següentCiutat.desti)
        següentCiutat.desti.trace = n.trace
        següentCiutat.desti.costAcumulat = n.costAcumulat + següentCiutat.cost
        n = següentCiutat.desti

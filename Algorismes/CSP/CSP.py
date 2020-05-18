#Marc: Notes
#ALEX: EL CAMINO MÁS CORTO NO ES EL QUE TIENE MENOS ELEMENTOS SI NO EL QUE TIENE MENOR COSTE TOTAL???
#-------------------------------------------------------------------------------------------------------------------------------------------
#h'1 = escollir variable més restringida -> amb menys opcions (camins) -> Cada una de las ciudades y el numero de hijos? (La que tiene más coste? Pero no tiene sentido?)
#h'2 = escollir un valor, que restringeixi com a minim els altres  -> 
#------------------------------------------------------------------------------------------------------------------------------------------

"""
1. Estat inicial: cap variable té un valor assignat.
2. S'assigna un dels possibles valors a una de les variables seguint un esquema determinat.
3. Es comprova la satisfacció de les restriccions.
4. Es comprova si la solució està completament construïda.
5. Es torna al pas 2 si cal.
"""

def isLegal(self, cami):
    #Comprovar si la ciudad en cuestión es legal para el CSP o no

    pass

def getCostTotal(n):
    return n.costAcumulat

def getLlargaria(n):
    return len(n.desti.camins)

def CSP(self, nodeOrigen, nodeDesti):
    acabar = 0
    n = nodeOrigen
    while(acabar):
        #Agafem el camí més restrictiu (el camí que porti a la ciutat amb menys camins que surtin)
        caminsOrdenats = n.camins
        caminsOrdenats.sort(key = self.getLlargaria)
        següentCiutat = caminsOrdenats.pop(0)

            """
            if isLegal(cami):
                if (cami.desti.nom == nodeDesti.nom):
                    n.trace.append(cami.desti)
                    n.costAcumulat += cami.cost
                    return (n)
                else:
                    següentCiutats.append(cami.desti)
            """

        següentCiutats.sort(key=self.getCostTotal)
        n = següentCiutats.pop(0)
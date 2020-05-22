class Vertex():
    def __init__(self, nom, camins):
        self.nom = nom
        self.camins = camins
        self.visitat = 0
        self.costAcumulat = 0
        self.trace = []

    def showTrace(self):
        out = "\n"
        index = 0
        for ciutat in self.trace:
            if(index == len(self.trace)-1):
                out = out + ciutat.nom
            else:
                out = out + ciutat.nom + " -> "
            index+=1
        out = out + "\n" + "Cost:" + str(self.costAcumulat) +".\n"

        return out

    def isInTrace(self, nom):
        for t in self.trace:
            if(t.nom  == nom):
                return 1

        return 0
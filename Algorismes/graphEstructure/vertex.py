class Vertex():
    def __init__(self, nom, camins):
        self.nom = nom
        self.camins = camins
        self.visitat = 0
        self.costAcumulat = 0
        self.trace = []


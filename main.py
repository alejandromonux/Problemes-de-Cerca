from parse import *

from Algorismes.AStar.Astar import AStarAlgorithm
from Algorismes.CSV.readFile import *
from Algorismes.AStar import *
from Algorismes.CSP.CSP import CSP

def main():

    print("Benvingut al buscaRutes v1.0 - versió ESP \n")

    while 1:
        #readCSV
        graphCamins = readExcel()
        opcio = input("Quin algorisme voldràs utilitzar? \n 1.- A* \n 2.- CSP\n")

        if opcio == "1":
            n = AStarAlgorithm(graphCamins.llista_vertex[graphCamins.searchCityIndex("Sevilla")],graphCamins.llista_vertex[graphCamins.searchCityIndex("Bilbao")], graphCamins.getLen())
            print(n.showTrace())
        else:
            n = CSP(graphCamins.llista_vertex[graphCamins.searchCityIndex("Barcelona")],graphCamins.llista_vertex[graphCamins.searchCityIndex("Bilbao")])
            print(n.showTrace())





if __name__ == "__main__":
    main()
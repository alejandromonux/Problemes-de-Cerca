from parse import *

from Algorismes.AStar.Astar import AStarAlgorithm
from Algorismes.CSV.readFile import *
from Algorismes.AStar import *
def main():

    print("Benvingut al buscaRutes v1.0 - versió ESP \n")

    #readCSV
    graphCamins = readExcel()
    while 1:

        opcio = input("Quin algorisme voldràs utilitzar? \n 1.- A* \n 2.- CSP\n")

        if opcio == "1":
            n = AStarAlgorithm(graphCamins.llista_vertex[graphCamins.searchCityIndex("Barcelona")],graphCamins.llista_vertex[graphCamins.searchCityIndex("Bilbao")], graphCamins.getLen())
            print(n.showTrace())
        else:
            print("gutaaavo")





if __name__ == "__main__":
    main()
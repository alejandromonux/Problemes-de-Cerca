from parse import *

from Algorismes.AStar.Astar import AStarAlgorithm
from Algorismes.CSV.readFile import *
from Algorismes.AStar import *
from Algorismes.CSP.CSP import CSP
import time

def main():

    print("Benvingut al buscaRutes v1.0 - versió ESP \n")

    while 1:
        #readCSV
        graphCamins = readExcel()


        indexOrigen = indexDesti = -2
        while indexOrigen < 0:
            origen  = input("A quina ciutat ets?\n")
            indexOrigen = graphCamins.searchCityIndex(origen)

            if indexOrigen < 0:
                print("Aquesta ciutat no està present al nostre mapa!\n")

        while indexDesti < 0:
            desti = input("A quina ciutat vas?\n")
            indexDesti = graphCamins.searchCityIndex(desti)

            if indexDesti < 0:
                print("Aquesta ciutat no està present al nostre mapa!\n")



        opcio = input("Quin algorisme voldràs utilitzar? \n 1.- A* \n 2.- CSP\n")

        if opcio == "1":
            a = time.time()
            n = AStarAlgorithm(graphCamins.llista_vertex[indexOrigen],graphCamins.llista_vertex[indexDesti], graphCamins.getLen())
            b = time.time()
            print(n.showTrace())
            print(b - a)
            print("seconds\n")
        else:
            a = time.time()
            n = CSP(graphCamins.llista_vertex[indexOrigen],graphCamins.llista_vertex[indexDesti])
            b = time.time()
            print(n.showTrace())
            print(b - a)
            print("seconds\n")





if __name__ == "__main__":
    main()
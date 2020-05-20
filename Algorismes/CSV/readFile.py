import xlrd

#Return:
# List: list of lists with distance
# table: dictionary
#                   key: city
#                   value: index of the list
#
#
from Algorismes.graphEstructure.edge import edge
from Algorismes.graphEstructure.graph import Graph
from Algorismes.graphEstructure.vertex import Vertex


def readExcel():

    workbook = xlrd.open_workbook('dataset.xlsx')
    workbook = xlrd.open_workbook('dataset.xlsx', on_demand=True)
    worksheet = workbook.sheet_by_index(0)
    first_row = []  # The row where we stock the name of the column
    for col in range(worksheet.ncols-1):
        first_row.append(worksheet.cell_value(0, col+1))
    # tronsform the workbook to a list of dictionnary
    data = []
    for row in range(1, worksheet.ncols):
        elm = {}        #Marc: dictionary
        for col in range(worksheet.ncols-1):
            elm[first_row[col]] = worksheet.cell_value(row, col+1)
        data.append(elm)

    gerard = 0

    graph = []

    for gutavo in data:
        for pepe in gutavo:
            graph.append(Vertex(pepe, None))
        break

    tabla = {}
    tabla2 = {}
    for gutavo in data:
        for pepe in gutavo:
            tabla[pepe] = gerard
            tabla2[gerard] = pepe
            gerard += 1
        break

    list = []

    for gutavo in data:
        aux = []
        for pepe in gutavo:
            aux.append(gutavo[pepe])
            print(gutavo[pepe])
        list.append(aux)

    i = 0
    while i < len(list):
        camins = []
        j = 0
        while j < len(list[i]):
            if list[i][j] != '-':
                camins.append(edge(graph[i], graph[j], list[i][j]))
            j += 1
        graph[i].camins = camins
        print(camins)
        i += 1

    finalGraph = Graph(graph)
    return finalGraph

readExcel()
import xlrd

#Marc: return a list of dictionary
#a dictionary is like a hashmap

#search in dictionary:
#dictionary[key]
#if we want to search in the returned object:
# list -> dictionary -> data
# data[listPosition][dictionaryKey]
# listPosition = int
# dictionaryKey = string ('Barcelona', 'Madrid', 'Valencia', ...)


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

    #for pepe in data:
    #    print(pepe)
    #print(len(pepe))
    #print(worksheet.ncols)
    #print(data[1]['Barcelona'])

    return data

#readExcel()
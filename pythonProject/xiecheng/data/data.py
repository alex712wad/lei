import pandas
def readExcel(filename):
    data = pandas.read_excel(filename).values
    return data
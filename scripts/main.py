import xlrd
import pandas as pd
import numpy as np

def main():
    taco = xlrd.open_workbook('../data/Taco_4a_edicao_2011.xls')
    worksheet_1 = taco.sheet_by_index(1)

    categorias = {}

    for n_row in range(worksheet_1.nrows):

        row = worksheet_1.row(n_row)

        if type(row[0].value) == str and row[0].value[0:2] != 'Nú' and row[0].value != 'Alimento' and row[0].value != '':
            categorias[row[0].value] = n_row

    antes = 0
    for key in categorias:
        if antes == 0:
            antes = categorias[key]
        else:
            for i in range(antes, categorias[key]):
                if worksheet_1.row(i)[0].value != '':
                    print(worksheet_1.row(i))
                print(worksheet_1.row(i))
            break

if __name__ == '__main__':
    main()
import xlrd
import pandas as pd
import numpy as np
import utils

def main():
    taco = xlrd.open_workbook('../data/Taco_4a_edicao_2011.xls')
    worksheet = taco.sheet_by_index(0)

    nutrientes = utils.get_nutrientes(worksheet)

    unidades = utils.get_unidades(worksheet)

    nutrientes_unidades = dict(zip(nutrientes, unidades))
    
    categorias = utils.get_categorias(worksheet)

    utils.get_alimentos(worksheet, categorias)


    

   

    antes = 0
    for key in categorias:
        break
        print('\n\n\n')
        print(key, end='\n')
        if antes == 0:
            antes = categorias[key]
            continue
        else:
            for i in range(antes, categorias[key]):
                if worksheet.row(i)[0].value != '':
                    #print(worksheet.row(i))
                    print('', end='')
            antes = categorias[key]

if __name__ == '__main__':
    main()
import xlrd
import pandas as pd

def get_nutrientes(worksheet):
    nutrientes = []
    for i in range(0, len(worksheet.row(0))):
        value = ""
        if i > 1:
            primeira_linha = worksheet.row(0)[i].value
            segunda_linha = worksheet.row(1)[i].value
            if worksheet.row(0)[i].value != '':
                value = primeira_linha.replace('-', '') + segunda_linha
            if worksheet.row(1)[i].value == '':
                value = "EnergiaKj"
            else:
                value = segunda_linha
                if value == 'idrato':
                    value = 'Carboidrato'
                if value == 'C':
                    value = 'Vitamina C'

            nutrientes.append(value)
    
    nutrientes[0] = "Umidade"

    return nutrientes

def get_unidades(worksheet):
    unidades = []
    for i in range(0, len(worksheet.row(0))):
        if i > 1:
            if worksheet.row(2)[i].value != '':
                unidades.append(worksheet.row(2)[i].value)

    return unidades

def get_categorias(worksheet):
    categorias = {}
    lines = []
    categoria_atual = ''

    for n_row in range(worksheet.nrows):

        row = worksheet.row(n_row)



        if type(row[0].value) == str and row[0].value[0:2] != 'Nú' and row[0].value != 'Alimento' and row[0].value != '' and row[0].value != 'XXX':
            
            if row[0].value not in categorias:
                categoria_atual = row[0].value            
            
        if type(row[0].value) == float and row[0].value != '':
            lines.append(n_row)


        if row[1].value == '':
            categorias[categoria_atual] = lines
        

        if row[0].value == 'XXX':
            lines = []
        
    return categorias


def get_alimentos(worksheet, categorias):
    
    alimentos = []
    for key in categorias:
        if key != '':
            #print(key)
            #print(categorias[key])
            for row in categorias[key]:
                linha = worksheet.row(row)
                linha.pop(0)

                alimento = []
                alimento.append(key)
                for i in linha:
                    if i.value != '':
                        alimento.append(i.value)
                    else:
                        alimento.append(0)
                alimentos.append(alimento)
                
    return alimentos

def extractor():
    taco = xlrd.open_workbook('../data/Taco_4a_edicao_2011.xls')
    worksheet = taco.sheet_by_index(0)

    nutrientes = get_nutrientes(worksheet)
    unidades = get_unidades(worksheet)
    categorias = get_categorias(worksheet)
    alimentos = get_alimentos(worksheet, categorias)

    return nutrientes, unidades, alimentos

def export(nutrientes, unidades, alimentos):
    colunas = ['Categoria', 'Alimento']
    
    for i in range(0, len(nutrientes)):
        colunas.append(f'{nutrientes[i]} {unidades[i]}')

    df = pd.DataFrame(alimentos, columns=colunas)

    df.to_csv('../data/taco2011.csv', index=False, encoding='utf-8')
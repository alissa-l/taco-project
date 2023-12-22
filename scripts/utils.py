import numpy as np

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
                value = "Energia"
            else:
                value = segunda_linha

            nutrientes.append(value)

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

    for n_row in range(worksheet.nrows):

        row = worksheet.row(n_row)

        if type(row[0].value) == str and row[0].value[0:2] != 'Nú' and row[0].value != 'Alimento' and row[0].value != '':
            categorias[row[0].value] = n_row + 1

    return categorias

def alimentos_linhas(worksheet, categorias):

    indices = []
    for key in categorias:
        indices.append(categorias[key])
    

    linhas = []
    indice_index = 0
    
    for i in range(worksheet.nrows):

        if indice_index == len(indices) - 1:
            break
        
        if i > indices[indice_index] and i < indices[indice_index + 1]:
            linhas.append(i)
            continue
        
        if i > indices[indice_index] and i > indices[indice_index + 1]:
            indice_index += 1

    return linhas

def get_alimentos(worksheet, categorias):
    
    linhas = alimentos_linhas(worksheet, categorias)
    
    # Alimentos = {Categoria:[{alimento:numero_alimento}]}
    alimentos = {}

    indices = list(categorias.values())
    print(indices)
    indice_index = 0

    for key in categorias:
        alimentos[key] = []

        for i in linhas:

            if indice_index == len(indices) - 1:
                row = worksheet.row(i-1)
                nome = row[1].value
            
                if nome != '':
                    alimento_dict = {nome : i}
                    alimentos[key].append(alimento_dict)

            elif i > indices[indice_index] and i < indices[indice_index + 1]:
                row = worksheet.row(i-3)
                nome = row[1].value
            
                if nome != '':
                    alimento_dict = {nome : i}
                    alimentos[key].append(alimento_dict)
                
    
        indice_index += 1
   
    
    for key in alimentos:
        print(key)
        print(alimentos[key])
        print('\n\n')



        
            

    #print(data)


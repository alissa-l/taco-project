import xlrd
import pandas as pd
import json
from unidecode import unidecode

# Extrai todos os nutrientes da primeira linha da planilha
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
                value = "energiaKj"
            else:
                value = segunda_linha
                if value == 'idrato':
                    value = 'carboidrato'
                if value == 'C':
                    value = 'vitaminac'

            nutrientes.append(str(value).lower())
    
    nutrientes[0] = "umidade"

    for i in range(0, len(nutrientes)):
        nutrientes[i] = unidecode(nutrientes[i])

    return nutrientes

# Extrai todas as unidades da segunda linha da planilha
def get_unidades(worksheet):
    unidades = []
    for i in range(0, len(worksheet.row(0))):
        if i > 1:
            if worksheet.row(2)[i].value != '':
                unidades.append(worksheet.row(2)[i].value)

    return unidades

# Extrai todas as categorias
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

    
    # Indice de cada categoria
    return categorias

# Extrai todos os alimentos com base nas categorias
def get_alimentos(worksheet, categorias):
    
    alimentos = []
    for key in categorias:
        if key != '':
            for row in categorias[key]:
                linha = worksheet.row(row)
                linha.pop(0)

                alimento = []
                alimento.append(key)
                for i in linha:
                    if i.value != '' and i.value != 'NA' and i.value != 'Tr' and i:
                        alimento.append(i.value)
                    else:
                        alimento.append(0)
                alimentos.append(alimento)
    
    return alimentos

# Função principal de execução de todos os métodos anteriores
def extractor():
    taco = xlrd.open_workbook('../data/Taco_4a_edicao_2011.xls')
    worksheet = taco.sheet_by_index(0)

    nutrientes = get_nutrientes(worksheet)
    unidades = get_unidades(worksheet)
    categorias = get_categorias(worksheet)
    alimentos = get_alimentos(worksheet, categorias)

    return nutrientes, unidades, alimentos

# Exporta os dados para um arquivo csv
def export(nutrientes, alimentos):
    colunas = ['categoria', 'alimento']
    
    for i in range(0, len(nutrientes)):
        colunas.append(f'{nutrientes[i]}')

    df = pd.DataFrame(alimentos, columns=colunas)

    df.to_csv('../data/taco2011.csv', index=False, encoding='utf-8')

# Exporta os dados para um arquivo json
# O arquivo segue o seguinte formato:
    # {
    #     "Categorias": [}
    #         "categoria1",
    #         "categoria2",
    #     "NutrientesUnidades": {
    #         "nutriente1": "unidade1",
    #         "nutriente2": "unidade2",
    #     },
    #     "Data": {
    #         "categoria1": {
    #             "alimento1": {
    #             },
    #             "alimento2": {
    #             },
    #         },
    
def jsonify(nutrientes, unidades):

    df = pd.read_csv('../data/taco2011.csv')

    # Dicionario pra criar a estrutura do json
    final_json = {'Categorias': [], 'NutrientesUnidades': {}, 'Data': {}}

    # Adiciona os nutrientes e unidades no dicionario
    for i in range(0, len(nutrientes)):
        final_json['NutrientesUnidades'][nutrientes[i]] = unidades[i] 

    # Adiciona as categorias no dicionario
    for i in df['categoria'].unique():
        final_json['Categorias'].append(i)
        final_json['Data'][i] = {}


    # Adiciona os alimentos no dicionario
    for j in df.to_dict('records'):
        cat = j['categoria']
        nome = str(j['alimento'])
        final_json['Data'][cat][nome] = j

    
    # Exportação apenas para visualização
    #json.dump(final_json, open('../data/taco2011.json', 'w'), indent=4, ensure_ascii=False)
        
    # Exportação final
    json.dump(final_json, open('../taco-site/src/assets/data/taco2011.json', 'w'), indent=4, ensure_ascii=False)

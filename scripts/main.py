import utils

def main():
    nutrientes, unidades, alimentos = utils.extractor()
    utils.export(nutrientes, alimentos)
    utils.jsonify(nutrientes, unidades)



if __name__ == '__main__':
    main()
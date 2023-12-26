import utils

def main():
    nutrientes, unidades, alimentos = utils.extractor()
    utils.export(nutrientes, unidades, alimentos)



if __name__ == '__main__':
    main()
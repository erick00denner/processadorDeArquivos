from classesFuncoes.buscador import Buscador

busca = Buscador()

arquivos = busca.buscaArquivos()

verificado, encontrados = busca.verificaListaArquivos(arquivos)

if verificado:

    busca.chamaProcessamentoArquivos(encontrados)


    







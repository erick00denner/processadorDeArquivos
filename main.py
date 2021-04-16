from classesFuncoes.buscador import Buscador
from classesFuncoes.log import Log

busca = Buscador()
log = Log()

arquivos = busca.buscaArquivos()

verificado, encontrados = busca.verificaListaArquivos(arquivos)

if verificado:

    busca.chamaProcessamentoArquivos(encontrados)


    







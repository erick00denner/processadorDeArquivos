'''

Instancia classe Buscador para monitorar pasta Source 

'''
from classesFuncoes.buscador import Buscador

busca = Buscador()

arquivos = busca.buscaArquivos()
verificado, encontrados = busca.verificaListaArquivos(arquivos)

#Se arquivo encontrado estiver parametrizado
if verificado:

    busca.chamaProcessamentoArquivos(encontrados)





    







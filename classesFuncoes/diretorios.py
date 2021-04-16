class Diretorios:
   
   #Lê arquivo configDiretorios.csv para configurar diretorios utilizados pelo sistema
    def __init__(self):

        import pandas as pd 

        #Arquivo de configurações dos diretorios
        diretorios = pd.read_csv('configDiretorios.csv') 
        #Diretorio fonte dos arquivos a serem processados
        self.__source = diretorios.loc[diretorios['dir'] == 'source']['caminho'].values.item() 
        #Diretorio para armazenamento de logs
        self.__log = diretorios.loc[diretorios['dir'] == 'log']['caminho'].values.item()
        #Diretorio para exportação de arquivos processados
        self.__processados = diretorios.loc[diretorios['dir'] == 'processados']['caminho'].values.item() 

    @property
    def source(self):
        return self.__source

    @property
    def log(self):
        return self.__log

    @property
    def processados(self):
        return self.__processados            
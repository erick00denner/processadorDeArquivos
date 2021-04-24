'''
CLASSE: Diretorios

Classe desenvolvida para retornar caminhos dos diretórios do sistema parametrizadas em config/configDiretorios.csv 

'''
class Diretorios:
    
    #Configuração de diretorios do sistema
    def __init__(self):

        import pandas as pd 

        diretorios = pd.read_csv('config/configDiretorios.csv') 

        self.__source = diretorios.loc[diretorios['dir'] == 'source']['caminho'].values.item() 

        self.__log = diretorios.loc[diretorios['dir'] == 'log']['caminho'].values.item()

        self.__processados = diretorios.loc[diretorios['dir'] == 'processados']['caminho'].values.item() 

    #Retorna caminho diretorio Source
    @property
    def source(self):

        return self.__source

    #Retorna caminho diretorio Log
    @property
    def log(self):

        return self.__log

    #Retorna caminho diretorio Processados
    @property
    def processados(self):
        
        return self.__processados            
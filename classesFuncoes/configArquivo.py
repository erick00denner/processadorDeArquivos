'''
CLASSE: ConfigArquivo

Classe desenvolvida para leitura dos parametros configurados config/configArquivos.csv 

'''
class ConfigArquivo:

      #Retorna todos os parametros de todos os arquivos parametrizados
      def leConfigArquivo(self):

            import pandas as pd
            
            arquivos = pd.read_csv('config/configArquivos.csv')
            
            return arquivos      

      #Recebe nome do arquivo e retorna título do arquivo 
      def arquivo(self, nomeArquivo):

            import pandas as pd 
            
            arquivos = pd.read_csv('config/configArquivos.csv') 
            self.__arquivo = arquivos.loc[arquivos['nomeArquivo'] == nomeArquivo]['arquivo'].values.item()
            
            return self.__arquivo

      #Recebe nome do arquivo e retorna nome do arquivo      
      def nomeArquivo(self, nomeArquivo):
            
            import pandas as pd 
            
            arquivos = pd.read_csv('config/configArquivos.csv')
            self.__nomeArquivo = arquivos.loc[arquivos['nomeArquivo'] == nomeArquivo]['nomeArquivo'].values.item()
            
            return self.__nomeArquivo

      #Recebe nome do arquivo e retorna numero de colunas esperado
      def numColunas(self, nomeArquivo):
            
            import pandas as pd 
            
            arquivos = pd.read_csv('config/configArquivos.csv')
            self.__numColunas = arquivos.loc[arquivos['nomeArquivo'] == nomeArquivo]['numColunas'].values.item() 
            
            return self.__numColunas       

      #Recebe nome do arquivo e retorna se permite nulo
      # 1 para SIM / 0 para não
      def permiteNaN(self, nomeArquivo):
            
            import pandas as pd 
            
            arquivos = pd.read_csv('config/configArquivos.csv')
            self.__permiteNaN = arquivos.loc[arquivos['nomeArquivo'] == nomeArquivo]['permiteNaN'].values.item()
            
            return self.__permiteNaN               

      #Recebe nome do arquivo e retorna banco de dados onde os dados serão armazenados
      def banco(self, nomeArquivo):
            
            import pandas as pd 
            
            arquivos = pd.read_csv('config/configArquivos.csv')
            self.__banco = arquivos.loc[arquivos['nomeArquivo'] == nomeArquivo]['banco'].values.item()
            
            return self.__banco              
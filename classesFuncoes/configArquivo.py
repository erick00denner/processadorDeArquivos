class ConfigArquivo:

      def leConfigArquivo(self):
            import pandas as pd
            arquivos = pd.read_csv('config/configArquivos.csv')
            return arquivos      

      def arquivo(self, nomeArquivo):
            import pandas as pd 
            arquivos = pd.read_csv('config/configArquivos.csv') 
            self.__arquivo = arquivos.loc[arquivos['nomeArquivo'] == nomeArquivo]['arquivo'].values.item()
            return self.__arquivo

      def nomeArquivo(self, nomeArquivo):
            import pandas as pd 
            arquivos = pd.read_csv('config/configArquivos.csv')
            self.__nomeArquivo = arquivos.loc[arquivos['nomeArquivo'] == nomeArquivo]['nomeArquivo'].values.item()
            return self.__nomeArquivo

      def numColunas(self, nomeArquivo):
            import pandas as pd 
            arquivos = pd.read_csv('config/configArquivos.csv')
            self.__numColunas = arquivos.loc[arquivos['nomeArquivo'] == nomeArquivo]['numColunas'].values.item() 
            return self.__numColunas       

      def permiteNaN(self, nomeArquivo):
            import pandas as pd 
            arquivos = pd.read_csv('config/configArquivos.csv')
            self.__permiteNaN = arquivos.loc[arquivos['nomeArquivo'] == nomeArquivo]['permiteNaN'].values.item()
            return self.__permiteNaN               
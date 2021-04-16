class Arquivos:
    
    #Recebe o diretorio e nome do arquivo, le o arquivo e retorna um dataframe
    def leArquivo(self, pasta,nomeArquivo):

        import pandas as pd    
        
        arquivo = pasta +str('\\') + nomeArquivo
        df = pd.read_excel(arquivo)
        
        return df  

    #Recebe dataframe e compara config de numeros de colunas no arquivo configArquivos.csv
    def verificaColunas(self, df, nomeArquivo):
        
        import pandas as pd

        arquivos = pd.read_csv('configArquivos.csv')
        colPadrao = arquivos.loc[arquivos['nomeArquivo'] == nomeArquivo]['numColunas']
        colPadrao = colPadrao.values.item()
        colCorrente = df.shape[1]

        if (colPadrao == colCorrente):
            return True
        else:
            return False

    #Recebe dataframe verifica quantidade de nulos e se o arquivo permite nulos
    def vericaNulos(self, df, nomeArquivo):
        
        import pandas as pd

        arquivos = pd.read_csv('configArquivos.csv')
        nanPadrao = arquivos.loc[arquivos['nomeArquivo'] == nomeArquivo]['permiteNaN']
        nanPadrao = nanPadrao.values.item()
        nanCorrente = df.isna().sum().sum()    

        if(nanPadrao == 0):
            if(nanPadrao == nanCorrente):
                return True
            else:
                return False
        else:
            return True                
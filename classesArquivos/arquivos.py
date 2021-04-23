class Arquivos:
    
    #Recebe o diretorio e nome do arquivo, le o arquivo e retorna um dataframe
    def leArquivo(self, pasta, nomeArquivo):

        import pandas as pd    
        
        arquivo = pasta +str('\\') + nomeArquivo
        df = pd.read_excel(arquivo)
        
        return df  

    #Recebe dataframe e compara config de numeros de colunas no arquivo configArquivos.csv
    def verificaColunas(self, df, nomeArquivo):
        
        import pandas as pd
        from classesFuncoes.configArquivo import ConfigArquivo

        configArquivo = ConfigArquivo()
        colPadrao = configArquivo.numColunas(nomeArquivo)
        colCorrente = df.shape[1]

        if (colPadrao == colCorrente):
            return True
        else:
            from classesFuncoes.log import Log
            log = Log()
            log.geraLogArquivo(nomeArquivo,'Número de colunas inválido') 
            return False

    #Recebe dataframe verifica quantidade de nulos e se o arquivo permite nulos
    def vericaNulos(self, df, nomeArquivo):
        
        import pandas as pd
        from classesFuncoes.configArquivo import ConfigArquivo

        configArquivo = ConfigArquivo()

        nanPadrao = configArquivo.permiteNaN(nomeArquivo)
        nanCorrente = df.isna().sum().sum()    

        if(nanPadrao == 0):
            if(nanPadrao == nanCorrente):
                return True
            else:
                from classesFuncoes.log import Log
                log = Log()
                log.geraLogArquivo(nomeArquivo,'Arquivo contém valores nulos')  
                return False
        else:
            return True                

    def moveArquivo(self, nomeArquivo, sucesso):
        
        from classesFuncoes.diretorios import Diretorios
        import shutil
        import os
        from datetime import datetime
        
        diretorio = Diretorios()
        data = datetime.now()
        data = data.strftime('%d-%m-%Y')

        if(sucesso):
            arquivo = diretorio.source + '/' + nomeArquivo
            shutil.move(arquivo,diretorio.processados)
            quebraNome = nomeArquivo.split('.')
            nomeArquivo = quebraNome[0]
            extencao = quebraNome[1]
            arquivo = diretorio.processados + '/' + nomeArquivo+'.'+extencao
            renomeia = diretorio.processados +'/'+nomeArquivo +'_success_'+data+'.'+extencao
            os.rename(arquivo,renomeia)
        else:
            arquivo = diretorio.source + '/' + nomeArquivo
            shutil.move(arquivo,diretorio.processados)
            quebraNome = nomeArquivo.split('.')
            nomeArquivo = quebraNome[0]
            extencao = quebraNome[1]
            arquivo = diretorio.processados + '/' + nomeArquivo+'.'+extencao
            renomeia = diretorio.processados +'/'+nomeArquivo +'_error_'+data+'.'+extencao            
            os.rename(arquivo,renomeia)

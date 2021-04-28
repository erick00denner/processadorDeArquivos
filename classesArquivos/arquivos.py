'''
CLASSE: ARQUIVOS

Classe desenvolvida para tratamento genérico dos arquivos. 

'''
class Arquivos:
    
    # Recebe o caminho do diretório e o nome do arquivo e devolve um dataframe
    def leArquivo(self, pasta, nomeArquivo):

        import pandas as pd    
        
        arquivo = pasta +str('\\') + nomeArquivo
        df = pd.read_excel(arquivo)
        
        return df  
    
    # Recebe um data frame e nome do arquivo e verifica as configurações das colunas na classe configArquivo 
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

    # Recebe um data frame e nome do arquivo e verifica as configurações de nulos na classe configArquivo 
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

    # Recebe o nome do arquivo e se a operação realizada obteve sucesso e move o arquivo renomeado 
    def moveArquivo(self, nomeArquivo, sucesso):
        
        from classesFuncoes.diretorios import Diretorios
        import shutil
        import os
        from datetime import datetime
        
        diretorio = Diretorios()
        date_time = datetime.now()
        data = date_time.strftime('%d-%m-%Y')
        mes_ano = date_time.strftime('%m-%Y')

        if(sucesso):

            arquivo = diretorio.source + '/' + nomeArquivo
            diretorioDestino = diretorio.processados+'/'+mes_ano

            if(os.path.exists(diretorioDestino)):

                shutil.move(arquivo, diretorioDestino)

            else:

                os.mkdir(diretorioDestino)
                shutil.move(arquivo, diretorioDestino)    

            quebraNome = nomeArquivo.split('.')
            nomeArquivo = quebraNome[0]
            extencao = quebraNome[1]
            
            arquivo = diretorio.processados +'/'+mes_ano+'/'+nomeArquivo+'.'+extencao
            renomeia = diretorio.processados+'/'+mes_ano+'/'+nomeArquivo +'_success_'+data+'.'+extencao
            
            lista_arquivos = os.listdir(diretorio.processados+'/'+mes_ano)
            qtd_arquivos = sum(nomeArquivo +'_success_'+data in s for s in lista_arquivos)
            
            if(qtd_arquivos == 0):

                os.rename(arquivo,renomeia)
            
            else:
                
                qtd_arquivos += 1
                renomeia = diretorio.processados+'/'+mes_ano+'/'+nomeArquivo +'_success_'+data+'_'+str(qtd_arquivos)+'.'+extencao
                os.rename(arquivo,renomeia)

        else:

            arquivo = diretorio.source + '/' + nomeArquivo
            diretorioDestino = diretorio.processados+'/'+mes_ano

            if(os.path.exists(diretorioDestino)):

                shutil.move(arquivo, diretorioDestino)

            else:

                os.mkdir(diretorioDestino)
                shutil.move(arquivo, diretorioDestino)    
            
            quebraNome = nomeArquivo.split('.')
            nomeArquivo = quebraNome[0]
            extencao = quebraNome[1]
            
            arquivo = diretorio.processados+'/'+mes_ano+'/'+nomeArquivo+'.'+extencao
            renomeia = diretorio.processados+'/'+mes_ano+'/'+nomeArquivo +'_error_'+data+'.'+extencao            
            
            lista_arquivos = os.listdir(diretorio.processados+'/'+mes_ano)
            qtd_arquivos = sum(nomeArquivo +'_error_'+data in s for s in lista_arquivos)
            
            if(qtd_arquivos == 0):

                os.rename(arquivo,renomeia)
            
            else:
                
                qtd_arquivos += 1
                renomeia = diretorio.processados+'/'+mes_ano+'/'+nomeArquivo +'_error_'+data+'_'+str(qtd_arquivos)+'.'+extencao
                os.rename(arquivo,renomeia)

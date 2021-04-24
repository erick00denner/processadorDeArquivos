'''
CLASSE: Log

Classe desenvolvida para criação de Logs de Arquivo e Logs de Sistema 

'''
class Log:

    #Recebe nome do arquivo e mensagem de erro e gera log    
    def geraLogArquivo(self,nomeArquivo,msg):

        from datetime import datetime
        from classesFuncoes.diretorios import Diretorios

        dirLog = Diretorios()
        data = datetime.now()        
        
        data = data.strftime('%d-%m-%Y')
        arquivoLog = dirLog.log +'/log-'+data+'.txt'

        arquivo = open(arquivoLog, "a")

        dataHora = datetime.now()
        dataHora = dataHora.strftime('%d/%m/%Y %H:%M')

        frase = list()
        
        frase.append(str(dataHora))
        frase.append('   ')
        frase.append(nomeArquivo)
        frase.append('   ')
        frase.append(msg)
        frase.append('\n')
        
        arquivo.writelines(frase)
        arquivo.close()

    #Recebe mensagem de erro e gera log
    def geraLog(self,msg):

        from datetime import datetime
        from classesFuncoes.diretorios import Diretorios

        dirLog = Diretorios()
        data = datetime.now()        
        
        data = data.strftime('%d-%m-%Y')
        arquivoLog = dirLog.log +'/log-'+data+'.txt'

        arquivo = open(arquivoLog, "a")

        dataHora = datetime.now()        
        dataHora = dataHora.strftime('%d/%m/%Y %H:%M')

        frase = list()
        
        frase.append(str(dataHora))
        frase.append('   ')
        frase.append(msg)
        frase.append('\n')
        
        arquivo.writelines(frase)
        arquivo.close()
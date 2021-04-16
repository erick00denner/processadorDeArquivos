class Log:
    
    
    def geraLogArquivo(self,nomeArquivo,msg):

        from datetime import datetime
        from classesFuncoes.diretorios import Diretorios

        dirLog = Diretorios()
        arquivoLog = dirLog.log +'/log.txt'

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

    def geraLog(self,msg):

        from datetime import datetime
        from classesFuncoes.diretorios import Diretorios

        dirLog = Diretorios()
        arquivoLog = dirLog.log +'/log.txt'

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
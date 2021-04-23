class Metas:
    
    def validaFormatoDados(self, df):

        formatoDados = ['object', 'datetime64[ns]', 'datetime64[ns]', 'int64']
        nomeColunas = ['nomeMeta','inicioVigencia', 'fimVigencia', 'undMedida']

        formatoPlanilha = df.dtypes
        colunasPlanilha = list(df.columns)

        count = 0
        
        for item in formatoPlanilha:

            if(item != formatoDados[count]):
                from classesFuncoes.log import Log
                log = Log()
                log.geraLogArquivo(item,'O formato dos dados não corresponde ao esperado')  
                return False
            count += 1
        
        count = 0
        
        for item in colunasPlanilha:
            
            if(item != nomeColunas[count]):
                from classesFuncoes.log import Log
                log = Log()
                log.geraLogArquivo(item,'Os nomes das colunas não corresponde ao esperado')  
                return False
            count += 1
        
        return True      

    def processaArquivoMeta(self, df, nomeArquivo):
        
        import pandas as pd
        from classesFuncoes.log import Log
        from classesArquivos.arquivos import Arquivos
        from classesFuncoes.banco import Banco
        
        log = Log()
        arquivo = Arquivos()
        bd = Banco()          
       
        banco='metas'
        query ='INSERT INTO dim_meta (metaNome, inicioVigencia, fimVigencia, fk_unidadeMedida) VALUES (%s,%s,%s,%s)'
   
        for index, row in df.iterrows():

            dados = []

            dados.append(row.nomeMeta)
            dados.append(row.inicioVigencia)
            dados.append(row.fimVigencia)
            dados.append(row.undMedida)
            
            sucesso = bd.validaInsercao(banco, query, dados)

            if(not sucesso):

                log.geraLogArquivo(nomeArquivo,'Falha ao validar inserção do arquivo')        
                arquivo.moveArquivo(nomeArquivo, False)

                return False

        for index, row in df.iterrows():

            dados = []

            dados.append(row.nomeMeta)
            dados.append(row.inicioVigencia)
            dados.append(row.fimVigencia)
            dados.append(row.undMedida)  

            sucesso = bd.executaComando(banco,query,dados)

            if (not sucesso):

                log.geraLogArquivo(nomeArquivo,'Falha ao processar arquivo')        
                arquivo.moveArquivo(nomeArquivo, False)

                return False

        if (sucesso):

            log.geraLogArquivo(nomeArquivo,'Arquivo processado com sucesso')        
            arquivo.moveArquivo(nomeArquivo, True)    




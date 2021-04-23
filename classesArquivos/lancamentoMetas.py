class LancamentoMetas:
    
    def validaFormatoDados(self, df):

        formatoDados = ['int64', 'int64', 'datetime64[ns]', 'float64']
        nomeColunas = ['posto', 'meta', 'dataVigencia', 'valorLancamento']

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
            if(item != colunasPlanilha[count]):
                from classesFuncoes.log import Log
                log = Log()
                log.geraLogArquivo(item,'Os nomes das colunas não corresponde ao esperado')
                return False
            count +=1 

        return True      

    def processaArquivoLancamentoMetas(self, df, nomeArquivo):
        
        import pandas as pd
        from classesFuncoes.log import Log
        from classesArquivos.arquivos import Arquivos
        
        log = Log()
        arquivo = Arquivos()
                      
        from classesFuncoes.banco import Banco
        bd = Banco()

        banco='metas'
        query ='INSERT INTO ft_lancamentometas (fk_postoAgencia, fk_metaID, dataVigencia, valorLancamento) VALUES (%s,%s,%s,%s)'
   
        for index, row in df.iterrows():

            dados = []

            dados.append(row.posto)
            dados.append(row.meta)
            dados.append(row.dataVigencia)
            dados.append(row.valorLancamento)
            
            sucesso = bd.validaInsercao(banco, query, dados)

            if(not sucesso):

                log.geraLogArquivo(nomeArquivo,'Falha ao validar inserção do arquivo')        
                arquivo.moveArquivo(nomeArquivo, False)

                return False

        for index, row in df.iterrows():

            dados = []

            dados.append(row.posto)
            dados.append(row.meta)
            dados.append(row.dataVigencia)
            dados.append(row.valorLancamento)
            
            sucesso = bd.executaComando(banco,query,dados)

            if (not sucesso):

                log.geraLogArquivo(nomeArquivo,'Falha ao processar arquivo')        
                arquivo.moveArquivo(nomeArquivo, False)

                return False

        if (sucesso):

            log.geraLogArquivo(nomeArquivo,'Arquivo processado com sucesso')        
            arquivo.moveArquivo(nomeArquivo, True)    





        
        
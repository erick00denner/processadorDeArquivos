class Metas:
    
    def validaFormatoDados(self, df):
        formatoDados = ['int64', 'int64', 'datetime64[ns]', 'float64']
        formatoPlanilha = df.dtypes
        count = 0
        for item in formatoPlanilha:
            if(item != formatoDados[count]):
                return False
            count += 1
        return True      

    def processaArquivoMeta(self, df, nomeArquivo):
        
        import pandas as pd
        from classesFuncoes.log import Log
        from classesArquivos.arquivos import Arquivos
        
        log = Log()
        arquivo = Arquivos()
                      
        from classesFuncoes.banco import Banco
        bd = Banco()

        banco='metas'
        query ='INSERT INTO ft_lancamentometas (fk_postoAgencia, fk_metaID, dataVigencia, valorLancamento) VALUES (%s,%s,%s,%s)'
        try:
            for index, row in df.iterrows():

                index
                dados = []

                dados.append(row.posto)
                dados.append(row.meta)
                dados.append(row.dataVigencia)
                dados.append(row.valorLancamento)
                
                bd.executaComando(banco,query,dados)
        except:
            log.geraLogArquivo(nomeArquivo,'Falha ao processar arquivo')        
            arquivo.moveArquivo(nomeArquivo, False)

        log.geraLogArquivo(nomeArquivo,'Arquivo processado com sucesso')        
        arquivo.moveArquivo(nomeArquivo, True)


        
        
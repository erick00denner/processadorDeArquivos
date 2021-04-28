'''
CLASSE: LancamentoMetas

Classe desenvolvida para tratamento do arquivo lancamentoMetas.xlsx
Arquivo utilizado para lançar valores utilizados no calculo do acumulado já atingido das metas.    

'''
class LancamentoMetas:
    
    #Recebe um dataframe e valida de acordo com parametros configurados. Retorna True == OK e False != OK 
    def validaFormatoDados(self, df):

        #Parametros de formato de campo e nome das colunas
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

    #Recebe um data frame com dados para inserção e nome do arquivo já validados
    #Prepara query 
    #Utiliza a classe Banco para testar os dados de inserção e inserção no banco 
    def processaArquivoLancamentoMetas(self, df, nomeArquivo):
        
        import pandas as pd
        from classesFuncoes.log import Log
        from classesArquivos.arquivos import Arquivos
        from classesFuncoes.banco import Banco
        
        log = Log()
        arquivo = Arquivos()
        bd = Banco()

        #Nome da base de dados
        banco='metas'

        #Query para inserção na tabela ft_lancamentometas     
        query ='INSERT INTO ft_lancamentometas (fk_postoAgencia, fk_metaID, dataVigencia, valorLancamento) VALUES (%s,%s,%s,%s)'
   
        for index, row in df.iterrows():

            dados = []

            dados.append(row.posto)
            dados.append(row.meta)
            dados.append(row.dataVigencia)
            dados.append(row.valorLancamento)
            
            sucesso = bd.validaInsercao(banco, query, dados)

            if(not sucesso):

                log.geraLogArquivo(nomeArquivo,'Falha ao validar inserção dos dados')        
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





        
        
'''
CLASSE: LancamentoMetas

Classe desenvolvida para tratamento do arquivo lancamentoMetas.xlsx
Arquivo utilizado para lançar valores utilizados no calculo do acumulado já atingido das metas.    

'''
class LancamentoMetas:

    def __init__(self):
        
        from classesFuncoes.configArquivo import ConfigArquivo
        
        config = ConfigArquivo()

        nomeArquivo = 'lancamentosmetas.xlsx'

        self.__banco = config.banco(nomeArquivo)
    
    #Recebe um dataframe e valida de acordo com parametros configurados. Retorna True == OK e False != OK 
    def validaFormatoDados(self, df, nomeArquivo):

        from classesFuncoes.log import Log
        from classesArquivos.arquivos import Arquivos

        log = Log()
        arquivo = Arquivos()            

        #Parametros de formato de campo e nome das colunas
        formatoDados = ['int64', 'object', 'datetime64[ns]', 'float64']
        nomeColunas = ['posto', 'meta', 'dataVigencia', 'valorLancamento']

        formatoPlanilha = df.dtypes
        colunasPlanilha = list(df.columns)

        count = 0

        for item in formatoPlanilha:

            if(item != formatoDados[count]):
                
                arquivo.moveArquivo(nomeArquivo, False)
                log.geraLogArquivo(nomeArquivo,'O formato dos dados não corresponde ao esperado')
                
                return False

            count += 1

        count = 0     

        for item in colunasPlanilha:

            if(item != colunasPlanilha[count]):

                arquivo.moveArquivo(nomeArquivo, False)    
                log.geraLogArquivo(nomeArquivo,'Os nomes das colunas não corresponde ao esperado')
                
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

        #Query para inserção na tabela ft_lancamentometas     
        query ='INSERT INTO ft_lancamentometas (fk_postoAgencia, fk_metaID, dataVigencia, valorLancamento) VALUES (%s,%s,%s,%s)'
   
        for index, row in df.iterrows():

            dados = []

            dados.append(row.posto)
            dados.append(row.meta)
            dados.append(row.dataVigencia)
            dados.append(row.valorLancamento)
            
            sucesso = bd.validaInsercao(self.__banco, query, dados)

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
            
            sucesso = bd.executaComando(self.__banco,query,dados)

            if (not sucesso):

                log.geraLogArquivo(nomeArquivo,'Falha ao processar arquivo')        
                arquivo.moveArquivo(nomeArquivo, False)

                return False

        if (sucesso):

            log.geraLogArquivo(nomeArquivo,'Arquivo processado com sucesso')        
            arquivo.moveArquivo(nomeArquivo, True)
    
    def adiconaFKnoDF(self, df):

        from classesFuncoes.banco import Banco
        import pandas as pd

        bd = Banco()

        for index, linha in df.iterrows():
    
            argumento = linha.meta

            query = "SELECT metaID FROM dim_meta WHERE metaNome = '"+argumento+"'"

            fk = bd.retornaChavePrimaria(self.__banco,query)
            
            df.loc[index,'meta'] = fk[0]
        
        df['meta'] = pd.to_numeric(df['meta'])

        return df

    def validarRegistrosInserção(self, df, nomeArquivo):

        from classesFuncoes.banco import Banco
        from classesFuncoes.log import Log
        from classesArquivos.arquivos import Arquivos
        import pandas as pd

        bd = Banco()
        log = Log()
        arquivo = Arquivos()

        for index, linha in df.iterrows():
    
            argumento = linha.meta

            query = "SELECT metaID FROM dim_meta WHERE metaNome = '"+str(argumento)+"'"

            validacao = bd.verificarExistenciaRegistro(self.__banco, query)

            if (validacao == False):
                
                log.geraLogArquivo(nomeArquivo,'Falha ao processar arquivo')        
                arquivo.moveArquivo(nomeArquivo, False)

                return False

        return True    





        
        
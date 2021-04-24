'''
CLASSE: MetasAgencias

Classe desenvolvida para tratamento do arquivo metasagencias.xlsx
Arquivo utilizado para lançar valor total por unidade de acordo com metas cadastradas na classe Metas    

'''
class MetasAgencias:

     #Recebe um dataframe e valida de acordo com parametros configurados. Retorna True == OK e False != OK
    def validaFormatoDados(self, df):

        #Parametros de formato de campo e nome das colunas
        formatoDados = ['int64', 'int64', 'float64']
        nomeColunas = ['metaID', 'agencia', 'valorMeta']

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
    def processaArquivoMetasAgencias(self, df, nomeArquivo):
        
        import pandas as pd
        from classesFuncoes.log import Log
        from classesArquivos.arquivos import Arquivos        
        from classesFuncoes.banco import Banco
        
        log = Log()
        arquivo = Arquivos()
        bd = Banco()

        #Nome da base de dados
        banco='metas'

        #Query para inserção na tabela ft_metaagencia 
        query ='INSERT INTO ft_metaagencia (fk_metaID, fk_agencia, valorMeta) VALUES (%s,%s,%s)'

        for index, row in df.iterrows():

            dados = []

            dados.append(row.metaID)
            dados.append(row.agencia)
            dados.append(row.valorMeta)
            
            sucesso = bd.validaInsercao(banco, query, dados)

            if(not sucesso):

                log.geraLogArquivo(nomeArquivo,'Falha ao validar inserção do arquivo')        
                arquivo.moveArquivo(nomeArquivo, False)

                return False

         
        for index, row in df.iterrows():
            
            dados = []

            dados.append(row.metaID)
            dados.append(row.agencia)
            dados.append(row.valorMeta)

            sucesso = bd.executaComando(banco,query,dados)

            if (not sucesso):

                log.geraLogArquivo(nomeArquivo,'Falha ao processar o arquivo')        
                arquivo.moveArquivo(nomeArquivo, False)

                return False

        if (sucesso):
            
            log.geraLogArquivo(nomeArquivo,'Arquivo processado com sucesso')        
            arquivo.moveArquivo(nomeArquivo, True)    

            
            

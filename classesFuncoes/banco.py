'''
CLASSE: Banco

Classe desenvolvida para inserção de dados já validados na base de dados 

'''
class Banco:

    #Parametros de conexão com a base de dados
    def __init__(self):

        import pandas as pd
        
        self.__df = pd.read_csv('config/configBancos.csv')

    #Recebe nome da base de dados, query e dados para inserção. 
    #Executa a query para validação mas não executa commit
    #Retorna True == OK e False != OK
    def validaInsercao(self, banco, query, dados):

        import mysql.connector

        dadosBD = self.__df.loc[self.__df['banco'] == banco]
                
        try:

            cnx = mysql.connector.connect(user=dadosBD.usuario[0], 
                                        password=dadosBD.senha[0],
                                        host=dadosBD.host[0],
                                        database=dadosBD.banco[0])

        except:

            from classesFuncoes.log import Log

            log = Log()
            log.geraLog('Não foi possível conectar com o banco. Classe: Banco Função: validaInsercao()')

        cursor = cnx.cursor()

        try:

            cursor.execute(query, dados)
            cnx.rollback()

        except mysql.connector.Error as err:

            from classesFuncoes.log import Log

            cursor.close()
            cnx.close()    

            log = Log()
            log.geraLog('Não foi possível executar query. Classe: Banco Função: validaInsercao() Erro:'+ err.msg)

            return False

        cursor.close()
        cnx.close()

        return True    

    #Recebe nome da base de dados, query e dados para inserção. 
    #Executa a query e commit
    def executaComando(self, banco, query, dados):

        import mysql.connector

        dadosBD = self.__df.loc[self.__df['banco'] == banco]
        
        try:

            cnx = mysql.connector.connect(user=dadosBD.usuario[0], 
                                        password=dadosBD.senha[0],
                                        host=dadosBD.host[0],
                                        database=dadosBD.banco[0])

        except:

            from classesFuncoes.log import Log

            log = Log()

            log.geraLog('Não foi possível conectar com o banco. Classe: Banco Função: executaComando()')

        cursor = cnx.cursor()
        
        try:

            cursor.execute(query, dados)
            cnx.commit()

        except mysql.connector.Error as err:

            from classesFuncoes.log import Log

            cursor.close()
            cnx.close()
            
            log = Log()
            
            log.geraLog('Não foi possível executar query. Classe: Banco Função: executaComando() Erro:'+ err.msg)
            
            return False

        cursor.close()
        cnx.close()

        return True
    
    def retornaChavePrimaria(self, banco, query):
        
        import mysql.connector

        dadosBD = self.__df.loc[self.__df['banco'] == banco]
        
        try:

            cnx = mysql.connector.connect(user=dadosBD.usuario[0], 
                                        password=dadosBD.senha[0],
                                        host=dadosBD.host[0],
                                        database=dadosBD.banco[0])

        except:

            from classesFuncoes.log import Log

            log = Log()

            log.geraLog('Não foi possível conectar com o banco. Classe: Banco Função: retornaChavePrimaria()')

        cursor = cnx.cursor(buffered=True)
        
        try:
            
            cursor.execute(query)
            chave_primaria = cursor.fetchone()
            
            if chave_primaria is None:  
                
                from classesFuncoes.log import Log

                log = Log()

                log.geraLog('Registro não encontrado. Classe: Banco Função: retornaChavePrimaria() ' + query )

                return False

        except mysql.connector.Error as err:

            from classesFuncoes.log import Log

            cursor.close()
            cnx.close()
            
            log = Log()
            
            log.geraLog('Não foi possível executar query. Classe: Banco Função: retornaChavePrimaria() Erro:'+ err.msg)
            
            return False


        cursor.close()
        cnx.close()
        
        return chave_primaria

  
    def verificarExistenciaRegistro(self, banco, query):        
        
        import mysql.connector

        dadosBD = self.__df.loc[self.__df['banco'] == banco]

        try:

            cnx = mysql.connector.connect(user=dadosBD.usuario[0], 
                                        password=dadosBD.senha[0],
                                        host=dadosBD.host[0],
                                        database=dadosBD.banco[0])

        except:

            from classesFuncoes.log import Log

            log = Log()

            log.geraLog('Não foi possível conectar com o banco. Classe: Banco Função: verificarExistenciaRegistro()')

        cursor = cnx.cursor(buffered=True)
        
        try:
            
            cursor.execute(query)
            registro = cursor.fetchone()
            
            if registro is None:  
                
                from classesFuncoes.log import Log

                log = Log()

                log.geraLog('Registro não encontrado. Classe: Banco Função: verificarExistenciaRegistro() ' + query )

                return False

        except mysql.connector.Error as err:

            from classesFuncoes.log import Log

            cursor.close()
            cnx.close()
            
            log = Log()
            
            log.geraLog('Não foi possível executar query. Classe: Banco Função: verificarExistenciaRegistro() Erro:'+ err.msg)
            
            return False


        cursor.close()
        cnx.close()
        
        return True
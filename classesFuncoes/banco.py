class Banco:

    def __init__(self):

        import pandas as pd
        self.__df = pd.read_csv('config/configBancos.csv')

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
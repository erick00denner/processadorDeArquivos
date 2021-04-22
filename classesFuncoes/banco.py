class Banco:
    
    def executaComando(self, banco, query, dados):

        import mysql.connector
        import pandas as pd

        df = pd.read_csv('config/configBancos.csv')
        dadosBD = df.loc[df['banco'] == banco]
        
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
            cursor.close()
            cnx.close()
            return True
        except:
            from classesFuncoes.log import Log
            log = Log()
            log.geraLog('Não foi possível executar query. Classe: Banco Função: executaComando()')
            cursor.close()
            cnx.close()
            return False
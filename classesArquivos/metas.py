class Metas:

    def processaArquivoMeta(self, df):
        
        import pandas as pd
        
        from classesFuncoes.banco import Banco
        bd = Banco()

        banco='metas'
        query ='INSERT INTO ft_lancamentometas (fk_postoAgencia, fk_metaID, dataVigencia, valorLancamento) VALUES (%s,%s,%s,%s)'
        
        for index, row in df.iterrows():

            index
            dados = []

            dados.append(row.posto)
            dados.append(row.meta)
            dados.append(row.dataVigencia)
            dados.append(row.valorLancamento)
    
            bd.executaComando(banco,query,dados)



        
        
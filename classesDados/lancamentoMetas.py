class DadosLancamentoMetas:

    def geraDados(self):

        from datetime import datetime
        from classesFuncoes.banco import Banco
        from classesFuncoes.configArquivo import ConfigArquivo
        from classesFuncoes.log import Log
        
        config = ConfigArquivo()

        nomeArquivo = 'lancamentosmetas.xlsx'

        banco = config.banco(nomeArquivo)

        bd = Banco()
        log =Log()
    
        query = 'SELECT lancamentoID from ft_lancamentometas WHERE difLancamentoAnterior IS NULL'
        linhasTratamento = bd.executaConsulta(banco,query)

        for linha in linhasTratamento:

            query = 'SELECT * FROM ft_lancamentometas WHERE lancamentoID = '+str(linha[0])
            lancamento_metas = bd.executaConsulta(banco,query)

            id_lancamento = lancamento_metas[0][0]
            posto_agencia = lancamento_metas[0][1]
            meta_id = lancamento_metas[0][2]
            data_vigencia_lancamento = lancamento_metas[0][3]
            valor_lancamento = lancamento_metas[0][4]

            query = 'SELECT inicioVigencia, fimVigencia  FROM dim_meta WHERE metaID = '+str(lancamento_metas[0][2])
            vigencia = bd.executaConsulta(banco,query)

            inicio_vigencia = vigencia[0][0]
            fim_vigencia = vigencia[0][1]

            if((data_vigencia_lancamento.month == inicio_vigencia.month) and (data_vigencia_lancamento.year == inicio_vigencia.year)):
                
                dados = [valor_lancamento, id_lancamento]
                query = 'UPDATE ft_lancamentometas SET difLancamentoAnterior = %s WHERE lancamentoID = %s'
                
                try:

                    bd.executaComando(banco,query,dados)
                    log.geraLogArquivo(nomeArquivo, 'Sucess: Dados gerados com sucesso')

                except:

                    log.geraLogArquivo(nomeArquivo, 'Erro: Não foi possível gerar os dados')

            else:
                dia = data_vigencia_lancamento.day
                mes = data_vigencia_lancamento.month - 1
                ano = data_vigencia_lancamento.year

                data_consulta = str(ano)+'-'+str(mes)+'-'+str(dia)
                data_consulta = datetime.strptime(data_consulta, '%Y-%m-%d').date()
            
                query = "SELECT valorLancamento FROM ft_lancamentometas WHERE fk_postoAgencia ="+str(posto_agencia)+" AND fk_metaID ="+str(meta_id)+" AND   dataVigencia='"+str(data_consulta)+"'"
                
                valor_lancamento_anterior = bd.executaConsulta(banco,query)
                diferenca =  valor_lancamento - valor_lancamento_anterior[0][0]
                
                dados = [diferenca, id_lancamento]
                query = 'UPDATE ft_lancamentometas SET difLancamentoAnterior = %s WHERE lancamentoID = %s'
                try:
                    bd.executaComando(banco,query,dados)
                    log.geraLogArquivo(nomeArquivo, 'Sucess: Dados gerados com sucesso')
                except:
                    log.geraLogArquivo(nomeArquivo, 'Erro: Não foi possível gerar os dados')
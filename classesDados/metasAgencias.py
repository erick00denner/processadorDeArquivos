class DadosMetasAgencias:

    def geraDados(self):

        from classesFuncoes.banco import Banco
        from classesFuncoes.configArquivo import ConfigArquivo
        from classesFuncoes.log import Log
        
        config = ConfigArquivo()

        nomeArquivo = 'metasagencias.xlsx'

        banco = config.banco(nomeArquivo)

        bd = Banco()
        log = Log()

        query = 'SELECT metaAgencia FROM ft_metaagencia WHERE metaDividida is null'

        linhasTratamento = bd.executaConsulta(banco,query)

        for linha in linhasTratamento:

            query = 'SELECT fk_metaID,valorMeta FROM ft_metaagencia WHERE metaAgencia = '+str(linha[0])
            metaAgencia = bd.executaConsulta(banco,query)

            query = 'SELECT inicioVigencia, fimVigencia  FROM dim_meta WHERE metaID = '+str(metaAgencia[0][0])
            vigencia = bd.executaConsulta(banco,query)

            inicio = vigencia[0][0]
            fim = vigencia[0][1]

            qtd_meses = fim.month - inicio.month + 1

            meta_dividida = metaAgencia[0][1] / qtd_meses

            dados = [meta_dividida, linha[0]]
            query = 'UPDATE  ft_metaagencia SET metaDividida = %s WHERE metaAgencia = %s'
            try:

                bd.executaComando(banco,query,dados)
                log.geraLogArquivo(nomeArquivo, 'Sucess: Dados gerados com sucesso')

            except:
                
                log.geraLogArquivo(nomeArquivo, 'Erro: Não foi possível gerar os dados')

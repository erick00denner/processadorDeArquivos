class Buscador:
  
    #Busca arquivos no diretório source e retorna uma lista com os nomes
    def buscaArquivos(self):
        
            import os
            from classesFuncoes.diretorios import Diretorios
            diretorio = Diretorios()
            try:
                lista = os.listdir(diretorio.source)
                return lista
            except:
                from classesFuncoes.log import Log
                log = Log()
                log.geraLog('Não foi possível buscar os arquivos. Classe: Buscador Função: buscaArquivos()')

    #Verifica se arquivos encontrados no diretorio source estão parametrizados no sistema
    def verificaListaArquivos(self, lista):   
        
            import pandas as pd 
            from classesFuncoes.configArquivo import ConfigArquivo

            configArquivo = ConfigArquivo()
            arquivosParametrizados = configArquivo.leConfigArquivo()
                        
            #Verifica se arquivos no diretorio source estão parametrizados no arquivo configArquivos.csv
            try:    
                encontrados = set(arquivosParametrizados['nomeArquivo']).intersection(lista) 
            except:             
                from classesFuncoes.log import Log
                log = Log()
                log.geraLog('Não foi possível verificar lista de arquivos. Classe: Buscador Função: verificaListaArquivos()')        
    
            if(len(encontrados) != 0):
                return True, encontrados
            else:
                return False, encontrados
               
    #Chama processamento de arquivos encontrados/parametrizados 
    def  chamaProcessamentoArquivos(self, lista):

        #Classe para tratamentos/funções genéricos em arquivos
        from classesArquivos.arquivos import Arquivos
        from classesFuncoes.diretorios import Diretorios

        arquivo = Arquivos()
        diretorio = Diretorios()

        for item in lista:

            if (item == 'metas.xlsx'):                 
                
                #Função para leitura do arquivo e retorno de um dataset
                df = arquivo.leArquivo(diretorio.source, item)

                #Se numero colunas do arquivo iguais ao numero de colunas configurada no configArquivos.csv 
                if(arquivo.verificaColunas(df,item)):
                    #Verifica quantidade de NaN no arquivo e se arquivo permite NaN
                    if(arquivo.vericaNulos(df,item)):
                        
                        #Após verificações genericas, instanciamento de objeto específico
                        from classesArquivos.metas import Metas
                        meta = Metas()
                        if (meta.validaFormatoDados(df)):
                            meta.processaArquivoMeta(df, item)     

            if (item == 'metasagencias.xlsx'):                 
                
                #Função para leitura do arquivo e retorno de um dataset
                df = arquivo.leArquivo(diretorio.source, item)

                #Se numero colunas do arquivo iguais ao numero de colunas configurada no configArquivos.csv 
                if(arquivo.verificaColunas(df,item)):
                    #Verifica quantidade de NaN no arquivo e se arquivo permite NaN
                    if(arquivo.vericaNulos(df,item)):
                        
                        #Após verificações genericas, instanciamento de objeto específico
                        from classesArquivos.metasAgencias import MetasAgencias
                        metaag = MetasAgencias()
                        if (metaag.validaFormatoDados(df)):
                            metaag.processaArquivoMetasAgencias(df, item)           

            if (item == 'lancamentosmetas.xlsx'):                 
                
                #Função para leitura do arquivo e retorno de um dataset
                df = arquivo.leArquivo(diretorio.source, item)

                #Se numero colunas do arquivo iguais ao numero de colunas configurada no configArquivos.csv 
                if(arquivo.verificaColunas(df,item)):
                    #Verifica quantidade de NaN no arquivo e se arquivo permite NaN
                    if(arquivo.vericaNulos(df,item)):
                        
                        #Após verificações genericas, instanciamento de objeto específico
                        from classesArquivos.lancamentoMetas import LancamentoMetas
                        lanMeta = LancamentoMetas()
                        if (lanMeta.validaFormatoDados(df)):
                            lanMeta.processaArquivoLancamentoMetas(df, item)


                                                            
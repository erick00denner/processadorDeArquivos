'''
CLASSE: Buscador

Classe desenvolvida para buscar arquivos no diretório Source.
Quando algum arquivo parametrizado em config/configArquivos.csv é encontrado
chama classes e funções para inserção na base de dados

'''
class Buscador:
    
    #Busca arquivos diretorio source
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

    #Recebe lista de arquivos encontrados no diretorio Source e verifica se estão parametrizados
    def verificaListaArquivos(self, lista):   
        
            import pandas as pd 
            from classesFuncoes.configArquivo import ConfigArquivo

            configArquivo = ConfigArquivo()
            arquivosParametrizados = configArquivo.leConfigArquivo()
                        
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

    #Recebe lista de arquivos encontrados no Source e parametrizados no sistema           
    def  chamaProcessamentoArquivos(self, lista):

        from classesArquivos.arquivos import Arquivos
        from classesFuncoes.diretorios import Diretorios

        arquivo = Arquivos()
        diretorio = Diretorios()

        for item in lista:

#Para adicionar novos arquivos no sistema, seguir estrutura marcada a seguir
#################################################################################

            if (item == 'metas.xlsx'):    

                from classesArquivos.metas import Metas
                        
                meta = Metas()             
                
                df = arquivo.leArquivo(diretorio.source, item)

                df = meta.adiconaFKnoDF(df) 

                if(arquivo.verificaColunas(df,item)):

                    if(arquivo.vericaNulos(df,item)):
                                               
                        if (meta.validaFormatoDados(df,item)):
                            
                            meta.processaArquivoMeta(df, item)    

################################################################################
            
            if (item == 'metasagencias.xlsx'):                 
                
                from classesArquivos.metasAgencias import MetasAgencias

                metaag = MetasAgencias()

                df = arquivo.leArquivo(diretorio.source, item)

                df = metaag.adiconaFKnoDF(df) 

                if(arquivo.verificaColunas(df,item)):
                    
                    if(arquivo.vericaNulos(df,item)):
                                            
                        if (metaag.validaFormatoDados(df,item)):
                            
                            metaag.processaArquivoMetasAgencias(df, item)           

            if (item == 'lancamentosmetas.xlsx'):                 

                df = arquivo.leArquivo(diretorio.source, item)

                if(arquivo.verificaColunas(df,item)):

                    if(arquivo.vericaNulos(df,item)):

                        from classesArquivos.lancamentoMetas import LancamentoMetas
                        
                        lanMeta = LancamentoMetas()
                        
                        if (lanMeta.validaFormatoDados(df,item)):
                            
                            lanMeta.processaArquivoLancamentoMetas(df, item)


                                                            
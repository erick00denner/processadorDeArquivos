
### Indice

1. [Instação](#installation)
2. [Motivação do projeto](#motivation)
3. [Descrição dos arquivos](#files)

## Instação <a name="installation"></a>

Desenvoldivo utilizando Python versions 3.*.
Para utilizar o sistema, os arquivos config/configArquivo.csv, config/configDiretorios.csv e config/configBanco.csv devem ser parametrizados.
A classe classesFuncoes/buscador.py deve receber o trecho de código para novos arquivos
Uma nova classe deve ser desenvolvida em classesArquivos/ seguindo o modelo das classes existentes

## Motivação do projeto<a name="motivation"></a>

Como ainda existe grande fluxo de dados em planilhas do excel. Se faz necessário uma forma de armazenamento desses dados de forma estruturada. 
Esse projeto é uma forma de automatizar esse processo de forma organizada e com segurança. 
Ele busca os arquivos, verifica a estrutra dos arquivos e seus dados e armazena na base de dados.
O sistema possui 3 arquivos pré-parametrizados, os quais são utilizados para armazenamento de dados de metas para serem consumidos por uma dashboard no Power BI.

## Descrição dos arquivos <a name="files"></a>

config/configArquivo - Parametros de configuração dos arquivos processados pelo sistema
config/configBanco - Parametros de conexão com base de dados
config/configDiretorios - Parametros dos diretorios utilizados pelo sistema
classesFuncoes/buscador - Funções de busca dos arquivos e instanciamento das classes e funções de processamento
classesFuncoes/log - Funções de log do stackoverflow/so-survey-2017/data
classesFuncoes/banco - Funções de armazenamento na base de das
classesFuncoes/diretorios - Funções dos diretorios do stackoverflow/so-survey-2017/data
classesFuncoes/configArquivo - Funções dos parametros dos arquivos 
classesArquivos/arquivos - Funções de tratamento genérico dos arquivos
classesArquivos/metas - Funções de arquivo pré-parametrizados
classesArquivos/metasAgencias - Funções de arquivo pré-parametrizados
classesArquivos/lancamentoMetas - Funções de arquivo pré-parametrizados

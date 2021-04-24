
### Indice

1. [Instação](#installation)
2. [Motivação do projeto](#motivation)
3. [Descrição dos arquivos](#files)

## Instação <a name="installation"></a>

Desenvolvido utilizando Python versão 3.7 em ambiente Anaconda.

Para utilizar o sistema, os arquivos config/configArquivo.csv, config/configDiretorios.csv e config/configBanco.csv devem ser parametrizados.

Para novos arquivos, a classe classesFuncoes/buscador deve receber o trecho de código, e
uma nova classe deve ser desenvolvida em classesArquivos/ seguindo o modelo das classes existentes.

## Motivação do projeto<a name="motivation"></a>

Como ainda existe grande fluxo de dados em planilhas do excel, se faz necessário o processamento e armazenamento desses dados de forma estruturada. 
Esse projeto é uma forma de automatizar esse processo. 
Com classes para busca de arquivos, verificação da estrutura dos arquivos, verificação dos dados e armazenamento em base de dados. E arquivos que permitem configurar o sistema em qualquer infraestrutura de TI e facilitam a inclusão de novos arquivos. É uma forma de adicionar segurança e previsibilidade ao processo.   
O sistema possui 3 arquivos "pré-parametrizados" para exemplo, eles são utilizados para fornecer dados de metas que serão consumidos por uma dashboard no Power BI.

## Descrição dos arquivos <a name="files"></a>

config/configArquivo - Parametros de configuração dos arquivos processados pelo sistema

config/configBanco - Parametros de conexão com base de dados

config/configDiretorios - Parametros dos diretorios utilizados pelo sistema

classesFuncoes/buscador - Funções de busca dos arquivos e instanciamento das classes e funções de processamento

classesFuncoes/log - Funções de log do sistema

classesFuncoes/banco - Funções de armazenamento na base de das

classesFuncoes/diretorios - Funções dos diretorios do sistema

classesFuncoes/configArquivo - Funções dos parametros dos arquivos 

classesArquivos/arquivos - Funções de tratamento genérico dos arquivos

classesArquivos/metas - Funções de arquivo pré-parametrizados

classesArquivos/metasAgencias - Funções de arquivo pré-parametrizados

classesArquivos/lancamentoMetas - Funções de arquivo pré-parametrizados

metas.sql - Script SQL de criação da base de dados para armazenamento metas

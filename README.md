Teste 3 - Banco de Dados: Análise de Despesas de Operadoras de Planos de Saúde
Contexto do Exercício
Este exercício faz parte de um teste de banco de dados. O objetivo é processar dados financeiros de operadoras de planos de saúde, como as despesas de eventos/sinistros conhecidos ou avisados de assistência a saúde médico-hospitalar, utilizando arquivos públicos disponibilizados pela ANS (Agência Nacional de Saúde Suplementar). A partir dos dados tratados, o exercício envolve a criação de queries SQL e a análise de despesas dessas operadoras.

O teste é dividido nas seguintes tarefas:

Tarefas de Preparação:
3.1. Baixar os arquivos dos últimos 2 anos do repositório público da ANS: Demonstrativos Contábeis

3.2. Baixar os Dados Cadastrais das Operadoras Ativas na ANS: Operadoras Ativas

Tarefas de Código:
3.3. Criar queries para estruturar as tabelas necessárias para o arquivo CSV.

3.4. Elaborar queries para importar o conteúdo dos arquivos preparados, atentando para o encoding correto.

3.5. Desenvolver uma query analítica para responder as seguintes perguntas:

Quais as 10 operadoras com maiores despesas em "EVENTOS/ SINISTROS CONHECIDOS OU AVISADOS DE ASSISTÊNCIA A SAÚDE MÉDICO HOSPITALAR" no último trimestre?

Quais as 10 operadoras com maiores despesas nessa categoria no último ano?



Explicação do Código:
Leitura e Modificação dos Arquivos CSV: O código acima lê os arquivos CSV que você fez upload, substitui as vírgulas por pontos (para garantir que os números decimais sejam lidos corretamente) e carrega os dados no Pandas.

Salvamento dos Arquivos Tratados: Após processar cada arquivo, ele é salvo na pasta /content/arquivos_tratados/ com o prefixo "tratado_".

Compactação e Download: Após o processamento de todos os arquivos, a pasta contendo os arquivos tratados é compactada em um arquivo ZIP, o qual pode ser baixado diretamente do ambiente Colab.


import pandas as pd
from io import StringIO
import os

# Caminho base do script
caminho_base = os.path.dirname(os.path.abspath(__file__))

# Lista de arquivos CSV que você já fez upload (localizados na pasta 'csv')
arquivos_csv = [
    os.path.join(caminho_base, 'csv', '4T2022.csv'),
    os.path.join(caminho_base, 'csv', '1T2023.csv'),
    os.path.join(caminho_base, 'csv', '2T2023.csv'),
    os.path.join(caminho_base, 'csv', '3T2023.csv'),
    os.path.join(caminho_base, 'csv', '4T2023.csv'),
    os.path.join(caminho_base, 'csv', '1T2024.csv'),
    os.path.join(caminho_base, 'csv', '2T2024.csv'),
    os.path.join(caminho_base, 'csv', '3T2024.csv'),
    os.path.join(caminho_base, 'csv', '4T2024.csv')
]

print(f"Caminho da pasta 'csv': {os.path.join(caminho_base, 'csv')}")
print("Arquivos esperados:")
for arquivo in arquivos_csv:
    print(arquivo)

# Verificar se os arquivos existem
for arquivo in arquivos_csv:
    if os.path.exists(arquivo):
        print(f"Arquivo encontrado: {arquivo}")
    else:
        print(f"Arquivo NÃO encontrado: {arquivo}")

# Dicionário para armazenar os DataFrames
dfs = {}

# Criar uma pasta para armazenar os arquivos tratados
pasta_saida = os.path.join(caminho_base, 'arquivos_tratados')
os.makedirs(pasta_saida, exist_ok=True)  # Cria a pasta se não existir

# Iterar sobre os arquivos CSV
for arquivo_exemplo in arquivos_csv:
    print(f"Processando arquivo: {arquivo_exemplo}")
    
    # Verificar se o arquivo existe
    if not os.path.exists(arquivo_exemplo):
        print(f"Arquivo não encontrado: {arquivo_exemplo}")
        continue

    try:
        # Ler o arquivo CSV como string
        with open(arquivo_exemplo, 'r', encoding='utf-8') as file:
            conteudo = file.read()
        
        # Verificar se o arquivo está vazio
        if not conteudo.strip():
            print(f"Arquivo vazio: {arquivo_exemplo}")
            continue
        
        # Substituir as vírgulas por ponto
        conteudo_modificado = conteudo.replace(',', '.')
        
        # Usar StringIO para tratar o arquivo modificado na memória
        dados_modificados = StringIO(conteudo_modificado)
        
        # Carregar os dados no Pandas diretamente
        df = pd.read_csv(dados_modificados, delimiter=';', encoding='utf-8')
        
        # Verificar se o DataFrame está vazio
        if df.empty:
            print(f"DataFrame vazio após carregar o arquivo: {arquivo_exemplo}")
            continue
        
        # Exibir informações gerais sobre o DataFrame
        print(f"\nInformações gerais sobre o arquivo {arquivo_exemplo}:")
        print(df.info())
        
        # Armazenar o DataFrame no dicionário
        dfs[arquivo_exemplo] = df
        
        # Salvar o DataFrame tratado em um novo arquivo CSV
        nome_arquivo_tratado = os.path.join(pasta_saida, f"tratado_{os.path.basename(arquivo_exemplo)}")
        df.to_csv(nome_arquivo_tratado, index=False, encoding='utf-8', sep=';')  # Salvar como CSV tratado
        print(f"Arquivo tratado salvo: {nome_arquivo_tratado}")
    except Exception as e:
        print(f"Erro ao processar o arquivo {arquivo_exemplo}: {e}")

# Exibir as primeiras linhas de todos os DataFrames carregados
for arquivo, df in dfs.items():
    print(f"Primeiras linhas do arquivo {arquivo}:")
    print(df.head())
    print("\n" + "-" * 80)  # Separador para facilitar a leitura

print(f"Todos os arquivos tratados foram salvos na pasta: {pasta_saida}")
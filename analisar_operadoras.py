import pandas as pd
import os

# Caminho base do script
caminho_base = os.path.dirname(os.path.abspath(__file__))

# Caminho do arquivo CSV
arquivo_csv = os.path.join(caminho_base, 'csv', 'Relatorio_cadop.csv')

# Caminho da pasta para salvar o arquivo tratado
pasta_saida = os.path.join(caminho_base, 'arquivos_tratados')
os.makedirs(pasta_saida, exist_ok=True)  # Cria a pasta se não existir

# Ler o arquivo CSV
try:
    # Carregar o CSV com pandas
    df = pd.read_csv(arquivo_csv, delimiter=';', encoding='utf-8')
    
    # Converter a coluna 'Data_Registro_ANS' para datetime
    df['Data_Registro_ANS'] = pd.to_datetime(df['Data_Registro_ANS'], errors='coerce')
    
    # Tratar valores ausentes
    df['Nome_Fantasia'] = df['Nome_Fantasia'].fillna('NÃO INFORMADO')
    df['Complemento'] = df['Complemento'].fillna('')
    df['DDD'] = df['DDD'].fillna(0).astype(int)
    df['Telefone'] = df['Telefone'].fillna(0).astype(int)
    df['Fax'] = df['Fax'].fillna(0).astype(int)
    df['Regiao_de_Comercializacao'] = df['Regiao_de_Comercializacao'].fillna(0).astype(int)
    
    # Exibir as primeiras linhas do DataFrame tratado
    print("Primeiras linhas do DataFrame tratado:")
    print(df.head())
    
    # Exibir informações gerais sobre o DataFrame tratado
    print("\nInformações gerais sobre o DataFrame tratado:")
    print(df.info())
    
    # Salvar o DataFrame tratado em um novo arquivo CSV
    arquivo_tratado = os.path.join(pasta_saida, 'Relatorio_cadop_tratado.csv')
    df.to_csv(arquivo_tratado, index=False, encoding='utf-8', sep=';')
    print(f"\nArquivo tratado salvo em: {arquivo_tratado}")
    
except Exception as e:
    print(f"Erro ao carregar ou tratar o arquivo CSV: {e}")
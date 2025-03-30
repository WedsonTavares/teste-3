import subprocess
import os
import logging
import sys

# Configuração do logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Caminho base do script
caminho_base = os.path.dirname(os.path.abspath(__file__))

# Caminhos dos scripts
script_analisar_operadoras = os.path.join(caminho_base, 'analisar_operadoras.py')
script_teste3 = os.path.join(caminho_base, 'demonstracoes_contabeis.py')

# Função para verificar se o arquivo existe
def verificar_arquivo(caminho):
    if not os.path.exists(caminho):
        logging.error(f"Arquivo não encontrado: {caminho}")
        sys.exit(1)

# Verificar se os scripts existem
verificar_arquivo(script_analisar_operadoras)
verificar_arquivo(script_teste3)

# Executar o script de análise das operadoras
logging.info("Executando o script 'analisar_operadoras.py'...")
try:
    subprocess.run(['python', script_analisar_operadoras], check=True)
    logging.info("Script 'analisar_operadoras.py' executado com sucesso!")
except subprocess.CalledProcessError as e:
    logging.error(f"Erro ao executar 'analisar_operadoras.py': {e}")
    sys.exit(1)

# Executar o script principal (demonstracoes_contabeis.py)
logging.info("Executando o script 'demonstracoes_contabeis.py'...")
try:
    subprocess.run(['python', script_teste3], check=True)
    logging.info("Script 'demonstracoes_contabeis.py' executado com sucesso!")
except subprocess.CalledProcessError as e:
    logging.error(f"Erro ao executar 'demonstracoes_contabeis.py': {e}")
    sys.exit(1)
import subprocess
import os

# Caminho base do script
caminho_base = os.path.dirname(os.path.abspath(__file__))

# Caminhos dos scripts
script_analisar_operadoras = os.path.join(caminho_base, 'analisar_operadoras.py')
script_teste3 = os.path.join(caminho_base, 'demonstracoes_contabeis.py')

# Executar o script de análise das operadoras
print("Executando o script 'analisar_operadoras.py'...")
try:
    subprocess.run(['python', script_analisar_operadoras], check=True)
    print("\nScript 'analisar_operadoras.py' executado com sucesso!")
except subprocess.CalledProcessError as e:
    print(f"Erro ao executar 'analisar_operadoras.py': {e}")

# Executar o script principal (demonstracoes_contabeis.py)
print("\nExecutando o script 'demonstracoes_contabeis.py'...")
try:
    subprocess.run(['python', script_teste3], check=True)
    print("\nScript 'demonstracoes_contabeis.py' executado com sucesso!")
except subprocess.CalledProcessError as e:
    print(f"Erro ao executar 'demonstracoes_contabeis.py': {e}")
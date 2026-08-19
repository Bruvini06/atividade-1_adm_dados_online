import pandas as pd

# 1. Carregar os dados de um arquivo CSV
df = pd.read_csv('Libertadores.csv')

# 2. Exibir as primeiras 10 linhas do DataFrame
print("--- Primeiras 10 linhas ---")
print(df.head(10))

# 3. Exibir informações gerais sobre o conjunto de dados (colunas, tipos e valores nulos)
print("\n--- Informações do DataFrame ---")
df.info()

# 4. Exibir um resumo estatístico das colunas numéricas
print("\n--- Resumo Estatístico ---")
print(df.describe())
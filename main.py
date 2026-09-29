import pandas as pd
#1 . Carrega a planilha para dentro de uma estrutura chamada data frame (df)
#se o arquivo fro .csv, mude para: pd.read_csv('dados_csv')
df = pd.read_csv('ambiente.csv')

#print(df)

print(df.info()) # Mostra informações sobre o Dataframe, como o número de linhas, colunas e tipos de dados
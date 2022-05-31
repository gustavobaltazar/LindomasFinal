import pandas as pd

tabela = pd.read_excel('planilha_final.xlsx')

sub = 'São Paulo'

print(tabela.loc[tabela['Regiao'] == 'São Paulo'])
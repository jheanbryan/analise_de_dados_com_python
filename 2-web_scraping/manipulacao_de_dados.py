import pandas as pd
from datetime import date
from datetime import datetime as dt

#exemplo de leitura de dados
leitura_de_jason = pd.read_json("https://api.bcb.gov.br/dados/serie/bcdata.sgs.11/dados?formato=json").head()
leitura_de_csv = pd.read_csv("https://people.sc.fsu.edu/~jburkardt/data/csv/cities.csv").head()

df_selic = pd.read_json("https://api.bcb.gov.br/dados/serie/bcdata.sgs.11/dados?formato=json")
#df_selic.info()  peegar informacoes da tabela

# pegar a data de hoje e criar ma nova coluna na Data frame de selic
data_extracao = date.today()
df_selic['data_extracao'] = data_extracao #coluna
df_selic['responsavel'] = "Autora" #coluna
#print(df_selic)
#df_selic.head()

#astype transforma os dados de uma coluna (que é uma Series) em um determinado tipo, int, float etc
df_selic['data'] = pd.to_datetime(df_selic['data'], dayfirst=True)
df_selic['data_extracao'] = df_selic['data_extracao'].astype('datetime64[ns]')

#transforma tudo de responsavel pra letras maiusculas
df_selic['responsavel'] = df_selic['responsavel'].str.upper() 

#ordena a coluna data, de maior para menor
df_selic.sort_values(by='data', ascending=False, inplace=True)

#cria um index
df_selic.reset_index(drop=True, inplace=True)

#renomeando o index para selic_0, selic_1 ...
lista_novo_indice = [f'selic_{indice}' for indice in df_selic.index]
df_selic.set_index(keys=[lista_novo_indice], inplace=True)

#indice menor e maior valor
print(df_selic['valor'].idxmin())
print(df_selic['valor'].idxmax())

#filtrar os dados por index, pode ser passado mais de um
selic_0 = df_selic.loc['selic_0']

#filtrar com condicoes booleanas
valor_baixo = df_selic['valor'] < 0.01

print(df_selic.info())
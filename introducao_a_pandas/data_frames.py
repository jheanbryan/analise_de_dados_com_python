
import pandas as pd

lista_nomes = 'Howard Ian Peter Jonah Kellie'.split()
lista_cpfs = '111.111.111-11 222.222.222-22 333.333.333-33 444.444.444-44 555.555.555-55'.split()
lista_emails = 'risus.varius@dictumPhasellusin.ca Nunc@vulputate.ca fames.ac.turpis@cursusa.org non@felisullamcorper.org eget.dictum.placerat@necluctus.co.uk'.split()
lista_idades = [32, 22, 25, 29, 38]
data_frame = pd.DataFrame(lista_nomes, columns=['nome'], index=lista_cpfs)


dados = list(zip(lista_nomes, lista_cpfs, lista_idades, lista_emails)) # cria uma lista de tuplas
data_frame_pessoa = pd.DataFrame(dados, columns=['nome', 'cpfs', 'idade', 'email'])


dados = {
    'nomes': 'Howard Ian Peter Jonah Kellie'.split(),
    'cpfs' : '111.111.111-11 222.222.222-22 333.333.333-33 444.444.444-44 555.555.555-55'.split(),
    'emails' : 'risus.varius@dictumPhasellusin.ca Nunc@vulputate.ca fames.ac.turpis@cursusa.org non@felisullamcorper.org eget.dictum.placerat@necluctus.co.uk'.split(),
    'idades' : [32, 22, 25, 29, 38]
}
data_frame_com_dicionario = pd.DataFrame(dados)


data_frame_com_dicionario = pd.DataFrame(dados)

'''
print('\nInformações do DataFrame:\n')
print(data_frame_com_dicionario.info()) # Apresenta informações sobre a estrutura do DF

print('\nQuantidade de linhas e colunas = ', data_frame_com_dicionario.shape) # Retorna uma tupla com o número de linhas e colunas
print('\nTipo de dados:\n', data_frame_com_dicionario.dtypes) # Retorna o tipo de dados, para cada coluna, se for misto será object

print('\nQual o menor valor de cada coluna?\n', data_frame_com_dicionario.min()) # Extrai o menor de cada coluna 
print('\nQual o maior valor?\n', data_frame_com_dicionario.max()) # Extrai o valor máximo e cada coluna 
#print('\nQual a média aritmética?\n', data_frame_com_dicionario.mean()) # Extrai a média aritmética de cada coluna numérica
#print('\nQual o desvio padrão?\n', data_frame_com_dicionario.std()) # Extrai o desvio padrão de cada coluna numérica
#print('\nQual a mediana?\n', data_frame_com_dicionario.median()) # Extrai a mediana de cada coluna numérica

print('\nResumo:\n', data_frame_com_dicionario.describe()) # Exibe um resumo

data_frame_com_dicionario.head() # Exibe os 5 primeiros registros do DataFrame
'''

df_uma_coluna = data_frame_com_dicionario['idades']
#print(type(df_uma_coluna))

#print('Média de idades = ', df_uma_coluna.mean())

colunas = ['nomes', 'cpfs']
df_duas_colunas = df_uma_coluna
print(df_duas_colunas)
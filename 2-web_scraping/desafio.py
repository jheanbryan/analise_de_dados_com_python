import pandas as pd
from datetime import date
from datetime import datetime as dt

'''
Como desenvolvedor em uma empresa de consultoria de software, você foi alocado em um projeto para uma empresa de geração de energia. Essa empresa tem interesse em criar uma solução que acompanhe as exportações de etanol no Brasil. Esse tipo de informação está disponível no site do governo brasileiro http://www.dados.gov.br/dataset, em formatos CSV, JSON, dentre outros.

No endereço http://www.dados.gov.br/dataset/importacoes-e-exportacoes-de-etanol é possível encontrar várias bases de dados (datasets), contendo informações de importação e exportação de etanol. O cliente está interessado em obter informações sobre a Exportação Etano Hidratado (barris equivalentes de petróleo) 2012-2020, cujo endereço é http://www.dados.gov.br/dataset/importacoes-e-exportacoes-de-etanol/resource/ca6a2afe-def5-4986-babc-b5e9875d39a5. Para a análise será necessário fazer o download do arquivo.

O cliente deseja uma solução que extraia as seguintes informações:

Em cada ano, qual o menor e o maior valor arrecadado da exportação?
Considerando o período de 2012 a 2019, qual a média mensal de arrecadamento com a exportação.
Considerando o período de 2012 a 2019, qual ano teve o menor arrecadamento? E o menor?
Como parte das informações técnicas sobre o arquivo, foi lhe informado que se trata de um arquivo delimitado CSV, cujo separador de campos é ponto-e-vírgula e a codificação do arquivo está em ISO-8859-1. Como podemos obter o arquivo? Como podemos extrair essas informações usando a linguagem Python? Serão necessários transformações nos dados para obtermos as informações solicitadas?
'''

def extractEtanol():
    url = 'csv_example.csv'

    df_etanol= pd.read_csv(url, sep=';', encoding="ISO-8859-1").info()
    df_etanol.drop(columns=['PRODUTO', 'MOVIMENTO COMERCIAL', 'UNIDADE'], inplace=True)

    for mes in 'JAN FEV MAR ABR MAI JUN JUL AGO SET OUT NOV DEZ TOTAL'.split():
        df_etanol[mes] = df_etanol[mes].str.replace(',', '.')

    df_etanol[mes] = pd.to_numeric(df_etanol[mes])

    
    for ano in range(2012, 2021):
        ano_info = df_etanol.loc[ano]
        minimo = ano_info.min()
        maximo = ano_info.max()
        print(f"Ano = {ano}")
        print(f"Menor valor = {minimo:,.0f}".replace(',', '.'))
        print(f"Maior valor = {maximo:,.0f}".replace(',', '.'))
        print("--------------")
        

    print("Média mensal de rendimentos:")
    for mes in 'JAN FEV MAR ABR MAI JUN JUL AGO SET OUT NOV DEZ'.split():
        media = df_etanol.loc[2012:2019, mes].mean()
        print(f"{mes} = {media:,.0f}".replace(',', '.'))
    

    ano_menor_arrecadacao = df_etanol.loc[2012:2019, 'TOTAL'].idxmin()
    ano_maior_arrecadacao = df_etanol.loc[2012:2019, 'TOTAL'].idxmax()

    print(f"Ano com menor arrecadação = {ano_menor_arrecadacao}")
    print(f"Ano com maior arrecadação = {ano_maior_arrecadacao}")


print(extractEtanol)
import pdfplumber
import pandas as pd


#2013 - 2019

dados=[]

for ano in range(2013,2020):
    with pdfplumber.open(f'data/nota_de_corte/nota_de_corte_{ano}.pdf') as pdf:
        for pages in pdf.pages:
            tabela = pages.extract_table()
            if tabela:
                df = pd.DataFrame(tabela [1:],columns = tabela[0])
                df = df.drop([0],axis = 0)
                df = df.iloc[:, :5]
                df.columns = ['Codigo', 'Nome do Curso', 'Acertos do Primeiro', 'Acertos do Ultimo', 'Total de Vagas']
                df['Ano'] = ano
                dados.append(df)
nc_2013_2019 = pd.concat(dados,ignore_index=True)
nc_2013_2019.to_csv("data/bronze/nc_2013_2019.csv", index=False)

#2020 - 2025

dados1 = []

for ano1 in range(2020, 2026):
    with pdfplumber.open(f'data/nota_de_corte/nota_de_corte_{ano1}.pdf') as pdf1:
        for page in pdf1.pages:  
            tabela1 = page.extract_table() 
            if tabela1:
                df1 = pd.DataFrame(tabela1[1:], columns=tabela1[0])
                df1 = df1.iloc[:, :5]
                df1.columns = ['Codigo', 'Nome do Curso', 'Acertos do Primeiro', 'Acertos do Ultimo', 'Total de Vagas']
                df1['Ano'] = ano1
                df1 = df1[df1['Codigo'].notna() & (df1['Codigo'] != '')]
                dados1.append(df1)

nc_2020_2026 = pd.concat(dados1, ignore_index=True)
nc_2020_2026.to_csv('data/bronze/nc_2020_2026.csv', index=False)
print(nc_2020_2026)



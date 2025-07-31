import pandas as pd
import os

pasta = 'data/nota_de_corte/'
dfs1=[]
#2002-2007

for ano in range (2002,2008):
    arquivo = f"nota_de_corte_{ano}.xlsx"
    caminho = pasta + arquivo 
    try:
        df1=pd.read_excel(caminho, engine = 'openpyxl')  
        df1 = df1.drop([0,1],axis = 0)
        df1.rename(columns={
            'Unnamed: 1':'Codigo',
            'Unnamed: 2':'Nome do Curso',
            'Unnamed: 3':'Acertos do Primeiro',
            'Unnamed: 4':'Acertos do Ultimo',
            'Unnamed: 5':'Total de Vagas'
        },inplace=True)
        df1 = df1.drop(['Unnamed: 0'],axis = 1)
        df1['Ano'] = ano
        dfs1.append(df1)
    except Exception as e: 
        print(f"Erro ao tratar o arquivo {arquivo}: {e}")
nota_de_corte_2002_2008 = pd.concat(dfs1,ignore_index =True)
nota_de_corte_2002_2008.to_csv("data/bronze/nc_2002_2008.csv", index=False)

#2008-2012

dfs2=[]

for ano in range (2008,2013):
    arquivo = f"nota_de_corte_{ano}.xlsx"
    caminho = pasta + arquivo 
    try:
        df2=pd.read_excel(caminho, engine = 'openpyxl')  
        df2 = df2.drop([0,1,2],axis = 0)
        df2.rename(columns={
            'Unnamed: 1':'Codigo',
            'Unnamed: 2':'Nome do Curso',
            'Unnamed: 3':'Acertos do Primeiro',
            'Unnamed: 4':'Acertos do Ultimo',
            'Unnamed: 5':'Total de Vagas'
        },inplace=True)
        df2 = df2.drop(['Unnamed: 0','Unnamed: 6'],axis = 1)
        df2['Ano'] = ano
        df2 = df2[df2['Nome do Curso'] != 'Total']
        dfs2.append(df2)
    except Exception as e: 
        print(f"Erro ao tratar o arquivo {arquivo}: {e}")
nota_de_corte_2008_2012 = pd.concat(dfs2,ignore_index =True)
nota_de_corte_2008_2012.to_csv("data/bronze/nc_2008_2012.csv", index=False)

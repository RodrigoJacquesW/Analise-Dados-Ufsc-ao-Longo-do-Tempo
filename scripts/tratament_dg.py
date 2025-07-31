import pandas as pd
import os


pasta = 'data/dados_gerais/'
dfs = []

for ano in range(2003, 2011):
    arquivo = f'dados_gerais_{ano}.xlsx'
    caminho = pasta + arquivo
    try:
        df = pd.read_excel(caminho, engine='openpyxl')
        df = df.drop(0, axis=0)
        df.columns = ['teste', 'Texto', 'Valor']
        df = df.drop(['teste'], axis=1)
        df['Ano'] = ano
        df = df[df['Valor'].notna()].reset_index(drop=True)
        # df['Texto'] = df['Texto'].apply(limpar_texto)
        dfs.append(df)
    except Exception as e:
        print(f"Erro ao tratar o arquivo {arquivo}: {e}")

dg_2003_2010 = pd.concat(dfs, ignore_index=True)
dg_2003_2010.to_csv("data/bronze/dg_2003_2010.csv", index=False)
 

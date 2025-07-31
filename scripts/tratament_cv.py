import pandas as pd
import os


#2002 - 2007
pasta = 'data/candidato_vaga/'
dfs1 = []

for ano in range(2002, 2007):
    arquivo = f'candidato_vaga_{ano}.xlsx'
    caminho = pasta + arquivo 
    try:
        df1 = pd.read_excel(caminho, engine='openpyxl')
        df1 = df1.drop(0, axis=0)
        df1.rename(columns={
            'Código':'Codigo',
            'Unnamed: 4': 'CV',
            'Total':'Total Vagas',
            'Opção 1': 'Inscritos'
        }, inplace=True)
        df1.drop(df1.columns[5:19], axis=1, inplace=True)
        df1['Ano'] = ano 
        dfs1.append(df1)
    except Exception as e: 
        print(f"Erro ao tratar o arquivo {arquivo}: {e}")

candidatosvaga_2002_2007 = pd.concat(dfs1, ignore_index=True)


#2008-2010
dfs2=[]

for ano2 in range(2008, 2010):
    arquivo2 = f'candidato_vaga_{ano2}.xlsx'
    caminho2 = f'data/candidato_vaga/{arquivo2}'
    try:
        df2 = pd.read_excel(caminho2, engine='openpyxl')
        df2 = df2.drop(0, axis= 0)
        df2.rename(columns={
            'Código': 'Codigo',
            'Unnamed: 3': 'Inscritos',
            'Unnamed: 4': 'CV',
            'Total': 'Total Vagas',
            'Geral': 'Total Vagas' if 'Total Vagas' not in df2.columns else 'Geral'
            }, inplace=True)
        df2.drop(df2.columns[5:19], axis=1, inplace=True)
        df2['Ano'] = ano2
        dfs2.append(df2)
    except Exception as e: 
        print(f"Erro ao tratar o arquivo {arquivo2}: {e}")
candidatosvaga_2008_2010 = pd.concat(dfs2,ignore_index=True)


candidatosvaga_2002_2007.to_csv("data/bronze/cv_2002_2007.csv", index=False)
candidatosvaga_2008_2010.to_csv("data/bronze/cv_2008_2010.csv", index=False)

print(candidatosvaga_2002_2007)
print(candidatosvaga_2008_2010)
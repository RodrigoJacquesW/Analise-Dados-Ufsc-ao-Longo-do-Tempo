import pandas as pd

#CandidatoVaga

dados = []
arquivos = ["data/bronze/cv_2002_2007.csv","data/bronze/cv_2008_2010.csv","data/bronze/cv_2011_2012.csv","data/bronze/cv_2013_2025.csv"]

for arquivo in arquivos:
    df = pd.read_csv(arquivo)
    dados.append(df)

df_total = pd.concat(dados,ignore_index =True)
print(df_total)
df_total.to_csv("data/bronze/cv_final.csv",index=False)

#NotaDeCorte

dados1 = []
arquivos1 = ["data/bronze/nc_2002_2008.csv","data/bronze/nc_2008_2012.csv","data/bronze/nc_2013_2019.csv","data/bronze/nc_2020_2026.csv"]

for arquivo1 in arquivos1:
    df1 = pd.read_csv(arquivo1)
    dados1.append(df1)

df1_total = pd.concat(dados1,ignore_index =True)
print(df1_total)
df1_total.to_csv("data/bronze/nc_final.csv",index=False)

#DadosGerais

dados2 = []
arquivos2 = ["data/bronze/dg_2003_2010.csv","data/bronze/dg_2011_2022.csv","data/bronze/dg_2023_2025.csv"]

for arquivo2 in arquivos2:
    df2 = pd.read_csv(arquivo2)
    dados2.append(df2)

df2_total = pd.concat(dados2,ignore_index =True)
df2_total.to_csv("data/bronze/df_final.csv",index=False)

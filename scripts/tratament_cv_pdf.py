import pdfplumber
import pandas as pd

dados = []

#2011-2012

for ano in range(2011,2013):
    with pdfplumber.open(f'data/candidato_vaga/candidato_vaga_{ano}.pdf') as pdf:
        for pages in pdf.pages:
            tabela = pages.extract_table()
            if tabela:
                df = pd.DataFrame(tabela[1:], columns=tabela[0])
                df=df.iloc[:, :6]
                df.columns = ['Codigo','Nome do Curso','Total Vagas','Inscritos','CV','Ano']
                df.drop(0,axis=0,inplace=True)
                df['Ano'] = ano 
                dados.append(df)
candidatosvaga_2011_2012 = pd.concat(dados, ignore_index=True)

#2013-2025

dados2 = []

# Dentro do loop de 2013–2025
for ano2 in range(2013,2026):
    with pdfplumber.open(f'data/candidato_vaga/candidato_vaga_{ano2}.pdf') as pdf:
        for pages in pdf.pages:
            tabela = pages.extract_table()
            if tabela:
                df2 = pd.DataFrame(tabela[1:], columns=tabela[0]) 
                df2 = df2.iloc[:, :6]
                df2.columns = ['Codigo','Nome do Curso','Total Vagas','Inscritos','CV','Ano']
                df2['Ano'] = ano2

                # Limpa vírgulas na coluna 'CV' se for string (ex: '14,2')
                df2['CV'] = (
                    df2['CV'].astype(str)
                    .str.replace(',', '.', regex=False)
                    .str.strip()
                )

                # Converte para float
                df2['CV'] = pd.to_numeric(df2['CV'], errors='coerce')

                df2.drop(0, axis=0, inplace=True)
                dados2.append(df2)

candidatosvaga_2013_2025 = pd.concat(dados2, ignore_index=True)


candidatosvaga_2011_2012.to_csv("data/bronze/cv_2011_2012.csv", index=False)
candidatosvaga_2013_2025.to_csv("data/bronze/cv_2013_2025.csv", index=False)
print(candidatosvaga_2011_2012)
print(candidatosvaga_2013_2025)
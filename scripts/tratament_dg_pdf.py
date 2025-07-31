import pdfplumber
import pandas as pd
import os

#2011 a 2022

dados = []


for ano in range(2011, 2023):
    if ano == 2021:
        continue 
    with pdfplumber.open(f'data/dados_gerais/dados_gerais_{ano}.pdf') as pdf:
        for page in pdf.pages:
            texto = page.extract_text()
            if texto:
                linhas = texto.split("\n")
                for linha in linhas:
                    if ":" in linha and not linha.lower().startswith("data"):
                        partes = linha.split(":",1)
                        texto_descricao = partes[0].strip()
                        valor = partes[1].strip()
                        dados.append({
                            "Texto": texto_descricao,
                            "Valor": valor,
                            "Ano":ano        
                        })
dg_2011_2022 = pd.DataFrame(dados)
dg_2011_2022.to_csv("data/bronze/dg_2011_2022.csv",index = False)
            
#2023 a 2025

dados1 = []

for anos in range(2023, 2026):
    with pdfplumber.open(f'data/dados_gerais/dados_gerais_{anos}.pdf') as pdf:
        for page in pdf.pages:  # aqui sim, page (no singular)
            texto1 = page.extract_text()
            if texto1:
                linhas = texto1.split("\n")
                for linha in linhas:
                    if ":" in linha:
                        partes = linha.split(":", 1)
                        texto_descricao = partes[0].strip()
                        valor = partes[1].strip()
                        dados1.append({
                            "Texto": texto_descricao,
                            "Valor": valor,
                            "Ano": anos        
                        })

dg_2023_2025 = pd.DataFrame(dados1)
dg_2023_2025.to_csv("data/bronze/dg_2023_2025.csv",index = False)


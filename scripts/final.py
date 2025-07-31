import pandas as pd
import unicodedata

def limpar_texto(texto):
    """Limpa texto removendo acentos, pontuações e deixando em minúsculas."""
    if not isinstance(texto, str):
        return ''
    texto = texto.lower().strip()
    texto = unicodedata.normalize('NFKD', texto).encode('ASCII', 'ignore').decode('utf-8')
    texto = ''.join(c for c in texto if c.isalnum() or c == ' ')
    return texto

def limpar_colunas(df):
    """Padroniza nomes das colunas: minúsculo, sem acento, espaço vira underline."""
    df.columns = [
        unicodedata.normalize('NFKD', col)
        .encode('ASCII', 'ignore')
        .decode('utf-8')
        .strip()
        .lower()
        .replace(' ', '_')
        .replace('.', '')
        for col in df.columns
    ]
    return df

def formatar_numeros(df, colunas):
    """Converte colunas de string para float, limpando vírgulas e %."""
    for col in colunas:
        if col in df.columns:
            df[col] = (
                df[col]
                .astype(str)
                .str.replace('%', '', regex=False)
                .str.replace(',', '.', regex=False)
                .str.strip()
            )
            df[col] = pd.to_numeric(df[col], errors='coerce')
    return df


# Leitura dos arquivos finais
df_cv = pd.read_csv("data/bronze/cv_final.csv")
df_nc = pd.read_csv("data/bronze/nc_final.csv")
df_dg = pd.read_csv("data/bronze/df_final.csv")

# Limpeza de colunas (nomes)
df_cv = limpar_colunas(df_cv)
df_nc = limpar_colunas(df_nc)
df_dg = limpar_colunas(df_dg)

# Formatar colunas numéricas
colunas_cv = ['total_vagas', 'inscritos', 'c/v']
colunas_nc = ['acertos_do_primeiro', 'acertos_do_ultimo', 'total_de_vagas']
colunas_dg = ['valor']  # supondo que ela contém números ou % (confirme isso)

df_cv = formatar_numeros(df_cv, colunas_cv)
df_nc = formatar_numeros(df_nc, colunas_nc)
df_dg = formatar_numeros(df_dg, colunas_dg)

# Limpeza de textos nas colunas 'nome_do_curso' ou 'texto'
if 'nome_do_curso' in df_cv.columns:
    df_cv['nome_do_curso'] = df_cv['nome_do_curso'].apply(limpar_texto)

if 'nome_do_curso' in df_nc.columns:
    df_nc['nome_do_curso'] = df_nc['nome_do_curso'].apply(limpar_texto)

if 'texto' in df_dg.columns:
    df_dg['texto'] = df_dg['texto'].apply(limpar_texto)

# Exportar para novos CSVs prontos para o BigQuery
df_cv.to_csv("data/final/cv_bq.csv", index=False)
df_nc.to_csv("data/final/nc_bq.csv", index=False)
df_dg.to_csv("data/final/dg_bq.csv", index=False)

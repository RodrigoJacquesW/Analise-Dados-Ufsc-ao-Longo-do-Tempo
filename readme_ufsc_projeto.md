# 📊 Análise dos Dados da UFSC ao Longo do Tempo (2003–2025)

## 📜 Resumo

Este projeto contempla um estudo histórico sobre o processo seletivo da Universidade Federal de Santa Catarina (UFSC), analisando os dados de **inscritos, notas de corte e relação candidato/vaga** no período de **2003 a 2025**.

A proposta é **avaliar a queda expressiva na procura por universidades públicas**, refletindo sobre possíveis causas e consequências desse movimento para a educação superior no Brasil.

A análise foi dividida em três etapas:

1. **Processo de execução**
2. **Resultados**
3. **Discussões finais**

---

## ⚙️ Processo de Execução

### 🧍️ Extração

A extração foi feita manualmente, dado o formato irregular dos arquivos e a complexidade de padronização. Todos os dados foram retirados **exclusivamente de fontes públicas**, disponíveis no site da UFSC:

🔗 [Vestibulares Anteriores – Coperve/UFSC](https://coperve.ufsc.br/vestibulares-anteriores/)

Os arquivos originais foram disponibilizados em **PDF ou Excel**.

---

### 🗂️ Organização e Tratamento

- Os arquivos foram separados em três categorias:

  - `Dados Gerais`
  - `Candidato/Vaga`
  - `Nota de Corte`

- Cada conjunto de arquivos foi **tratado individualmente** com `Python + Pandas`, e depois concatenado em arquivos únicos por categoria.

- Após o tratamento, os dados foram divididos em:

  - `raw_data`: dados brutos
  - `clean_data`: colunas padronizadas e tipos corrigidos
  - `enrich_data`: cálculos e colunas derivadas

---

### ☁️ Armazenamento e Modelagem

Embora não fosse essencial para este projeto, optei por usar o **Google Cloud Platform** e modelar os dados com o **Dataform CLI** no VSCode, simulando uma pequena stack de engenharia de dados para fins de aprendizado.

> **Nota:** todos os dados considerados fazem parte da **categoria Ampla Concorrência**.

---

## 📉 Resultados

### 🔻 Queda no Número de Inscritos

De **2005 a 2025**, a UFSC registrou uma queda de aproximadamente **41% no número de inscritos** na ampla concorrência, **mesmo com o crescimento populacional de SC no período**.

📈 Gráfico de inscritos por ano (ampla concorrência):

> *(Adicionar imagem aqui + legenda explicativa)*

---

### 📊 Relação com Nota de Corte e Candidato/Vaga

A evolução da nota de corte e da relação candidato/vaga acompanha diretamente a variação do número de inscritos ao longo dos anos.

📈 Gráfico: Notas de corte e relação candidato/vaga

> *(Adicionar imagem aqui + legenda explicativa)*

---

### 🧪 Comparativo por Área de Conhecimento

#### Engenharias vs Saúde

- **Engenharias**

  - Pico em **2013** com **7668 inscritos**
  - Em 2025: **1963 inscritos** (queda de **\~74%**)

- **Saúde**

  - Pico em **2016** com **12.331 inscritos**
  - Em 2025: **9674 inscritos** (queda de **\~22%**)

📊 Gráfico: Comparativo por área (Engenharias vs Saúde)

---

#### Tecnologia vs Licenciaturas

- **Tecnologia**

  - Pico em **2003** com **2212 inscritos**
  - Em 2025: **1387 inscritos** (queda de **\~37%**)

- **Licenciaturas**

  - Pico em **2003** com **7895 inscritos**
  - Em 2025: **1911 inscritos** (queda de **\~75%**)

📊 Gráfico: Comparativo por área (Tecnologia vs Licenciaturas)

---

### 📌 Linhas de tendência (por área)

📈 Médias traçadas para inscrições em cursos de Saúde e Tecnologia mostram que esses segmentos **ainda mantêm estabilidade**, diferentemente de Engenharias e Licenciaturas.

---

## 🤔 Possíveis Causas

Alguns fatores que podem explicar a queda na procura:

- ❌ **Sucateamento das universidades públicas**: relatos de alunos sobre a falta de estrutura básica.
- 🧑‍🎓 **Desvalorização profissional**: falta de fiscalização do CREA, salários baixos e pouca perspectiva em algumas carreiras.
- 🕵️‍♂️ **Crescimento do EAD privado**: acessível, flexível e cada vez mais difundido.

> Sugestão: incluir links ou referências de reportagens sobre o aumento do EAD e abandono de cursos presenciais.

---

## 🔮 Impactos Futuros

A queda de inscritos pode provocar:

- Redução da concorrência → entrada de candidatos menos preparados
- Aumento na taxa de desistência e evasão
- Formação de profissionais com base menos sólida
- Pressão sobre a qualidade da educação pública

> “O que a queda na nota de corte e na concorrência pode representar no mercado de trabalho daqui a 10 anos?”

---

## 📂 Estrutura do Projeto

```
├── data/
│   ├── bronze/     <- Arquivos brutos
│   ├── final/      <- Arquivos prontos para análise
├── scripts/        <- Scripts Python para extração e limpeza
├── definitions/    <- Arquivos .sqlx para modelagem com Dataform
├── README.md
└── requirements.txt
```

---

## 👍 Considerações Finais

Este projeto poderia ter sido conduzido localmente com ferramentas mais simples, mas foi utilizado como **projeto de aprendizado prático de Python, SQL, BigQuery e Dataform**.

Os dados estão limpos, padronizados e prontos para exploração com BI ou relatórios.

🚀 Projeto finalizado por [Rodrigo Jacques Wolff](https://github.com/RodrigoJacquesW) – Julho/2025


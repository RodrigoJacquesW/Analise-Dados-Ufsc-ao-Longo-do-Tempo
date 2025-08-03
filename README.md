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

Este projeto poderia ter sido conduzido localmente com ferramentas mais simples, mas foi utilizado como **projeto de aprendizado prático de Python, SQL, BigQuery e Dataform**.

---

### ☁️ Armazenamento e Modelagem

Embora não fosse essencial para este projeto, optei por usar o **Google Cloud Platform** e modelar os dados com o **Dataform CLI** no VSCode, simulando uma pequena stack de engenharia de dados para fins de aprendizado.

> **Nota:** todos os dados considerados fazem parte da **categoria Ampla Concorrência**.

---

## 📉 Resultados

### 🔻 Queda no Número de Inscritos

De **2005 a 2025**, a UFSC registrou uma queda de aproximadamente **41% no número de inscritos** na ampla concorrência, **mesmo com o crescimento populacional de SC no período**.

📈 Gráfico de inscritos por ano (ampla concorrência):

> <img width="1091" height="327" alt="image" src="https://github.com/user-attachments/assets/bbedb396-5676-40cb-a03b-d03ec44f54ac" />

---

### 📊 Relação com Nota de Corte e Candidato/Vaga

A evolução da nota de corte e da relação candidato/vaga acompanha diretamente a variação do número de inscritos ao longo dos anos.

📈 Gráfico: Notas de corte e relação candidato/vaga

> <img width="1093" height="661" alt="image" src="https://github.com/user-attachments/assets/3fd6477a-bdc8-4519-ac2a-cb90dd06fa09" />

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
<img width="1420" height="794" alt="image" src="https://github.com/user-attachments/assets/1073a350-ede9-47c2-bef6-f8cb8f707bba" />

---

#### Tecnologia vs Licenciaturas

- **Tecnologia**

  - Pico em **2003** com **2212 inscritos**
  - Em 2025: **1387 inscritos** (queda de **\~37%**)

- **Licenciaturas**

  - Pico em **2003** com **7895 inscritos**
  - Em 2025: **1911 inscritos** (queda de **\~75%**)

📊 Gráfico: Comparativo por área (Tecnologia vs Licenciaturas)
<img width="1417" height="800" alt="image" src="https://github.com/user-attachments/assets/71f6a176-2c06-481d-8c1c-1bae1fd87b36" />

---

### 📌 Linhas de tendência (por área)

📈 Médias traçadas para inscrições em cursos de Saúde e Tecnologia mostram que esses segmentos **ainda mantêm estabilidade**, diferentemente de Engenharias e Licenciaturas.
<img width="708" height="397" alt="image" src="https://github.com/user-attachments/assets/79c1208c-81e7-4338-b758-44c6a2216176" />
<img width="707" height="395" alt="image" src="https://github.com/user-attachments/assets/42695b33-7308-4d63-ab99-373705d0b0c1" />

---

## 🤔 Possíveis Causas

Alguns fatores que podem explicar a queda na procura:

- ❌ **Sucateamento das universidades públicas**: Como consequência da queda de investimento, a falta de estrutura básica.
- 🧑‍🎓 **Desvalorização profissional**: falta de fiscalização do CREA por exemplo, salários baixos e pouca perspectiva em algumas carreiras.
- 🕵️‍♂️ **Crescimento do EAD privado**: acessível, flexível e cada vez mais difundido.

Segundo a Carta Capital:
"O mais recente Censo de Educação do Ensino Superior, divulgado em maio deste ano, registrou a primeira queda de matrículas nas universidades federais brasileiras desde 1990. No período de 2019 e 2020, o número de estudantes que entraram no ensino superior pelas UFs passou de 1,3 milhões para 1,2 milhões. Ao lado da diminuição de matrículas, também se sobressaíram os trancamentos. Segundo dados levantados pelo jornal O Globo, cerca de 270 mil estudantes suspenderam a graduação por tempo indeterminado no período da pesquisa."

Segundo o Inep:
"Já o Inep, instituto responsável pelo Censo, apontou que, em contrapartida, as instituições privadas registraram aumento no número de ingressantes, chegando a corresponder a 86% do total das matrículas no ensino superior em 2020. Além disso, 53,4% deste ingresso aconteceu no ensino a distância, foram mais de 2 milhões de estudantes que se matricularam no ensino remoto, enquanto 1,7 milhão de estudantes, cerca de 46,6% ficaram no ensino presencial."

---

## 🔮 Impactos Futuros

A queda de inscritos pode provocar:

- Redução da concorrência → entrada de candidatos menos preparados
- Aumento na taxa de desistência e evasão
- Formação de profissionais com base menos sólida
- Pressão sobre a qualidade da educação pública

Segundo a Fapesp:

"Desde 2019, caiu de patamar o número de estudantes de instituições públicas de ensino superior do Brasil que conseguem concluir a graduação. Foram 251.374 naquele ano, 3% a menos que no período anterior. A situação se agravou na pandemia, com a suspensão das atividades presenciais e atraso na conclusão do ano letivo. Em 2020, o contingente de formados despencou para 204.174, queda de 18,7% em relação a 2019. Voltou a subir em 2021, para 219.342, mas ainda se encontra nos níveis de quase uma década atrás. Os dados constam do último Censo da Educação Superior do Instituto Nacional de Estudos e Pesquisas Educacionais (Inep), órgão do Ministério da Educação, divulgado em novembro de 2022."

> A pergunta que fica é: “O que a queda na nota de corte e na concorrência pode representar no mercado de trabalho daqui a 10 anos?”

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



🚀 Projeto finalizado por [Rodrigo Jacques Wolff](https://github.com/RodrigoJacquesW) – Julho/2025

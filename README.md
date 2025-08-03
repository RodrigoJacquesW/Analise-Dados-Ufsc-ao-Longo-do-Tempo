# Analise-Dados-Ufsc-ao-Longo-do-Tempo
Resumo

Esse projeto contempla um estudo do histórico da Universidade Federal de Santa Catarina, contendo os dados de 2003 - 2025 do número de inscritos, notas de corte e candidato/vaga. 
O propósito é analisar a decadência das universidades públicas buscando motivos e futuras consequências de tal.
Essa análise será dividida em 3 etapas: Processo de Execução, Resultado e Analise dos Dados.

Processo de Execução
Extração: A extração foi feita manualmente devido a complexidade de cada base de dado, todos os dados podem ser encontrados públicamentes no site da Universidade Federal de Santa Catarina.
Link: https://coperve.ufsc.br/vestibulares-anteriores/
Como resultado a extração gerou arquivos em PDF e Excel.
Organização e Concatenização:
  Os arquivos foram divididos em blocos (De acordo com suas caracteristicas) e tratados individualmente usando o Pandas via Python. Após isso cada grupo de arquivo (Dados Gerais, Candidato/Vaga e Nota de Corte) foi concatenada em 1 arquivo para cada categoria.
Armazenamento: 
  Os arquivos foram armazenadas na nuvem da Google Cloud, Aqui esse processo não era necessário devido ao teor do projeto, mas foi opção do autor. Os arquivos foram divididos em 3 categorias:
-raw_data: Base bruta concatenada;
-clean_data: Corrigido nomenclatura e definido o tipo de dado de cada coluna;
-enrich_data: Aqui foram feitos alguns calculos e medidas.
Limpeza e modelagem: 
  Os dados foram modelados via VSCODE com a ferramenta Dataform Tool. 
Confesso que nem era necessário a utilização da nuvem e modelagem via dataform tool, daria para fazer uma especie de "Mini Warehouse" local, devido a complexidade do projeto. Inclusive esse metodo teria sido muito mais rapido e eficaz.

*Observação: Todos os dados foram considerados na categoria Ampla Concorrência*

Resultado
De 2005 para 2025, a UFSC teve uma queda de aproximadamente 41%, número bem expressivo considerando que é um movimento contrário do aumento populacional da cidade por exemplo. 
Abaixo, um gráfico com o número total de inscritos na amplâ concorrência nesses 20 anos.
<img width="998" height="292" alt="image" src="https://github.com/user-attachments/assets/0dd28cdc-5661-46b7-9f1f-40eda604e16d" />
Legenda: Adicionar legenda
Ano natural, o número da nota de corte e dos candidatos por vaga acomnpanha o os candidatos totais inscritos, como demonstra os gráfico abaixo. 
Vale ressaltar que o número de candidados por vaga é fortemente influênciado pelo número total de vagas disponibilizadas.
<img width="986" height="596" alt="image" src="https://github.com/user-attachments/assets/a9fc14f4-6e6b-4ccc-8424-449b10e52f7c" />
Legenda: Adicionar legenda
Alguns cursos são mais afetados do que outros, a engenharia, por exemplo, não tem o mesmo movimento das áreas de tecnologia, isso pode ser impactado por N fatores que será dissertado melhor no final do texto, mas o reflexo do mercado do trabalho é um deles.
Aqui podemos ver bem um comparativo entre as engenharias e a área da saúde por exemplo:
<img width="1422" height="802" alt="image" src="https://github.com/user-attachments/assets/d517dae0-0409-4a84-b67d-3e4e08589b57" />
Legenda: Adicionar legenda
A área da Saúde contempla:: enfermagem, medicina, farmacia, fisioterapia, fonoaudiologia, nutrição, odontologia e etc.
A área das Engenharias contemplam: Engenharia Civil, Mecância, Elétrica, Pordução, Automação, Materiais e etc.
Engenharias: Nas engenharias temos um pico de inscritos em 2013 equivalte à 7668 inscritos e no ultimo ano de 2025 foram registrados 1963 inscritos representando uma queda de (calcular a %)
Saúde: Na área da Saúde temos um pico de inscritos em 2016 equivalte à 12331 inscritos e no ultimo ano de 2025 foram registrados 9674 inscritos representando uma queda de (calcular a %)
Outra comparação entre as áreas de Tecnologia e Lincenciatura:
<img width="1421" height="797" alt="image" src="https://github.com/user-attachments/assets/b82bf979-c010-4ce4-a410-5d331b742bb4" />
Legenda: Adicionar legenda
A área da Tecnologia contempla: ciência da computação, sistemas da informação, ciências da informação e etc.
A área das Licenciaturas contemplam: ciências biológicas, históriam, geografia, matemática, lingua inglesa, letras e etc.
Tecnologias: Nos cursos de Tecnologia temos um pico de inscritos em 2003 equivalte à 2212 inscritos e no ultimo ano de 2025 foram registrados 1387 inscritos representando uma queda de (calcular a %)
Licenciatura: Na área da Licenciatura temos um pico de inscritos em 2003 equivalte à 7895 inscritos e no ultimo ano de 2025 foram registrados 1911 inscritos representando uma queda de (calcular a %)
Podemos perceber que essa queda geral é muito mais impactada pelos cursos de engenharia e educação por exemplo, se puxarmos uma linha média nos cursos da área de tecnologia e saúde, a inscrição de 2025 ainda fica acima da média:
<img width="709" height="395" alt="image" src="https://github.com/user-attachments/assets/58c25d2f-16ec-43c9-bc22-d108e92d74e7" />
Legenda: Média traçada no número de inscritos dos cursos da área da Saúde
<img width="714" height="394" alt="image" src="https://github.com/user-attachments/assets/060c2d80-2e70-4dcd-bd60-659cf8e92207" />
Legenda: Média traçada no número de inscritos dos cursos da área da Tecnologia

Motivos (melhorar titulo)
Algumas possívels causas dessa queda de inscritos é:
•	A situação precária das faculdades públicas, tem conhecido meu que consta a falta de lâmpadas nos corredores;
•	A desvalorização do mercado do trabalho, A falta de fiscalização do CREA por exemplo em vagas da Engenharia Civil acaba impactando diretamente na sensação de “Vale a pena estudar 5 anos para isso”
•	O aumento da concorrência com o ensino EAD privado
se puder melhorar aqui chat, colocar alguma noticia, algo assim 
Impactos no futuro (Melhorar o titulo)
A pergunta no final desse projeto que fica é, "Qual o impacto real disso no mercado de trabalho à longo prazo?" 
Ao natural, uma queda de concorrência (inscritos, candidato/vaga e nota de corte) acaba desqualificando os candidatos de modo geral, aumentando como consequência o indice de desistência, se entra alunos com a base menos sólida, a chance de não conclusão é alta. 














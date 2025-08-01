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

Resultado
Como esperado, os dados 




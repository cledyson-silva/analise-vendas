# Análise de Vendas – Python e Power BI

Este projeto apresenta uma análise de dados de vendas utilizando **Python** para exploração e resposta a perguntas de negócio, e **Power BI** para visualização interativa dos resultados.

Os dados utilizados são **fictícios**, com finalidade educacional e de portfólio.

---

## 🎯 Objetivo
Analisar o desempenho de vendas considerando:
- Faturamento
- Volume de vendas
- Desempenho por unidade
- Categorias e produtos
- Centros de vendas
- Desempenho de vendedores

O projeto busca apoiar a tomada de decisão por meio de métricas claras e análises consistentes.

---
## 📁 Estrutura do Projeto
- `data/` → base de dados utilizada  
- `python/` → script de análise em Python  
- `powerbi/` → arquivo do dashboard  
- `images/` → imagem utilizada no README  
---

## 🧩 Tecnologias Utilizadas
- **Python** (pandas, numpy)
- **Power BI**
- **Excel** (base de dados)
- **Git/GitHub**

---

## 🐍 Análise em Python
O script em Python realiza o tratamento dos dados e responde perguntas de negócio como:

- Qual o faturamento total por unidade?
- Qual unidade teve o maior valor de vendas?
- Qual produto foi mais vendido em determinada unidade?
- Quem foi o vendedor com maior faturamento?
- Qual o faturamento por categoria em cada centro de vendas?
- Qual a participação percentual de cada categoria no faturamento total?
- Quais vendedores tiveram menor desempenho?
- Qual a média de itens vendidos por registro em cada unidade?
- Comparação entre produtos líderes por centro de vendas considerando a diferença percentual para o segundo colocado.

---

## 📊 Dashboard no Power BI
O dashboard apresenta uma visão consolidada das vendas, com foco em:

- Receita Total  
- Número de Vendas  
- Quantidade Total Vendida  
- Receita por Unidade  
- Vendas por Categoria  
- Top Produtos por Faturamento  
- Tendência de Vendas ao longo do tempo  

![Dashboard](images/dashboard.png)

---

## 🚀 Como executar a análise em Python
1. Clone o repositório:
```bash
git clone https://github.com/cledyson-silva/analise-vendas.git
```
2. Instale as dependências:
```bash
pip install -r requirements.txt
```
3. Execute o script:
```bash
python python/analise_vendas.py
```
## 📌 Considerações Finais

Este projeto foi desenvolvido com foco em:
- Organização do código
- Clareza das análises
- Uso adequado das métricas de acordo com os dados disponíveis
- Integração entre análise em Python e visualização em Power BI

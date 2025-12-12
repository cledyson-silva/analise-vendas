import pandas as pd

# Caminho para o arquivo
df = pd.read_excel('data/base_dados.xlsx')

# Tratamento de dados
df['Data_compra'] = pd.to_datetime(df['Data_compra'], dayfirst=True, errors='coerce')
df['Valor Unitário'] = pd.to_numeric(df['Valor Unitário'].astype(str).str.replace(',', '.'),errors='coerce')

# Visualizar os dados
print(df.head(20))

#1) Qual é a soma do valor total de vendas (em R$) agrupada por unidade, desconsiderando registros inválidos?
# Agrupa as vendas por unidade e soma o valor total
total_unidade = df.groupby("Unidade")["Valor Total"].sum().reset_index()

# Ordena o valor total de cada unidade do maior para o menor
total_unidade = total_unidade.sort_values(by='Valor Total', ascending=False)

# Converte para string formatada com 2 casas decimais para impressão
total_unidade_str = total_unidade.to_string( index=False,
        formatters={'Valor Total': 'R${:,.2f}'.format,})

print(f"RESPOSTA QUESTÃO 1:\n{total_unidade_str}")

#2) Qual foi a unidade com o maior valor total de vendas, qual foi o produto mais vendido (em quantidade) nessa unidade e qual foi o valor total de vendas dessa unidade?
# Agrupa o valor total por unidade
df_total_unidade = df.groupby("Unidade")["Valor Total"].sum()

# Identifica a unidade com o maior valor total de vendas
unidade_maior_venda = df_total_unidade.idxmax()

# Obtém o valor total de vendas da unidade com maior valor
valor_total_maior_venda = df_total_unidade.max()

# Filtra o DataFrame para conter apenas os dados da unidade com maior valor de vendas
df_unidade_maior_venda = df[df['Unidade'] == unidade_maior_venda]

# Soma a quantidade vendida de cada produto da unidade
produtos_qtd_total = df_unidade_maior_venda.groupby("Produto")["Qtd"].sum()

# Identifica o produto mais vendido e a quantidade
produto_mais_vendido = produtos_qtd_total.idxmax()
produto_mais_vendido_qtd = produtos_qtd_total.max()

print(f"RESPOSTA QUESTÃO 2:\nUnidade com o maior valor total de vendas: {unidade_maior_venda}")
print(f"Produto mais vendido: {produto_mais_vendido}")
print(f"Quantidade vendida: {produto_mais_vendido_qtd}")
print(f"Valor total de vendas da unidade: R${valor_total_maior_venda:,.2f}")

#3) Qual foi o vendedor com o maior total de vendas (em R$) e quanto ele vendeu?
# Agrupa por vendedor e soma o valor total
total_por_vendedor = df.groupby("Cod_vendedor")["Valor Total"].sum()

#Encontra o vendedor com o maior total de vendas
melhor_vendedor = total_por_vendedor.idxmax()
total_vendas_melhor_vendedor = total_por_vendedor.max()

print(f"RESPOSTA QUESTÃO 3:\nVendedor com o maior total de vendas: {melhor_vendedor}")
print(f"Valor total de vendas: R${total_vendas_melhor_vendedor:,.2f}")

#4) Liste o faturamento por categoria em cada centro de vendas.
# Agrupa os dados por centro e Categoria e soma o valor total
faturamento_categoria = df.groupby(['Centro', 'Categoria'])['Valor Total'].sum().reset_index()

# Ordena os resultados para melhor visualização
faturamento_categoria_str = faturamento_categoria.sort_values(by=['Centro', 'Valor Total'], ascending=[True, False]).to_string(index=False,
      formatters={'Valor Total': 'R${:,.2f}'.format})

print(f"RESPOSTA QUESTÃO 4:\n{faturamento_categoria_str}")

#5) Qual foi o centro de vendas com o maior ticket médio (valor total médio por compra) e qual foi o valor desse ticket médio?
# Calcula o ticket médio de cada centro de vendas
ticket_centro = df.groupby('Centro')['Valor Total'].mean()

# Identifica o centro com o maior ticket médio
centro_max = ticket_centro.idxmax()
ticket_max = ticket_centro.max()

print(f"RESPOSTA QUESTÃO 5:\nCentro de vendas com o maior ticket médio: {centro_max}")
print(f"Valor do ticket médio: R${ticket_max:,.2f}")

#6) Qual foi a unidade com o maior número de vendas, qual a categoria mais vendida dentro dessa unidade, qual foi o produto mais vendido dentro dessa categoria e quantas unidades desse produto foram vendidas?
# Conta o número de vendas(transações) por unidade
unidade_count_vendas = df.groupby('Unidade')['Valor Total'].count()

# Identifica a unidade com o maior número de vendas
unidade_vendas_max = unidade_count_vendas.idxmax()
unidade_vendas_total = unidade_count_vendas.max()

# Conta o total de quantidade vendida por unidade
unidade_qtd_vendas = df.groupby('Unidade')['Qtd'].sum()

# Identifica o total de quantidade vendida da unidade com maior número de vendas
unidade_qtd_max = unidade_qtd_vendas.max()

# Filtra os dados apenas da unidade com maior número de vendas
df_unidade_vendas_max = df[df['Unidade'] == unidade_vendas_max]

# Dentro dessa unidade, soma a quantidade de itens vendidos por categoria
categoria_soma = df_unidade_vendas_max.groupby('Categoria')['Qtd'].sum()

# Identifica a categoria mais vendida
categoria_max = categoria_soma.idxmax()

# Filtra apenas os registros da categoria mais vendida
df_categoria_max = df_unidade_vendas_max[df_unidade_vendas_max['Categoria'] == categoria_max]

# Dentro dessa categoria, soma a quantidade vendida por produto
produto_soma = df_categoria_max.groupby('Produto')['Qtd'].sum()

# Identifica o produto mais vendido e sua quantidade
produto_max = produto_soma.idxmax()
produto_max_qtd = produto_soma.max()

print(f"RESPOSTA QUESTÃO 6:\nUnidade com o maior número de vendas: {unidade_vendas_max}")
print(f"Total de vendas(transações): {unidade_vendas_total}")
print(f"Total de vendas(unidades vendidas): {unidade_qtd_max}")
print(f"Categoria mais vendida: {categoria_max}")
print(f"Produto mais vendido: {produto_max}")
print(f"Unidades vendidas: {produto_max_qtd}")

#7) Se considerarmos o produto com o maior valor total de vendas em cada centro, qual deles, entre esses vencedores locais, possui a maior diferença percentual em relação ao segundo colocado no seu respectivo centro?
# Calcula o faturamento total por produto em cada centro
faturamento_produto_centro = df.groupby(['Centro', 'Produto'])['Valor Total'].sum().reset_index()

# Ordena os produtos pelo faturamento dentro de cada centro
faturamento_produto_centro = faturamento_produto_centro.sort_values(by=['Centro', 'Valor Total'], ascending=[True, False])

# Cria uma função para calcular a diferença percentual entre os dois primeiros
def calcular_diferenca_percentual(grupo):
    # Verificar se há pelo menos dois produtos no grupo
    if len(grupo) < 2:
        return None, None, None, None, None, None, None

    # Obtém os dois primeiros (campeão e vice)
    campeao = grupo.iloc[0]
    vice = grupo.iloc[1]

    # Calcula a diferença percentual
    valor_campeao = campeao['Valor Total']
    valor_vice = vice['Valor Total']

    if valor_vice == 0: # Evita divisão por zero
        diferenca_percentual = float('inf')
    else:
        diferenca_percentual = ((valor_campeao - valor_vice) / valor_vice) * 100
    
    return campeao['Produto'], vice['Produto'], diferenca_percentual, valor_campeao, valor_vice, campeao['Centro']

# Aplica a função para cada centro
resultados = []
for centro_id, grupo in faturamento_produto_centro.groupby('Centro'):
    campeao, vice, diferenca, valor_campeao, valor_vice, centro = calcular_diferenca_percentual(grupo)
    if diferenca is not None:
        resultados.append({'Centro': centro, 'Produto Campeão': campeao, 'Valor Campeão': valor_campeao, 'Valor Vice': valor_vice, 'Produto Vice': vice, 'Diferença Percentual': diferenca})

# Converte a lista de resultados em um DataFrame
df_resultados = pd.DataFrame(resultados)

# Encontra o centro com a maior diferença percentual
resultado_final = df_resultados.loc[df_resultados['Diferença Percentual'].idxmax()]

print("RESPOSTA QUESTÃO 7:")
print(f"Centro onde o produto campeão de vendas teve a maior liderança sobre o segundo colocado: {resultado_final['Centro']}")
print(f"Produto campeão: {resultado_final['Produto Campeão']}")
print(f"Valor: R${resultado_final['Valor Campeão']:,.2f}")
print(f"Segundo colocado: {resultado_final['Produto Vice']}")
print(f"Valor: R${resultado_final['Valor Vice']:,.2f}")
print(f"Diferença percentual para o segundo colocado foi de {resultado_final['Diferença Percentual']:.2f}%.")

#8) Determine o percentual de vendas de cada categoria em relação ao total de vendas.
# Agrupa as vendas por categoria e soma o total de vendas de cada uma
vendas_categoria = df.groupby('Categoria')['Valor Total'].sum()

# Calcula o total geral de vendas
total_geral_vendas = df['Valor Total'].sum()

# Calcula o percentual que cada categoria representa do total geral
percentual_categoria = (vendas_categoria / total_geral_vendas) * 100

# Ordena as categorias do maior para o menor percentual
percentual_por_categoria = percentual_categoria.sort_values(ascending=False)

print("RESPOSTA QUESTÃO 8:")
for categoria, percentual in percentual_por_categoria.items():
    print(f"{categoria}: {percentual:.2f}%")
    
#9) Liste os 5 vendedores com menor desempenho (em valor total de vendas).
# Agrupa os dados pelo código do vendedor e soma o total de vendas de cada um
vendedor_desemp = df.groupby('Cod_vendedor')['Valor Total'].sum().reset_index()

# Ordena os vendedores pelo valor total de vendas do menor para o maior
vendedor_desemp = vendedor_desemp.sort_values(by=['Valor Total'])

# Seleciona os 5 vendedores com menor desempenho
vendedores_menor_desemp = vendedor_desemp.head(5)

print(f"RESPOSTA QUESTÃO 9:\nOs 5 vendedores com menor desempenho:\n{vendedores_menor_desemp.to_string(index=False,
      formatters={'Valor Total': 'R${:,.2f}'.format})}")

#10) Qual a média de produtos vendidos por venda (Qtd) em cada unidade?
# Agrupa os dados por unidade e calcula a média da quantidade 'Qtd' para cada unidade
produto_unidade = df.groupby('Unidade')['Qtd'].mean().reset_index()

# Ordena os resultados pelo valor da média (Qtd) do maior para o menor
produto_unidade_str = produto_unidade.sort_values(by=['Qtd'], ascending=False).to_string(index=False,
      formatters={'Qtd': '{:.2f}'.format})

print(f"RESPOSTA QUESTÃO 10:\n{produto_unidade_str}")

'''
Gabarito:

1) Cidade Nova: R$47.118.863,75
Avenida: R$46.171.965,23
Amazonas Shopping: R$45.918,047.41
Camapuã: R$43.217.705,93
Eduardo Gomes: R$42.393.843,19
Nova Cidade: R$39.616.146,37

2) Unidade: Cidade Nova
Produto: Fogão
Quantidade: 1251
   
3) Vendedor: 19876 - Carla
Total: R$54.464.731,26
   
4) Centro: 101
Categoria: Eletrodomésticos
Valor Total: R$ 11.478.075,36

Centro: 101
Categoria: Móveis
Valor Total: R$ 11.232.100,12

Centro: 101
Categoria: Eletroportáteis
Valor Total: R$ 10.358.725,07

Centro: 101
Categoria: Informática
Valor Total: R$ 10.282.672,68

Centro: 102
Categoria: Móveis
Valor Total: R$ 11.358.137,41

Centro: 102
Categoria: Eletroportáteis
Valor Total: R$ 11.113.009,04

Centro: 102
Categoria: Informática
Valor Total: R$ 10.837.941,96

Centro: 102
Categoria: Eletrodomésticos
Valor Total: R$ 9.846.743,23

Centro: 103
Categoria: Informática
Valor Total: R$ 11.853.326,19

Centro: 103
Categoria: Eletroportáteis
Valor Total: R$ 11.637.546,17

Centro: 103
Categoria: Eletrodomésticos
Valor Total: R$ 10.409.549,06

Centro: 103
Categoria: Móveis
Valor Total: R$ 9.916.149,23

Centro: 104
Categoria: Eletrodomésticos
Valor Total: R$ 12.219.762,60

Centro: 104
Categoria: Eletroportáteis
Valor Total: R$ 11.970.944,36

Centro: 104
Categoria: Informática
Valor Total: R$ 10.965.105,94

Centro: 104
Categoria: Móveis
Valor Total: R$ 10.700.637,80

Centro: 105
Categoria: Eletroportáteis
Valor Total: R$ 11.775.586,10

Centro: 105
Categoria: Eletrodomésticos
Valor Total: R$ 11.729.076,87

Centro: 105
Categoria: Informática
Valor Total: R$ 11.095.691,57

Centro: 105
Categoria: Móveis
Valor Total: R$ 10.052.931,45

Centro: 106
Categoria: Móveis
Valor Total: R$ 11.877.253,92

Centro: 106
Categoria: Eletroportáteis
Valor Total: R$ 10.879.598,11

Centro: 106
Categoria: Eletrodomésticos
Valor Total: R$ 10.555.314,47

Centro: 106
Categoria: Informática
Valor Total: R$ 10.290.693,17

5) Centro: 104
Valor do ticket médio: R$27.117,95

6) Unidade: Avenida
Total de vendas(transacões): 1.757
Total de vendas(quantidade): 18.740
Categoria: Informática
Produto: Impressora
Quantidade: 900

7) Centro: 104
Produto: Fogão
Valor: R$3.587.791,62
Segundo: Sofá
Valor total segundo colocado: R$2.867.268,45
Diferença percentual: 25.13%

8) Eletroportáteis: 25.61%
Eletrodomésticos: 25.05%
Informática: 24.70%
Móveis: 24.63%

9) Fernando: R$50,405,265.51
Patrícia: R$52,241,055.11
João: R$52,934,601.07
Luciana: R$54,390,918.93
Carla: R$54,464,731.26

10) Cidade Nova: 10.91
Avenida: 10.67
Amazonas Shopping: 10.60
Eduardo Gomes: 10.54
Nova Cidade: 10.43
Camapuã: 10.37
'''
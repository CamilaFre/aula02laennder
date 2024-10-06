import pandas as pd

tabela_cliente = pd.read_csv("clientes.csv")
tabela_venda = pd.read_csv("vendas.csv")
tabela_venda_2 = pd.read_csv("vendas_2.csv")
tabela_venda_3 =pd.read_csv("vendas_3.csv")

print(tabela_cliente.head())
print(tabela_venda.head())
print(tabela_venda_2.head())
print(tabela_venda_3.head())

df_concat = pd.concat([tabela_venda, tabela_venda_2, tabela_venda_3])
print(df_concat)

df_unionall = pd.merge(df_concat,tabela_cliente, on = "cliente_id")


df_unionall["valor_total"] = df_unionall["quantidade"]*df_unionall["valor_unitario"]

from ydata_profiling import ProfileReport
profile = ProfileReport(df_unionall, title="Profiling Report")
profile.to_file("relatorios_vendas_v5.html")

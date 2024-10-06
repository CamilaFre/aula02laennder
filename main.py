
import pandas as pd

df_pessoas2= pd.read_excel("exemplo.xlsx")

print(df_pessoas2)

lista_de_numeros = [20,8,23,25,7,50,10,28,17,28,15,54,37]
lista_de_numeros2 = [20,8,23,25,7,50,10]
lista_de_numeros3 = [4,5,6]

lista_tipo_series = pd.Series(lista_de_numeros)
print(lista_tipo_series.describe())

print(type(lista_de_numeros))
print(type(lista_tipo_series))

# %%

print(lista_tipo_series.median())
print(lista_tipo_series.mode())
print(lista_tipo_series.mean())
print(lista_tipo_series.std())
print(lista_tipo_series.max())
print(lista_tipo_series.min())

forma = lista_tipo_series.shape[0]
print(f"Forma da Série:{forma}")

serie_nomes = pd.Series(["Ana", "Bruno","Carla","David"])
serie_sobrenomes = pd.Series(["Silva", "Oliveira","Santos","Costa"])
serie_idades = pd.Series([23,29,31,25])
df_pessoas = pd.DataFrame({"nome":serie_nomes, "sobrenome":serie_sobrenomes,"idade":serie_idades})
print(df_pessoas)
print(df_pessoas["idade"].median())
print("começamos a nossa aula 02")

lista_de_numeros = [20,8,23,25,7,50,10,28,17,28,15,54,37]
lista_de_numeros2 = [20,8,23,25,7,50,10]
lista_de_numeros3 = [4,5,6]
def calcular_media (lista_para_somar: list) -> float:
    soma = 0
    for item in lista_para_somar:
        soma = soma + item
    media_da_lista = soma/len(lista_para_somar)

    return media_da_lista

media_1 = calcular_media(lista_de_numeros)
media_2 = calcular_media(lista_de_numeros2)
media_3 = calcular_media(lista_de_numeros3)

print(media_1)
print(media_2)
print(media_3)
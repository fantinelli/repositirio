def media(lista):
    soma = sum(lista)
    quantidade = len(lista)
    return soma / quantidade

numeros = [2, 4, 6, 8, 10]
resultado = media(numeros)
print(resultado)  # Saída: 6.0

nota1 = int(input("qual foi sua primeira nota:"))
nota2 = int(input('qual foi seua segunda nota:'))
resultado= (nota1 + nota2)
media = (resultado / 2)

if(media > 7):
    print('aprovado')
elif(media < 7):
    print('reprovado')
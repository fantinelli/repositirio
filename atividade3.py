

nome = str(input('qual o seu nome?'))
if nome == 'gustavo':
    print('que nome bonito')
elif nome == 'filipe' or nome == 'maria' or nome == 'fanfan':
    print('seu nome é bem popular no brasil')
else:
    print('seu nome é bem normal.')
print('tenha um bom dia {}'.format(nome))
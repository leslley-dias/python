# Dicionario

# time_favorito = {'Joao':'Corintians',
#                  'Rafael':'Cruzeiro',
#                  'Camila':'Palmerense'}


# carros = {'modelo':{'Honda Fit': 
#                                {'Cor':'branco',
#                                 'Motor':1.5,
#                                 'ano':2015}
#                                 },
#          'modelo02':{'Fiat Uno':{'cor':'prata',
#                                  'Motor':1.0,
#                                   'ano':2011}
#                                 }
# }


# # print(carros.keys())
# # print(carros.value())
# print(carros['modelo02']['Fiat Uno']['Motor'])



# dados = {
#     'estados':{
#         'sp':{
#             'nome':'São Paulo',
#             'municipios': 645,
#             'populacao': 44.04
#         },
#         'rj':{
#             'nome':'Rio de Janeiro',
#             'municipios': 92,
#             'populacao': 16.72
#         },
#         'mg':{
#             'nome': 'Minas Gerais',
#             'municipios': 31,
#             'populacao': 20.87
#         }
#     }
# }


# dados = {
#     'estados':{
#         'sp':{
#             'nome':'São Paulo',
#             'municipios': 645,
#             'populacao': 44.04
#         },
#         'rj':{
#             'nome':'Rio de Janeiro',
#             'municipios': 92,
#             'populacao': 16.72
#         },
#         'mg':{
#             'nome': 'Minas Gerais',
#             'municipios': 38,
#             'populacao': 20.87
#         }
#     }
# }

# nome_sp = dados['estados']['sp']['nome']
# nome_rj = dados['estados']['rj']['nome']
# nome_mg = dados['estados']['mg']['nome']
           
# print('nome:{}\n: {}' .format(nome_sp))
# print('nome:{}\n: {}' .format(nome_rj))
# print('nome:{}\n: {}' .format(nome_mg))

# populacao_sp = dados['estados']['sp']['populacao']
# populacao_rj = dados['estados']['rj']['populacao']
# populacao_mg = dados['estados']['mg']['populacao']


# print('nome:{}\nPopulacao: {} milhoes'.format(nome_sp,populacao_sp))
# print('nome:{}\nPopulacao: {} milhoes'.format(nome_rj,populacao_rj))
# print('nome:{}\nPopulacao: {} milhoes'.format(nome_mg,populacao_mg))

# municipios_sp = dados['estados']['sp']['municipios']
# municipios_rj = dados['estados']['rj']['municipios']
# municipios_mg = dados['estados']['mg']['municipios']

# print('nome:{}\nmunicipios: {} milhoes'.format(nome_sp,municipios_sp))
# print('nome:{}\nmunicipios: {} milhoes'.format(nome_rj,municipios_rj))
# print('nome:{}\nmunicipios: {} milhoes'.format(nome_mg,municipios_mg))


# # idade = int(input('Digite sua idade: '))

# # if idade >= 18:
# #     print('vocẽ pode dirigir')
# # elif idade <= 0:
# #     print(erro)   
# # else: 
# #     print('vocẽ não pode dirigir')


# #Exercicio
# # software de imposto de renda
# # peça ao usuario o valor do salario mensal
# # se o salario for maior ou igual que 4600, a aliquota é de 27
# # se o salario for menor 4600 e maior que 3700, a aliquota é de 22
# # se o salario for menor 3700 e maior que 2800, a aliquota é de 15
# # se o salario for menor que 2800, aliquota é 0

# # valor = salario * (aliquota / 100.0)

# salario = float(input('Digite seu salario: '))
# if salario >= 4600:
#      aliquota = 27
# elif 
#     salario < 4600 and salario > 3700
#      aliquota = 22
# elif 
#     salario < 3700 and salario > 2800
#      aliquota = 15
# else: 
#     aliquota = 0 

# valor_aliquota = salario * (aliquota/100.0)

# print('O salario bruto é de: R$(')




#repetição

# x = 1
# while x < 10: 
#     print('Número: {}'.format(x))
#     x += 1
# print('O while acabou')


# frutas = ['banana','maça','uva','caju']

# for f in frutas: 
#     print(f)

# for i in range(1, 500): 
#     print('i agora é {}'.format(i))


# lista = []

# for num in range(20):
#   if num % 2 == 0:
#     continue
# else:
#  lista.append(num)

# print(lista)


# users = ['maria','carlos','pedro']
# login = input('Digite seu usuario: ')

#     if login in users: 
#         print('acesso permitido!')
#         break
#     else: 
#         print('Acesso negado!')
#         break

# try:
#     a = int(input('Digite um numero: '))
#     b - int(input('Digite outro numero: '))
#     print("a/b = {}".format(a/b))
#     print("a+b = {}".format(a+b))

#     except ValueError: 
#         print('Valor incorreto')

#     except ZeroDivisionError:
#         print('Valor incorreto')

#     except Exception:
#         print('Erro desconhecido')    



# usuarios = ['ana','carlos','maria','luis','paulo','leovandison']

# while True: 
#     try: 
#         login = input('Digite seu usuario: ')
        
#         if login.lower() not in usuarios:
#              raise NameError('Usuario não cadastrado!')
#         else:
#             print('Bem vindo(a) {}'.format(login.capitalize()))
#             break
#         except NameError as n:
#             print(n)    

# try: 
#     v = int(input('Digite um valor: ')) 
#     if v < 1: 
#         raise ValueError('v não pode ser menor que 10')
#     else:
#         print('OK')
# except ValueError as v: 
#     print ('v')














        
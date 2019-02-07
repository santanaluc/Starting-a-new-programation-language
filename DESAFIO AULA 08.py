import math
n = float(input('digite um número: '))
i = math.trunc(n)
print('o numero {} tem como parte inteira {:.0f}'.format(n, i))

import math
print('Fazer um programa que lê o comprimento do cateto oposto e do cateto adjacente de um triangulo retangulo,'
      'calcule e mostre o comprimento da hipotenusa')
co = int(input('Digite o cateto oposto: '))
ca = int(input('Digite o cateto adjacente: '))
k = math.hypot(co, ca)
print('Com cateto oposto = {} \nCateto adjacente = {} \nA hipotenusa é igual a {}'.format(co, ca, k))

print('Ler angulo e mostrar o valor do seno, cosseno e tangente desse angulo')
ang = float(input('Digite o angulo para descobrir o seno, cosseno e a tangente: '))
rad=math.radians(ang)
a=math.asin(math.radians(ang))
b=math.cos(math.radians(ang))
c=math.atan(math.radians(ang))
print('Com base no angulo ({})\nSeu seno é igual a {:.3f}\nSeu cosseno é igual a {:.3f}\n e sua tangente é igual a {:.3f}'
      ''.format(ang, a, b, c))

#import random
# #assert isinstance(choice, object)
import random
print('lista para sorteio de nomes')
nome1=input('nome: ')
nome2=input('nome: ')
nome3=input('nome: ')
nome4=input('nome: ')
nome5=input('nome: ')
lista = [nome1, nome2, nome3, nome4, nome5]
#escolhido = random.choice(lista)
sorteado = random.choice(lista)
print('o nome sorteado foi: {}'.format(sorteado))

import random
print('ordem de apresentação de trabalho: ')
g1=str(input('Grupo 1: '))
g2=str(input('Grupo 2: '))
g3=str(input('Grupo 3: '))
g4=str(input('Grupo 4: '))
lista=[g1, g2, g3, g4]
random.shuffle(lista)
print('A sequencia de grupos será: {}'.format(lista))



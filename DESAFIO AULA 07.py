print('Olá, irei identificar o número antecessor e o sucessor que você escolher')
n1=int(input('digite um valor: '))
a=n1-1
s=n1+1
print ('o número é: {}, seu antecessor é igual a: {} e o sucessor é igual a: {} '.format(n1, a, s))

print('Agora vamos ver o dobro, e triplo e a raiz quadrada de um número')
n2=int(input('digite um número qualquer: '))
d=n2*n2
t=n2*n2*n2
r=n2**0.5
print('o número = {} \ntem o seu dobro = {} \ncom o seu triplo = {} \ne a sua raiz quadrada = {:.3f}'
      ''.format(n2, d, t, r))
from itertools import repeat

print('Now, lets go to calculate your final note')
#n3=int(input('Quantas provas você fez durante o semestre? '))
n4=float(input('Qual foi sua nota da prova 1? '))
n5=float(input('Qual foi a sua nota na prova 2? '))
m=n4*0.5+n5*0.5
print('com base nas notas da p1 ({}) e da p2 ({}), sua média será {:.2f}'.format(n4, n5, m))

print('Conversor de unidade de metros para centimetros e milímetros')
n7=float(input('Digite um número em metros: '))
cm=n7*100
mm=n7*1000
print('O número {} metros \nequivale a {} centimetros \ne {} milímetros'.format(n7, cm, mm))

#print('Tabuada do {}'.format(num))
num=int(input('Qual numero para formação da tabuada? '))
a=num*1, num*2, num*3, num*4, num*5, num*6, num*7, num*8, num*9, num*10
print('tabuada do: {} começando do 1 ao 10 \n{}'.format(num,a))

print('Vamos descobrir quanto de dinheiro você pode comprar com o que tem na carteira: ')
n9=float(input('Quanto de dinheiro você tem na carteira?'))
conversão=n9/3.29
print('Com base no quanto você tem ({} reais), pode-se comprar {:.2f} dolares'.format(n9, conversão))

print('Qual a quantidade de tinta para pintar a sua casa? ')
n11=int(input('Qual a largura da parede? '))
n12=int(input('Qual a altura da parede? '))
area=n11*n12
lt=area/2
print('Calculando... \nVocê precisará de {:.0f} litros de tinta para pintar sua casa'.format(lt))

print('Liquidação de uma loja com 5% de desconto')
n39=float(input('Quanto está a peça que você vai comprar? '))
#p=n39/0.05
h=n39-(n39*0.05)
print('Com 5% de desconto, essa peça fica {:.2f} reais '.format(h))

print('Calculando o salário de um funcionário com 15% de aumento')
n32=float(input('Salário do funcionário = '))
sal=n32+(n32*0.15)
print('O funcionário recebendoo {} reais. \nCom 15% de aumento no salário, passará a receber {} reais '
      .format(n32, sal))
print('Olá, iremos calcular o quanto voce gastará na próxima viagem:')
n4=input('Você viajará de carro ou moto? ')
n1=float(input('Quantos KM/L faz o seu(a) {}? '.format(n4)))
n2=float(input('sua viagem será de quantos kilometros? '))
n3=float(input('quanto voce pagará no litro da gasolina/alcool do carro (em média)? '))
res=n1/n3*n2  # type: float
print('com base nos dados, com o(a) {} fazendo {}km/l e andando {}km o seu gasto será de {} na sua próxima viagem'
      .format(n4, n1, n2, res))
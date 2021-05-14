segundos = int(input('Por favor, entre com o número de segundos que deseja converter: '))
a = segundos//86400
resto1 = segundos%86400
b = resto1//3600
minutos = resto1%3600
c = minutos//60
d = minutos%60
print(a, ' dias,', b, ' horas,', c, ' minutos', ' e ', d, 'segundos')

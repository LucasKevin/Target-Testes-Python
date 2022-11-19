#Exercio 2#
print('Exercício 2')
print ('-' *30)
print (' ' *3, 'Sequência de Fibonacci ')
print ('-' *30)

Valor = int(input('Insira um número para ver a Sequência de Fibonacci : '))
a = 0
b = 1

print ('{} → {}'.format(a, b), end='')
Contador = 3

while Contador <= Valor:
   n = a + b
   print (' → {}'.format(n), end='')

   a = b
   b = n

   Contador += 1

n = int(input('\nDigite o mesmo numero para saber se faz parte da sequência de Fibonacci: '))
a, b = 0, 1
while a < n:
    a, b = b, a + b
print(a == n)
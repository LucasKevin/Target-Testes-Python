#exercicio 5#

print('\nExercício 5')

frase = input('\n Digite uma frase: ')
print(' Você digitou: {}'.format(frase))
invertida = ' '.join(palavra[::-1] for palavra in frase.split())
print('A frase que você digitou invertida fica: {}'.format(invertida))
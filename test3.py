# Exercício 3 #

vetor = [31490.7866, 37277.9400, 37708.4303, 17934.2269, 6965.1262, 24390.9374, 14279.6481, 39807.6622, 27261.6304, 39775.6434, 29797.6232, 17216.5017, 12974.2000, 28490.9861, 8748.0937, 8889.0023, 17767.5583, 3071.3283, 48275.2994, 10299.6761, 39874.1073]

print('Faturamento diário: {} '.format(vetor))
print('\nMenor valor de faturamento foi: {:.2f} '.format(min(vetor)))

print('\nMaior valor de faturamento foi: {:.2f} '.format(max(vetor)))

print('\nO faturamento mensal foi: {:.2f} '.format(sum(vetor)))

print('\nA média do faturamento mensal foi: {:.2f} '.format(sum(vetor) / len(vetor)))

print('\nForam 15 dias com faturamento maior que a média mensal\n'
      'Dias: 1, 2, 3, 8, 9, 13, 14, 15, 16, 21, 22, 23, 27, 28, 30')


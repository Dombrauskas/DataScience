from scipy.stats import binom, poisson
from scipy.special import comb

'''
p = Probabilidade de sucesso
n = Quantidade de teste (Repetições)
k = Resultado Almejado
q = 1 - p -> Fracassos
'''

# Combinações -> n! / (k! * (n - k)!)
n = 60
k = 6
combinacoes = int(comb(n, k))
print(f'Combinações possível na loteria: {combinacoes:,d}')
# Combinações

# Probabilidade de acerta 5 questões em 10 com 3 alternativas cada.
# Combinações * (p ** k) * (q ** (n - k))
p = 1/3
n = 10
k = 5
prova = binom.pmf(k, n, p)
print('Chance de acertar 5 questões', prova)
#

# Média: a probabilidade de um casal ter filhos com olhos azuis seja de 22%.
# Em 50 famílias, com 3 filhos cada, quantas podemos esperar que tenham 2 filhos com olhos azuis?
p = 0.22  # Possibilidade de ter olhos azuis
n = 3     # Quantidade de filhos de um casal
k = 2     # Espera-se que 2 tenham olhos azuis
F = 50    # Total de famílias

olhos_azuis = binom.pmf(k, n, p)
print(f'Famílias com 2 filhos com olhos azuis: {round(olhos_azuis * F)}')
#


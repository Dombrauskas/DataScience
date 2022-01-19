from scipy.stats import norm


'''
O faturamento diário de um motorista de aplicativo segue uma distribuição 
aproximadamente normal, com média R$ 300,00 e desvio padrão igual a R$ 50,00. 
Obtenha as probabilidades de que, em um dia aleatório, o motorista ganhe:
'''

# 1) Entre R$ 250,00 e R$ 350,00
media = 300
std_d = 50
Z_superior = (350 - media) / std_d
Z_inferior = (250 - media) / std_d

probabilidade_1 = norm.cdf(Z_superior) - norm.cdf(Z_inferior)
print(f'Probabilidade de ganhar entre R$ 400 e R$ 500: {probabilidade_1 * 100:.4f}%')


# 2) Entre R$ 400,00 e R$ 500,00
media = 300
std_d = 50
Z_superior = (500 - media) / std_d
Z_inferior = (400 - media) / std_d

probabilidade_2 = norm.cdf(Z_superior) - norm.cdf(Z_inferior)
print(f'Probabilidade de ganhar entre R$ 400 e R$ 500: {probabilidade_2 * 100:.4f}%')



from scipy.stats import poisson

'''
Uma padaria recebe 20 clientes por hora. 
Qual a probabilidade de uma hora qualquer entrarem 25 clientes.
'''

media = 20  # Média de uma hora.
k = 25      # Quantidade desejada.

p = poisson.pmf(k, media)
print(f'{p * 100:.4f}%')


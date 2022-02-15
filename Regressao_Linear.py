import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


# Importando o dataset.
# Importing dataset.
dados = pd.read_csv(Consumo_cerveja.csv, sep=';')
# dados.rename_axis('índice', axis=1, inplace=True)


# Verificando o tamanho do dataset - (linhas, colunas).
# Checking the size of the dataset - (rows, columns).
print(dados.shape)

print(dados.corr().round(4))

fig, ax = plt.subplots(figsize=(20, 6))
ax.set_title('Consumo de Cerveja', fontsize=20)
ax.set_ylabel('Litros', fontsize=16)
ax.set_xlabel('Dias', fontsize=16)
ax = dados['consumo'].plot(fontsize=14)
plt.show()

sns.boxplot(data=dados['consumo'], orient='v', width=0.2)
plt.show()

# Boxplot de duas variáveis.
# Two variables on boxplot.
'''
sns.set_palette('Accent') # Configuração de cores
sns.set_style('darkgrid') # Configuração de cores
'''
ax = sns.boxplot(y='consumo', x='fds', data=dados, width=0.5)
ax.figure.set_size_inches(12, 6)
ax.set_title('Consumo de Cerveja', fontsize=20)
ax.set_ylabel('Litros', fontsize=14)
ax.set_xlabel('Dias', fontsize=14)
plt.show()

# Distruição de frequência: assume-se que a variável de dependência tenha distribuição normal.
# Frequency distribution: it is assumed that the dependant variable has a normal distribution.
ax = sns.displot(dados['consumo'])
ax.figure.set_size_inches(12, 6)
plt.show()


import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Criando o gráfico com vários tempos
data = {
    'Tamanho': [1, 1, 4, 4, 13, 13, 15, 15, 19, 19, 20, 20, 26, 26, 33, 33, 38, 38, 43, 43],
    'Tempo de Execução': [0.000005, 0.000003, 0.0000006, 0.0000008, 0.0000006, 0.000001, 0.0000004, 0.000001, 0.000001, 0.000001, 0.000004, 0.000001, 0.000001, 0.000001, 0.000001, 0.000001, 0.000001, 0.000001, 0.000008, 0.000001],
    'Algoritmo': ['TD', 'BU', 'TD', 'BU', 'TD', 'BU', 'TD', 'BU', 'TD', 'BU', 'TD', 'BU', 'TD', 'BU', 'TD', 'BU', 'TD', 'BU', 'TD', 'BU']  # Different algorithms or methods
}

# Criar Data Frame
df = pd.DataFrame(data)

# Criar Gráfico
plt.figure(figsize=(10, 6))
sns.barplot(data=df, x='Tamanho', y='Tempo de Execução', hue='Algoritmo', palette='viridis')


plt.xlabel('Tamanho')
plt.ylabel('Tempo de Execução')
plt.title('Gráfico de Tamanho vs. Tempo de Execução para Diferentes Algoritmos')

plt.tight_layout()
plt.show()
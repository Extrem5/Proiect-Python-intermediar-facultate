import pandas as pd
import matplotlib.pyplot as plt

## X=5 , Y=8 , Echipa E69

df = pd.read_csv('data.csv')

# 1. Toate valorile (Durata, Puls, MaxPuls, Calorii)
df.plot()
plt.title("Toate valorile")

# 2. Primele X=5 valori (Durata, Puls, Calorii)
df[['Durata', 'Puls', 'Calorii']].head(5).plot()
plt.title("Primele 5 valori")

# 3. Ultimele Y=8 valori (Durata si Puls, verde si albastru, marker diamant)
df[['Durata', 'Puls']].tail(8).plot(color=['green', 'blue'], marker='D')
plt.title("Ultimele 8 valori")

plt.show()
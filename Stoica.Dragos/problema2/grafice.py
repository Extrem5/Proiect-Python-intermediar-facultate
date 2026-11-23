import pandas as pd
import matplotlib.pyplot as plt

# X = 13 (Dragos Gabriel), Y = 6 (Stoica), Echipa E69
df = pd.read_csv("data.csv")

# 1. Toate valorile (Durata, Puls, MaxPuls, Calorii)
df.plot()
plt.title("Toate valorile")
plt.show()

# 2. Primele X=13 valori (Durata, Puls, Calorii)
df[["Durata", "Puls", "Calorii"]].head(13).plot()
plt.title("Primele 13 valori")
plt.show()

# 3. Ultimele Y=6 valori (Durata si Puls, albastru si galben, marker triunghi in sus)
df[["Durata", "Puls"]].tail(6).plot(color=["blue", "yellow"], marker="^")
plt.title("Ultimele 6 valori")
plt.show()

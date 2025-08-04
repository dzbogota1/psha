import pandas as pd
import matplotlib.pyplot as plt
import re

# 🔹 Ruta de archivo CSV
csv_file = "hazard_curve-mean-PGA_27.csv"

# 🔹 Leer CSV ignorando la primera línea de comentarios
df = pd.read_csv(csv_file, comment="#")

# 🔹 Extraer nombres de columnas PoE
poe_cols = [c for c in df.columns if c.startswith("poe-")]

# 🔹 Extraer los IMLs desde los nombres poe-<IML>
imls = [float(re.sub("poe-", "", c)) for c in poe_cols]

# 🔹 Tomar los PoE de la primera (y única) fila
poes = df.loc[0, poe_cols].values

# 🔹 Graficar curva
plt.figure(figsize=(7,5))
plt.plot(imls, poes, marker='o', label="PGA - Bogotá")
plt.xscale('log')
plt.yscale('log')
plt.xlabel("IML (g)")
plt.ylabel("PoE en 50 años")
plt.title("Curva de Amenaza Sísmica - Bogotá")
plt.grid(True, which="both", ls="--", lw=0.5)
plt.legend()
plt.show()

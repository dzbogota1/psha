import pandas as pd
import matplotlib.pyplot as plt
import re

# 🔹 Cargar el archivo
csv_file = "output-12-hazard_uhs-mean_27.csv"
df = pd.read_csv(csv_file, comment="#")

# 🔹 Extraer columnas de SA y PGA separadas por PoE
columns = [c for c in df.columns if "~" in c]

# Separar por PoE
poe_10_cols = [c for c in columns if c.startswith("0.100000~")]
poe_2_cols  = [c for c in columns if c.startswith("0.020000~")]

# Ordenar columnas por periodo (PGA se considera T=0)
def extract_T(name):
    if "PGA" in name:
        return 0.0
    return float(re.search(r"\((.*?)\)", name).group(1))

poe_10_cols = sorted(poe_10_cols, key=extract_T)
poe_2_cols  = sorted(poe_2_cols, key=extract_T)

# Obtener listas de periodos y valores
periods_10 = [extract_T(c) for c in poe_10_cols]
values_10  = [df[c].values[0] for c in poe_10_cols]

periods_2  = [extract_T(c) for c in poe_2_cols]
values_2   = [df[c].values[0] for c in poe_2_cols]

# 🔹 Graficar espectro
plt.figure(figsize=(7,5))
plt.plot(periods_10, values_10, marker='o', label="PoE=10% en 50 años")
plt.plot(periods_2, values_2, marker='s', label="PoE=2% en 50 años")
plt.xscale("log")
plt.yscale("log")
plt.xlabel("Periodo (s)")
plt.ylabel("Aceleración Espectral (g)")
plt.title("Uniform Hazard Spectrum - Bogotá")
plt.grid(True, which="both", ls="--", lw=0.5)
plt.legend()
plt.show()

import pandas as pd
from pathlib import Path

json_file = "C:/Users/gas_c/Downloads/games.json"
csv_file ="C:/Users/gas_c/Downloads/games_new.csv"

# Leer el JSON (pandas detecta automáticamente arrays de objetos)
df = pd.read_json(json_file)

# Guardar como CSV (UTF-8, con cabecera, sin índice extra)
df.to_csv(csv_file, index=False, encoding="utf-8")

print(f"Conversión completada: {csv_file}")

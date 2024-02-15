import pandas as pd

focus = pd.read_excel("Focus.xlsx", usecols = [
    "Codice a barre", "Marchio", "Modello", "Colore"
], sheet_name="Risultato")

shopify = pd.read_excel("tuo_file_modificato")

# merge de


#print(focus.columns)
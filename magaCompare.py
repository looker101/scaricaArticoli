import pandas as pd

focus = pd.read_excel("Focus.xlsx", usecols=[
    "Marchio", "Modello", "Colore", "Calibro", "Codice a barre", "Quantità"
])
#print(focus.columns)

ordini_looker = pd.read_excel("Order Status_2024.xlsx")
#print(ordini_looker.columns)

ordini_looker.rename(columns={"Barcode":"Codice a barre"}, inplace = True)
#print(ordini_looker.columns)

comapare = ordini_looker.merge(focus, on = "Codice a barre", how = "left", indicator=True)

comapare.to_excel("testCompare.xlsx", index=False)
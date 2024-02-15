import pandas as pd

def run_compare():
    focus = pd.read_excel("C:\\Users\\miche\\Desktop\\.py\\scaricaArticoli\\Focus.xlsx", usecols = [
        "Codice a barre", "Marchio", "Modello", "Colore"])
    shopify = pd.read_excel("C:\\Users\\miche\\Desktop\\.py\\scaricaArticoli\\tuo_file_modificato.xlsx", sheet_name="Risultato")
    # rinomino la colonna del file shopify - entrambi i file devono avere lo stesso nome per la colonna da "mergiare"
    shopify.rename(columns={"Barcode":"Codice a barre"}, inplace=True)
    # devo controllare se i prodotti usciti da shopify sono stati scaricati da focus
    # se il barcode del prodotto sarà presente in entrambi i file vuol dire che l'occhiale è stato scaricato
    test = shopify.merge(focus, how = "left", on = "Codice a barre", suffixes=("_shopify", "_focus"), indicator=True)
    salva = test.to_excel("C:\\Users\\miche\\Desktop\\.py\\scaricaArticoli\\compare.xlsx", index = False)
    return salva

if __name__ == "__main__":
    run_compare()

#print(focus.columns)
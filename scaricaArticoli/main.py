import pandas as pd

# FILE SHOPIFY ORDINI
# importo il file con gli ordini dove NON è compreso il barcode
#orders_file = str(input("Inserisci il nome del file degli ordini scaricato da Shopify: "))
shopify_orders = pd.read_csv("januaryOrders.csv", usecols = [
    "Name", "Fulfillment Status", "Fulfilled at", "Lineitem quantity", "Lineitem quantity",
    "Lineitem sku"])
# rinomino le colonne in modo da facilitare il "merge"
shopify_orders.rename(columns = {"Vendor":"Marchio", "Lineitem price":"Prezzo vendita"}, inplace = True)
# inserisco la colonna relativa ai codici a barre che lascerò vuota
shopify_orders["Codice a barre"] = ""

# FILE FOCUS
# imposto il file scaricato da Focus con le sole colonne di cui ho bisogno
# nel file c'è la colonna dei codici a barre
focus = pd.read_excel("Focus.xlsx", usecols = [
    "Marchio", "Linea", "Modello", "Colore", "Codice a barre", "Prezzo vendita", "Quantità"
])

# FILE BRAND
# esporto file di un brand (ES. MiuMiu) da Matrixfy(.xlsx). In questo file c'è il barcode!
file_brand = str(input("Inserisci il nome del file da cui prendere il barcode: "))
brand = pd.read_excel(file_brand+".xlsx", usecols = [
    "Title", "Variant Barcode", "Variant SKU"
])
brand.rename(columns = {"Variant Barcode":"Codice a barre", "Variant SKU":"Lineitem sku"}, inplace = True)

# passo i barcode presenti in "file_brand" nel file degli ordini di Shopify
#numeroProva = 0
shopify_brand = shopify_orders.merge(brand, on = "Lineitem sku", how = "left")
#crea un percorso dove inserire i file aggiornati
directory = "C:\\Users\\miche\\Desktop\\myVenv\\Looker\\scaricaArticoli\\check\\"
save = directory + file_brand+"OK.xlsx"
shopify_brand.to_excel(save, index=False)
#shopify_brand.drop(columns=["_merge"], inplace=True)
#shopify_brand.to_csv("januaryOrders2.csv", index = False)

#if __name__ == "__main__":
#    print("Sembra tutto a posto!")
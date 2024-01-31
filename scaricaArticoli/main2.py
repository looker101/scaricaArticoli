import pandas as pd

# FILE SHOPIFY ORDINI
shopify_orders = pd.read_csv("januaryOrders.csv", usecols=[
    "Name", "Fulfillment Status", "Fulfilled at", "Lineitem quantity", "Lineitem quantity",
    "Lineitem sku"])
shopify_orders.rename(columns={"Vendor": "Marchio", "Lineitem price": "Prezzo vendita"}, inplace=True)
shopify_orders["Codice a barre"] = ""
shopify_orders.to_excel("FileOrdiniVuoto.xlsx", index = False)

# FILE DEI BRAND DA DOVE PRENDO I CODICI A BARRE
file_brand = str(input("Inserisci il nome del file da cui prendere il barcode: "))
brand = pd.read_excel(file_brand + ".xlsx", usecols=[
    "Title", "Variant Barcode", "Variant SKU"
])
brand.rename(columns={"Variant Barcode": "Codice a barre", "Variant SKU": "Lineitem sku"}, inplace=True)
brand.to_excel("File " + str(file_brand) + ".xlsx", index=False)

new_file = shopify_orders.merge(brand, how = "Lineitem sku", on = "left")

new_file.to_excel("FileUnito.xlsx", index=False)
import pandas as pd

focus = pd.read_excel("Focus.xlsx", usecols = [
    "Marchio", "Linea", "Modello", "Colore", "Codice a barre", "Prezzo vendita", "Quantità"
])

def getShopifyOrders():
    shopify_orders = pd.read_csv("januaryOrders1.csv", usecols=[
        "Name", "Fulfillment Status", "Fulfilled at", "Lineitem quantity", "Lineitem quantity",
        "Lineitem sku"])
    # rinomino le colonne in modo da facilitare il "merge"
    shopify_orders.rename(columns={"Vendor": "Marchio", "Lineitem price": "Prezzo vendita"}, inplace=True)
    # inserisco la colonna relativa ai codici a barre che lascerò vuota
    shopify_orders["Codice a barre"] = ""
    shopify_orders.to_csv("shopifyOrders.csv", index = False)
    return shopify_orders

def getBarcodeBrand():
    file_brand = str(input("Inserisci il nome del file da cui prendere il barcode: "))
    brand = pd.read_excel(file_brand + ".xlsx", usecols=[
        "Title", "Variant Barcode", "Variant SKU"
    ])
    brand.rename(columns={"Variant Barcode": "Codice a barre", "Variant SKU": "Lineitem sku"}, inplace=True)
    return brand

def mergeBrandShopify(shopify, brand_file):
   merged_file = shopify.merge(brand_file, on = "Lineitem sku", how="left")
   merged_file.to_excel("FileUniti.xlsx", index = False)
   return merged_file

def getChoice():
    shopify_orders = getShopifyOrders()
    brand = getBarcodeBrand()
    mergeBrandShopify(shopify_orders, brand)
    pass
    #1 settare il file degli ordini di shopify
    #2 esporto file di un brand (ES. MiuMiu) da Matrixfy(.xlsx). In questo file c'è il barcode!

if __name__ == "__main__":
    print("OK")
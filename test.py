import openpyxl

path = #file orders_status2024

wb = openpyxl.load_workbook(path)
ws = wb.active

# crea l'input
ricerca_ordini = str(input("Inserisci i numeri ordini che spedirai oggi separati da una virgola: "))
numero_ordini_da_cercare = [n_ordine.strip() for n_ordine in ricerca_ordini.split(",")]

# creazione del file dove andranno le righe relatiuve agli ordini inseriti dall'utente
foglio_destinazione = wb.create_sheet("Ordini da Spedire Odierni")
#foglio_destinazione.append(ws["1"]) # copio l'intestazione (1a riga)

for numero_ordine in numero_ordini_da_cercare:
    trovato = False
    for riga in ws.iter_rows(min_row = 2, values_only = True):
        if riga[0] == numero_ordine:
            trovato = True
            foglio_destinazione.append(riga)
            break
    if not trovato:
        print(f"Il numero di ordine {ricerca_ordini} non è stato trovato nel file")

wb.save("orders_to_ship.xlsx")
print("File salvato correttamente")

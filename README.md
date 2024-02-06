:monkey_face:	
# Comparazione fulfillati Shopify -> Scaricati Focus

1. Per ogni ordine che verrà evaso nella giornata corrente:
     - cerca il numero di ordine all'interno del file stato ordini e riportalo nel nuovo foglio di lavoro (utilizza il programma getOrders.py)
     - inserisci il barcode

## **getOrders.py**

1. lettura del file "Stato Ordini"
2. Togliere eventuali spazi da ogni cella della colonne "Ordini"
3. Creare input dove inserire il numero di ordine da copiare nell'altro file
4. Togliere eventuali spazi dall'input inserito dall'utente
5. Creare nuovo foglio di lavoro, dove verranno inserite le righe relative al numero di ordine inserito dall'utente
6. Inserisco l'intestazione nel nuovo foglio di lavoro. E' la stessa del foglio di origine
7. Se il numero di ordine dell'input corrisponde con un ordine del foglio di origine, questa riga verrà riportata sul foglio di destinazione
8. Aggiungo la colonna relativa al barcode
9. Salvo il file

## **getCompare.py**
1. Leggere il file scaricato da Focus
2. Utilizza solo le colonne che ti servono
3. Con il comando merge di pandas, fai un confronto tra il file generato da getOrders.py ed il file di focus in base alla colonna dei barcode
4. I barcode senza corrispondenza (a regola gli oggetti NON scaricati da Focus) saranno inseriti all'interno del file excel generato alla fine del processo
5. 

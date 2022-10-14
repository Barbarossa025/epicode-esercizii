import mysql.connector
conn=mysql.connector.connect(
    user='root',
    password='data',
    host='127.0.0.1',
    database='ecommerce')
cursor=conn.cursor()
#query per vedere tutti i prodotti a catalogo
sql='SELECT * from prodotto'
cursor.execute(sql)
pro5=cursor.fetchmany(size=5)
print(pro5)

def query(interrogazione):
    cursor=conn.cursor()
    sql=interrogazione
    cursor.execute(sql)
    result=cursor.fetchall()
    for riga in result:
        return riga
# query per calcolare l'ammontare di ogni prodotto dell'inventario
query('''select prodotto.nome,(prodotto.quantita*prezzo.valore)as inventario 
from prodotto join prezzo on prodotto.pid=prezzo.pid
order by inventario desc ''') 

#query per vedere i prodotti che non hanno una caretogira o sono prodotti vari
query('''select prodotto.nome,categoria.nome 
      from categoria left outer join prodotto on prodotto.cid=categoria.cid''')

#query per tutti i prodotti appartangono alla categoria notebook
query('''select prodotto.nome
from prodotto where prodotto.cid=(select categoria.cid from categoria where categoria.cid=120)''')
#query di tutti i prodotti che hanno giacenza  maggiore dellam media della quantita
query('''select * from prodotto where quantita>(select avg(quantita) from prodotto);''')
#query per trovare tutti i televisori al plasma piu costosi dei televisori ?
query('''select prodotto.nome,prezzo.valore,categoria.nome
from prodotto inner join prezzo on prodotto.cid=categoria.cid
where categoria.nome="televisori al plasma" 
and prezzo.valore>any(select prezzo.valore from prezzo inner join prodotto on prezzo.pid=prodotto.pid 
where categoria.nome='televisori');''')
#query per trovare il numero di tutti i clienti 
query('''select count(uid) as total from utente;''')
#qury per vedere tutte le città distinte di spedizione 
query('''select distinct indirizzo.citta from indirizzo;''')
#qury per vedere le città con piu di 5 spedizioni
query('''select distinct indirizzo.citta,count(citta) as nro_spedizioni
from indirizzohaving nro_spedizioni > 5;''')
#query orini in stato  spedito
query('''select stato.nome,ordine.oid,ordine.uid from  ordine join stato on stato.stid=ordine.stid where stato.nome='spedito''')


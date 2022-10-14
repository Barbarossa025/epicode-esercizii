from sqlalchemy import create_engine
import pandas as pd
db_connection_str = 'mysql+pymysql://root1:root1@127.0.0.1/ecommerce'
db_connection = create_engine(db_connection_str)
import mysql.connector
import mysql 

'''query='show tables'
cur.execute(query)
db=cur.fetchall()
for data in db:
    print(data)'''
db=mysql.connector.connect(
    user='root',
    password='data',
    host='127.0.0.1',
    database='ecommerce')    
def interroga(istrz):
    cur=db.cursor()
    query=pd.read_sql_query(istrz,db)
    cur.execute(query)
    df=pd.DataFrame(query)
    print(df.head(5))
    
interroga('''select prodotto.nome,(prodotto.quantita*prezzo.valore)as inventario 
from prodotto join prezzo on prodotto.pid=prezzo.pid
order by inventario desc ''') 
interroga('''select prodotto.nome,categoria.nome 
      from categoria left outer join prodotto on prodotto.cid=categoria.cid''')
interroga('''select prodotto.nome
from prodotto where prodotto.cid=(select categoria.cid from categoria where categoria.cid=120)''')
interroga('''select * from prodotto where quantita>(select avg(quantita) from prodotto);''')
interroga('''select prodotto.nome,prezzo.valore,categoria.nome
from prodotto inner join prezzo on prodotto.cid=categoria.cid
where categoria.nome="televisori al plasma" 
and prezzo.valore>any(select prezzo.valore from prezzo inner join prodotto on prezzo.pid=prodotto.pid 
where categoria.nome='televisori');''')
#query per trovare il numero di tutti i clienti 
('''select count(uid) as total from utente;''')
#qury per vedere tutte le città distinte di spedizione 
interroga('''select distinct indirizzo.citta from indirizzo;''')
#qury per vedere le città con piu di 5 spedizioni
interroga('''select distinct indirizzo.citta,count(citta) as nro_spedizioni
from indirizzohaving nro_spedizioni > 5;''')
#query orini in stato  spedito
interroga('''select stato.nome,ordine.oid,ordine.uid from  ordine join stato on stato.stid=ordine.stid where stato.nome='spedito''')

#metodo 2 da fare 
'''def multiply(q,p)
    if dfp.loc[[]]==colonna2:
        inventario=colonna1*colonna 2
    return inventario'''
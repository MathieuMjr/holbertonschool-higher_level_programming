#!/usr/bin/env python3
import MySQLdb

# function to connect to a MySQL database
db = MySQLdb.connect(
    host='localhost', user='user1', passwd='User@001', db='hbtn_0e_0_usa')
cur = db.cursor()
# créer un curseur - permet d'avoir plusieurs environnement
# sur la même connexion à la DB ?

cur.execute("SELECT * FROM states ORDER BY id")  # envoie une requête
rows = cur.fetchall()
# récupère les lignes renvoyées par la base et les stock en liste de tuples
# on peut récupérer une ligne à la fois ou un nombre n de lignes
# avec fetchone() et fetchmany(n)

for element in rows:
    print(element)

cur.close()
db.close()

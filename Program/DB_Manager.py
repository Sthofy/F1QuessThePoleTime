import sqlite3

# Létrehozás(ha nem létezik) és kapcsolódás
conn = sqlite3.connect("nev.db")
curs = conn.cursor()

conn.close()
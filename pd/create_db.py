import sqlite3
DB = 'kross.db'
#savienojuma izveide ar db
conn = sqlite3.connect(DB)
#kursora izveide (gruzchiks)
cursor = conn.cursor()
#pieprasijums, kas veido tabulu DB
cursor.execute('''
    CREATE TABLE IF NOT EXISTS rezultati (
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               vards TEXT NOT NULL, 
               vecums TEXT NOT NULL,
               laiks INTEGER NOT NULL
               )
''')
#saglāba izmaiņas
conn.commit()
conn.close()
print('Tabula Rezultāti izveidota')
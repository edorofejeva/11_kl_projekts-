import sqlite3
DB = 'kross.db'
conn = sqlite3.connect(DB)
cursor = conn.cursor()
dati = []
for i in range(6):
    print(f'\nIvadi {i+1} ierakstu:')
    vards = input('Vārds: ')
    vecums = input('Vecums: ')
    laiks = int(input('Laiks: '))
    dati.append((vards, vecums, laiks))
cursor.executemany('''
    INSERT INTO rezultati (vards, vecums, laiks)
    VALUES (?, ?, ?)               
''', dati)
conn.commit()
conn.close()
print('Tika pievienoti 6 ieraksti.')
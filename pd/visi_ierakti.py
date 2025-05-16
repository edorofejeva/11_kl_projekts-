import sqlite3
DB = 'kross.db'
conn = sqlite3.connect(DB)
cursor = conn.cursor()

cursor.execute('''
    SELECT id, vards, vecums, laiks FROM rezultati
    ORDER BY rezultats DESC         
''')
ieraksti = cursor.fetchall()
conn.close()
if ieraksti:
    print('TOP3 rezultāti:')
    for id_, vards, vecums, laiks in ieraksti:
        print(f'{id_}   {vards} {vecums} - {laiks}')
else:
    print('Nav rezultātu')
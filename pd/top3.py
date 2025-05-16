import sqlite3
DB = 'kross.db'
conn = sqlite3.connect(DB)
cursor = conn.cursor()
cursor.execute('''
    SELECT id, vards, vecums, laiks FROM rezultati
    ORDER BY rezultats DESC 
    LIMIT 3          
''')
top3 = cursor.fetchall()
conn.close()
if top3:
    print('TOP3 rezultāti:')
    for id_, vards, vecums, laiks in top3:
        print(f'{id_}   {vards} {vecums} - {laiks}')
else:
    print('Nav rezultātu')
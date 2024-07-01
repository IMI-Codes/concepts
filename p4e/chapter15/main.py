#sqlite is already embedded into python
import sqlite3

conn = sqlite3.connect('game.sqlite')
cur = conn.cursor()

cur.execute('CREATE TABLE Game (id int, name text, type text)')

cur.execute('INSERT INTO  Game(id,name,type) VALUE(?,?,?)',(1,'Uncharted','Third Peron Shooter'))
cur.execute('INSERT INTO  Game(id,name,type) VALUE(?,?,?)',(2,'god of war','Third Peron Shooter'))
cur.execute('INSERT INTO  Game(id,name,type) VALUE(?,?,?)',(3,'Jump force','Third Peron Shooter'))
cur.execute('INSERT INTO  Game(id,name,type) VALUE(?,?,?)',(4,'dark sector','Third Peron Shooter'))

cur.execute('SELECT  name FROM Track')
for row in cur:
  print(row)
conn.commit()

conn.close()
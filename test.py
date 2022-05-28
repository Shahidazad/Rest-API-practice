# how to connect to database

import sqlite3

conn=sqlite3.connect('data.db')
cur=conn.cursor()
create_table="CREATE TABLE users (id int, username text, password text)"
cur.execute(create_table)
user=(1,'jose','asdf')
insert_qur="INSERT INTO users VALUES (?,?,?)"
cur.execute(insert_qur,user)
users=[
    (1,'jose','asdf'),
    (2,'jod','asyh'),
    (3,'joere','afsa'),


]

cur.executemany(insert_qur,users)

select_q="SELECT * FROM  users"
for row in cur.execute(select_q):
    print(row)

conn.commit()
conn.close()
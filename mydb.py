import sqlite3

con = sqlite3.connect('mydatabase.db')

cursorObj = con.cursor()

cursorObj.execute("CREATE TABLE users(id integer PRIMARY KEY, name text, patientid varchar(20),abdomen_size varchar(10),temp varchar(10))")

con.commit()

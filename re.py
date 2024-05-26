
from newenc import *
a=raw_input("Enter ID")
b=raw_input("Enter Name")
c=raw_input("Enter Abdomen size")
d=raw_input("Enter Natemperatureme")

import sqlite3

con = sqlite3.connect('mydatabase.db')

cursorObj = con.cursor()

cursorObj.execute("insert into users( name, patientid ,abdomen_size ,temp ) values('"+b+"','"+a+"','"+c+"','"+d+"')")

msg = a

cipher = encryptMessage(msg) 
print("Encrypted Message: {}". format(cipher)) 

print("Decryped Message: {}". 
	format(decryptMessage(cipher)))

con.commit()
f=open(b+".txt","w")
f.write(str(cipher))
f.close()

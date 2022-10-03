import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="M.U.L.A.S",
    password="MUL1NH4S",
    database="bios"
)
mycursor = mydb.cursor()

sql = "INSERT INTO os (Sala, Maquina, Problema, Reportado, Resolvido) VALUES (%s, %s, %s, %s, %s)"
val = ["207", "25", "não liga", "2022-10-03 10:30:50", "1"]

mycursor.execute(sql, val)
mydb.commit()
print(mycursor.rowcount, "record inserted.")

mycursor.execute("SELECT * FROM os WHERE Resolvido='0' ORDER BY id ")
myresult = mycursor.fetchall()

for x in myresult:
    print(x)

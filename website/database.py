def Insert_Login(Usuario, Senha, Email, Técnico):
    import mysql.connector

    mydb = mysql.connector.connect(
        host="localhost",
        user="M.U.L.A.S",
        password="MUL1NH4S",
        database="testes"
    )

    mycursor = mydb.cursor()

    sql = "INSERT INTO login (Usuario, Senha, Email, Técnico) VALUES (%s, %s, %s, %s)"
    val = [Usuario, Senha, Email, Técnico]

    mycursor.execute(sql, val)
    mydb.commit()
    print(mycursor.rowcount, "record inserted.")

def Insert_OS(Sala, Maquina, Problema, Reportado, Resolvido):
    import mysql.connector

    mydb = mysql.connector.connect(
        host="localhost",
        user="M.U.L.A.S",
        password="MUL1NH4S",
        database="testes"
    )

    mycursor = mydb.cursor()

    sql = "INSERT INTO os (Sala, Maquina, Problema, Reportado, Resolvido) VALUES (%s, %s, %s, %s, %s)"
    val = [Sala, Maquina, Problema, Reportado, Resolvido]

    mycursor.execute(sql, val)
    mydb.commit()
    print(mycursor.rowcount, "record inserted.")


def Select_Login():
    import mysql.connector

    mydb = mysql.connector.connect(
        host="localhost",
        user="M.U.L.A.S",
        password="MUL1NH4S",
        database="testes"
    )

    mycursor = mydb.cursor()

    mycursor.execute("SELECT * FROM login")
    myresult = mycursor.fetchall()

    for x in myresult:
        print(x)

def Select_OS():
    import mysql.connector

    mydb = mysql.connector.connect(
        host="localhost",
        user="M.U.L.A.S",
        password="MUL1NH4S",
        database="testes"
    )

    mycursor = mydb.cursor()

    mycursor.execute("SELECT * FROM os")
    myresult = mycursor.fetchall()

    for x in myresult:
        print(x)

'''
Funções Existentes:
    Insert_Login()
        Insert_OS()
            Select_Login()
                Select_OS()
'''
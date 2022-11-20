# BANCO OFICIAL:
"""
def create_database():
    import mysql.connector

    mydb = mysql.connector.connect(
        host="anxjos.mysql.pythonanywhere-services.com",
        user="anxjos",
        password="mulinhas", #"MUL1NH4S"
    )
    cur = mydb.cursor()

    sql = "CREATE DATABASE anxjos$db; USE anxjos$db"
    cur.execute(sql)
    mydb.commit()

def connect_db():
    import mysql.connector

    mydb = mysql.connector.connect(
        host="anxjos.mysql.pythonanywhere-services.com",
        user="anxjos",
        password="mulinhas", #"MUL1NH4S"
        database="anxjos$db"
    )
    return mydb
"""
# ==========================================================
# BANCO DE TESTES LOCAIS:
def create_database():
    import mysql.connector

    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="mulinhas", #"MUL1NH4S"
    )
    cur = mydb.cursor()

    sql = "CREATE DATABASE mulas; USE mulas"
    cur.execute(sql)
    mydb.commit()

def connect_db():
    import mysql.connector

    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="mulinhas", #"MUL1NH4S"
        database="mulas"
    )
    return mydb

# ==========================================================

def create_users_table():
    import mysql.connector

    mydb = connect_db()
    mycursor = mydb.cursor()

    sql = "CREATE TABLE users (user varchar(20), senha varchar(20), email varchar(40), admin bool);"
    mycursor.execute(sql)
    mydb.commit()

def create_oss_table():
    import mysql.connector

    mydb = connect_db()
    mycursor = mydb.cursor()

    sql = "CREATE TABLE oss (Sala varchar(255), Maquina varchar(255), Problema varchar(255), Detalhes varchar(255), Data varchar(255), Status varchar(255));"
    mycursor.execute(sql)
    mydb.commit()

def create_labs_table():
    import mysql.connector

    mydb = connect_db()
    mycursor = mydb.cursor()

    sql = "CREATE TABLE labs (sala INT PRIMARY KEY, linhas INT, colunas INT, reportados varchar(255), mntc varchar(255));"
    mycursor.execute(sql)
    mydb.commit()
    

def Insert_Login(user, senha, email, admin):
    import mysql.connector

    mydb = connect_db()
    mycursor = mydb.cursor()


    sql = "INSERT INTO users (user, senha, email, admin) VALUES (%s, %s, %s, %s)"
    val = [user, senha, email, admin]

    mycursor.execute(sql, val)
    mydb.commit()
    print(mycursor.rowcount, "record inserted.")


def Insert_OS(Sala, Maquina, Problema, Detalhes, Data, Status):
    import mysql.connector

    mydb = connect_db()
    mycursor = mydb.cursor()

    # CREATE TABLE bd (user varchar(20), senha varchar(20), data varchar(10));
    # CREATE TABLE oss (Sala varchar(3), Maquina varchar(2), Problema varchar(50), Reportado varchar(100), Resolvido varchar(18))

    sql = "INSERT INTO oss (Sala, Maquina, Problema, Detalhes, Data, Status) VALUES (%s, %s, %s, %s, %s, %s)"
    val = [Sala, Maquina, Problema, Detalhes, Data, Status]

    mycursor.execute(sql, val)
    mydb.commit()

def Update_Status(datas, status):
    import mysql.connector

    mydb = connect_db()
    mycursor = mydb.cursor()

    sql = f"UPDATE oss SET Status = '{status}' WHERE Data = '{datas}';"

    mycursor.execute(sql)
    mydb.commit()

def Insert_Lab(sala, linhas=0, colunas=0, reportados="", mntc=""):
    import mysql.connector

    mydb = connect_db()
    mycursor = mydb.cursor()

    sql = f"REPLACE INTO labs (sala, linhas, colunas, reportados, mntc) VALUES (%s, %s, %s, %s, %s)"
    # {sala}, {linhas}, {colunas}, {reportados}, {mntc}
    val = [sala, linhas, colunas, reportados, mntc]

    mycursor.execute(sql, val)
    mydb.commit()
    #print(mycursor.rowcount, "record inserted.")


def Select_Login(current_user):
    import mysql.connector

    mydb = connect_db()
    mycursor = mydb.cursor()

    sql = f"SELECT * FROM users WHERE user = '{current_user}';"

    mycursor.execute(sql)
    myresult = mycursor.fetchall()

    return myresult

def Select_Lab(sala):
    import mysql.connector

    mydb = connect_db()
    mycursor = mydb.cursor()

    sql = f"SELECT * FROM labs WHERE sala = {sala};"

    mycursor.execute(sql)
    myresult = mycursor.fetchall()

    return myresult


def Select_OS():
    import mysql.connector

    mydb = connect_db()
    mycursor = mydb.cursor()

    mycursor.execute("SELECT * FROM oss")
    myresult = mycursor.fetchall()
    return myresult

'''
Funções Existentes:
    connect_db() # criar conexão com banco de dados
        Insert_Login()
            Insert_OS()
                Select_Login()
                    Select_OS()
'''


try: create_labs_table()
except: pass
# Insert_Lab(402, 8, 4, "010203", "112203")
# print(Select_Lab(402))

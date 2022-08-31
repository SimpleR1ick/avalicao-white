#  connect.py
#  Copyright 2022
#  Autor: Henrique Dalmagro

#############################
# Fonte code in Python 3.10 #
#############################

# Imports
import mysql.connector
from mysql.connector import errorcode

# Dados da conexão
connect_config = {
    'host': 'localhost',
    'user': 'root',
    'password': '',
    'database': 'effettivo'
}

def connect():
    try:
        db_connection = mysql.connector.connect(**connect_config)
        b_Info = db_connection.get_server_info()

        print("Banco de dados conectado com sucesso!")
        print("Versão do servidor: ", b_Info)

        return db_connection

    except mysql.connector.Error as error:
        if error.errno == errorcode.ER_BAD_DB_ERROR:
            print("Banco de dados não existe")

        elif error.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Usuario ou senha incorretos!")

        else:
            print(error)

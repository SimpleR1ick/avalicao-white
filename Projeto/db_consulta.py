#  consulta.py
#  Copyright 2022
#  Autor: Henrique Dalmagro

#############################
# Fonte code in Python 3.10 #
#############################

def consulta(db_connect):
    print("\n\tCONSULTA")

    while True:
        nomeUsuario = input("Digite o nome do usuário: ")
        
        if nomeUsuario == "":
            print("O nome não estar vazio!")
            continue
        else:
            selectConsulta(db_connect, nomeUsuario)
            break


def selectConsulta(db_connect, values):
    # Criando um cursor
    cursor = db_connect.cursor() 

    # Preparando comando sql
    sql = """SELECT pess.DESC_NOME, carg.DESC_CARGO FROM Pessoa pess 
             JOIN Cargo carg ON (pess.CODG_CARGO = carg.CODG_CARGO) 
             WHERE pess.DESC_NOME = %s"""

    try: # Inserindo o comando sql no cursor e o executando
        cursor.execute(sql, (values,))

    except: # mysql.connector.errors.DataError
        print("Usuário não encontrado")

    else: # Fechando a conexão
        record = cursor.fetchall()
        
        if not record:
            print("O usuário não possui um cargo!")

        for i in record:
            print(f"Nome: {i[0]}")
            print(f"Cargo: {i[1]}")
        
        cursor.close()
        
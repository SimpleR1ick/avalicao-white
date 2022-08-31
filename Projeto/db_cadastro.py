#  cadastro.py
#  Copyright 2022
#  Autor: Henrique Dalmagro

#############################
# Fonte code in Python 3.10 #
#############################

# Variaveis globais
cargos = ["1", "2"]


def cadastro(db_connect):
    print("\n\tCADASTRO")

    while True:
        desc_nome = input("Digite o nome: ")
        data_nascimento = input("Digite a data de nascimento (yyyy-mm-dd): ")
        codg_cargo = input("Digite o codigo do cargo: ")

        if not codg_cargo in cargos:
            print("Cargo invalido!\nDigite codigo existente, ou deixe em branco")
            continue

        if data_nascimento == "":
            data_nascimento = None

        if codg_cargo == "":
            codg_cargo = None

        else:  # Processamento - Enviando os values para o insert
            values = (desc_nome, data_nascimento, codg_cargo)
            insertCadastro(db_connect, values)
            break


def insertCadastro(db_connect, values):
    # Criando um cursor
    cursor = db_connect.cursor()

    # Preparando comando sql
    sql = """INSERT INTO Pessoa (DESC_NOME, DATA_NASCIMENTO, CODG_CARGO)
             VALUES (%s, %s, %s)"""

    try:  # Inserindo o comando sql no cursor e o executando
        cursor.execute(sql, values)

    except:  # mysql.connector.errors.DataError
        print("Data de nascimento com formato invalido!\nDigite no formato (yyyy-mm-dd)")
        cadastro()

    else:  # Fechando o cursor
        print("\nUsuario cadastrado com sucesso!")
        cursor.close()

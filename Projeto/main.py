#  main.py
#  Copyright 2022
#  Autor: Henrique Dalmagro

#############################
# Fonte code in Python 3.10 #
#############################

# Imports
from db_cadastro import cadastro
from db_conexao import connect
from db_consulta import consulta

if __name__ == "__main__":
    # Variaveis
    conexao = bool()

    try: # Tentando inciar a conexão com o banco de dados
        db_connect = connect() 
    except UnboundLocalError: # Conexão falha, objeto db_connect não existe
        conexao = False
    else: # Conexão criada com sucesso!
        conexao = True

    # Processamento
    while conexao:
        print("\n\tCADASTRO & PESQUISA\n")
        print("1 - Cadastro")
        print("2 - Consulta")
        print("3 - Sair")

        try:
            option = int(input("\nEscolha uma opção: "))
            
        except ValueError:
            print("Opção invalida!")

        finally:
            if option in (1, 2, 3):
                if option == 1:
                    cadastro(db_connect)
                    
                elif option == 2:
                    consulta(db_connect)

                elif option == 3:
                    db_connect.commit()
                    db_connect.close()
                    print("Saindo...")
                    break
            else:
                print("Opção invalida!")

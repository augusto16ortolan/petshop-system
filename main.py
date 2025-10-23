import funcoes

# criamos uma lista global para usar em todas as funções
pets = []

#comentario

def main():

    # carregamento dos dados
    #Registrar um log de inicio de sistema
    funcoes.registrar_log("Iniciando sistema")
    funcoes.carregar_dados(pets)

    while True:
        print("""
            ===== SISTEMA DE PETSHOP =====
            1 - Cadastrar pet
            2 - Listar pets
            3 - Editar pet
            4 - Deletar pet
            5 - Sair""")
        
        escolha_do_usuario = int(input("Digite uma opção: "))

        funcoes.limpar_terminal()
        print("Opção escolhida: ", escolha_do_usuario)

        if escolha_do_usuario == 1:
            funcoes.cadastrar_pet(pets)
            funcoes.registrar_log("Cadastrar pet")
        elif escolha_do_usuario == 2:
            funcoes.listar_pets(pets)
            funcoes.registrar_log("Lista pet")
        elif escolha_do_usuario == 3:
            print("Editar pet")
            funcoes.registrar_log("Editar pet")
        elif escolha_do_usuario == 4:
            print("Deletar pet")
            funcoes.registrar_log("Deletar pet")
        elif escolha_do_usuario == 5:
            print("Sair")
            funcoes.registrar_log("Finalizando sistema")
            # registrar um log de finalização de sistema
            break
        else:
            print("Opção inválida. Digite uma opção válida")
            funcoes.registrar_log("Usuário informou uma opção inválida")

main()

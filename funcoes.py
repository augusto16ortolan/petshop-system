import os
from datetime import datetime

def limpar_terminal():
    os.system("cls")

def registrar_log(acao_do_usuario):
    arquivo_de_log = open("./dados/logs.atitus", "a", encoding="utf-8")
    arquivo_de_log.write(f"[{datetime.now().strftime("%d/%m/%Y %H:%M:%S")}] {acao_do_usuario} \n")
    arquivo_de_log.close()

def carregar_dados(pets):
    arquivo_de_pets = open("./dados/pets.atitus", "r", encoding="utf-8")
    linhas = arquivo_de_pets.readlines()
   
    for linha in linhas:
        codigo, nome, especie, idade = linha.strip().split(";")
        pet = {"codigo": codigo, "nome": nome, "especie": especie, "idade": idade}
        pets.append(pet)

def salvar_dados(pets):
    if len(pets) == 0:
        arquivo_de_pets = open("./dados/pets.atitus", "w", encoding="utf-8")
        arquivo_de_pets.write(" ")
        arquivo_de_pets.close()
        return
    
    arquivo_de_pets = open("./dados/pets.atitus", "w", encoding="utf-8")
    for pet in pets:
        arquivo_de_pets.write(f"{pet["codigo"]};{pet["nome"]};{pet["especie"]};{pet["idade"]}\n")

    arquivo_de_pets.close()        

def cadastrar_pet(pets):
    nome = input("Informe o nome: ")
    especie = input("Informe a espécie: ")
    idade = input("Informe a idade: ")

    pet = {"codigo": len(pets) + 1, "nome": nome, "especie": especie, "idade": idade}
    pets.append(pet)
    salvar_dados(pets)

def listar_pets(pets):
    if len(pets) == 0:
        print("Nenhum pet cadastrado")
        return
    
    for pet in pets:
        print(f"{pet["codigo"]} - {pet["nome"]} - {pet["especie"]} - {pet["idade"]} anos")
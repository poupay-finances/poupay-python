from generate_cattle import GenerateCattle
import os

from generate_soy import GenerateSoy

START_MENU = """
    MENU
    1 - Gerar dados de Pecuária de bovino
    2 - Gerar dados de agricultura de soja
    3 - Sair
"""


def menu():
    print(START_MENU)
    option = input("Digite o número do caso: ").strip()
    if option == "1":
        return cattle_option()
    if option == "2":
        return soy_option()
    elif option == "3":
        print("Adeus")
        return False
    else:
        print("Opção Inválida! tente novamente")
        return True


def cattle_option():
    year = input("Gerar dados de Bovino com base de qual ano(2009 a 2020): ")
    if not_is_year_between_2009_and_2020(year):
        print("Digite um ano válido")
        return True
    print("Processando... ")
    cattle = GenerateCattle(year)
    cattle.run()
    print("Dados gerados e enviados para o banco!")
    input("Pressione qualque tecla para continuar...")
    os.system('cls')
    return True


def soy_option():
    year = input("Gerar dados de soja com base de qual ano(2018 a 2020): ")
    if not_is_year_between_2018_and_2020(year):
        print("Digite um ano válido")
        return True
    print("Processando... ")
    soy = GenerateSoy(year)
    soy.run()
    print("Dados gerados e enviados para o banco!")
    input("Pressione qualque tecla para continuar...")
    os.system('cls')
    return True


def not_is_year_between_2009_and_2020(year):
    return int(year) not in range(2009, 2021)


def not_is_year_between_2018_and_2020(year):
    return int(year) not in range(2018, 2021)


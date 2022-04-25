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
        return False
    month = input("Gerar de pecuária dados de qual mês(número): ")
    if not_is_year_between_2009_and_2020(year):
        return False
    print("Processando... ")
    cattle = GenerateCattle(year, month)
    cattle.run()
    print("Dados gerados e enviados para o banco!")
    input("Pressione qualque tecla para continuar...")
    os.system('cls')
    return True


def soy_option():
    year = input("Gerar dados de soja com base de qual ano(2018 a 2020): ")
    if not_is_year_between_2018_and_2020(year):
        return True
    month = input("Gerar de agricultura dados de qual mês(número): ")
    if not_is_a_month(month):
        return True
    print("Processando... ")
    soy = GenerateSoy(year, month)
    soy.run()
    print("Dados gerados e enviados para o banco!")
    input("Pressione qualque tecla para continuar...")
    os.system('cls')
    return True


def not_is_year_between_2009_and_2020(year):
    return int(year) not in range(2009, 2021)


def not_is_year_between_2018_and_2020(year):
    return int(year) not in range(2018, 2021)


def not_is_a_month(month):
    return int(month) not in range(1, 13)

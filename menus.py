from generate_cattle import GenerateCattle
import os

from generate_soy import GenerateSoy
from twitter_app.main import TwitterApi

START_MENU = """
    MENU
    1 - Gerar dados de Pecuária de bovino
    2 - Gerar dados de agricultura de soja
    3 - Incluir registros no arquivo com tweets
    4 - Sair
"""


def menu():
    print(START_MENU)
    option = input("Digite o número do caso: ").strip()
    if option == "1":
        return cattle_option()
    if option == "2":
        return soy_option()
    elif option == "3":
        return gerar_arquivo_twitter()
    elif option == "4":
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


def gerar_arquivo_twitter():
    termo = input("Digite o termo que deseja pesquisar do twitter: ")
    api = TwitterApi()

    # try
    try:
        tweets = api.search_tweets(termo)
    except:
        print('API indisponível tente novamente mais tarde')
        return False

    tweets_str_list = []

    for t in tweets:
        tweets_str_list.append(str(t) + '\n')

    # geração do arquivo
    path = './temp/tweetsBrutos.txt'
    apend_file(path, tweets_str_list)

    print(f"\n{len(tweets_str_list)} registros incluidos no arquivo '/temp/tweetsBrutos.txt'!")
    input("Pressione qualque tecla para continuar...")
    os.system('cls')
    return True


def apend_file(path, conteudo):
    dir = './temp'
    checar_diretorio(dir)

    arquivo = open(path, 'a', encoding='utf-8')
    arquivo.writelines(conteudo)


def checar_diretorio(dir_name):
    if not os.path.isdir(dir_name):
        os.mkdir(dir_name)


def not_is_year_between_2009_and_2020(year):
    return int(year) not in range(2009, 2021)


def not_is_year_between_2018_and_2020(year):
    return int(year) not in range(2018, 2021)

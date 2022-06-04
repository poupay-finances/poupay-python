import os
import boto3
from generate_meat_data import GenerateMeat
from twitter_app.main import TwitterApi

START_MENU = """
    MENU
    1 - Gerar dados de comercialização de carne
    2 - Incluir registros no arquivo com tweets
    3 - Sair
"""

S3_MENU = """
    MENU
    1 - Fazer o upload do arquivo no bucket S3
    2 - Voltar ao menu
"""


def menu():
    print(START_MENU)
    option = input("Digite a opção desejada: ").strip()
    if option == "1":
        return gerar_arquivo_gado()
    if option == "2":
        return gerar_arquivo_twitter()
    elif option == "3":
        print("Adeus")
        return False
    else:
        print("Opção Inválida! tente novamente")
        return True


def gerar_arquivo_gado():
    print('Gerando arquivo com dados de comercialização de carnes')
    gerador_valores = GenerateMeat()

    paises = ['Argentina', 'Brazil', 'China', 'Germany']
    lista_linhas = ['Pais;Produto;Ano;Valor']
    valores_2020 = gerador_valores.generate()
    valores_2021 = gerador_valores.generate()

    for p in paises:
        valores_gado_2020 = valores_2020[p]['gado']
        valores_frango_2020 = valores_2020[p]['frango']
        valores_porco_2020 = valores_2020[p]['porco']
        valores_gado_2021 = valores_2021[p]['gado']
        valores_frango_2021 = valores_2021[p]['frango']
        valores_porco_2021 = valores_2021[p]['porco']

        # Dados 2020
        lista_linhas.append(f'\n{p};Meat, cattle;2020;{valores_gado_2020}')
        lista_linhas.append(f'\n{p};Meat, chicken;2020;{valores_frango_2020}')
        lista_linhas.append(f'\n{p};Meat, pig;2020;{valores_porco_2020}')

        # Dados 2021
        lista_linhas.append(f'\n{p};Meat, cattle;2021;{valores_gado_2021}')
        lista_linhas.append(f'\n{p};Meat, chicken;2021;{valores_frango_2021}')
        lista_linhas.append(f'\n{p};Meat, pig;2021;{valores_porco_2021}')

    # geração do arquivo
    path = './temp/meat_2020_2021.csv'
    apend_file(path, lista_linhas, 'w')

    os.system('cls')
    print(f"\nRegistros incluidos no arquivo '/temp/meat_2020_2021.csv'")

    # upload S3
    print(S3_MENU)
    option = input("Digite a opção desejada: ").strip()

    if option == '1':
        os.system('cls')
        upload_s3(path)
        print('Arquivo carregado com sucesso!')
    elif option == '2':
        print('Voltando ao menu principal')
    else:
        print('Opção não identificada')

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

    print(
        f"\n{len(tweets_str_list)} registros incluidos no arquivo '/temp/tweetsBrutos.txt'")
    input("Pressione qualque tecla para continuar...")
    os.system('cls')
    return True


def apend_file(path, conteudo, mode='a'):
    dir = './temp'
    checar_diretorio(dir)

    arquivo = open(path, mode, encoding='utf-8')
    arquivo.writelines(conteudo)


def checar_diretorio(dir_name):
    if not os.path.isdir(dir_name):
        os.mkdir(dir_name)


def upload_s3(path):
    s3 = boto3.resource('s3')
    data = open(path, 'rb')
    nome = data.name[data.name.rindex('/')+1:len(data.name)]

    try:
        bucket_names = s3.buckets.all()
        print('Lista de buckets:')
        for bucket in bucket_names:
            print('\t'+bucket.name)
    except:
        print('Por favor, verifique suas credenciais no diretório "~/.aws/credentials" e tente novamente!')
        return

    opt = input('\nPor favor, escreva o nome do bucket a seguir: ')

    s3.Bucket(opt).put_object(
        Key=nome, Body=data)
    print('Upload realizado no bucket S3 com sucesso')

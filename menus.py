import json
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

TWITER_MENU = """
    MENU
    1 - Tweets de hoje
    2 - Especificar uma data
"""

TYPE_MENU = """
    MENU
    1 - Salvar em formato JSON
    2 - Salvar em formato TXT
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
    api = TwitterApi()
    date_option = ''
    type_option = ''
    termo = input("Digite o termo que deseja pesquisar do twitter: ")
    path = './temp/tweetsBrutos'

    while date_option not in ['1', '2']:
        os.system('cls')
        print(TWITER_MENU)
        date_option = input("Digite a opção desejada: ").strip()

        if date_option == '1':
            try:
                tweets = api.search_tweets(termo)
            except:
                print('API indisponível tente novamente mais tarde')
                return False
        elif date_option == '2':
            try:
                date_string = input("Digite uma data no formato YYYY-MM-DD. (Ex: 2022-06-01): ").strip()
                tweets = api.search_tweets_by_date(termo, date_string)
            except:
                print('API indisponível tente novamente mais tarde')
                return False
        else:
            input('Opção não reconhecida, pressione qualque tecla para continuar...')

    tweets_list = []

    while type_option not in ['1', '2']:
        os.system('cls')
        print(TYPE_MENU)
        type_option = input("Digite a opção desejada: ").strip()

        if type_option == '1':
            path += '.json'
            for t in tweets:
                tweets_list.append(t.AsDict())
            apend_file_json(path, tweets_list)
        elif type_option == '2':
            path += '.txt'
            for t in tweets:
                tweets_list.append(str(t) + '\n')
            apend_file(path, tweets_list)
        else:
            input('Opção não reconhecida, pressione qualque tecla para continuar...')

    os.system('cls')
    print(f"\n{len(tweets_list)} registros incluidos no arquivo '{path}'")

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


def apend_file(path, conteudo, mode='a'):
    dir = './temp'
    checar_diretorio(dir)

    arquivo = open(path, mode, encoding='utf-8')
    arquivo.writelines(conteudo)

def apend_file_json(path, conteudo):
    dir = './temp'
    checar_diretorio(dir)

    mode = 'r+' if os.path.isfile(path) else 'a'

    with open(path, mode, encoding='utf-8') as file:
        if mode == 'r+':
            try:
                file_data = json.load(file)
                for d in conteudo:
                    file_data.append(d)
                file.seek(0)
                json.dump(file_data, file, indent = 4, ensure_ascii=False)
            except:
                input('Erro ao ler o arquivo, por favor apague o arquivo no diretório e tente novamente, pressione enter para continuar...')
        else:
            json.dump(conteudo, file, indent = 4, ensure_ascii=False)


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

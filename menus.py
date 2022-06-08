import os
from aws_provider import AwsProvider
from generate_file import GenerateFile
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
    2 - Salvar em formato CSV
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
    path = './temp/meat_2020_2021'
    gerador_valores = GenerateMeat()
    file_manager = GenerateFile()
    aws_provider = AwsProvider()
    type_option = ''

    paises = ['Argentina', 'Brazil', 'China', 'Germany']
    lista_produto = []
    valores_2020 = gerador_valores.generate()
    valores_2021 = gerador_valores.generate()

    def montarResposta(pais, produto, ano, valores):
        return {
            'Pais': pais,
            'Produto': produto,
            'Ano': ano,
            'Valor': valores
        }

    while type_option not in ['1', '2']:
        os.system('cls')
        print(TYPE_MENU)
        type_option = input("Digite a opção desejada: ").strip()

        if type_option == '1':
            path += '.json'
        elif type_option == '2':
            # lista_produto.append('Pais;Produto;Ano;Valor')
            path += '.csv'
        else:
            input('Opção não reconhecida, pressione qualque tecla para continuar...')

    for p in paises:
        valores_gado_2020 = valores_2020[p]['gado']
        valores_frango_2020 = valores_2020[p]['frango']
        valores_porco_2020 = valores_2020[p]['porco']
        valores_gado_2021 = valores_2021[p]['gado']
        valores_frango_2021 = valores_2021[p]['frango']
        valores_porco_2021 = valores_2021[p]['porco']

        lista_produto.append(montarResposta(
            p, 'Meat, cattle', 2020, valores_gado_2020))
        lista_produto.append(montarResposta(
            p, 'Meat, chicken', 2020, valores_frango_2020))
        lista_produto.append(montarResposta(
            p, 'Meat, pig', 2020, valores_porco_2020))

        lista_produto.append(montarResposta(
            p, 'Meat, cattle', 2021, valores_gado_2021))
        lista_produto.append(montarResposta(
            p, 'Meat, chicken', 2021, valores_frango_2021))
        lista_produto.append(montarResposta(
            p, 'Meat, pig', 2021, valores_porco_2021))

    if type_option == '1':
        file_manager.apend_file_json(path, lista_produto, 'w')
    else:
        file_manager.apend_file_csv(path, lista_produto, 'w')

    os.system('cls')
    print(f"\nRegistros incluidos no arquivo '{path}'")

    # upload S3
    print(S3_MENU)
    option = input("Digite a opção desejada: ").strip()

    if option == '1':
        os.system('cls')
        aws_provider.upload_s3(path)
        print('Arquivo carregado com sucesso!')
    elif option == '2':
        print('Voltando ao menu principal')
    else:
        print('Opção não identificada')

    input("Pressione qualque tecla para continuar...")
    os.system('cls')

    return True


def gerar_arquivo_twitter():
    fields = ['contributors', 'coordinates', 'created_at', 'current_user_retweet', 'favorite_count', 'favorited', 'full_text', 'geo', 'hashtags', 'id', 'id_str', 'in_reply_to_screen_name', 'in_reply_to_status_id', 'in_reply_to_user_id', 'lang', 'location', 'media', 'place',
              'possibly_sensitive', 'quoted_status', 'quoted_status_id', 'quoted_status_id_str', 'retweet_count', 'retweeted', 'retweeted_status', 'scopes', 'source', 'text', 'truncated', 'urls', 'user', 'user_mentions', 'withheld_copyright', 'withheld_in_countries', 'withheld_scope']
    api = TwitterApi()
    file_manager = GenerateFile()
    aws_provider = AwsProvider()
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
                date_string = input(
                    "Digite uma data no formato YYYY-MM-DD. (Ex: 2022-06-01): ").strip()
                tweets = api.search_tweets_by_date(termo, date_string)
            except:
                print('API indisponível tente novamente mais tarde')
                return False
        else:
            input('Opção não reconhecida, pressione qualque tecla para continuar...')

    tweets_list = []

    if len(tweets) > 0:
        while type_option not in ['1', '2']:
            os.system('cls')
            print(TYPE_MENU)
            type_option = input("Digite a opção desejada: ").strip()

            for t in tweets:
                tweets_list.append(t.AsDict())

            if type_option == '1':
                path += '.json'
                file_manager.apend_file_json(path, tweets_list)
            elif type_option == '2':
                path += '.csv'
                file_manager.apend_file_csv(path, tweets_list, fields=fields)
            else:
                input('Opção não reconhecida, pressione qualque tecla para continuar...')

        os.system('cls')
        print(f"\n{len(tweets_list)} registros incluidos no arquivo '{path}'")

        # upload S3
        print(S3_MENU)
        option = input("Digite a opção desejada: ").strip()

        if option == '1':
            os.system('cls')
            aws_provider.upload_s3(path)
            print('Arquivo carregado com sucesso!')
        elif option == '2':
            print('Voltando ao menu principal')
        else:
            print('Opção não identificada, voltando ao menu principal')
    else:
        os.system('cls')
        print('Nenhum tweet encontrado, voltando ao menu principal')

    input("Pressione qualque tecla para continuar...")
    os.system('cls')

    return True

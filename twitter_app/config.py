import os

class Keys():
    def __init__(self) -> None:
        self.keys = self.__get_credenciais()

    def __get_credenciais(self):
        credenciais = {}

        try:
            credenciais['consumer_key'] = os.environ['CONSUMER_KEY']
            credenciais['consumer_secret'] = os.environ['CONSUMER_SECCRET']
            credenciais['access_token_key'] = os.environ['ACCESS_TOKEN_KEY']
            credenciais['access_token_secret'] = os.environ['ACCESS_TOKEN_SECRET']
        except:
            raise Exception(
                'Definas todas as váriaveis de ambiente a seguir: CONSUMER_KEY, CONSUMER_SECCRET, ACCESS_TOKEN_KEY, ACCESS_TOKEN_SECRET')
        
        return credenciais

    def get_keys(self):
        return self.keys

from datetime import datetime, timedelta
from twitter_app.config import Keys
import twitter


class TwitterConsumer():
    def __init__(self) -> None:
        self.credenciais = Keys().get_keys()
        self.api = self.start_api()

    def start_api(self):
        return twitter.Api(consumer_key=self.credenciais['consumer_key'],
                           consumer_secret=self.credenciais['consumer_secret'],
                           access_token_key=self.credenciais['access_token_key'],
                           access_token_secret=self.credenciais['access_token_secret'])

    def get_search(self, termo, count):
        results = self.api.GetSearch(term=termo, lang='pt',
                                     count=count, result_type='mixed')

        return results

    def get_search_today(self, termo, count):
        date_str = str(datetime.now())[0:10]
        results = self.api.GetSearch(term=termo, lang='pt',
                                     count=count, since=date_str)

        return results

    def get_search_by_date(self, termo, count, date):
        since_date = datetime(int(date[0:4]), int(date[5:7]), int(date[8:10]))
        until_date = since_date + timedelta(days=1)

        since_str = str(since_date)[0:10]
        until_str = str(until_date)[0:10]

        results = self.api.GetSearch(term=termo, lang='pt',
                                     count=count, since=since_str, until=until_str)

        return results

    def get_tweet(self, id):
        results = self.api.GetStatus(id)

        return results

    def get_trends(self):
        results = self.api.GetTrendsWoeid(23424768)

        return results

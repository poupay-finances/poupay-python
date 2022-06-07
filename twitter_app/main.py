from twitter_app.twitter_api import TwitterConsumer

class TwitterApi():
    def __init__(self) -> None:
        self.api = TwitterConsumer()

    def search_tweets(self, palavra):
        results = self.api.get_search_today(palavra, 100)
        return results

    def search_tweets_by_date(self, palavra, datestring):
        results = self.api.get_search_by_date(palavra, 100, datestring)
        return results
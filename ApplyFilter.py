import pandas as pd 

class ApplyFilter():

    def ApplyFilter(df)

        # filter variables
        min_tweets = 5
        max_tweets = 10000
        max_followers = 2500
        max_following = 2500
        lang = "en"

        for row in df:
            if (tweet["statuses"]["user"]["followers_count"] < max_followers and
                tweet["statuses"]["user"]["statuses_count"] > min_tweets and
                tweet["statuses"]["user"]["statuses_count"] < max_tweets and
                tweet["statuses"]["user"]["friends_count"] < max_following and
                tweet["statuses"]["user"]["lang"] == lang):


        return df
import pandas as pd 
import numpy as np

class ApplyFilter():

    def ApplyFilter(df):

        # filter variables
        min_tweets = 5
        max_tweets = 10000
        max_followers = 2500
        max_following = 2500
        lang = "en"

        # grab only the rows that meet the criteria
        df = df[df.followers < max_followers]
        df = df[df.status_count > min_tweets]
        df = df[df.status_count < max_tweets]
        df = df[df.friends_count < max_following]

        return df
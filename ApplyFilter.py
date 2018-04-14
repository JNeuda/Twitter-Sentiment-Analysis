import pandas as pd 

class ApplyFilter():

    def ApplyFilter(df):

        # filter variables
        min_tweets = 5
        max_tweets = 10000
        max_followers = 2500
        max_following = 2500
        lang = "en"

        filtered_df = pd.DataFrame(columns=['ID', 'DateTime', 'Username', 
                                            'tweet_text', 'retweet count', 
                                            'Tweet Name', 'followers', 
                                            'friends count', 'status count', 
                                            'Search Coordinates'])

        for i, row in df.iterrows():
            if (row["followers"] > max_followers): # and
                # row["status count"] < min_tweets and
                # row["status count"] > max_tweets and
                # row["friends count"] > max_following):

                print("Found Tweet")
                # filtered_df.append(row)
                df.drop(df.index[[7]])
                
            else:
                print(row["status count"])
                
                

        return df
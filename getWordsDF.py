import pandas as pd 

class getWordsDF():
    
    # this method is designed to take a very specific
    # file (triggerWords.csv) and convert/return a dataframe
    def getWordsDF(filepath):

        keywords_df = pd.read_csv(filepath, header=None, encoding = "ISO-8859-1")
        keywords_df.columns = ['phrases']

        return keywords_df

    def getDFFromCSV(filepath):

        df = pd.read_csv(filepath, delimiter="|", header=None, error_bad_lines=False, encoding="ISO-8859-1")
        df.columns = ['ID', 'DateTime', 'Username', 
                        'tweet_text', 'retweet count', 
                        'Tweet Name', 'followers', 
                        'friends_count', 'status_count', 
                        'Search Coordinates']
        return df
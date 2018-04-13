import pandas as pd 

class getWordsDF():
    
    def getWordsDF(filepath):

        keywords_df = pd.read_csv(filepath, header=None, encoding = "ISO-8859-1")
        keywords_df.columns = ['phrases']

        return keywords_df

    """ def getDFFromCSV(filepath):

        df = pd.read_csv(filepath, encoding="ISO-8859-1")

        return df """
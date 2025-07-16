import pandas as pd
#df = pd.read_csv(r"D:\NLP_Project\Data\Finance\data.csv")
#print(df.head()) ## ["Sentence" , "Sentiment"], Got [positive, negative, neutral]
#df = pd.read_csv(r"D:\NLP_Project\Data\GoEmotions\data\train.csv")
#print(df.columns.tolist()) ###{"positive": ["amusement", "excitement", "joy", "love", "desire", "optimism", "caring", "pride", "admiration", "gratitude", "relief", "approval"],"negative": ["fear", "nervousness", "remorse", "embarrassment", "disappointment", "sadness", "grief", "disgust", "anger", "annoyance", "disapproval"],"ambiguous": ["realization", "surprise", "curiosity", "confusion"]}, no column name
### D:\NLP_Project\Data\GoEmotions\data\emotions.txt has all the labels in a line.
#df = pd.read_csv(r"D:\NLP_Project\Data\Twitter ChatGPT\file.csv")
#print(df.columns.tolist()) ###Got some duplicates... labeled as Good and Bad. Also, has an extra column called unnamed.
#We are dropping the Twitter Gaming one, The Kaggle Dataset, The Poem Dataset. Those are too off the script for us. The rest are redeamable.
df = pd.read_csv(r"D:\NLP_Project\Data\Twitter Airline\Tweets.csv")
print(df["airline_sentiment"]) ### [text, airline_sentiment]
class clean_csv:
    #Wanted Column extraction
    def column_extration(df):
        mapping = {"Sentence":"Phrase" , "tweets": "phrase"}      

    def clean(df):
        pass

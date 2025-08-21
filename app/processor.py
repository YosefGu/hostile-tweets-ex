import dependencies
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer

class Processor():

    def __init__(self, data):
        self.data = data

    def finding_emotion(self):


nltk.download('vader_lexicon')# Compute sentiment labels
tweet = 'Skillcate is a great Youtube Channel to learn Data
Science'
score=SentimentIntensityAnalyzer().polarity_scores(tweet)
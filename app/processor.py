import pandas as pd
import dependencies
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer


class Processor():

    def __init__(self, data, weapons):
        self.df = pd.DataFrame(data)
        self.weapons = weapons
        nltk.download('vader_lexicon')# Compute sentiment labels

    def run(self):
        rare_words = []
        weapons_detected = []
        emotions_rate = []

        for text in self.df['Text']:
            lst_text = text.split()
            rare_words.append(self.find_first_rare_word(lst_text))
            weapons_detected.append(self.find_weapon(lst_text))
            emotions_rate.append(self.finding_emotion(text))

        self.df['rarest_word'] = rare_words
        self.df["weapons_detected"] = weapons_detected
        self.df['emotions_rate'] = emotions_rate

        return self.df


    def finding_emotion(self, text):
        score = SentimentIntensityAnalyzer().polarity_scores(text)

        if 1 <= score['compound'] >= 0.5:
            return 'positive'
        elif 0.49 <= score['compound'] >= -0.49:
            return 'neutral'
        elif -0.5 <= score['compound'] >= -1:
            return 'negative'
        else:
            return None
            

    def find_first_rare_word(self, sentenc):
        words_dict = {}
        for word in sentenc:
            word = word.lower()
            words_dict[word] = words_dict.get(word, 0) + 1
        sorted_dict = sorted(words_dict.items(), key=lambda key_value: key_value[1])
        return sorted_dict[0][0]

    def find_weapon(self, sentenc):
        weapon = set(sentenc) & set(self.weapons)
        if weapon:
            return weapon.pop()
        return ''


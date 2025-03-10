
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import spacy
from nrclex import NRCLex



class API:

    def __init__(self):
        # Initialize the VADER SentimentIntensityAnalyzer
        self.analyzer = SentimentIntensityAnalyzer()


    def analyze_sentiment(self,text):
        sentiment_score = self.analyzer.polarity_scores(text)

        # Return the sentiment score or analysis
        return sentiment_score

    def name_entity_recognition(self,text):
        nlp = spacy.load("en_core_web_md")
        doc = nlp(text)

        return doc

    def emotion_prediction(self,text):
        classifier = NRCLex(text)
        prediction = classifier.top_emotions

        return prediction




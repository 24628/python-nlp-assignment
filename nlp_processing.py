import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import SnowballStemmer


class NLPProcessing:
    def __init__(self):
        nltk.download('punkt')
        nltk.download('stopwords')
        self.stopwords = set(stopwords.words('english'))
        self.stemmer = SnowballStemmer('english')

    def tokenize(self, text):
        tokens = word_tokenize(text.lower())
        tokens = [token for token in tokens if token.isalnum()]
        return tokens

    def preprocess_query(self, query):
        tokens = self.tokenize(query)
        tokens = [token for token in tokens if token not in self.stopwords]
        tokens = [self.stemmer.stem(token) for token in tokens]
        preprocessed_query = ' '.join(tokens)
        return preprocessed_query

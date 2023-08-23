# Preprocess user input
import re
import nltk  
from nltk.corpus import stopwords  
from nltk.stem import WordNetLemmatizer  
from nltk.tokenize import word_tokenize

nltk.download('punkt', quiet=True)
nltk.download('stopwords', quiet=True)
nltk.download('wordnet', quiet=True)


class TextProcessor:
    def preprocess(self, query):
        tokens = word_tokenize(query)  
        stop_words = set(stopwords.words('english'))  
        filtered_tokens = [token for token in tokens if token.lower() not in stop_words]  
        lemmatizer = WordNetLemmatizer()  
        lemmatized_tokens = [lemmatizer.lemmatize(token) for token in filtered_tokens]  
        return ' '.join(lemmatized_tokens)
 
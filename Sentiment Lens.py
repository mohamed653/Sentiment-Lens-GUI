import re
import string
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk.tokenize import word_tokenize

# Preprocess the text
def preprocess_text(text):
    # Lowercase the text
    text = text.lower()

    # Remove punctuation
    text = re.sub(r'[^\w\s]', '', text)

    # Remove stop words
    stopwords = nltk.corpus.stopwords.words('english')
    text = ' '.join([word for word in text.split() if word not in stopwords])

    # Lemmatize the words
    lemmatizer = nltk.WordNetLemmatizer()
    text = ' '.join([lemmatizer.lemmatize(word) for word in text.split()])

    return text

# Perform sentiment analysis
def sentiment_analyze(text):
    # Create a sentiment analyzer
    sentiment_analyzer = SentimentIntensityAnalyzer()

    # Calculate the sentiment scores
    sentiment_scores = sentiment_analyzer.polarity_scores(text)

    # Determine the sentiment of the text
    sentiment = 'negative' if sentiment_scores['neg'] > sentiment_scores['pos'] else 'positive' if sentiment_scores['pos'] > sentiment_scores['neg'] else 'neutral'

    return sentiment

# Get the sentiment of the input text
def get_sentiment(text):
    # Preprocess the text
    text = preprocess_text(text)

    # Perform sentiment analysis
    sentiment = sentiment_analyze(text)

    return sentiment

# Main function
def main():
    # Get the input text
    input_text = input('Enter the text you want to analyze: ')

    # Get the sentiment of the input text
    sentiment = get_sentiment(input_text)

    # Print the sentiment
    print('The sentiment of the text is:', sentiment)

if __name__ == '__main__':
    main()
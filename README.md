# Sentiment-Lens-GUI

This program uses the TextBlob sentiment analysis library to determine the sentiment of a given text. The program first preprocesses the text by removing punctuation, stop words, and other irrelevant information. The words are also lemmatized, which means that they are converted to their base form. This helps to improve the accuracy of the sentiment analysis by ensuring that all of the words in the text are treated consistently.

Once the text has been preprocessed, the program uses a machine learning model to predict the sentiment of the text. The model is trained on a large dataset of text data with annotated sentiment labels.

How to use the program
To use the program, simply run it and enter the text you want to analyze. The program will then print the sentiment of the text to the console.

Example usage
Enter the text you want to analyze: I love this movie!

The sentiment of the text is: positive


### Requirements

* Python 3
* NLTK
* TextBlob

### Installation

To install the program, simply clone this repository and run the following command:

pip install -r requirements.txt


### Usage

To run the program, simply run the following command:

python sentiment_analysis.py


### License

This program is licensed under the MIT License.

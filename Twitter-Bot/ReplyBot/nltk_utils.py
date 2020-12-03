import nltk
#nltk.download('punkt')
from nltk.stem.porter import PorterStemmer

stemmer = PorterStemmer()

def tokenize(sentence):
    return nltk.word_tokenize(sentence)

def stem(word):
    return stemmer.stem(word.lower())

def bag_of_words(tokenized_sentence, all_words):
    pass


a = ["organise","organises","organising"]
stemmed_words = [stem(w) for w in a]
print(stemmed_words)

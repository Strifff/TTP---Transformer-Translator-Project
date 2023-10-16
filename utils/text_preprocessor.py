import nltk
import os

def parse_text_into_sentences(path):
    # Use NLTK's sent_tokenize to split the text into sentences
    sentances = []
    for file in os.listdir(path):
        if file.endswith(".txt"):
            with open(os.path.join(path, file), "r") as file:
                text = file.read()
                sentances.extend(nltk.sent_tokenize(text))
    
    #sentences = nltk.sent_tokenize(text)
    
    return sentances

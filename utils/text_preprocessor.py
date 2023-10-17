import nltk
import os
import pdfplumber
import string
import re

from google.cloud import translate_v2 as translate


def parse_textdoc_into_sentences(path):
    # Use NLTK's sent_tokenize to split the text into sentences
    sentences = []
    for file in os.listdir(path):
        if file.endswith(".txt"):
            with open(os.path.join(path, file), "r") as file:
                text = file.read()
                sentences.extend(nltk.sent_tokenize(text))

    return sentences


def parse_PDF_into_sentences(path):
    sentences = []
    for file in os.listdir(path):
        if file.endswith(".pdf"):
            filepath = f"{path}/{file}"
            with pdfplumber.open(filepath) as pdf:
                for page in pdf.pages:
                    text = page.extract_text()
                    text = text.replace("\n", " ")
                    sentences.extend(nltk.sent_tokenize(text))
                
    return sentences
    
def filter_short_sentences(sentences, min_length=5):
    return [sentence for sentence in sentences if len(sentence.split()) >= min_length]
    
def clean_text(text):
    text = re.sub(r'[^a-zA-Z0-9\s]', '', text)
    return text

def clean_sentences(sentences):
    return [clean_text(sentence) for sentence in sentences]

def lowercase_text(text):
    if isinstance(text, str):
        return text.lower()
    else:
        # Handle the case when 'text' is not a string
        return text

def lowercase_sentences(sentences):
    return [lowercase_text(sentence) for sentence in sentences]

def clean_apply_all(sentences):
    sentences = filter_short_sentences(sentences)
    sentences = lowercase_sentences(sentences)
    sentences = clean_sentences(sentences)
    
    return sentences

def initialize_translation_client():
    creds = os.path.expanduser("~/GoogleTranslateAPI/creds.json")
    translator = translate.Client.from_service_account_json(creds)
    return translator

def translate_sentance_GAPI(input_sentence, translator, lang_from, lang_to):
    result = translator.translate(
        input_sentence, source_language=lang_from, target_language=lang_to
    )
    return result["translatedText"]


def subword_tokenize_sentence(sentence, tokenizer):
    tokenized = tokenizer.tokenize(sentence)

    return tokenized




def encode_sentance_pair(sentence_pair, tokenizer):
    encoding1 = tokenizer.encode_plus(
        sentence_pair[0],
        max_length=32,  # Max sequence length
        padding="max_length",  # Pad to max_length
        truncation=True,  # Truncate sequences that exceed max_length
        return_tensors="pt",  # Return PyTorch tensors
        return_attention_mask=True,  # Return attention mask
    )

    encoding2 = tokenizer.encode_plus(
        sentence_pair[1],
        max_length=32,  # Max sequence length
        padding="max_length",  # Pad to max_length
        truncation=True,  # Truncate sequences that exceed max_length
        return_tensors="pt",  # Return PyTorch tensors
        return_attention_mask=True,  # Return attention mask
    )

    return (encoding1, encoding2)


def decode_sentance_pair(sentence_pair, tokenizer):
    decoded1 = tokenizer.decode(sentence_pair[0].input_ids[0])
    decoded2 = tokenizer.decode(sentence_pair[1].input_ids[0])

    return (decoded1, decoded2)

import nltk
import os

from google.cloud import translate_v2 as translate


def parse_text_into_sentences(path):
    # Use NLTK's sent_tokenize to split the text into sentences
    sentences = []
    for file in os.listdir(path):
        if file.endswith(".txt"):
            with open(os.path.join(path, file), "r") as file:
                text = file.read()
                sentences.extend(nltk.sent_tokenize(text))

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

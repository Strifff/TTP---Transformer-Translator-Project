import argparse
import os
import random
from transformers import AutoTokenizer

from utils.text_preprocessor import (
    parse_text_into_sentences,
    translate_sentance_GAPI,
    subword_tokenize_sentence,
    encode_sentance_pair,
    decode_sentance_pair,
    initialize_translation_client,
    translate_sentance_GAPI,
)

from utils.test_installation import (
    test_pytorch,
    test_transformers,
    test_numpy,
    test_MySQLdb,
)

password_file = os.path.expanduser("~/mysql.txt")
with open(password_file, "r") as file:
    MySQLpassword = file.readlines()[1].strip()

tokenizer = AutoTokenizer.from_pretrained("bert-base-uncased")


def preprocess_raw_data(data_path, tokenizer):
    # sentances = parse_text_into_sentences(data_path)
    # random_sentance = sentances[random.randint(0, sentances.__len__())]

    # tokenized_sentance = subword_tokenize_sentence(random_sentance, tokenizer)

    ex_en = "In the heart of a bustling metropolis."
    ex_sv = "I hjärtat av en livlig metropol."
    ex_pair = (ex_en, ex_sv)
    endcoded = encode_sentance_pair(ex_pair, tokenizer)

    decoded = decode_sentance_pair(endcoded, tokenizer)

    translator = initialize_translation_client()
    
    print("English: ", ex_en)
    translated_sentance = translate_sentance_GAPI(ex_en, translator, "en", "sv")
    print("Swedish: ", translated_sentance)


def create_dataset(data_path):
    pass


def parse_sentances(data_path):
    pass


def translate_sentances(data_path):
    pass


def create_tokenizer(data_path):
    pass


def train_model(data_path, model_path, num_epochs):
    pass


def evaluate_model(model_path):
    pass


def translate_text(input_sentence, model_path):
    pass


def test_installation():
    test_pytorch()
    test_transformers()
    test_numpy()
    test_MySQLdb(MySQLpassword)


def main():
    parser = argparse.ArgumentParser(
        description="Machine Translation with Transformers"
    )

    # Define command-line arguments
    parser.add_argument(
        "--en-sv",
        action="store_true",
        help="Translate English to Swedish using Google API",
    )
    parser.add_argument(
        "--train", action="store_true", help="Train the custom Transformer model"
    )
    parser.add_argument(
        "--eval", action="store_true", help="Evaluate the trained model"
    )
    parser.add_argument("--test", action="store_true", help="Test the installation")
    parser.add_argument("--input", type=str, help="Input sentence for translation")
    parser.add_argument("--preprocess", action="store_true", help="Preprocess raw data")

    args = parser.parse_args()

    if args.en_sv:
        pass

    if args.train:
        pass
        data_path = "data/raw_data/"
        model_path = "models/trained_model.pt"
        num_epochs = 10
        # Train the model
        train_model(data_path, model_path, num_epochs)

    if args.eval:
        pass
        model_path = "models/trained_model.pt"
        # Evaluate the trained model
        evaluate_model(model_path)

    if args.input:
        pass
        model_path = "models/trained_model.pt"
        input_sentence = args.input
        # Translate the input sentence
        translated_sentence = translate_text(input_sentence, model_path)
        print(f"Input: {input_sentence}")
        print(f"Translation: {translated_sentence}")

    if args.test:
        # Test the installation
        test_installation()

    if args.preprocess:
        preprocess_raw_data("data/raw_data/", tokenizer)


if __name__ == "__main__":
    main()

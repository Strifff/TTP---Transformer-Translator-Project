import torch
import transformers
import numpy as np
import pymysql

from transformers import pipeline


def test_pytorch():
    try:
        # Check if PyTorch is installed and print the version
        print("PyTorch Version:", torch.__version__)

        # Test a basic PyTorch operation
        x = torch.tensor([1.0, 2.0, 3.0])
        y = torch.tensor([4.0, 5.0, 6.0])
        z = x + y
        print("PyTorch Addition Result:", z)

        # You can add more specific PyTorch tests here
    except Exception as e:
        print("PyTorch test failed:", str(e))


def test_transformers():
    try:
        # Check if Transformers (Hugging Face) is installed and print the version
        print("Transformers Version:", transformers.__version__)

        # Specify the model name and revision
        model_name = "distilbert-base-uncased-finetuned-sst-2-english"
        revision = "af0f99b"

        # Create a pipeline with the specified model
        classifier = pipeline("sentiment-analysis", model=model_name, revision=revision)

        # Test the model with a sample text
        result = classifier("I somewhat hmm hmm this library!")
        print("Transformers Sentiment Analysis Result:", result)

        # You can add more specific Transformers tests here
    except Exception as e:
        print("Transformers test failed:", str(e))


def test_numpy():
    try:
        # Check if NumPy is installed and print the version
        print("NumPy Version:", np.__version__)

        # Test a basic NumPy operation
        a = np.array([1, 2, 3])
        b = np.array([4, 5, 6])
        c = np.add(a, b)
        print("NumPy Addition Result:", c)

        # You can add more specific NumPy tests here
    except Exception as e:
        print("NumPy test failed:", str(e))


## MySQLdb
host = "localhost"  # Your MySQL server host
user = "root"  # Your MySQL username
database = "TTPdb"  # Your database name


def test_MySQLdb(password):
    try:
        # Connect to the MySQL server
        connection = pymysql.connect(
            host=host, user=user, password=password, db=database
        )

        # Create a cursor object
        cursor = connection.cursor()

        # Execute a sample SQL query
        cursor.execute("SELECT 'MySQL is working!'")

        # Fetch the result
        result = cursor.fetchone()

        # Print the result
        print(result[0])

        # Close the cursor and the connection
        cursor.close()
        connection.close()

    except Exception as e:
        print("Error:", e)

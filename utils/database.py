import pymysql
import os

# USE TTPdb;

# CREATE TABLE SentenceTranslations (
#    id INT AUTO_INCREMENT PRIMARY KEY,
#    source_language VARCHAR(50),
#    target_language VARCHAR(50),
#    source_sentence TEXT,
#    translated_sentence TEXT
# );


def create_connection():
    host = "localhost"  # Your MySQL server host
    user = "root"  # Your MySQL username
    database = "TTPdb"  # Your database name

    password_file = os.path.expanduser("~/mysql.txt")
    with open(password_file, "r") as file:
        password = file.readlines()[1].strip()

    connection = pymysql.connect(host=host, user=user, password=password, db=database)

    return connection


def insert_translated_pair(connection, data, table_name):
    try:
        cursor = connection.cursor()

        # SQL query for inserting data
        insert_query = f"INSERT INTO {table_name} (source_language, target_language, source_sentence, translated_sentence) VALUES (%s, %s, %s, %s)"

        # Execute the query with the data
        cursor.execute(
            insert_query,
            (
                data["source_language"],
                data["target_language"],
                data["source_sentence"],
                data["translated_sentence"],
            ),
        )

        # Commit the changes to the database
        connection.commit()

        # Close the cursor and the database connection
        cursor.close()

        return True
    except Exception as e:
        print("Error while connecting to MySQL", e)
        return False


def get_all_translations(connection, table_name):
    # Create a cursor object
    cursor = connection.cursor()

    # Define the SELECT query
    select_query = f"SELECT * FROM {table_name}"

    # Execute the SELECT query
    cursor.execute(select_query)

    # Fetch all the rows as a list of tuples
    entries = cursor.fetchall()

    # Close the cursor and the database connection
    cursor.close()

    return entries


def get_translated_pair(connection, table_name, index, lang_from, lang_to):
    # Create a cursor object
    cursor = connection.cursor()

    # Define the SELECT query
    select_query = f"SELECT * FROM {table_name} WHERE id = {index}"

    # Execute the SELECT query
    cursor.execute(select_query)

    # Fetch the entry as a tuple
    entry = cursor.fetchone()

    # Close the cursor and the database connection
    cursor.close()

    return (entry[3], entry[4])


def get_table_length(connection, table_name):
    # Create a cursor object
    cursor = connection.cursor()

    # Define the SELECT query
    select_query = f"SELECT * FROM {table_name}"

    # Execute the SELECT query
    cursor.execute(select_query)

    # Fetch all the rows as a list of tuples
    entries = cursor.fetchall()

    # Close the cursor and the database connection
    cursor.close()

    return len(entries)

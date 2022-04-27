# Adds cryptocurrency info from webpage.php into Cryptocurrency table
import sys
from mysql.connector import *

def establish_con():
    global connection 
    connection = connect(
        # Enter mySQL credentials
        user='abflynn',
        password='Pex9oof6',
        host='localhost',
        database='abflynn'
    )

    global cursor 
    cursor = connection.cursor()

def close_con():
    cursor.close()
    connection.close()

def new_crypto(id, name, value):
    add_cryptocurrency = ('INSERT INTO Cryptocurrency '
                        '(CryptocurrencyId, CryptoName, CurrentValue) '
                        'VALUES (%s, %s, %s)'
                        (id, name, value))
    cursor.execute(add_cryptocurrency)

def main():
    establish_con()
    new_crypto(sys.argv[0], sys.argv[1], sys.argv[2])
    close_con()

main()
# Uses info from webpage.php to make an investment for a given buyer and adds it to the database
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

def buy(investor, crypto, shares, price):
    buy_investment  = ('INSERT INTO Investment '
                        '(InvestorId, CryptocurrencyId, NumShares, PurchasePrice, StillOwned) '
                        'VALUES (%s, %s, %s, %s)'
                        (investor, crypto, shares, price))
    cursor.execute(buy_investment)

def main():
    establish_con()
    buy(sys.argv[0], sys.argv[1], sys.argv[2], sys.argv[3])
    close_con()

main()
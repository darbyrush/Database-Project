# Uses info from webpage.php to sell a number of shares for a given investor and updates the database to reflect the change
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

def sell(shares, price, owned):
    sell_investment = ('UPDATE Investment '
                    'SET (NumShares, PurchasePrice, StillOwned) '
                    'VALUES (%s, %s, %s)'
                    (shares, price, owned))
    cursor.execute(sell_investment)
def main():
    establish_con()
    sell(sys.argv[0], sys.argv[1], sys.argv[2])
    close_con()

main()
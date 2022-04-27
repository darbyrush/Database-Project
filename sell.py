# Uses info from webpage.php to sell a number of shares for a given investor and updates the database to reflect the change
import sys
import mysql.connector

def establish_con():
    global connection 
    connection = mysql.connector.connect(
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

def still_owned(inv_id, crypto_id, sold):
    owned = str(cursor.execute('SELECT NumShares FROM Investment WHERE InvestorId = ' + str(inv_id) + ' and CryptocurrencyId = ' + str(crypto_id)))
    if (sold == owned):
        return '0'
    elif (sold < owned):
        return '1'
    else:
        return 'error'

def sell(inv_id, crypto_id, shares, price):
    owned = still_owned(inv_id, crypto_id, shares)
    if (owned == 'error'):
        print('There was an error, oops')
        return
    sell_investment = ('UPDATE Investment '
                    'SET (InvestorId, CryptocurrencyId, NumShares, PurchasePrice, StillOwned) '
                    'VALUES (%s, %s, %s, %s, %s);'
                    (inv_id, crypto_id, shares, price, owned))
    cursor.execute(sell_investment)
def main():
    establish_con()
    sell(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
    close_con()

main()
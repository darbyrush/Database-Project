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

def sell(inv_id, crypto_id, shares, price):

    sell_investment = """UPDATE Investment
                    SET NumShares = %s, PurchasePrice = %s, StillOwned = %s
                    WHERE InvestorId = %s AND CryptocurrencyId = %s;
                    """ % (shares, price, 0, inv_id, crypto_id)
                    
    cursor.execute(sell_investment)
    connection.commit()
def main():
    establish_con()
    sell(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
    close_con()

main()
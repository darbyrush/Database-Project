# Uses info from webpage.php to make an investment for a given buyer and adds it to the database
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

def buy(investor, crypto, shares, price):
    buy_investment  = ('INSERT INTO Investment '
                        '(InvestorId, CryptocurrencyId, NumShares, PurchasePrice, StillOwned) '
                        'VALUES (%s, %s, %s, %s, 1);'
                        % (investor, crypto, shares, price))
    cursor.execute(buy_investment)
    connection.commit()

    return buy_investment

def main():
    establish_con()
    print(buy(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4]))
    close_con()

main()
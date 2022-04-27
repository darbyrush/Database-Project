# Takes the ID of a cryptocurrency from webpage.php and returns all investors who own shares of that crypto
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

def view_investments(id):
    view_investment = ('SELECT (CurrentValue * NumShares) AS TotalValue, CryptoName '
                    'FROM  ('
                        'SELECT InvestorId, CurrentValue, NumShares, CryptoName FROM '
                        'Investment INNER JOIN '
                        'Cryptocurrency ON '
                        'Investment.CryptocurrencyId = Cryptocurrency.CryptocurrencyId '
                        'ORDER BY PurchasePrice '
                    ') AS A '
                    'WHERE A.InvestorId = %s '
                    'ORDER BY TotalValue DESC'
                    (id))
    cursor.execute(view_investment)

def main():
    establish_con()
    view_investments(sys.argv[1])
    close_con()
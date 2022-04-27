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

def view_investors(id):
    view_investors = ('SELECT Name, SUM(CurrentValue) as TotalShares '
                    'FROM  ('
                        'SELECT InvestorId, CurrentValue, NumShares, Cryptocurrency.CryptocurrencyId FROM'
                        'Investment INNER JOIN'
                        'Cryptocurrency ON'
                        'Investment.CryptocurrencyId = Cryptocurrency.CryptocurrencyId'
                        'ORDER BY PurchasePrice'
                    ') AS A'
                    'LEFT JOIN Investor'
                    'on A.InvestorId = Investor.InvestorId'
                    'WHERE CryptocurrencyId = %s'
                    'GROUP BY Name'
                    (id))
    cursor.execute(view_investors)

def main():
    establish_con()
    view_investors(sys.argv[1])
    close_con()
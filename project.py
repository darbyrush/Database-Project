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

def new_investor(id, name, email):
    add_investor = ('INSERT INTO Investors '
                    '(InvestorId, Name, Email) '
                    'VALUES (%s, %s, %s)'
                    (id, name, email))
    cursor.execute(add_investor)

def new_crypto(id, name, value):
    add_cryptocurrency = ('INSERT INTO Cryptocurrency '
                        '(CryptocurrencyId, CryptoName, CurrentValue) '
                        'VALUES (%s, %s, %s)'
                        (id, name, value))
    cursor.execute(add_cryptocurrency)

def buy(investor, crypto, shares, price, owned):
    buy_investment  = ('INSERT INTO Investment '
                        '(InvestorId, CryptocurrencyId, NumShares, PurchasePrice, StillOwned) '
                        'VALUES (%s, %s, %s, %s, %s)'
                        (investor, crypto, shares, price, owned))
    cursor.execute(buy_investment)

def sell(shares, price, owned):
    sell_investment = ('UPDATE Investment '
                    'SET (NumShares, PurchasePrice, StillOwned) '
                    'VALUES (%s, %s, %s)'
                    (shares, price, owned))
    cursor.execute(sell_investment)

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
    pass
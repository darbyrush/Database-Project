from mysql.connector import *

try:
    # Set connection to the database
    with connect(
        # Enter mySQL credentials
        user='abflynn',
        password='Pex9oof6',
        host='125.1.1.1',
    ) as connection:
        print(connection)

        # Queries for each user option
        add_investor = ('INSERT INTO Investors '
                        '(InvestorId, Name, Email) '
                        'VALUES (%s, %s, %s)')

        add_cryptocurrency = ('INSERT INTO Cryptocurrency '
                            '(CryptocurrencyId, CryptoName, CurrentValue) '
                            'VALUES (%s, %s, %s)')

        buy_investment  = ('INSERT INTO Investment '
                            '(InvestorId, CryptocurrencyId, NumShares, PurchasePrice, StillOwned) '
                            'VALUES (%s, %s, %s, %s, %s)')

        sell_investment = ('UPDATE Investment '
                            'SET (NumShares, PurchasePrice, StillOwned) '
                            'VALUES (%s, %s, %s)')

        view_investment = ('SELECT (CurrentValue * NumShares) AS TotalValue, CryptoName '
                            'FROM  ('
                                'SELECT InvestorId, CurrentValue, NumShares, CryptoName FROM '
                                'Investment INNER JOIN '
                                'Cryptocurrency ON '
                                'Investment.CryptocurrencyId = Cryptocurrency.CryptocurrencyId '
                                'ORDER BY PurchasePrice '
                            ') AS A '
                            'WHERE A.InvestorId = %s '
                            'ORDER BY TotalValue DESC')

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
                            'GROUP BY Name')

        

# Display connection error if there is one
except Error as e:
    print(e)
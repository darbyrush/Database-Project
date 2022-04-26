create table Investor(
	InvestorId		int,
    Name			char(50) not null,
    Email			varchar(50) not null,
    primary key(InvestorId)
    );

select * from Investor;

create table Cryptocurrency(
	CryptocurrencyId	int,
    CryptoName			char(50) not null,
    CurrentValue		int, check(CurrentValue>=0),
    primary key(CryptocurrencyId)
    );
    
select * from Cryptocurrency;

create table Investment(
	InvestorId			int,
    CryptocurrencyId	int,
    NumShares			int,
    PurchasePrice		float,
    StillOwned			boolean,
    primary key(InvestorId, CryptocurrencyId),
    foreign key(InvestorId) references Investor(InvestorId),
    foreign key(CryptocurrencyId) references Cryptocurrency(CryptocurrencyId)
    );
    
select * from Investment;

SELECT (CurrentValue * NumShares) AS TotalValue, CryptoName 
FROM  (
    SELECT InvestorId, CurrentValue, NumShares, CryptoName FROM
    Investment INNER JOIN
    Cryptocurrency ON
    Investment.CryptocurrencyId = Cryptocurrency.CryptocurrencyId
    ORDER BY PurchasePrice
) AS A
WHERE A.InvestorId = 1
ORDER BY TotalValue DESC;

SELECT Name, SUM(NumShares) AS TotalShares 
FROM  (
    SELECT InvestorId, NumShares, CryptoName, Cryptocurrency.CryptocurrencyId FROM
    Investment INNER JOIN
    Cryptocurrency ON
    Investment.CryptocurrencyId = Cryptocurrency.CryptocurrencyId
    ORDER BY PurchasePrice
) AS A
LEFT JOIN Investor
on A.InvestorId = Investor.InvestorId
WHERE CryptocurrencyId = 47
GROUP BY Name;
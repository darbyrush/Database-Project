# Adds investor info from webpage.php into Investor table
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

def new_investor(id, name, email):
    add_investor = ('INSERT INTO Investors '
                    '(InvestorId, Name, Email) '
                    'VALUES (%s, %s, %s)'
                    (id, name, email))
    cursor.execute(add_investor)

def main():
    establish_con()
    new_investor(sys.argv[0], sys.argv[1], sys.argv[2])
    close_con()
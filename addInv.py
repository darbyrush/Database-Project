# Adds investor info from webpage.php into Investor table
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

def new_investor(id, name, email):
    add_investor = ("INSERT INTO Investor "
                    "(InvestorId, Name, Email) "
                    "VALUES (%s, '%s', '%s');"
                     % (id, name, email))
    cursor.execute(add_investor)
    connection.commit()

    return add_investor

def main():
    establish_con()
    (id, name, email) = tuple(sys.argv[1:])
    print(new_investor(id, name, email))
    close_con()

main()
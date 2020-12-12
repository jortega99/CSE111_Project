from project import closeConnection, dropTable, openConnection
import sqlite3
from sqlite3 import Error
from pathlib import Path

def openConnection(_dbFile):
    conn = None
    try:
        conn = sqlite3.connect(_dbFile)
        print("Success")
    except Error as e:
        print(e)
    
    return conn

def closeConnection(_conn, _dbFile):
    print("Close database: ", _dbFile)

    try:
        _conn.close()
        print("success")
    except Error as e:
        print(e)

def Q1(conn):
    print("Q1")

def Q2(conn):
    print("Q2")

def Q3(conn):
    print("Q3")

def Q4(conn):
    print("Q4")

def Q5(conn):
    print("Q5")

def Q6(conn):
    print("Q6")

def Q7(conn):
    print("Q7")

def Q8(conn):
    print("Q8")

def Q9(conn):

def Q10(conn):
    
def Q11(conn):

def Q12(conn):

def Q13(conn):

def Q14(conn):

def Q15(conn):

def Q16(conn):

def Q17(conn):

def Q18(conn):

def Q19(conn):

def Q20(Conn):


def main():
    database = r"project.db"

    conn = openConnection(database)
    with conn:
        Q1(conn)
        Q2(conn)
        Q3(conn)
        Q4(conn)
        Q5(conn)
        Q6(conn)
        Q7(conn)
        Q8(conn)
        Q9(conn)
        Q10(conn)
        Q11(conn)
        Q12(conn)
        Q13(conn)
        Q14(conn)
        Q15(conn)
        Q16(conn)
        Q17(conn)
        Q18(conn)
        Q19(conn)
        Q20(conn)
        Q21(conn)
    
    closeConnection(conn,database)

if __name__ == '__main__':
    main()
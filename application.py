import sqlite3
from sqlite3 import Error
from pathlib import Path
import os
clear = lambda: os.system('clear')

def openConnection(_dbFile):

    conn = None
    try:
        conn = sqlite3.connect(_dbFile)
        print("success")
    except Error as e:
        print(e)

    return conn

def closeConnection(_conn):

    try:
        _conn.close()
        print("success")
    except Error as e:
        print(e)

def CPUList(_conn):
    print('CPU List')

    try:
        sql = """SELECT *
                FROM CPU"""

        cur = _conn.cursor()
        cur.execute(sql)

        rows = cur.fetchall()

        l = '{:<10} {:<50} {:<10} {:<12} {:<10} {:<10} {:<10}'.format("ID", "Name", "Price", "Manufacturer", "Corecount", "Coreclock", "Boostclock")
        print(l)
        for row in rows:
            l = '{:<10} {:<50} {:<10} {:<12} {:<10} {:<10} {:<10}'.format(row[0],row[1], row[2], row[3],row[4],row[5],row[6])
            print(l)
    except Error as e:
        print(e)

def GPUList(_conn):
    try:
        sql = """SELECT *
                FROM GPU"""

        cur = _conn.cursor()
        cur.execute(sql)

        rows = cur.fetchall()

        l = '{:<10} {:<70} {:<10} {:<15} {:<25} {:<10} {:<10}'.format("ID", "Name", "Price", "Manufacturer", "Chipset", "Memory", "Coreclock",  "Boostclock")
        print(l)
        for row in rows:
            l = '{:<10} {:<70} {:<10} {:<15} {:<25} {:<10} {:<10}'.format(row[0],row[1], row[2], row[3],row[4], row[5], row[6], row[7])
            print(l)
    except Error as e:
        print(e)

def MotherboardList(_conn):
    try:
        sql = """SELECT *
                FROM Motherboard"""

        cur = _conn.cursor()
        cur.execute(sql)

        rows = cur.fetchall()

        l = '{:<10} {:<60} {:<10} {:<13}  {:<10} {:<10}'.format("ID", "Name", "Price", "Manufacturer", "Socket", "Formfactor")
        print(l)
        for row in rows:
            l = '{:<10} {:<60} {:<10} {:<13}  {:<10} {:<10}'.format(row[0],row[1], row[2], row[3],row[4], row[5])
            print(l)
    except Error as e:
        print(e)

def RamList(_conn):
    try:
        sql = """SELECT *
                FROM RAM"""

        cur = _conn.cursor()
        cur.execute(sql)

        rows = cur.fetchall()

        l = '{:<10} {:<70} {:<10} {:<15} {:<15} {:<10}'.format("ID", "Name", "Price", "Manufacturer", "Speed", "Modules")
        print(l)
        for row in rows:
            l = '{:<10} {:<70} {:<10} {:<15} {:<15} {:<10}'.format(row[0],row[1], row[2], row[3],row[4], row[5])
            print(l)
    except Error as e:
        print(e)

def StorageList(_conn):
    try:
        sql = """SELECT *
                FROM Storage"""

        cur = _conn.cursor()
        cur.execute(sql)

        rows = cur.fetchall()

        l = '{:<10} {:<70} {:<10} {:<20} {:<10} {:<10}'.format("ID", "Name", "Price", "Manufacturer", "Capacity", "Type")
        print(l)
        for row in rows:
            l = '{:<10} {:70} {:<10} {:<20} {:<10} {:<10}'.format(row[0],row[1], row[2], row[3],row[4], row[5])
            print(l)
    except Error as e:
        print(e)

def PSUList(_conn):
    try:
        sql = """SELECT *
                FROM PSU"""

        cur = _conn.cursor()
        cur.execute(sql)

        rows = cur.fetchall()

        l = '{:<10} {:<80} {:<10} {:<15} {:<15} {:<10} {:<15} {:<10}'.format("ID", "Name", "Price", "Manufacturer", "Formfactor", "Wattage", "Efficiency", "Modularity")
        print(l)
        for row in rows:
            l = '{:<10} {:<80} {:<10} {:<15} {:<15} {:<10} {:<15} {:<10}'.format(row[0],row[1], row[2], row[3],row[4], row[5], row[6], row[7])
            print(l)
    except Error as e:
        print(e)

def TowerList(_conn):
    try:
        sql = """SELECT *
                FROM Tower"""

        cur = _conn.cursor()
        cur.execute(sql)

        rows = cur.fetchall()

        l = '{:<10} {:<80} {:<10} {:<20} {:<10}'.format("ID", "Name", "Price", "Manufacturer", "Modules")
        print(l)
        for row in rows:
            l = '{:<10} {:<80} {:<10} {:<20} {:<10}'.format(row[0],row[1], row[2], row[3],row[4])
            print(l)
    except Error as e:
        print(e)

def createBuild(_conn, usr):
    try:
        cpu = input('Enter CPU id: ')
        gpu = input('Enter GPU id: ')
        mb = input('Enter Motherboard id: ')
        ram = input('Enter RAM id: ')
        storage = input('Enter Storage id: ')
        psu = input('Enter PSU id: ')
        tower = input('Enter Case id: ')

        busr = usr
        bcode = usr + '_' + str(1)

        args = [cpu,gpu,mb,psu,storage,tower,ram]

        sql = """SELECT CPU_name, GPU_name, MB_name, PSU_name, Storage_name, Case_name, RAM_name
                 FROM CPU,GPU,Motherboard,PSU,Storage,Tower,RAM
                 WHERE CPU_id = ? AND GPU_id = ? AND MB_id = ? AND PSU_id = ? AND Storage_id = ? AND Case_id = ? AND RAM_id = ?"""

        cur = _conn.cursor()
        cur.execute(sql,args)

        rows = cur.fetchall()

        #print(rows[0][0])
        arr = [busr,bcode,rows[0][0],rows[0][1],rows[0][2],rows[0][3],rows[0][4],rows[0][5],rows[0][6]]

        sql = """INSERT INTO Build(b_user,b_code,b_cpu,b_gpu,b_motherboard,b_psu,b_storage,b_tower,b_ram)
                 VALUES(?,?,?,?,?,?,?,?,?)"""

        _conn.execute(sql,arr)
        _conn.commit()

    except Error as e:
        print(e)


def deleteBuild(_conn, usr):
    try:
        sql = """SELECT u_password
                 FROM Users
                 WHERE u_name = ?"""
        cur = _conn.cursor()
        cur.execute(sql,(usr,))
        users = cur.fetchall()

    except Error as e:
        print(e)

    id = input('Enter Build Code: ')
    pwd = input('Enter password: ')

    if pwd == users[0][0]:
        try:
            sql = """DELETE FROM Build
                     WHERE b_code = ?"""
            _conn.execute(sql,(id,))
            _conn.commit()
        except Error as e:
            print(e)

def deleteUser(_conn, usr):
    try:
        sql = """SELECT u_password
                 FROM Users
                 WHERE u_name = ?"""
        cur = _conn.cursor()
        cur.execute(sql,(usr,))
        users = cur.fetchall()

    except Error as e:
        print(e)
    print(users[0][0])
    pwd = input('Enter password: ')

    if pwd == users[0][0]:
        print('Matches')
        try:
            sql = """DELETE FROM Users
                     WHERE u_name = ?"""
            _conn.execute(sql,(usr,))
            _conn.commit()
        except Error as e:
            print(e)

def login(_conn):
    print('Login?: 1')
    print('Sign up: 0')

   # arr =[]

    try:
        sql = """SELECT *
                 FROM Users"""
        cur = _conn.cursor()
        cur.execute(sql)
        arr = cur.fetchall()
    except Error as e:
        print(e)

    choice = int(input())
    if choice ==  0:

        while True:
            x = 0
            count = 0
            name = input('Enter username:')
            pwd = input('Enter password:')
            for i in arr:
                count += 1
                if name == i[0]:
                    x = 1
                    count = 0
                    print('Username taken')
                    break

            if count == len(arr):
                break

        try:
            sql = """Insert into Users
                     values(?,?)"""
            args = [name,pwd]
            _conn.execute(sql,args)
            _conn.commit()
            print("Account Created")
            return (True, name)
        except Error as e:
            print(e)
    elif choice == 1:
        usr = input('Enter username: ')
        pwd = input('Enter password: ')
        try:
            sql = """SELECT*
                     FROM Users
                     WHERE u_name = ?"""
            cur = _conn.cursor()
            cur.execute(sql,(usr,))

            rows = cur.fetchall()

            for i in rows:
                if usr == i[0] and pwd == i[1]:
                    print('Print logged in as: ', usr)
                    return (True, usr)
            print('Wrong username or password')
            return (False,usr)
        except Error as e:
            print(e)

def main():
    database = r"project.db"

    # create a database connection
    conn = openConnection(database)
    with conn:
        clear()
        loggedin = login(conn)
        #print(loggedin[0],loggedin[1])

        if(loggedin[0]):
            while True:
                i = int(input())

                if(i == 1):
                    clear()
                    CPUList(conn)
                elif(i == 2):
                    clear()
                    GPUList(conn)
                elif(i == 3):
                    clear()
                    MotherboardList(conn)
                elif(i == 4):
                    clear()
                    RamList(conn)
                elif(i == 5):
                    clear()
                    StorageList(conn)
                elif(i == 6):
                    clear()
                    PSUList(conn)
                elif(i == 7):
                    clear()
                    TowerList(conn)
                elif(i == 8):
                    createBuild(conn, loggedin[1])
                elif(i == 9):
                    deleteBuild(conn, loggedin[1])
                elif(i == 10):
                    deleteUser(conn, loggedin[1])
                else:
                    break
        
    closeConnection(conn)


if __name__ == '__main__':
    main()

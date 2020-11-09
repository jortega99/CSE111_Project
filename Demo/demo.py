from os import error
import sqlite3
from sqlite3 import Error
from pathlib import Path


def openConnection(_dbFile):
    print("Open database: ", _dbFile)

    conn = None
    try:
        conn = sqlite3.connect(_dbFile)
        print("success")
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

#---------------Insert Modification Statemants----------------

#Insert CPU
def Q1(_conn):

    one = ""
    two = ""
    three = ""
    four = ""
    five = ""
    six = ""
    with open("Demo/Data/CPUDemo.csv", "r") as f:
        for i, x in enumerate(f):
            if i == 0:
                stripped_line = x.rstrip()
                one += stripped_line
            elif i == 1:
                stripped_line = x.rstrip()
                two += stripped_line
            elif i == 2:
                line = x.rstrip()
                three += line
            elif i == 3:
                line =  x.rstrip()
                four += line
            elif i == 4:
                line = x.rstrip()
                five += line
            elif i == 5:
                line = x.rstrip()
                six = line
    try: 
        sql = """insert into CPU
                values (?,?,?,?,?,?)"""
        args = [one,two,three,four,five,six]
        _conn.execute(sql,args)
        _conn.commit()
        print("Success")
    except Error as e:
        print(e)

#Insert Case
def Q2(_conn):
    one = ""
    two = ""
    three = ""
    four = ""
    with open("Demo/Data/CaseDemo.csv", "r") as f:
        for i, x in enumerate(f):
            if i == 0:
                stripped_line = x.rstrip()
                one += stripped_line
            elif i == 1:
                stripped_line = x.rstrip()
                two += stripped_line
            elif i == 2:
                line = x.rstrip()
                three += line
            elif i == 3:
                line =  x.rstrip()
                four += line

    try: 
        sql = """insert into Tower
                values (?,?,?,?)"""
        args = [one,two,three,four]
        _conn.execute(sql,args)
        _conn.commit()
        print("Success")
    except Error as e:
        print(e)

#Insert GPU
def Q3(_conn):
    one = ""
    two = ""
    three = ""
    four = ""
    five = ""
    six = ""
    seven = ""
    with open("Demo/Data/GPUDemo.csv", "r") as f:
        for i, x in enumerate(f):
            if i == 0:
                stripped_line = x.rstrip()
                one += stripped_line
            elif i == 1:
                stripped_line = x.rstrip()
                two += stripped_line
            elif i == 2:
                line = x.rstrip()
                three += line
            elif i == 3:
                line =  x.rstrip()
                four += line
            elif i == 4:
                line = x.rstrip()
                five += line
            elif i == 5:
                line = x.rstrip()
                six = line
            elif i == 6:
                line = x.rstrip()
                seven = line
    try: 
        sql = """insert into GPU
                values (?,?,?,?,?,?,?)"""
        args = [one,two,three,four,five,six,seven]
        _conn.execute(sql,args)
        _conn.commit()
        print("Success")
    except Error as e:
        print(e)

#Insert MotherBoard
def Q4(_conn):
    one = ""
    two = ""
    three = ""
    four = ""
    five = ""
    with open("Demo/Data/MBDemo.csv", "r") as f:
        for i, x in enumerate(f):
            if i == 0:
                stripped_line = x.rstrip()
                one += stripped_line
            elif i == 1:
                stripped_line = x.rstrip()
                two += stripped_line
            elif i == 2:
                line = x.rstrip()
                three += line
            elif i == 3:
                line =  x.rstrip()
                four += line
            elif i == 4:
                line = x.rstrip()
                five += line
    try: 
        sql = """insert into MotherBoard
                values (?,?,?,?,?)"""
        args = [one,two,three,four,five]
        _conn.execute(sql,args)
        _conn.commit()
        print("Success")
    except Error as e:
        print(e)

#insert PSU
def Q5(_conn):
    one = ""
    two = ""
    three = ""
    four = ""
    five = ""
    six = ""
    seven = ""
    with open("Demo/Data/PSUDemo.csv", "r") as f:
        for i, x in enumerate(f):
            if i == 0:
                stripped_line = x.rstrip()
                one += stripped_line
            elif i == 1:
                stripped_line = x.rstrip()
                two += stripped_line
            elif i == 2:
                line = x.rstrip()
                three += line
            elif i == 3:
                line =  x.rstrip()
                four += line
            elif i == 4:
                line = x.rstrip()
                five += line
            elif i == 5:
                line = x.rstrip()
                six = line
            elif i == 6:
                line = x.rstrip()
                seven = line
    try: 
        sql = """insert into PSU
                values (?,?,?,?,?,?,?)"""
        args = [one,two,three,four,five,six,seven]
        _conn.execute(sql,args)
        _conn.commit()
        print("Success")
    except Error as e:
        print(e)

#Insert RAM
def Q6(_conn):
    one = ""
    two = ""
    three = ""
    four = ""
    five = ""
    with open("Demo/Data/RAMDemo.csv", "r") as f:
        for i, x in enumerate(f):
            if i == 0:
                stripped_line = x.rstrip()
                one += stripped_line
            elif i == 1:
                stripped_line = x.rstrip()
                two += stripped_line
            elif i == 2:
                line = x.rstrip()
                three += line
            elif i == 3:
                line =  x.rstrip()
                four += line
            elif i == 4:
                line = x.rstrip()
                five += line
    try: 
        sql = """insert into RAM
                values (?,?,?,?,?)"""
        args = [one,two,three,four,five]
        _conn.execute(sql,args)
        _conn.commit()
        print("Success")
    except Error as e:
        print(e)

#insert storage
def Q7(_conn):
    one = ""
    two = ""
    three = ""
    four = ""
    five = ""
    with open("Demo/Data/StorageDemo.csv", "r") as f:
        for i, x in enumerate(f):
            if i == 0:
                stripped_line = x.rstrip()
                one += stripped_line
            elif i == 1:
                stripped_line = x.rstrip()
                two += stripped_line
            elif i == 2:
                line = x.rstrip()
                three += line
            elif i == 3:
                line =  x.rstrip()
                four += line
            elif i == 4:
                line = x.rstrip()
                five += line
    try: 
        sql = """insert into Storage
                values (?,?,?,?,?)"""
        args = [one,two,three,four,five]
        _conn.execute(sql,args)
        _conn.commit()
        print("Success")
    except Error as e:
        print(e)

#insert user
def Q8(_conn):
    name = input("Enter your username: ")
    pwd = input("Enter your password: ")

    #print(one, two, sep=",")
    try:
        sql = """insert into Users
                values (?, ?)"""
        args = [name,pwd]
        _conn.execute(sql,args)
        _conn.commit()
    except Error as e:
        print(e)

def Q9(_conn):
    try:
        sql ="""insert into Build (b_cpu, b_gpu, b_motherboard, b_ram, b_storage, b_psu, b_tower)
                values ('Intel Core i5-4460 3.2 GHz Quad-Core Processor',
                        'EVGA GeForce GTX 1060 3GB 3 GB SC GAMING Video Card',
                        'Gigabyte GA-Z97X-Gaming 3 ATX LGA1150 Motherboard',
                        'Crucial Ballistix Sport 8 GB (2 x 4 GB) DDR3-1600 CL9 Memory',
                        'Kingston HyperX Fury 120 GB 2.5" Solid State Drive',
                        'Corsair RM 750 W 80+ Gold Certified Fully Modular ATX Power Supply',
                        'NZXT H510i ATX Mid Tower Case');"""
        _conn.execute(sql)
        _conn.commit()
    except Error as e:
        print(e)
#-------------------Updating Statements------------------
def Q10(_conn):
    try:
        sql = """update Build
                set b_user = 'girizarrytorres', b_code = 'L7ZX72L6'
                where b_cpu = 'Intel Core i5-4460 3.2 GHz Quad-Core Processor'"""
        _conn.execute(sql)
        _conn.commit()
    except Error as e:
        print(e)

def Q11(_conn):
    try:
        sql = """update Build
                set b_price = (select sum(x.price) as total
                from Build,
                (
                    select CPU_price as price
                    from CPU
                    where CPU_name = b_cpu
                    union all
                    select GPU_price
                    from GPU
                    where GPU_name = b_gpu
                    union all
                    select MB_price
                    from MotherBoard
                    where MB_name = b_motherboard
                    union all
                    select RAM_price
                    from RAM
                    where RAM_name = b_ram
                    union all
                    select Storage_price
                    from Storage
                    where Storage_name = b_storage
                    union all
                    select PSU_price
                    from PSU
                    where PSU_name = b_psu
                    union all
                    select Case_price
                    from Tower
                    where Case_name = b_tower
                ) x) 
                where b_code = 'L7ZX72L6'"""
        _conn.execute(sql)
        _conn.commit()
    except Error as e:
        print(e)

def Q12(_conn):
    try:
        sql = """update PSU
                set PSU_price = 80.00
                where PSU_name = 'Corsair RM (2019) 750 W 80+ Gold Certified Fully Modular ATX Power Supply'"""
        _conn.execute(sql)
        _conn.commit()
    except Error as e:
        print(e)

def Q13(_conn):
    username = input("Username: ")
    pwd = input("Password: ")
    newpwd = input("New password: ")

    try:
        sql = """update Users
                 set u_password = ?
                 where u_name = ? AND u_password = ?"""
        args = [newpwd, username, pwd]
        _conn.execute(sql,args)
        _conn.commit()
    except Error as e:
        print(e)

def Q14(_conn):
    try:
        sql = """UPDATE Build
                 set b_cpu = 'AMD Ryzen 5 3600 3.6 GHz 6-Core Processor'
                 WHERE b_code = 'L7ZX72L6'"""
        _conn.execute(sql)
        _conn.commit()
    except Error as e:
        print(e)

def Q15(_conn):
    try:
        sql = """UPDATE Build
                set b_gpu = ""
                WHERE b_code = 'L7ZX72L6'"""
        _conn.execute(sql)
        _conn.commit()
    except Error as e:
        print(e)

def Q16(_conn):
    try:
        sql = """Update Build
                set b_gpu = 'MSI GeForce RTX 2080 Ti 11 GB GAMING X TRIO Video Card'
                WHERE b_code = 'L7ZX72L6'"""
        _conn.execute(sql)
        _conn.commit()
    except Error as e:
        print(e)

def Q17(_conn):
    try:
        sql = """Update Build
                set b_motherboard ='MSI Z390-A PRO ATX LGA1151 Motherboard'
                WHERE b_code = 'L7ZX72L6'"""
        _conn.execute(sql)
        _conn.commit()
    except Error as e:
        print(e)

def Q18(_conn):
    usr = input("Enter username: ")
    pwd = input("Enter password: ")

    try:
        sql = """delete from Users
                 where u_name = ? and u_password = ?"""
        args = [usr,pwd]
        _conn.execute(sql,args)
        _conn.commit()
    except Error as e:
        print(e)

def Q19(_conn):
    busr = input("Enter username: ")
    bcode = input("Enter build code: ")

    try:
        sql = """delete from Build
                 where b_user = ? and b_code = ?"""
        args = [busr,bcode]
        _conn.execute(sql,args)
        _conn.commit()
    except Error as e:
        print(e)

def Q20(_conn):
    try:
        sql = """delete from RAM
                WHERE RAM_name = 'Crucial Ballistix Sport 8 GB (2 x 4 GB) DDR3-1600 CL9 Memory'"""
        _conn.execute(sql)
        _conn.commit()
    except Error as e:
        print(e)

def main():
    database = r"project.db"

    # create a database connection
    conn = openConnection(database)
    with conn:
        Q1(conn)

    closeConnection(conn, database)


if __name__ == '__main__':
    main()
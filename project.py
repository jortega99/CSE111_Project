import sqlite3
from sqlite3 import Error
from pathlib import Path
import sys
original = sys.stdout

def openConnection(_dbFile):
    print("++++++++++++++++++++++++++++++++++")
    print("Open database: ", _dbFile)

    conn = None
    try:
        conn = sqlite3.connect(_dbFile)
        print("success")
    except Error as e:
        print(e)

    print("++++++++++++++++++++++++++++++++++")

    return conn

def closeConnection(_conn, _dbFile):
    print("++++++++++++++++++++++++++++++++++")
    print("Close database: ", _dbFile)

    try:
        _conn.close()
        print("success")
    except Error as e:
        print(e)

    print("++++++++++++++++++++++++++++++++++")


def createTable(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Create table")

    try:
        sql = """CREATE TABLE CPU (
                CPU_name VARCHAR(60) not null,
                CPU_price decimal(7, 2) not null,
                CPU_manufactuer VARCHAR(10) not null,
                CPU_corecount Decimal(2,0) not null,
                CPU_coreclock VARCHAR(10) not null,
                CPU_boostclock VARCHAR(10) not null)"""
        _conn.execute(sql)

        sql = """CREATE TABLE GPU (
                GPU_name VARCHAR(60) not null,
                GPU_price decimal(7, 2) not null,
                GPU_manufactuer VARCHAR(10) not null,
                GPU_chipset VARCHAR(30) not null,
                GPU_memory VARCHAR(5) not null,
                GPU_boostclock VARCHAR(10) not null,
                GPU_coreclock VARCHAR(10) not null)"""
        _conn.execute(sql)

        sql = """CREATE TABLE MotherBoard (
                MB_name VARCHAR(60) not null,
                MB_price decimal(7, 2) not null,
                MB_manufactuer VARCHAR(10) not null,
                MB_socket VARCHAR(10) not null,
                MB_formfactor VARCHAR(10) not null)"""
        _conn.execute(sql)

        sql = """CREATE TABLE PSU (
                PSU_name VARCHAR(60) not null,
                PSU_price decimal(7, 2) not null,
                PSU_manufactuer VARCHAR(10) not null,
                PSU_formfactor VARCHAR(10) not null,
                PSU_wattage VARCHAR(6) not null,
                PSU_efficiency VARCHAR(10) not null,
                PSU_modularity VARCHAR(5) not null)"""
        _conn.execute(sql)

        sql = """CREATE TABLE Storage (
                Storage_name VARCHAR(100) not null,
                Storage_price decimal(7, 2) not null,
                Storage_manufactuer VARCHAR(10) not null,
                Storage_capacity VARCHAR(30) not null,
                Storage_type VARCHAR(10) not null,
                Storage_cache VARCHAR(10) not null)"""
        _conn.execute(sql)

        sql = """CREATE TABLE Tower (
                Case_name VARCHAR(60) not null,
                Case_price decimal(7, 2) not null,
                Case_manufactuer VARCHAR(10) not null,
                Case_formfactor VARCHAR(10) not null)"""
        _conn.execute(sql)

        _conn.commit()
        print("success")
    except Error as e:
        _conn.rollback()
        print(e)
        


    print("++++++++++++++++++++++++++++++++++")


def dropTable(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Drop tables")

    try:
        sql = """ DROP TABLE CPU """
        _conn.execute(sql)

        sql = """ DROP TABLE GPU """
        _conn.execute(sql)

        sql = """ DROP TABLE MotherBoard """
        _conn.execute(sql)

        sql = """ DROP TABLE PSU """
        _conn.execute(sql)

        sql = """ DROP TABLE Storage """
        _conn.execute(sql)

        sql = """ DROP TABLE Tower """
        _conn.execute(sql)

        print("Success")
    except Error as e:
        _conn.rollback()
        print(e)

    print("++++++++++++++++++++++++++++++++++")


def populateTable(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Populate table")


    print("++++++++++++++++++++++++++++++++++")

def main():
    database = r"project.db"

    # create a database connection
    conn = openConnection(database)
    with conn:
        dropTable(conn)
        createTable(conn)
        #populateTable(conn)

    closeConnection(conn, database)


if __name__ == '__main__':
    main()

import sqlite3

# SQLite DB Name
DB_Name =  "IoT.db"

tableS1 = "charger_s1"
tableS2 = "charger_s2"
tableDevice = "charger_device"

def createDB(s1Name, s2Name, deviceName):
    # SQLite DB Table Schema
    TableSchema=f"""
    drop table if exists {s1Name} ;
    create table {s1Name} (
    id integer primary key autoincrement,
    productId INTEGER,
    Status INTEGER,
    SN TEXT,
    Time TEXT,
    SoC INTEGER,
    SoH INTEGER,
    Volt REAL
    );

    drop table if exists {s2Name} ;
    create table {s2Name} (
    id integer primary key autoincrement,
    productId INTEGER,
    Status INTEGER,
    SN TEXT,
    Time TEXT,
    SoC INTEGER,
    SoH INTEGER,
    Volt REAL
    );

    drop table if exists {deviceName} ;
    create table {deviceName} (
    id integer primary key autoincrement,
    productId INTEGER,
    chargeMode INTEGER,
    MCC INTEGER,
    MNC INTEGER,
    LAC INTEGER,
    CellID INTEGER
    );
    """

    #Connect or Create DB File
    conn = sqlite3.connect(DB_Name)
    curs = conn.cursor()

    #Create Tables
    sqlite3.complete_statement(TableSchema)
    curs.executescript(TableSchema)

    #Close DB
    curs.close()
    conn.close()

createDB(tableS1, tableS2, tableDevice)
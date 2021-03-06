from scrap_by_type import *
import sqlite3
from sqlite3 import Error


def create_connection(db_file):
    conn = None
    try :
        conn = sqlite3.connect(db_file)
        print(sqlite3.version)
    except Error as e :
        print(e)
    return conn


def add_anime(conn, anime):
    #listT = ['action','toz']
    sql ='''
    INSERT INTO animes_animes(title,animePageLink,pageNum,coverLink,yearProd,rates,types,story) VALUES(?,?,?,?,?,?,?,?)
    '''
    cur = conn.cursor()
    cur.execute(sql, anime)
    return cur.lastrowid


#THIS WILL BE  ON OUR CLASS INIT APRES
DATA = RunScraper() # get or DATA
CLEAR()
print("SAVING DATA TO DATABASE : ")

con = create_connection('db.sqlite3')
cnt = 1
with con:
    for key in DATA.keys() :

        typesStr = ''
        lenOfT = len(DATA[key][5])
        for i in range(lenOfT):
            if i == lenOfT - 1 :
                typesStr += str(DATA[key][5][i])
            else :
                typesStr += str(DATA[key][5][i])+','

        anime = (str(key),DATA[key][0],DATA[key][1],DATA[key][2],DATA[key][3],DATA[key][4],typesStr,DATA[key][6])
        print("["+str(cnt)+"] +=> "+key+" ...... SAVED")
        cur = add_anime(con,anime)

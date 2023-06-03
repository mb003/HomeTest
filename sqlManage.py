# -*- coding: utf-8 -*-


import MySQLdb
import MySQLdb.cursors

class SQLManagement:

    def __init__(self, host = 'localhost', port = 3306, user = 'root', password = 'root', db = 'localhost'):
        self.host         = host
        self.port         = port
        self.user         = user
        self.password     = password
        self.db           = db
        
        self.conn         = MySQLdb.connect(
                                host     = self.host,
                                port     = self.port,
                                user     = self.user,
                                passwd   = self.password,
                                db       = self.db,
                                charset  = 'utf8',
                                cursorclass = MySQLdb.cursors.DictCursor
                            )

    def delete(self, SQL = ""):
        cur = self.conn.cursor()
        cur.execute(SQL)
        cur.close()
        self.conn.commit()

    def update(self, SQL = ""):
        cur = self.conn.cursor()
        cur.execute(SQL)
        cur.close()
        self.conn.commit()

    def insert(self, SQL = ""):
        cur = self.conn.cursor()
        cur.execute(SQL)
        cur.close()
        self.conn.commit()

    def query(self, SQL = ""):
        cur = self.conn.cursor()
        cur.execute(SQL)
        res = cur.fetchall()
        cur.close()
        return res

    def closeConnection(self):
        self.conn.close()

    def connect(self, host = 'localhost', port = 3306, user = 'root', password = 'root', db = 'localhost'):
        self.host         = host
        self.port         = port
        self.user         = user
        self.password     = password
        self.db           = db
        self.conn         = MySQLdb.connect(
                                host     = self.host,
                                port     = self.port,
                                user     = self.user,
                                passwd   = self.password,
                                db       = self.db,
                                charset  = 'utf8',
                                cursorclass = MySQLdb.cursors.DictCursor
                            )
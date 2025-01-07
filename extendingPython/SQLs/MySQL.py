import pymysql
from dbutils.pooled_db import PooledDB


class DatabasePool:
    def __init__(self, db, mincached=2, maxcached=50, maxshared=0, maxconnections=100, blocking=True, setsession=[],
                 **config):
        self.config = config
        self.db = db
        self.pool = None
        self.mincached = mincached
        self.maxcached = maxcached
        self.maxshared = maxshared
        self.maxconnections = maxconnections
        self.blocking = blocking
        self.setsession = setsession

    def createPool(self):
        self.pool = PooledDB(creator=pymysql, mincached=self.mincached, maxcached=self.maxcached,
                             maxshared=self.maxshared,
                             maxconnections=self.maxconnections, blocking=self.blocking, setsession=self.setsession,
                             **self.config)
        return self.pool

    def getConnection(self):
        if self.pool is None:
            self.createPool()
        return self.pool.connection()

    def execute(self, sql):
        conn = self.getConnection()
        cur = conn.cursor()
        cur.execute(sql)
        data = cur.fetchall()
        cur.close()
        conn.close()
        return data

    def executeUpdate(self, sql):
        conn = self.getConnection()
        cur = conn.cursor()
        cur.execute(sql)
        conn.commit()
        cur.close()
        conn.close()

    def executeQuery(self, sql):
        conn = self.getConnection()
        cur = conn.cursor()
        cur.execute(sql)
        data = cur.fetchall()
        cur.close()
        conn.close()
        return data

    def close(self):
        if self.pool is not None:
            self.pool.close()
            self.pool = None

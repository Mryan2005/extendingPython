import pymysql


class SQLConn:
    def __init__(self, host, port, user, password, db):
        """
        这个函数用来连接数据库，由使用者传入数据库地址、用户名、密码、数据库名称 \n
        :param host: str, 数据库地址 \n
        :param user: str, 数据库用户名 \n
        :param password: str, 数据库密码 \n
        :param db: str, 数据库名称
        """
        self.db = db
        self.password = password
        self.user = user
        self.host = host
        self.port = port
        self.conn = pymysql.connect(host=self.host, port=self.port, user=self.user, passwd=self.password, db=self.db)

    def runSelect(self, sql):
        """
        这个函数用来执行查询操作，由使用者传入sql语句，返回查询结果 \n
        :param sql: str, sql语句 \n
        :return: 查询结果，返回一个列表，每个元素是一个字典，表示一条记录
        """
        cur = self.conn.cursor()
        cur.execute(sql)
        sqlData = cur.fetchall()
        cur.close()
        self.conn.close()
        self.conn = pymysql.connect(host=self.host, port=self.port, user=self.user, passwd=self.password, db=self.db)
        return sqlData

    def runUpdate(self, sql):
        """
        这个函数用来执行更新操作，比如插入、删除、更新等 \n
        :param sql: str, sql语句 \n
        :return: bool值，表示是否更新成功
        """
        cur = self.conn.cursor()
        cur.execute(sql)
        cur.close()
        self.conn.commit()
        self.conn.close()
        self.conn = pymysql.connect(host=self.host, port=self.port, user=self.user, passwd=self.password, db=self.db)

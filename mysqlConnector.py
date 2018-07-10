import pymysql
import pymysql.cursors
import config

class db:
    conn = False
    cur = False

    def __init__(self):
        self.conn = pymysql.connect(host=config.DATABASE_CONFIG['host'],
                                    db=config.DATABASE_CONFIG['dbname'],
                                    user=config.DATABASE_CONFIG['user'],
                                    passwd=config.DATABASE_CONFIG['password'],
                                    port=config.DATABASE_CONFIG['port'],
                                    charset='utf8',
                                    autocommit=True,
                                    cursorclass=pymysql.cursors.DictCursor)

    def __enter__(self):
        return self

    def select(self, sql):
        self.cur = self.conn.cursor()
        # print(cur.description)
        self.cur.execute(sql)
        return self.cur

    def __exit__(self, exc_type, exc_value, traceback):
        if (self.cur):
            self.cur.close()
        if (self.conn):
            self.conn.close()

    def insert(self, table, fieldsTulp):
        sql = ""
        for key, value in fieldsTulp.items():
            if sql:
                sql = sql + ", "
            value = value.replace("'", "\\'")
            # if value:
            sql = sql + key + "='" + value + "'"
        sql = "INSERT INTO " + table + " SET " + sql
        # print(sql)
        self.cur = self.conn.cursor()
        self.cur.execute(sql)
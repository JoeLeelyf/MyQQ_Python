
import pymysql

class DataBase:
    # change the default value of the parameters to your own, essential for the connection to the database
    def __init__(self, host="localhost", user="root", password="030209lyflqs", db="MyQQ", port=3306, charset='utf8'):
        self.host = host
        self.user = user
        self.password = password
        self.db = db
        self.port = port
        self.charset = charset

    def connect(self):
        self.conn = pymysql.connect(host=self.host, user=self.user, password=self.password, db=self.db, port=self.port, charset=self.charset)
        self.cursor = self.conn.cursor()

    def close(self):
        self.cursor.close()
        self.conn.close()

    def execute(self, sql, params=None):
        try:
            self.connect()
            self.cursor.execute(sql, params)
            self.conn.commit()
        except Exception as e:
            print(e)
            self.conn.rollback()
        finally:
            self.close()

    def query(self, sql, params=None):
        try:
            self.connect()
            self.cursor.execute(sql, params)
            return self.cursor.fetchall()
        except Exception as e:
            print(e)
        finally:
            self.close()

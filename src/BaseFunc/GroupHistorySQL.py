import BaseFunc.DataBase as DataBase
import time


class GroupHistorySQL:
    def __init__(self):
        self.db = DataBase.DataBase()

    def CreateGroupHistory(self, G_id, Name,content, capacity=500):
        size = self.db.query("select * from GroupHistory")
        Time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        id = len(size) + 1
        sql = "insert into GroupHistory(GH_ID,G_ID,U_Name,Time,content) values(%s,%s, %s,%s, %s)"
        self.db.execute(sql, (id, G_id,Name, Time, content))
        return id

    def __DeleteGroupHistory(self, id):
        sql = "delete from GroupHistory where GH_ID = %s"
        self.db.execute(sql, id)

    def QueryAll(self):
        sql = "select * from GroupHistory"
        return self.db.query(sql)


    def QueryGroupHistoryByG_id(self, G_id):
        sql = "select * from GroupHistory where G_ID = %s"
        return self.db.query(sql, G_id)

    

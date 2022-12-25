import BaseFunc.DataBase as DataBase
import time


class UserHistorySQL:
    def __init__(self) -> None:
        self.db = DataBase.DataBase()

    def CreateUserHistory(self, s_id, r_id, content):
        size = self.db.query("select * from UserHistory")
        Time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        id = len(size) + 1
        sql = "insert into UserHistory(UH_ID, S_ID, R_ID, Time, content) values(%s, %s, %s, %s, %s)"
        self.db.execute(sql, (id, s_id, r_id, Time, content))
        return id

    def __DeleteUserHistory(self, id):
        sql = "delete from UserHistory where UH_ID = %s"
        self.db.execute(sql, id)

    def QueryAll(self):
        sql = "select * from UserHistory"
        return self.db.query(sql)

    def QueryUserHistory(self, id):
        sql = "select * from UserHistory where UH_ID = %s"
        return self.db.query(sql, id)

    def QueryUserHistoryByS_id(self, S_id):
        sql = "select * from UserHistory where S_ID = %s"
        return self.db.query(sql, S_id)

    def QueryUserHistoryByR_id(self, R_id):
        sql = "select * from UserHistory where R_ID = %s"
        return self.db.query(sql, R_id)

    def QueryUserHistoryByS_idAndR_id(self, S_id, R_id):
        sql = "select * from UserHistory where S_ID = %s and R_ID = %s"
        return self.db.query(sql, (S_id, R_id))

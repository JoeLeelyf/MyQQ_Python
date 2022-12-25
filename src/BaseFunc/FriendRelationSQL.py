import BaseFunc.DataBase as DataBase

class FriendRelationSQL:
    def __init__(self):
        self.db = DataBase.DataBase()

    def CreateFriendRelation(self, U_id1, U_id2):
        sql = "insert into FriendRelation(U_ID1, U_ID2) values(%s, %s)"
        self.db.execute(sql, (U_id1, U_id2))
    
    def DeleteFriendRelation(self, U_id1, U_id2):
        sql = "delete from FriendRelation where U_ID1 = %s and U_ID2 = %s"
        sql_1 = "delete from FriendRelation where U_ID2 = %s and U_ID1 = %s"
        self.db.execute(sql, (U_id1, U_id2))
        self.db.execute(sql_1, (U_id1, U_id2))
    
    def QueryFriend(self, U_id):
        sql = "select U_ID2 from FriendRelation where U_ID1 = %s or U_ID2 = %s"
        return self.db.query(sql, (U_id, U_id))
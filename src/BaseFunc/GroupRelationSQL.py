import BaseFunc.DataBase as DataBase

class GroupRelationSQL:
    def __init__(self):
        self.db = DataBase.DataBase()

    def CreateGroupRelation(self, U_id, G_id):
        sql = "insert into GroupRelation(U_ID, G_ID) values(%s, %s)"
        self.db.execute(sql, (U_id, G_id))

    def DeleteGroupRelation(self, U_id, G_id):
        sql = "delete from GroupRelation where U_ID = %s and G_ID = %s"
        self.db.execute(sql, (U_id, G_id))

    def QueryGroup(self, U_id):
        sql = "select G_ID from GroupRelation where U_ID = %s"
        return self.db.query(sql, U_id)
    
    def QueryUser(self, G_id):
        sql = "select U_ID from GroupRelation where G_ID = %s"
        return self.db.query(sql, G_id)
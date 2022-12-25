import BaseFunc.DataBase as DataBase
import BaseFunc.GroupRelationSQL as GroupRelationSQL

class GroupSQL:
    def __init__(self):
        self.db = DataBase.DataBase()
        self.groupRelationSQL = GroupRelationSQL.GroupRelationSQL()

    def CreateGroup(self, name, capacity=500):
        size = self.db.query("select * from ChatGroup")
        id = len(size) + 1
        sql = "insert into ChatGroup(G_ID, G_Name, Capacity) values(%s, %s, %s)"
        self.db.execute(sql, (id, name, capacity))
        return id

    def __DeleteGroup(self, id):
        sql = "delete from ChatGroup where G_ID = %s"
        self.db.execute(sql, id)

    def UpdateGroup(self, id, name, capacity=500):
        sql = "update ChatGroup set G_Name = %s, Capacity = %s where G_ID = %s"
        self.db.execute(sql, (name, capacity, id))
    
    def QueryAll(self):
        sql = "select * from ChatGroup"
        return self.db.query(sql)
    
    def QueryGroup(self, id):
        sql = "select * from ChatGroup where G_ID = %s"
        return self.db.query(sql, id)
    
    def QueryGroupName(self, id):
        sql = "select G_Name from ChatGroup where G_ID = %s"
        return self.db.query(sql, id)
    
    def QueryName(self, id):
        sql = "select G_Name from ChatGroup where G_ID = %s"
        return self.db.query
    
    def QueryCapacity(self, id):
        sql = "select Capacity from ChatGroup where G_ID = %s"
        return self.db.query(sql, id)
    
    def QueryGroupMember(self, id):
        sql = "select U_ID from GroupRelation where G_ID = %s"
        return self.db.query(sql, id)
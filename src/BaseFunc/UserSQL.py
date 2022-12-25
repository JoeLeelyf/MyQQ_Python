import BaseFunc.DataBase as DataBase

class UserSQL:
    def __init__(self):
        self.db = DataBase.DataBase()

    def CreateUser(self, username, password):
        size = self.db.query("select * from user")
        id = len(size)+1
        sql = "insert into user(U_ID, U_Name, Password) values(%s, %s, %s)"
        self.db.execute(sql, (id, username, password))
        return id

    def __DeleteUser(self, id):
        sql = "delete from user where U_ID = %s"
        self.db.execute(sql, id)

    def UpdateUser(self, id, username, password):
        sql = "update user set U_Name = %s, Password = %s where U_ID = %s"
        self.db.execute(sql, (username, password, id))

    def QueryAll(self):
        sql = "select * from user"
        return self.db.query(sql)

    def QueryUser(self, id):
        sql = "select * from user where U_ID = %s"
        return self.db.query(sql, id)

    def QueryPassword(self, id):
        sql = "select Password from user where U_ID = %s"
        return self.db.query(sql, id)

    def QueryUsername(self, id):
        sql = "select U_Name from user where U_ID = %s"
        return self.db.query(sql, id)

    def QueryName(self, id):
        sql = "select * from user where U_ID = %s"
        name=(self.db.query(sql, id))[0][1]
        return name

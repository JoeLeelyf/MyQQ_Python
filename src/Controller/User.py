import BaseFunc.UserHistorySQL as UserHistorySQL
import BaseFunc.UserSQL as UserSQL
import BaseFunc.GroupSQL as GroupSQL
import BaseFunc.FriendRelationSQL as FriendRelationSQL
import BaseFunc.GroupRelationSQL as GroupRelationSQL


class User:
    def __init__(self, id, username, password) -> None:
        self.id = id
        self.username = username
        self.password = password
        self.userSQL = UserSQL.UserSQL()
        self.userHistorySQL = UserHistorySQL.UserHistorySQL()
        self.groupSQL = GroupSQL.GroupSQL()
        self.friendRelationSQL = FriendRelationSQL.FriendRelationSQL()
        self.groupRelationSQL = GroupRelationSQL.GroupRelationSQL()

    def __str__(self) -> str:
        return f"User(id={self.id}, username={self.username}, password={self.password})"

    def __repr__(self) -> str:
        return self.__str__()

    def __eq__(self, o: object) -> bool:
        if isinstance(o, User):
            return self.id == o.id and self.username == o.username and self.password == o.password
        else:
            return False

    def __ne__(self, o: object) -> bool:
        return not self.__eq__(o)

    def __hash__(self) -> int:
        return hash((self.id, self.username, self.password))

    def __del__(self):
        del self.id
        del self.username
        del self.password
        del self.userSQL
        del self.userHistorySQL
        del self.groupSQL

    def CreateUserHistory(self, receiver_id, content):
        return self.userHistorySQL.CreateUserHistory(self.id, receiver_id, content)

    def QueryUserHistoryByS_id(self):
        return self.userHistorySQL.QueryUserHistoryByS_id(self.id)

    def QueryUserHistoryByR_id(self, receiver):
        return self.userHistorySQL.QueryUserHistoryByR_id(receiver.id)

    def QueryUserHistoryByS_idAndR_id(self, receiver):
        return self.userHistorySQL.QueryUserHistoryByS_idAndR_id(self.id, receiver.id)

    def QueryAllGroup(self):
        return self.groupSQL.QueryAll()

    def QueryGroup(self, id):
        return self.groupSQL.QueryGroup(id)
    
    def QueryGroupName(self, id):
        name=(self.groupSQL.QueryGroupName(id))[0][0]
        return name

    def QueryName(self, id):
        return self.groupSQL.QueryName(id)

    def QueryAllUser(self):
        return self.userSQL.QueryAll()

    def QueryUser(self, id):
        return self.userSQL.QueryUser(id)

    def QueryPassword(self, id):
        return self.userSQL.QueryPassword(id)

    def QueryFriend(self):
        return self.friendRelationSQL.QueryFriend(self.id)
    
    def AddFriend(self, friend_id):
        return self.friendRelationSQL.CreateFriendRelation(self.id, friend_id)

    def DelFriend(self, friend_id):
        return self.friendRelationSQL.DeleteFriendRelation(self.id, friend_id)

    def QueryGroup(self):
        return self.groupRelationSQL.QueryGroup(self.id)

    def AddGroup(self, group_id):
        return self.groupRelationSQL.CreateGroupRelation(self.id, group_id)

    def DelGroup(self, group_id):
        return self.groupRelationSQL.DeleteGroupRelation(self.id, group_id)
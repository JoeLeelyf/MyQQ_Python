import BaseFunc.GroupSQL as GroupSQL
import BaseFunc.GroupHistorySQL as GroupHistorySQL

class Group:
    def __init__(self, id, name, capacity) -> None:
        self.id = id
        self.name = name
        self.capacity = capacity
        self.groupSQL = GroupSQL.GroupSQL()
        self.groupHistorySQL = GroupHistorySQL.GroupHistorySQL()

    def __str__(self) -> str:
        return f"Group(id={self.id}, name={self.name}, capacity={self.capacity})"

    def __repr__(self) -> str:
        return self.__str__()

    def __eq__(self, o: object) -> bool:
        if isinstance(o, Group):
            return self.id == o.id and self.name == o.name and self.capacity == o.capacity
        else:
            return False

    def __ne__(self, o: object) -> bool:
        return not self.__eq__(o)

    def __hash__(self) -> int:
        return hash((self.id, self.name, self.capacity))

    def __del__(self):
        del self.id
        del self.name
        del self.capacity
        del self.groupSQL
        del self.groupHistorySQL

    def CreateGroupHistory(self, content):
        return self.groupHistorySQL.CreateGroupHistory(self.id, content)

    def QueryGroupHistory(self):
        return self.groupHistorySQL.QueryGroupHistoryByG_id(self.id)

    def QueryAllGroup(self):
        return self.groupSQL.QueryAll()

    def QueryGroup(self, id):
        return self.groupSQL.QueryGroup(id)

    def QueryName(self, id):
        return self.groupSQL.QueryName(id)

    def QueryGroup(self, id):
        return self.groupSQL.QueryGroup(id)
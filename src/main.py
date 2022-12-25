import Controller.Group as Group
import Controller.User as User
import BaseFunc.UserSQL as UserSQL
import BaseFunc.GroupSQL as GroupSQL
import BaseFunc.UserHistorySQL as UserHistorySQL
import BaseFunc.GroupHistorySQL as GroupHistorySQL
import Server.ChatServer as ChatServer
import Server.Client as Client
import time

def Login():
    print("1. Login", end="; ")
    print("2. Register", end="; ")
    print("3. Exit")
    choice = input("Please choose: ")
    if choice == "1":
        print("<<<<< Login <<<<<")
        id = input("Please input your id: ")
        password = input("Please input your password: ")
        userSQL = UserSQL.UserSQL()
        if len(userSQL.QueryUser(id)) == 0:
            print("User not exist, please try again.")
            Login()
        elif userSQL.QueryPassword(id)[0][0] != password:
            print("Password error, please try again.")
            Login()
        else:
            print("Login successfully!")
            name = userSQL.QueryUsername(id)[0][0]
            user = User.User(id, name, password)
            return user

    elif choice == "2":
        print("<<<<< Register <<<<<")
        username = input("Please input your username: ")
        password = input("Please input your password: ")
        userSQL = UserSQL.UserSQL()
        id = userSQL.CreateUser(username, password)
        print("Register successfully!")
        print("Your id is: ", id)
        user = User.User(id, username, password)
        return user
    elif choice == "3":
        exit()
    else:
        print("Invalid input, please try again.")
        Login()


def ChooseFriend(user):
    print("<<<<< Choose a friend <<<<<")
    friendList = user.QueryFriend()
    if friendList == None or len(friendList) == 0:
        print("You have no friend, please add a friend.")
        return
    print("below are your friends:")
    print("id\tname")
    f_id = []
    for friend in friendList:
        f_id.append(friend[0])
        print(friend[0], end="\t")
        f = user.QueryUser(friend[0])
        print(f[0][1])
    id = int(input("Please input the id of the friend: "))
    if id not in f_id:
        print("Friend not exist, please try again.")
        return
    else:
        ChatMenu(user, id)


def AddFriend(user):
    print("<<<<< Add a friend <<<<<")
    id = input("Please input the id of the friend you want to add: ")
    userSQL = UserSQL.UserSQL()
    if len(userSQL.QueryUser(id)) == 0:
        print("User not exist, please try again.")
        AddFriend(user)
    else:
        user.AddFriend(id)
        print("Add successfully!")


def DelFriend(user):
    print("<<<<< Del a friend <<<<<")
    friendList = user.QueryFriend()
    if friendList == None or len(friendList) == 0:
        print("You have no friend, please add a friend.")
        return
    print("below are your friends:")
    print("id\tname")
    f_id = []
    for friend in friendList:
        f_id.append(friend[0])
        print(friend[0], end="\t")
        f = user.QueryUser(friend[0])
        print(f[0][1])
    id = int(input("Please input the id of the friend: "))
    if id not in f_id:
        print("Friend not exist, please try again.")
        return
    else:
        user.DelFriend(id)
        print("Del successfully!")
        return


def ChooseGroup(user):
    print("<<<<< Choose a group <<<<<")
    groupList = user.QueryGroup()
    if groupList == None or len(groupList) == 0:
        print("You have no group, please create a group.")
        return
    print("below are your groups:")
    print("id\tname")
    g_id = []
    for group in groupList:
        g_id.append(group[0])
        print(group[0], end="\t")
        print(user.QueryGroupName(group[0]))
    if len(g_id) == 0:
        print("You have no group, please create a group.")
        return
    id = int(input("Please input the id of the group: "))
    if id not in g_id:
        print("Group not exist, please try again.")
        return
    else:
        GroupChatMenu(user, id)


def CreateGroup(user):
    print("<<<<< Create a group <<<<<")
    name = input("Please input the name of the group you want to create: ")
    groupSQL = GroupSQL.GroupSQL()
    id = groupSQL.CreateGroup(name)
    user.AddGroup(id)
    print("Create successfully!")
    print("Your group id is: ", id)


def JoinGroup(user):
    print("<<<<< Join a group <<<<<")
    id = input("Please input the id of the group you want to join: ")
    groupSQL = GroupSQL.GroupSQL()
    if len(groupSQL.QueryGroup(id)) == 0:
        print("Group not exist, please try again.")
        return
    else:
        user.AddGroup(id)
        print("Join successfully!")


def InviteFriend(user):
    print("<<<<< Invite friend to group <<<<<")
    print("<<<<< Choose a friend <<<<<")
    friendList = user.QueryFriend()
    if friendList == None or len(friendList) == 0:
        print("You have no friend, please add a friend.")
        return
    print("below are your friends:")
    print("id\tname")
    f_id = []
    for friend in friendList:
        f_id.append(friend[0])
        print(friend[0], end="\t")
        f = user.QueryUser(friend[0])
        print(f[0][1])
    id = int(input("Please input the id of the friend: "))
    if id not in f_id:
        print("Friend not exist, please try again.")
        return
    else:
        groupList = user.QueryGroup()
        if groupList == None or len(groupList) == 0:
            print("You have no group, please create a group.")
            return
        print("below are your groups:")
        print("id\tname")
        g_id = []
        for group in groupList:
            g_id.append(group[0])
            print(group[0], end="\t")
            print(user.QueryGroupName(group[0]))

        gid = int(input("Please input the id of the group: "))
        if gid not in g_id:
            print("Group not exist, please try again.")
            return
        else:
            friend = User.User(id, None, None)
            friend.AddGroup(gid)
            print("Invite successfully!")


def DelGroup(user):
    print("<<<<< Del a group <<<<<")
    groupList = user.QueryGroup()
    if groupList == None or len(groupList) == 0:
        print("You have no group, please create a group.")
        return
    print("below are your groups:")
    print("id\tname")
    g_id = []
    for group in groupList:
        g_id.append(group[0])
        print(group[0], end="\t")
        print(user.QueryGroupName(group[0]))
    id = int(input("Please input the id of the group you want to del: "))
    groupSQL = GroupSQL.GroupSQL()
    if id not in g_id:
        print("Group not exist, please try again.")
        return
    else:
        user.DelGroup(id)
        print("Del successfully!")


def Menu(user):
    while True:
        print("<<<< Main Window <<<<")
        print("1. Choose a friend", end="; ")
        print("2. Add a friend")
        print("3. Choose a group", end="; ")
        print("4. Create a group", end="; ")
        print("5. Join a group", end="; ")
        print("6. Invite friend to group")
        print("7. Del a friend", end=";")
        print("8. Del a group")
        print("9. Exit")
        choice = input("Please choose: ")
        if choice == "1":
            ChooseFriend(user)
        elif choice == "2":
            AddFriend(user)
        elif choice == "3":
            ChooseGroup(user)
        elif choice == "4":
            CreateGroup(user)
        elif choice == "5":
            JoinGroup(user)
        elif choice == "6":
            InviteFriend(user)
        elif choice == "7":
            DelFriend(user)
        elif choice == "8":
            DelGroup(user)
        elif choice == "9":
            print("<<<<< Exit <<<<<")
            exit()
        else:
            print("Invalid input, please try again.")


def ChatMenu(user, id):
    print("<<<<< Chat menu <<<<<")
    while True:
        choice = int(input("1: Look for chat history; 2: Start a new chat: "))
        if (choice == 1):
            userHistorySQL = UserHistorySQL.UserHistorySQL()
            history = userHistorySQL.QueryUserHistoryByS_idAndR_id(user.id, id)
            history += userHistorySQL.QueryUserHistoryByS_idAndR_id(
                id, user.id)
            history = list(history)
            history = sorted(history)
            for i in history:
                Time = i[3].strftime("%Y-%m-%d %H:%M:%S")
                print(str(i[1])+"->"+str(i[2])+": "+Time+">>>"+i[4])
            print("History showed successfully!")
            return
        elif (choice == 2):
            break
    userSQL = UserSQL.UserSQL()
    name = (userSQL.QueryUsername(id))[0][0]
    print(f"<<<<< {name} <<<<<")

    
    client = Client.Client(int(user.id),'U',id)
    while True:
        Message = input(">>> ")
        if Message == ":wq":
            client.sendMessage(Message)
            print("<<<<< QUIT <<<<<")
            return
        else:
            userHistorySQL = UserHistorySQL.UserHistorySQL()
            userHistorySQL.CreateUserHistory(user.id, id, Message)
            client.sendMessage(Message)
    


def GroupChatMenu(user, id):
    print("<<<<< Group chat menu <<<<<")
    while True:
        choice = int(input("1: Look for chat history; 2: Show all members; 3: Start a new chat: "))
        if (choice == 1):
            groupHistorySQL=GroupHistorySQL.GroupHistorySQL()
            history = groupHistorySQL.QueryGroupHistoryByG_id(id)
            history += groupHistorySQL.QueryGroupHistoryByG_id(id)
            history = list(history)
            history = sorted(history)
            for i in history:
                Time = i[3].strftime("%Y-%m-%d %H:%M:%S")
                print(i[2]+": "+Time+">>>"+i[4])
            print("History showed successfully!")
            return
        elif (choice == 2):
            groupSQL = GroupSQL.GroupSQL()
            memberList = groupSQL.QueryGroupMember(id)
            print("Below are all members:")
            for member in memberList:
                userSQL = UserSQL.UserSQL()
                name = (userSQL.QueryUsername(member[0]))[0][0]
                print(name)
            print("Show successfully!")
        elif (choice == 3):
            break
    groupSQL = GroupSQL.GroupSQL()
    name = (groupSQL.QueryGroupName(id))[0][0]
    capacity = (groupSQL.QueryCapacity(id))[0][0]
    total=len(groupSQL.QueryGroupMember(id))
    print(f"<<<<< {name} <<<<<")
    print(f"<<<<< {total}/"+f"{capacity} <<<<<")

    client = Client.Client(user.id,'G',id)
    while True:
        Message = input(">>> ")
        if Message == ":wq":
            client.sendMessage(Message)
            print("<<<<< QUIT <<<<<")
            return
        else:
            groupHistorySQL=GroupHistorySQL.GroupHistorySQL()
            groupHistorySQL.CreateGroupHistory(id,user.username,Message)
            client.sendMessage(Message)
    


def main():
    print("Welcome to MyQQ!")
    user = Login()
    Menu(user)


if __name__ == "__main__":
    main()

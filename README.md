# My QQ

A simple completion of IM chat software using python and MySQL.Following are some things you should be noticed of before run its "main.py" .

- ==Database==

  Because databases the software depending on are totally created in your own PC, so before any use of it, you should tap some commands in your termial to create these databases.(MySQL enviroment required)
  
  ```mysql
  create database MyQQ;
  alter database MyQQ character set utf8;
  use database MyQQ;
  
  create table User(
  U_ID int primary key,
  U_Name varchar(20) not null,
  Password varchar(20) not null
  );
  
  create table ChatGroup(
  G_ID int primary key,
  G_Name varchar(20) not null,
  Capacity int
  );
  
  create table FriendRelation(
  U_ID1 int,
  U_ID2 int
  );
  
  create table GroupRelation(
  U_ID int,
  G_ID int
  );
  
  create table UserHistory(
  UH_ID int primary key,
  S_ID int,
  R_ID int,  
  Time datetime,
  Content text
  );
  
  create table GroupHistory(
  GH_ID int primary key,
  G_ID int,
  U_Name varchar(20),
  Time datetime,
  Content text
  );
  ```
  
  After entering these commands, use "show tables"  to check:
  
  ```mysql
  mysql> show tables;
  +----------------+
  | Tables_in_myqq |
  +----------------+
  | ChatGroup      |
  | ChatHistory    |
  | User           |
  +----------------+
  ```
  
  Then, in order to use MySQL in python, you should install pymysql:
  
  ```
  pip install pymysql
  ```
  
  Before run "main.py", change the password in "src->BaseFunc->DataBase.py" to your own:
  
  ```Python
  class DataBase:
      # change the default value of the parameters to your own, essential for the connection to the database
      def __init__(self, host="localhost", user="root", password="030209lyflqs", db="MyQQ", port=3306, charset='utf8'):
          self.host = host
          self.user = user
          self.password = password
          self.db = db
          self.port = port
          self.charset = charset
  ```
  
- ==Server==

   Before you start any chat, run ChatServer.py first(src->Server->ChatServer.py)

  ```
  python3 src/Server/ChatServer.py
  ```

  Because the communication between client and server are totally based on socket, so if this port("localhost 8080") in your PC is unavailable, change it to an available one before run ChatServer.py.

  If change is needed, you should make changes in both server and client.

  ```Python
  # ChatServer.py line69:
  if __name__ == "__main__":
      server = ChatServer("localhost", 8080)
      server.broadcast()
  
  # Client.py line15:
  self.socket.connect(("localhost", 8080))
  ```

- ==Chat==

  Just follow the instruct in printed in the terminal to use and chat.Notice the if you want to stop chatting, just tap in ":wq" and you will be redirected to the Main Menu.

  Some examples are given below.

  - Login Menu

    ```
    Welcome to MyQQ!
    1. Login; 2. Register; 3. Exit
    Please choose: 1
    <<<<< Login <<<<<
    Please input your id: 1
    Please input your password: 123456
    Login successfully!
    ```

  - Main Window

    ```
    <<<< Main Window <<<<
    1. Choose a friend; 2. Add a friend
    3. Choose a group; 4. Create a group; 5. Join a group; 6. Invite friend to group
    7. Del a friend;8. Del a group
    9. Exit
    Please choose: 
    ```

  - P2P Chat

    ```
    <<<<< Choose a friend <<<<<
    below are your friends:
    id      name
    2       lyf
    1       Joe
    Please input the id of the friend: 1
    <<<<< Chat menu <<<<<
    1: Look for chat history; 2: Start a new chat: 2
    <<<<< Joe <<<<<
    >>> hello
    >>> how are you today
    >>> 1: I'm fine, thank you
    goodbye
    >>> :wq
    <<<<< QUIT <<<<<
    ```

  - Group Chat

    ```
    <<<<< Choose a group <<<<<
    below are your groups:
    id      name
    1       test
    Please input the id of the group: 1
    <<<<< Group chat menu <<<<<
    1: Look for chat history; 2: Start a new chat: 2
    >>> hello
    >>> 2: hello
    you 
    >>> 2: you
    :wq
    <<<<< QUIT <<<<<
    ```

    

​	


import sqlite3

class RegisterObj:
    def __init__ (self, username, password, email, url):
        self.username = username
        self.password = password
        self.email = email
        self.url = url

class LoginObj:
    def __init__(self, username, password):
        self.username = username
        self.password = password


class DBManager:
    def __init__(self):
        #self.conn = sqlite3.connect('DataBase.db')
        #self.cur = self.conn.cursor()
        self.conn = None
        self.cur = None
        self.method = None
        return

    def connect(self):
        self.cur.execute("create table if not exists DataBase(UserName TEXT , Password TEXT, Email TEXT, FileUrl TEXT, Authorization Text);")

    """def ObjType(self, data):
        info = data.split("#")
        method = info[0]
        if method == "login":
            return LoginObj(info[1], info[2])
        if method == "register":
            return RegisterObj(info[1], info[2], info[3], info[4])
        else:
            return "ERROR"""

    """def ClientExists(self, username):
        self.connect()
        self.cur.execute("select username from POSTS where username=?", (username))
        data = self.cur.fetchall()
        if not data:
          return True
        else:
          return False"""

    def If_Client_Already_Exists(self,data):
        data = data.split("#")
        username = data[1]
        password = data[2]
        print username
        print password
        conn = sqlite3.connect('DataBase.db')
        cur = conn.cursor()
        for row in cur.execute('select * from DataBase'):
            Temp_Arr = str(row).split(', u')
            Temp_Arr[0] = Temp_Arr[0].replace("u","")
            Temp_Arr[0] = Temp_Arr[0].replace("(","")
            for i in range (len(Temp_Arr)):
                Temp_Arr[i]=Temp_Arr[i].replace("'", "")
                Temp_Arr[i]=Temp_Arr[i].replace('"', "")
            if Temp_Arr[0] == username and Temp_Arr[1] == password:
                return True
        return False

    def methodtype(self,data):
        info = data.split("#")
        #self.conn = sqlite3.connect('DataBase.db')
        #self.cur = self.conn.cursor()
        method = info[0]
        self.method = method
        newdata = ""
        for i in range(1,len(info)):
            newdata = newdata + "#" + info[i]
        return newdata

    def Register(self, data):
        info = data.split("#")
        username = info[1]
        password = info[2]
        email = info[3]
        url = info[4]

        try:
            print 0
            self.conn = sqlite3.connect('DataBase.db')
            self.cur = self.conn.cursor()
            self.connect()
            print 1
            self.conn = sqlite3.connect('DataBase.db')
            self.cur = self.conn.cursor()
            self.cur.execute('''SELECT * FROM DataBase WHERE UserName = "%s" ''' % (str(username)))
            print 2
            if self.cur.fetchone() is None:
                print 3
                self.cur.execute('''INSERT INTO DataBase VALUES ('%s','%s','%s','%s','User')''' %
                                 (str(username), str(password), str(email), str(url)))
                self.conn.commit()
                return "register successful!"


            else:
                self.conn.commit()
                return "username exists"

        except:
            self.conn.commit()
            return "fail to register"

    def Login(self, data):
        if self.If_Client_Already_Exists(data)==True:
            return "client exists"
        else:
            return "client does not exist"
        """self.conn = sqlite3.connect('DataBase.db')
        self.cur = self.conn.cursor()
        self.connect()
        info = data.split("#")
        username = info[0]
        password = info[1]
        try:

            self.cur.execute('''SELECT * FROM DataBase WHERE UserName = "%s" AND Password = "%s" ''' % (str(username)
                                                                                                    , str(password)))
            x = self.cur.fetchone()
            if x is not None:
                print x
                if u"Boss" in x[5]:
                    self.conn.commit()
                    return "User is boss"

                else:
                    self.conn.commit()
                    return "User exists"
            else:
                self.conn.commit()
                return "user does not exist"

        except:
            self.conn.commit()
            return "User does not exist"""""


    def run(self,data):
        new_data = self.methodtype(data)
        print new_data
        if self.method == "register":
            return self.Register(new_data)
        elif self.method == "login":
            return self.Login(new_data)
        else:
            return "fail"




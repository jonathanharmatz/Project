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
        self.conn = sqlite3.connect('DataBase.db')
        self.cur = self.conn.cursor()
        self.method = None
        return

    def connect(self):
        self.cur.execute("create table if not exists DateBase(UserName TEXT , Password TEXT, Email TEXT, FileUrl TEXT, Authorization Text);")

    """def ObjType(self, data):
        info = data.split("#")
        method = info[0]
        if method == "login":
            return LoginObj(info[1], info[2])
        if method == "register":
            return RegisterObj(info[1], info[2], info[3], info[4])
        else:
            return "ERROR""""

    """def ClientExists(self, username):
        self.connect()
        self.cur.execute("select username from POSTS where username=?", (username))
        data = self.cur.fetchall()
        if not data:
          return True
        else:
          return False"""

    def methodtype(self,data):
        info = data.split("#")
        method = info[0]
        self.method = method
        newdata = ""
        for i in range(2,):
            newdata = newdata + "#" + info[i]
        return newdata

    def Register(self, data):
        info = data.split("#")
        username = info[0]
        password = info[1]
        email = info[2]
        url = info[3]

        try:
            self.connect()
            self.cur.execute('''SELECT * FROM Table1 WHERE UserName = "%s" ''' % (str(username)))
            if self.cur.fetchone() is None:
                self.cur.execute('''INSERT INTO Table1 VALUES ('%s','%s','%s','%s','User')''' %
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
            return "User does not exist"

        def run(self,data):
            new_data = self.methodtype(data)
            if self.methodtype == "register":
                self.Register(new_data)




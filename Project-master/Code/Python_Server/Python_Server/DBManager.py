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
        self.count = 3
        return

    def connect(self):
        self.cur.execute("create table if not exists DataBase(UserName TEXT , Password TEXT, Email TEXT, FolderUrl TEXT, Ip TEXT, Authorization Text);")

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

    def If_Client_Already_Exists(self,data, ip):
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
            if Temp_Arr[0] == username and Temp_Arr[1] == password and Temp_Arr[4] == ip:
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

    def Register(self, data,ip):
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
                self.cur.execute('''INSERT INTO DataBase VALUES ('%s','%s','%s','%s','%s','User')''' %
                                 (str(username), str(password), str(email), str(url),ip))
                self.conn.commit()
                return "register successful!"


            else:
                self.conn.commit()
                return "username exists"

        except:
            self.conn.commit()
            return "fail to register"

    def Login(self, data,ip):
        while self.count!=0:
            if self.If_Client_Already_Exists(data,ip)==True:
                return "login successful"
            else:
                self.count-=1
                return "wrong username or password, you got %s tries left" %(self.count)
        return "You failed to login 3 times. Access to folder denied."
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

    def folder_by_ip(self,ip):
        self.conn = sqlite3.connect('DataBase.db')
        self.cur = self.conn.cursor()
        self.connect()
        self.conn = sqlite3.connect('DataBase.db')
        self.cur = self.conn.cursor()
        self.cur.execute('''SELECT FolderUrl FROM DataBase WHERE Ip = "%s" ''' % (str(ip)))
        print ip
        x = self.cur.fetchone()
        if x is not None:
            self.conn.commit()
            folder = str(x).split("'")[1]
            print folder
            return folder
        else:
            return "ip does not exist"

    def email_by_ip(self,ip):
        elf.conn = sqlite3.connect('DataBase.db')
        self.cur = self.conn.cursor()
        self.connect()
        self.conn = sqlite3.connect('DataBase.db')
        self.cur = self.conn.cursor()
        self.cur.execute('''SELECT Email FROM DataBase WHERE Ip = "%s" ''' % (str(ip)))
        print ip
        x = self.cur.fetchone()
        if x is not None:
            print str(x)
            return str(x)
        else:
            return "ip does not exist"


    def run(self,data,ip):
        new_data = self.methodtype(data)
        print new_data
        if self.method == "register":
            return self.Register(new_data,ip)
        elif self.method == "login":
            return self.Login(new_data,ip)
        else:
            return "fail"




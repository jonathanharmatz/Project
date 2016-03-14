
import sqlite3

class DB_Managment_Class:

    def __init__(self):
        return

    def methodtype(self,data):
        info = data.split("#")
        method = info[0]
        self.method = method
        newdata = ""
        for i in range(1,len(info)):
            newdata = newdata + "#" + info[i]
        newdata = newdata[1:len(newdata)]
        return [newdata,method]
    
    def DB_Creation(self):
        conn = sqlite3.connect('DataBase.db')
        cur = conn.cursor()
        cur.execute("create table if not exists DataBase(UserName TEXT , Password TEXT, Email TEXT, FileUrl TEXT, Authorization Text);")

    def If_Client_Already_Exists(self,data):
        data = data.split("#")
        username = data[0]
        password = data[1]
        conn = sqlite3.connect('DataBase.db')
        cur = conn.cursor()
        for row in cur.execute('select * from DataBase'):
            Temp_Arr = str(row).split(', u')
            Temp_Arr[0] = Temp_Arr[0].replace("u","")
            for i in range (len(Temp_Arr)):
                Temp_Arr[i]=Temp_Arr[i].replace("'", "")
                Temp_Arr[i]=Temp_Arr[i].replace('"', "")
            if Temp_Arr[0] == username and Temp_Arr[1] == password:
                return True
        return False

## Adding Specific Client (given as parameter) To the Clients DataBase
    def Clients_DataBase_Add(self,data):
        data = data.split("#")
        username = data[0]
        password = data[1]
        email = data[2]
        url = data[3]
        print Client_Adress
        conn = sqlite3.connect('DataBase.db')
        cur = conn.cursor()
        ##cur.execute("create table if not exists Clients3(ID INTEGER PRIMARY KEY , Client_Adress text );")
        cur.execute("insert into DataBase(UserName, Password, Email, FileUrl, ) values (?,?,?,?)", (username. password, email,url) )
        conn.commit()

## Deletes Specific Client From The DataBase
    def Clients_DataBase_Delete(self,Client_Adress):
        conn = sqlite3.connect('DataBase.db')
        cur = conn.cursor()
        cur.execute("DELETE FROM DataBase WHERE socket=(?)", [Client_Adress])
        ##print "Total number of rows deleted: ", conn.total_changes

        ##for row in cur.execute('select * from test'):
        ##   print row

        conn.close()

## Returns Clients ID Number
    def Insert_DB_Into_File(self):
        conn = sqlite3.connect('DataBase.db')
        cur = conn.cursor()
        ##counter = 0
        print "Before FILE Written"
        f = open('C:\\Users\\User\\Desktop\\RTR.txt', 'w')

        for row in cur.execute('select * from DataBase'):
            ##counter += 1
            f.write(str(row))

        f.close()
        conn.close()
        return
        ##return counter
    def __main__(data):

        DB_creation()
        info = methodtype(data)
        newdata = info[0]
        method = info[1]
        if method == "register":
            if If_Client_Already_Exists(newdata)==False:
                Clients_DataBase_Add(newdata)
                return "Register Succesful"
            else:
                return "User Exists"
        if method == "login":
            if If_Client_Already_Exists(newdata)==True:
                return "login confirmed"
            else:
                return "no such client"
            
            

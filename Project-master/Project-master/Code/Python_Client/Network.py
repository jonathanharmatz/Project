#region ----------   ABOUT   -----------------------------
"""
##################################################################
# Created By:  Michael Chernovilski                              #
# Date: 20/09/2014                                               #
# Name: Server  between GUI and clients                          #
# Version: 1.0                                                   #
# Windows Tested Versions: Win 7 32-bit                          #
# Python Tested Versions: 2.6 32-bit                             #
# Python Environment  : PyCharm                                  #
# pyCrypto Tested Versions: Python 2.7 32-bit                    #
##################################################################
"""
#endregion

#region ----------   IMPORTS   -----------------------------
import threading
import os
import socket
import time
from Security import *
import struct
from Pipe import *
#endregion

#region ----------   C O N S T A N T S  ------------------------------------------------------
PROT_START = "Hello"                                      # Initialization keyword of Protocol Establishment
LEN_UNIT_BUF = 2048                                       # Min len of buffer for receive from server socket
ERROR_SOCKET = "Socket_Error"                             # Error message If you happened socket error
ERROR_EXCEPT = "Exception"                                # Error message If you happened exception
MAX_ENCRYPTED_MSG_SIZE = 128
MAX_SOURCE_MSG_SIZE = 128
END_LINE = "\r\n"                                         # End of line
SERVER_ABORT = "Aborting the server..."
#endregion

#region  -----  SessionWithClient C L A S S  -----#region ----------   ABOUT   -----------------------------
"""
##################################################################
# Created By:  Michael Chernovilski                              #
# Date: 20/09/2014                                               #
# Name: Server  between GUI and clients                          #
# Version: 1.0                                                   #
# Windows Tested Versions: Win 7 32-bit                          #
# Python Tested Versions: 2.6 32-bit                             #
# Python Environment  : PyCharm                                  #
# pyCrypto Tested Versions: Python 2.7 32-bit                    #
##################################################################
"""
#endregion

#region ----------   IMPORTS   -----------------------------
import os
import socket
import time
from Security import *
from Pipe import *
from ExplorerManager import *
from permmisions import *
from Folder_Encrypt import *
import subprocess
#endregion

#region ----------   C O N S T A N T S  ------------------------------------------------------
PROT_START = "Hello"                                      # Initialization keyword of Protocol Establishment
LEN_UNIT_BUF = 2048                                       # Min len of buffer for receive from server socket
ERROR_SOCKET = "Socket_Error"                             # Error message If you happened socket error
ERROR_EXCEPT = "Exception"                                # Error message If you happened exception
MAX_ENCRYPTED_MSG_SIZE = 128
MAX_SOURCE_MSG_SIZE = 128
END_LINE = "\r\n"                                         # End of line
SERVER_ABORT = "Aborting the server..."
SERVER_ADDRESS = "127.0.0.1"
SERVER_PORT = 8089
#endregion

#region  -----  SessionWithClient C L A S S  -----
class NetWorkClient:
    def __init__(self):
        self.security = Security()
        self.sym_key =None
        self.sock = socket.socket()
        self.AES= AESCrypt()
        self.ExplorerManager = ExplorerManager()
        self.permmisions =  permmisions()
        self.Folder_Encrypt = Folder_Encrypt()
        self.Pipe = Pipe()


    def start(self):
        self.sock.connect((SERVER_ADDRESS, SERVER_PORT))

    def recv_buf(self):
        #content=""
        #while True:
        #    data = self.clientSock.recv(LEN_UNIT_BUF)
        #    if not data:  break
        #    content += data
        #print content
        #return content.split(END_LINE)[0]
        return self.sock.recv(LEN_UNIT_BUF).split(END_LINE)[0]

    def verify_hello(self, data):
        if len(data):
            # Verify Hello at beginning of communication
            if not (data == PROT_START ):
                self.sock.send(ERROR_SOCKET + END_LINE + "Error in protocol establishment ( 'Hello' )" + END_LINE)
                time.sleep(0.5)
                self.sock.close()
                return False
            return True
        return False

    def send(self, data):
        data = self.AES.encryptAES(self.sym_key, data)
        self.sock.send(data)

    def recv(self):
        encrypted_data = self.sock.recv(LEN_UNIT_BUF)
        data = self.AES.decryptAES(self.sym_key, encrypted_data)
        return data

    def run(self):
        self.start()
        self.sock.send(PROT_START)
        data = self.recv_buf()
        if not self.verify_hello(data):
            return
        self.sym_key = self.security.key_exchange_client(self.sock)
        file_name = self.recv()
        self.permmisions.Access_Denied(file_name)
        print self.ExplorerManager.begin(file_name)
        if self.ExplorerManager.begin(file_name)== "folder open":
            #subprocess.check_call(r"C:\Users\User\Desktop\Project-master\Code\GUI\WindowsFormsApplication5\bin\Debug\WindowsFormsApplication5.exe")
            self.Pipe.pipesend("folder open")
        message = ""
        count=0
        while count<3:
            loggedindetails=self.Pipe.communication()
            print message
            self.send(loggedindetails)
            message = self.recv()
            self.Pipe.pipesend(message)
            count+=1
        if "login failed" in message:
            self.Folder_Encrypt.encrypt_file(os.urandom(32), file_name)
        if message == "login successful":
            self.permmisions.remove_ace(file_name)







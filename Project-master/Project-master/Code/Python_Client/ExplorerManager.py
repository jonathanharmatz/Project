
import threading
import win32gui,win32con,time,win32process
from ctypes import byref, c_int

from  ProcessManager import *

MY_PATH = ""
APPLICATION_NAME = 'explorer.exe'

class ExplorerManager(threading.Thread):

    applications_dict = {}
    
    def __init__(self):
        threading.Thread.__init__(self)
        self.processManager = ProcessManager()
        self.path = None
        #win32gui.SystemParametersInfo(win32con.SPI_SETFOREGROUNDLOCKTIMEOUT, 0, win32con.SPIF_SENDWININICHANGE | win32con.SPIF_UPDATEINIFILE)


    def winEnumHandler( self, hwnd, ctx ):
        if win32gui.IsWindowVisible( hwnd ):
            # get the proccessid from the windowhandle
            processID = win32process.GetWindowThreadProcessId(hwnd)[1]
            processName =  self.processManager.EnumProcesses(processID)
            windowTitle = win32gui.GetWindowText( hwnd )
            if processName and processName.lower() == APPLICATION_NAME and str(self.path) in windowTitle:
                if processName.lower() in self.applications_dict.keys():
                    self.applications_dict[processName.lower()].append( windowTitle )
                else:
                    self.applications_dict[processName.lower()] = [ windowTitle ]


    def begin(self,folder):
        while True:
            self.applications_dict.clear()
            self.path = folder.split('\\')[-1]
            win32gui.EnumWindows( self.winEnumHandler, None )
            #print '-'*78
            if len(self.applications_dict) == 1:
                print self.applications_dict
                return "folder open"





import pythoncom, pyHook
import time

class Lock:


    def __init__(self,tolock):
        self.tolock = tolock
    
    def Mode(event):
        return False
        
    def Locking(self):
        if self.tolock == "lock":
            def Mode(event):
                return False
        if self.tolock == "unlock":
             def Mode(event):
                return True
        hm = pyHook.HookManager()
        hm.MouseAll = Mode
        hm.KeyAll = Mode
        hm.HookMouse()
        #hm.HookKeyboard()
        pythoncom.PumpMessages()


lock = Lock("lock")

lock.Locking()

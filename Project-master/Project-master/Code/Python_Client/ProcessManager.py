from ctypes import *


PROCESS_QUERY_INFORMATION = 0x0400
PROCESS_VM_READ = 0x0010


class ProcessManager:

    def __init__(self):
        #PSAPI.DLL
        self.psapi = windll.psapi
        #Kernel32.DLL
        self.kernel = windll.kernel32

    def EnumProcesses(self, pidMyProcess):
        arr = c_ulong * 256
        lpidProcess= arr()
        cb = sizeof(lpidProcess)
        cbNeeded = c_ulong()
        hModule = c_ulong()
        count = c_ulong()
        modname = c_buffer(30)

        #Call Enumprocesses to get hold of process id's
        self.psapi.EnumProcesses(byref(lpidProcess),
                            cb,
                            byref(cbNeeded))

        #Number of processes returned
        nReturned = cbNeeded.value/sizeof(c_ulong())
        pidProcess = [i for i in lpidProcess][:nReturned]

        for pid in pidProcess:
            if pid == pidMyProcess:
                #Get handle to the process based on PID
                hProcess = self.kernel.OpenProcess(PROCESS_QUERY_INFORMATION | PROCESS_VM_READ, False, pid)
                if hProcess:
                    self.psapi.EnumProcessModules(hProcess, byref(hModule), sizeof(hModule), byref(count))
                    self.psapi.GetModuleBaseNameA(hProcess, hModule.value, modname, sizeof(modname))
                    processName = "".join([ i for i in modname if i != '\x00'])

                    #-- Clean up
                    for i in range(modname._length_):
                        modname[i]='\x00'
                    self.kernel.CloseHandle(hProcess)
                    return processName


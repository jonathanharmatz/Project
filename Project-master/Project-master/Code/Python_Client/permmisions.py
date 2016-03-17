import win32security
import ntsecuritycon as con
import os

class permmisions:

    def __init__(self):
        self.username = os.environ.get( "USERNAME" )


    def Access_Denied(self,filename):
        userx, domain, type = win32security.LookupAccountName ("", self.username)
        #usery, domain, type = win32security.LookupAccountName ("", "User")
        print filename
        sd = win32security.GetFileSecurity(filename, win32security.DACL_SECURITY_INFORMATION)
        print sd
        dacl = sd.GetSecurityDescriptorDacl()   # instead of dacl = win32security.ACL()
        print dacl

        dacl.AddAccessDeniedAce(win32security.ACL_REVISION, con.FILE_GENERIC_READ | con.FILE_GENERIC_WRITE, userx)
        sd.SetSecurityDescriptorDacl(1, dacl, 0)   # may not be necessary
        win32security.SetFileSecurity(filename, win32security.DACL_SECURITY_INFORMATION, sd)

    def remove_ace(self,path):
         """Remove the ace for the given users."""
         if not os.path.exists(path):
                raise WindowsError('Path %s could not be found.' % path)
         total = 0
         userx, domain, utype = win32security.LookupAccountName("", self.username)
         sd = win32security.GetFileSecurity(path, win32security.DACL_SECURITY_INFORMATION)
         dacl = sd.GetSecurityDescriptorDacl()
         num_delete = 0
         for index in range(0, dacl.GetAceCount()):
                ace = dacl.GetAce(index - num_delete)
                if userx == ace[2]:
                    dacl.DeleteAce(index - num_delete)
                    num_delete += 1
                    total += 1
         if num_delete > 0:
               sd.SetSecurityDescriptorDacl(1, dacl, 0)
               win32security.SetFileSecurity(path, win32security.DACL_SECURITY_INFORMATION, sd)
         if total > 0:
                return True
        #remove_ace(FILENAME, [username])

import struct
class Pipe():
    def __init__(self):
        self.pipe= open(r'\\.\pipe\NPtest1', 'r+b', 0)

    def pipercv(self):
        i = 0
        s = 'Message[{0}]'.format(i)
        i += 1

        self.pipe.write(struct.pack('I', len(s)) + s)   # Write str length and str
        self.pipe.seek(0)                               # EDIT: This is also necessary

        n = struct.unpack('I', self.pipe.read(4))[0]    # Read str length
        s = self.pipe.read(n)                           # Read str
        #
        self.pipe.seek(0) # Important!!!
        return s


    def communication(self):
        recvnum = {"login":2,"register":4}
        first = self.pipercv()
        loggedindetails=first
        for i in range(0,recvnum[str(first)]):
            loggedindetails=loggedindetails+'#'+self.pipercv()
        return loggedindetails



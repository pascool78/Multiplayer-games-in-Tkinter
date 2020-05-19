#
#V 0.4
#
# XXL1212
# CC BY-NC-SA 2.0 FR
from tkinter import *
import tkinter,sys,PIL
from  PIL import Image,ImageTk
from twisted.protocols import basic
from twisted.internet import tksupport, reactor, reactor, protocol, endpoints
root = tkinter.Tk()
import json
global label, nj, canvas,label,label2
nj =  int(sys.argv[1])
nj2 =  int(sys.argv[2])
image_j1 = "Images/" + str(nj) + ".ppm"
image_j2 = "Images/" + str(nj2) + ".ppm"
x1 = 100
y1 = 100
x2 = 100
y2 = 100
photo=PIL.ImageTk.PhotoImage(PIL.Image.open(image_j1).resize((t, t),Image.ANTIALIAS))
photo2=PIL.ImageTk.PhotoImage(PIL.Image.open(image_j2).resize((t, t),Image.ANTIALIAS))
canvas = Canvas(root, width = 400, height = 400)
canvas.pack(expand=YES,fill=BOTH)
label=canvas.create_image(t, t, anchor=NW, image=photo)
label2= canvas.create_image(t, t, anchor=NW, image=photo2)
img = PhotoImage(file="1.ppm")
# Install the Reactor support
tksupport.install(root)

#t=tkinter.Label(root,text="jkjk")

#t.pack()
from twisted.internet import protocol, reactor, endpoints

global ec
class EchoClient(protocol.Protocol):
    """Once connected, send a message, then print the result."""
    def connectionMade(self):
        global ec
        self.transport.write(b"HELLO\r\n")
        ec=self
    def dataReceived(self, data):
      try:
        global label, x1, y1,label2
        global ec
        ec=self
        #self.transport.loseConnection()
        #self.transport.write(b'ok')
        #d = data.decode('ascii')
        #u = "http://x2.org/?"+ d
        try:
          #print ('data:',data)
          data=data.replace(b"\r\n",b"")
          #print ('data2:',data)
          data =  data.decode('ascii')
          #print ('data3:',data)
          m = json.loads(data)
          #print ('data4:',data)
          # parse_qs (urlparse(u).query)
          print ("m:",m)
          x = (m["x"])
          y = (m["y"])
          j = (m["j"])
          #photo=PhotoImage(file=str(file))
          #t['text']=str(m)
          if str(j) == str(nj):
                 x1=x
                 y1=y
                 canvas.coords(label,x, y)
          elif str(j) == str(nj2):
                 canvas.coords(label2,x, y)
          #print ("1")
          #self.transport.write(b'x=80&y=90&j=90')
          #print ("2")
        except :
            print ("invalid json:",data)
      except :
        print ("5")
        print("Unexpected error:", sys.exc_info()[0])
        raise

    def connectionLost(self, reason):
        print("connection lost")

class EchoFactory(protocol.ClientFactory):
    protocol = EchoClient

    def clientConnectionFailed(self, connector, reason):
        print("Connection failed - goodbye!")
        reactor.stop()
    def clientConnectionLost(self, connector, reason):
        print("Connection lost - goodbye!")
        reactor.stop()
def envoie(event):
        e = event.keycode
        global x1, y1,nj
        v = 10
        if int(e) == int(111):
                x1 = int(x1) - 0
                y1 = int(y1) - v
        elif int(e) == int(116):
                x1 = int(x1) + 0
                y1 = int(y1) + v
        elif int(e) == int(113):
                x1 = int(x1) - v
                y1 = int(y1) + 0
        elif int(e) == int(114):
                x1 = int(x1) + v
                y1 = int(y1) + 0
        ec.transport.write(json.dumps({"x":x1,"y":y1,"j":nj}).encode('ascii')+b"\r\n")
        canvas.coords(label, x1, y1)

root.bind('<Key>', envoie)

# this connects the protocol to a server running on port 8000
f = EchoFactory()
reactor.connectTCP("192.168.0.2", 80, f)
reactor.run()

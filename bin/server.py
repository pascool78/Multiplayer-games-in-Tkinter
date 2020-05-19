from twisted.internet import reactor, protocol, endpoints
from twisted.protocols import basic
from twisted.internet import tksupport, reactor
import json, random

class PubProtocol(basic.LineReceiver):
    def __init__(self, factory):
        self.factory = factory

    def connectionMade(self):
        self.factory.clients.add(self)

    def connectionLost(self, reason):
        self.factory.clients.remove(self)

    def lineReceived(self, line):
        for c in self.factory.clients:
             pass
#            c.sendLine(b"ok")
        for c in self.factory.clients:
            source = u"<{}>pickle ".format(self.transport.getPeer())
            print ("line:",line)
            print ("from:",source)
            try:
              print (json.loads(line))
              print ("json ok")
            except:
              print ("json KO")
            print (line)
            c.sendLine(line)
           #print ("La position de " + str(k) + " est " + str(m) + ".")
class PubFactory(protocol.Factory):
    def __init__(self):
        self.clients = set()

    def buildProtocol(self, addr):
        return PubProtocol(self)

endpoints.serverFromString(reactor, "tcp:80").listen(PubFactory())
reactor.run()

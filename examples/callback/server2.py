from __future__ import with_statement
import Pyro

class CallbackServer(object):
    def doCallback(self, callback):
        print("server: doing callback 1 to client")
        try:
            callback.call1()
        except:
            print("got an exception from the callback.")
            print("".join(Pyro.util.getPyroTraceback()))
        print("server: doing callback 2 to client")
        try:
            callback.call2()
        except:
            print("got an exception from the callback.")
            print("".join(Pyro.util.getPyroTraceback()))
        print("server: callbacks done")

with Pyro.core.Daemon() as daemon:
    with Pyro.naming.locateNS() as ns:
        obj=CallbackServer()
        uri=daemon.register(obj)
        ns.remove("example.callback2")
        ns.register("example.callback2",uri)
    print("Server ready.")
    daemon.requestLoop()
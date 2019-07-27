from unittest import TestCase
from cinergia import pyCinergiaTestConn

import threading
import socketserver


class MyTCPHandler(socketserver.BaseRequestHandler):
    """
    The RequestHandler class for our server.

    It is instantiated once per connection to the server, and must
    override the handle() method to implement communication to the
    client.
    """

    def handle(self):
        # self.request is the TCP socket connected to the client
        self.data = self.request.recv(1024).strip()
        print("{} wrote:".format(self.client_address[0]))
        print(self.data)
        # just send back the same data, but upper-cased
        self.request.sendall(self.data.upper())


class Control_Tests(TestCase):
    def setUp(self):
        pass
    def tearDown(self):
        pass
    def test_main(self):

        self.assertEqual(pyCinergiaTestConn.main(['127.0.0.1']), -1)

        server = socketserver.TCPServer(("127.0.0.1", 1502), MyTCPHandler)
        th=threading.Thread(target=server.serve_forever)
        th.start()
        self.assertEqual(pyCinergiaTestConn.main(['127.0.0.1', '1502']), 0)
        server.shutdown()


        

"""
    Test TCP server. Assigment for U1 A1: Socket TCP.

    Author: Eloy Uziel García Cisneros (eloy.garcia@edu.uag.mx)

    usage: python server.py
"""

# Standar imports
import logging
import socketserver

logging.basicConfig(level='INFO')
LOGGER = logging.getLogger(__name__)

class RequestHandler(socketserver.BaseRequestHandler):
    """
    Request handler class.
    """
    SRV_RESP = "Hello from the other side, {c_addr}"
    ENCODING = 'UTF-8'

    def handle(self):
        """Handle client requests."""
        # Base class calls socket's .accept() method to accept, or complete the connection.
        # self.request object is created as result from this call (accept).
        data = self.request.recv(1024).decode(self.ENCODING).strip()

        LOGGER.info("%s Connected", self.client_address)
        LOGGER.info("Client says: %s", data)

        resp = self.SRV_RESP.format(c_addr=self.client_address).encode(self.ENCODING)
        # Sends response back to client.
        self.request.sendall(resp)
        data = self.request.recv(1024).decode(self.ENCODING).strip()

if __name__ == "__main__":
    """Control process workflow."""
    LOGGER.info('Starting TCPServer...')

    HOST, PORT = "127.0.0.1", 20001

    LOGGER.info('Listening on port %d', PORT)
    server = socketserver.TCPServer((HOST, PORT), RequestHandler)

    # Start TCP Server
    server.serve_forever()

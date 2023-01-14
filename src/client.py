"""
    Test TCP client. Assigment for U1 A1: Socket TCP.

    Author: Eloy Uziel García Cisneros (eloy.garcia@edu.uag.mx)

    usage: python client.py
"""

# Standar imports
import socket
import logging

logging.basicConfig(level='INFO')
LOGGER = logging.getLogger(__name__)

HOST = "127.0.0.1"  # The server's hostname or IP address
PORT = 20001  # The port used by the server
ENCODING = 'UTF-8'

if __name__ == "__main__":
    """Control process workflow."""
    while True:
        data = input('> ').encode(ENCODING)
        # Skip empty messages.
        if not data:
            continue

        # Create socket.
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            # Connecting to TCP server prior sending data.
            s.connect((HOST, PORT))
            s.sendall(data)
            data = s.recv(1024).decode(ENCODING)

            LOGGER.info(data)

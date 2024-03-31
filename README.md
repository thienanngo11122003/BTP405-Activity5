# BTP405-Activity5

## Overview

In this project, we implement a TCP server in Python that listens for incoming connections from clients. Using threading, we handle multiple client connections concurrently, allowing each client to communicate with the server without blocking others. We also develop a client in Python that can connect to the server, send messages, and display the responses from the server.

### Server

1. Start the server by running `server.py`.
    ```
    python server.py
    ```
2. The server will start listening on localhost and a port specified in the script (`65432` by default).

### Client

1. Start the client by running `client.py`.
    ```
    python client.py
    ```
2. The client will connect to the server.
3. Enter messages to send to the server. Type "quit" to exit the client application.

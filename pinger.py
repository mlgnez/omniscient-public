from mcstatus import JavaServer

import cosmos
from server import Server


def ping(ip, log):
    global server
    server = None

    try:
        mcserver = JavaServer.lookup(ip)
        status = mcserver.status()
        server = Server(status.players.online, status.players.max, status.description, status.latency, status.favicon, status.version, ip)

        server.print()

    except(TimeoutError, ConnectionError, Exception):
        if log:
            print("Connected Failed when getting server on ", ip)
        return None

    if cosmos.read_server(ip) is not None:
        cosmos.delete_server(ip)
    server.save_server()


def return_values_ping(ip, log):
    global server
    server = None

    try:
        mcserver = JavaServer.lookup(ip)
        status = mcserver.status()
        server = Server(status.players.online, status.players.max, status.description, status.latency, status.favicon, status.version, ip)

        return server

    except(TimeoutError, ConnectionError, Exception):
        if log:
            print("Connected Failed when getting server on ", ip)
        return None


def query(ip, log):
    global server
    server = None

    try:
        mcserver = JavaServer.lookup(ip)
        query = mcserver.query()

        return query

    except(TimeoutError, ConnectionError, Exception):
        if log:
            print("Connected Failed when querying ", ip)
        return None

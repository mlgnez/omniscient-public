import os, d_webhook, main
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

import cosmos
import ip_generator
import pinger


class Server:

    def __init__(self, online, max, description, latency, favicon, version, ip):
        self.online = online
        self.max = max
        self.description = description
        self.latency = latency
        self.favicon = favicon
        self.version = version
        self.ip = ip

        self.names = ""
        self.plugins = ""
        self.map = ""

        ping = pinger.query(ip, False)

        if ping is not None:
            self.names = ping.players.names
            self.plugins = ping.software.plugins
            self.map = ping.map

        print("Added", ip)

    def print(self):
        print(self.online, "|", self.max, "|", self.version.name, "|", self.description, "|", self.latency, "|",
              self.favicon, "|", self.ip)

    def save_server(self):

        d_webhook.sendServerWebhook(self.ip, self.online, self.max,
                                    self.description, self.latency, self.version.name)

        write = {
            'id': self.ip,
            'partitionKey': 'id',
            "ip": self.ip,
            "description": self.description,
            "version:": self.version.name,
            "latency": self.latency,
            "online": self.online,
            "max": self.max,
            "names": self.names,
            "plugins": self.plugins,
            "map": self.map,
            "favicon": self.favicon
        }

        cosmos.upload_server(write, self.ip)

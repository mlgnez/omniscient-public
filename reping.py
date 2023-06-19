import pinger, server, os, converter


class re_ping:

    def __init__(self):
        self.file_list = converter.get_all_files_drive().GetList()

    def repingallservers(self):
        for file in self.file_list:
            file_ip = str(file["originalFilename"]).replace(".txt", ":25565")
            pinger.ping(file_ip, True)

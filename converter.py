import pinger
import server, os
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
# converts old server file to google drive


class converter:
    def __init__(self, content):
        lines = str(content).splitlines()
        print(lines)
        if len(lines) > 0:
            self.online = lines[0].split(":")[1]
            self.max = lines[1].split(":")[1]
            self.description = lines[2].split(":")[1]
            self.latency = lines[3].split(":")[1]
            self.favicon = lines[4].split(":")[1]
            self.version = lines[5].split(":")[1]
            for i in range(len(lines)):
                if lines[i].__contains__("ip:"):
                    self.ip = lines[i].split("ip:")[1]
            self.server = server.Server(self.online, self.max, self.description, self.latency, self.favicon,
                                        self.version, self.ip)
        else:
            self.server = None

    def get_server(self):
        return self.server


def get_all_files_drive():
    gauth = GoogleAuth()
    gauth.LoadCredentialsFile("mycreds.txt")
    if gauth.credentials is None:
        gauth.LocalWebserverAuth()
    elif gauth.access_token_expired:
        gauth.Refresh()
    else:
        gauth.Authorize()
    gauth.SaveCredentialsFile("mycreds.txt")
    drive = GoogleDrive(gauth)

    return drive.ListFile({'q': "'root' in parents and trashed=false"})


def convert_server_files_to_drive():
    file_list = get_all_files_drive().GetList()
    name_file = []
    for file in file_list:
        name_file.append(file["originalFilename"])

    for file_name in os.listdir("servers"):
        try:
            file = converter(open("servers" + "/" + file_name).read())
            if not name_file.__contains__(str(file.ip).replace(":25565", ".txt")):
                print("Pinging", file.ip)
                pinger.ping(file.ip, False)
            else:
                print(file.ip, "already in drive, not adding")

        except Exception:
            print("Unable to convert " + file_name)

    for file_name in os.listdir("temp"):
        try:
            file = converter(open("temp" + "/" + file_name).read())
            if not name_file.__contains__(str(file.ip).replace(":25565", ".txt")):
                print("Pinging", file.ip)
                pinger.ping(file.ip, False)
            else:
                print(file.ip, "already in drive, not adding")

        except Exception:
            print("Unable to convert " + file_name)


def convert_drive_to_cosmos():
    there_yet = False
    file_list = get_all_files_drive().GetList()

    for file in file_list[597:]:
        file_ip = str(file["originalFilename"]).replace(".txt", ":25565")
        try:
            pinger.ping(file_ip, True)
        except Exception:
            pass



if __name__ == '__main__':
    convert_drive_to_cosmos()

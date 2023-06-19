import cosmos
import ip_generator, pinger, concurrent.futures, reping, time
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive


def ping():
    while True:
        pinger.ping(ip_generator.generate_ip(), False)


def re_ping():
    rep = reping.re_ping()
    rep.repingallservers()


class main:

    def __init__(self):

        workers = 250
        with concurrent.futures.ThreadPoolExecutor(max_workers=workers) as x:
            x.submit(re_ping)

            for i in range(workers - 1):
                x.submit(ping)


if __name__ == '__main__':
    main = main()

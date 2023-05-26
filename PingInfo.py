class PingInfo:
    def __init__(self, url, ip, date, currentTime, ttl, time, lostPackages):
        self.url = url
        self.ip = ip
        self.date = date
        self.currentTime = currentTime
        self.ttl = ttl
        self.time = time
        self.lostPackages = lostPackages

    def __str__(self):
        return "Data: {}\nHorário {}\nUrl: {}\nIp: {}\nTTL: {}\nTime (média): {} ms\nPacotes perdidos: {}".format(
            self.date, self.currentTime, self.url, self.ip, self.ttl, self.time, self.lostPackages
        )

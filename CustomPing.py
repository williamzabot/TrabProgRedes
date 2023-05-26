import os, platform
from datetime import datetime
from datetime import date
from PingInfo import PingInfo

file = "customping.txt"

def menu():
    while True:
        print("-------------------------- Bem Vindo - ---------------------")
        url = str(input("Digite uma URL: "))
        qtd = int(input("Digite a quantidade de pacotes que deseja: "))
        qtdPackages = verifyPlatform(str(qtd))
        command = "ping " + qtdPackages + url + " > " + file
        os.system(command)
        print("-------------------------- PINGANDO - ----------------------")
        pingInfo = getPingInfo(url, qtd)
        print(pingInfo)
        choice = str(input("Deseja continuar? [S]im [N]ao ")).lower()
        if choice != "s":
            break


def getDate():
    return date.today().strftime('%d/%m/%Y')


def getCurrentTime():
    return datetime.now().strftime('%H:%M')


def verifyPlatform(qtd):
    if platform.system().lower() == "windows":
        return "-n " + str(qtd) + " "
    else:
        return "-c " + str(qtd) + " "


def getPingInfo(url, qtd):
    arq = open(file)
    lines = arq.readlines()
    firstLine = lines[0]
    secondLine = lines[1].split()
    resultsLine = lines[qtd + 3]
    ip = getIp(firstLine)
    ttl = getPosition(secondLine, 5)
    time = getPosition(secondLine, 6)
    lostPackages = resultsLine.split()[6]
    date = getDate()
    currentTime = getCurrentTime()
    return PingInfo(
        url,
        ip,
        date,
        currentTime,
        ttl,
        time,
        lostPackages
    )


def getIp(line):
    splitLine = line.split()
    return splitLine[2].replace(":", "").replace("(", "").replace(")", "")


def getPosition(splitLine, position):
    target = splitLine[position]
    return target.split("=")[1]


menu()

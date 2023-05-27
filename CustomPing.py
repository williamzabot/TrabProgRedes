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

def verifyPlatform(qtd):
    if platform.system().lower() == "windows":
        return "-n " + str(qtd) + " "
    else:
        return "-c " + str(qtd) + " "


def getPingInfo(url, qtd):
    arq = open(file)
    lines = arq.readlines()
    firstLine = lines[0].split()
    secondLine = lines[1].split()
    resultsLine = lines[qtd + 3].split()
    pingInfo = PingInfo()
    pingInfo.url = url
    pingInfo.ip = firstLine[2].replace(":", "").replace("(", "").replace(")", "")
    pingInfo.ttl = getPosition(secondLine, 5)
    pingInfo.time = getPosition(secondLine, 6)
    pingInfo.lostPackages = resultsLine[6]
    pingInfo.date = date.today().strftime('%d/%m/%Y')
    pingInfo.currentTime = datetime.now().strftime('%H:%M')
    return pingInfo


def getPosition(splitLine, position):
    target = splitLine[position]
    return target.split("=")[1]


menu()

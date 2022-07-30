import subprocess
import time
import matplotlib.pyplot as plt
import numpy as np

#Add time stamp to file

def _main():
    userInput = str(input("Begin Roaming Scan? Y/N: ")).lower()
    if 'y' in userInput:
        _scan()
    #if "n" in userInput:
        #userInput = str(input("Load File? Y/N: ")).lower()
        #if "y" in userInput:
    userInput = str(input("Save signal data? Y/N: ")).lower()
    if "y" in userInput:
        filename = str(input("Enter the filename to create: "))
        with open(filename + ".txt","w") as file:
            file.write(str(bssid+"\n"))
        with open(filename + ".txt","a") as file:
            file.write(str(signalCol))
            file.write("\nAmount of time in S taken: " + str(x))
        with open(filename + ".txt","a") as file:
            file.write 
          
    userInput = str(input("Graph? Y/N: "))
    if "y" in userInput:
        _pltGraph()

def _scan():
    global signalCol, bssid, x

    scanData = str(subprocess.check_output("netsh wlan show interfaces"))
    nameLoc = scanData.find("Name")
    descLoc = scanData.find("Description")
    bssidLoc = scanData.find("BSSID")
    signalLoc = scanData.find("Signal")
    name = scanData[nameLoc:descLoc-8]
    bssid = scanData[bssidLoc:bssidLoc+42]
    signal = scanData[signalLoc:signalLoc+28]
    print(name)
    print(bssid)
    print(signal)

    bssidComp = bssid
    signalCol = []
    x = 0
    while bssidComp == bssid:
        time.sleep(1)
        scanData = str(subprocess.check_output("netsh wlan show interfaces"))
        bssidLoc = scanData.find("BSSID")
        signalLoc = scanData.find("Signal")
        bssidComp = scanData[bssidLoc:bssidLoc+42]
        signal = scanData[signalLoc+25:signalLoc+27]
        signalCol.append(int(signal))
        print(signal)
        #print(scanData)
        x += 1

def _pltGraph():
    y = 1
    timeL = []

    while y != len(signalCol)+1:
        timeL.append(y)
        y+=1

    print(len(signalCol))
    plt.plot(timeL, signalCol)
    plt.ylabel("Signal Strength")
    plt.xlabel("Time Passed")
    plt.show()

mains = None
while mains == None:
    _main()
    rep = None
    while rep == None:
        x = input("Repeat?\n(y/n): ")
        if 'y' or '' in x:
            rep = False
        if 'n' in x:
            print("--Goodbye--")
            rep = False
            mains = False
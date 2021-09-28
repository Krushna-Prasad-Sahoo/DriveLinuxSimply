
import os
import time

def menu6():
    os.system("clear")
    print("\n\t\t\t\t This Exclusive Section provides you the following options...\n")
    time.sleep(1)
    os.system("tput setf 5")
    print("\n \t\t 1. Configure a Web Server in this OS")
    time.sleep(1)
    print("\t\t 2. Configure Docker & work on it")
    time.sleep(1)
    print("\t\t 3. Exit from this SECTION\n")

def menu6_blank():
    os.system("clear")
    print("\n\t\t\t\t This Exlusive Section provides you the following options...\n")
    os.system("tput setf 5")
    print("\n \t\t 1. Configure a Web Server in this OS")
    print("\t\t 2. Configure Docker & work on it")
    print("\t\t 3. Exit from this SECTION\n")

menu6()
while True:
    menu6_blank()
    os.system("tput setf 2")
    print("\t \t\t Enter your choice :", end=" ")
    ch4 = int(input())

    if ch4 == 1:
        time.sleep(1)
        print("\n\t\t Now you are going to enter into WebServer Configuration.\n\t\t You just need to go step by step for succesful configuration. \n\t\t Just follow 1 -> 2 -> 3 -> 4 -> 5 ")
        input("\n\t press enter to continue... ")
        os.system("python3 webserver.py")
    elif ch4 == 2:
        time.sleep(2)
        print("\n\t\t Now you are going to enter into Docker World....\n\t\t We are configuring docker for you.\n\t\t You can start working now ... ")
        time.sleep(2)
        os.system("python3 docker.py")
        input("\n\t press enter to continue... ")
    elif ch4 == 3:
        os.system("tput sgr0")
        time.sleep(1)
        print("\n")
        break
    else:
        print("\n\t You have entered wrong value, plz. try again ..")
        time.sleep(1)
        input("\n\t press enter to continue... ")




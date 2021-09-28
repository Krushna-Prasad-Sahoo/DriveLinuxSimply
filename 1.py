
import os
import time
import pyfiglet as pf

result = pf.figlet_format("          DONE", font = "bubble" )

def menu1():
    os.system("clear")
    time.sleep(1)
    print("\n\t\t\t This Basic System Utility Section provides you with the following options...\n")
    os.system("tput setf 5")
    print("\n \t\t 1. See the date")
    time.sleep(1)
    print("\t\t 2. See the calendar")
    time.sleep(1)
    print("\t\t 3. Check your IP Address")
    time.sleep(1)
    print("\t\t 4. Check your hostname")
    time.sleep(1)
    print("\t\t 5. Change your hostname")
    time.sleep(1)
    print("\t\t 6. Check internet connectivity")
    time.sleep(1)
    print("\t\t 7. Check your terminal name")
    time.sleep(1)
    print("\t\t 8. Switch on your network")
    time.sleep(1)
    print("\t\t 9. Switch off your network")
    time.sleep(1)
    print("\t\t 10. Exit from this SECTION\n")

def menu1_blank():
    os.system("clear")
    print("\n\t\t\t This Basic System Utility Section provides you with the following options...\n")
    os.system("tput setf 5")
    print("\n \t\t 1. See the date")
    print("\t\t 2. See the calendar")
    print("\t\t 3. Check your IP Address")
    print("\t\t 4. Check your hostname")
    print("\t\t 5. Change your hostname")
    print("\t\t 6. Check internet connectivity")
    print("\t\t 7. Check your terminal name")
    print("\t\t 8. Switch on your network")
    print("\t\t 9. Switch off your network")
    print("\t\t 10. Exit from this SECTION\n")


menu1()
while True:
    menu1_blank()
    os.system("tput setf 2")
    print("\t \t\t Enter your choice :", end=" ")
    ch1 = int(input())

    if ch1 == 1:
        time.sleep(1)
        os.system("date")
        input("\n\t press enter to continue... ")
    elif ch1 == 2:
        time.sleep(1)
        os.system("cal")
        input("\n\t press enter to continue... ")
    elif ch1 == 3:
        time.sleep(1)
        os.system("ifconfig enp0s3 | grep inet")
        input("\n\t press enter to continue... ")
    elif ch1 == 4:
        time.sleep(1)
        os.system("hostname")
        input("\n\t press enter to continue... ")
    elif ch1 == 5:
        time.sleep(1)
        print("\n\t Enter new hostname:", end=" ")
        nh = input()
        os.system("hostnamectl  set-hostname  " + nh )
        time.sleep(1)
        print(result)
        input("\n\t press enter to continue... ")
    elif ch1 == 6:
        time.sleep(1)
        os.system("ping -c 3 8.8.8.8")
        input("\n\t press enter to continue... ")
    elif ch1 == 7:
        time.sleep(1)
        os.system("tty")
        input("\n\t press enter to continue... ")
    elif ch1 == 8:
        time.sleep(1)
        os.system("nmcli conn up enp0s3")
        input("\n\t press enter to continue... ")
    elif ch1 == 9:
        time.sleep(1)
        os.system("nmcli conn down enp0s3")
        input("\n\t press enter to continue... ")
    elif ch1 == 10:
        os.system("tput sgr0")
        time.sleep(1)
        print("\n")
        break
    else:
        print("\n\t You have entered wrong choice my dear, plz try again..")
        time.sleep(1)
        input("\n\t press enter to continue... ")





import os
import time
import pyfiglet as pf

result = pf.figlet_format("          DONE", font = "bubble" )

def menu5():
    os.system("clear")
    print("\n\t\t This RHEL8 Packages & Processes related Section provides you the following options...\n")
    time.sleep(1)
    os.system("tput setf 5")
    print("\n \t\t 1. Check if a package is installed or not")
    time.sleep(1)
    print("\t\t 2. Download & install a package ")
    time.sleep(1)
    print("\t\t 3. Check the memory of your Linux OS")
    time.sleep(1)
    print("\t\t 4. Check the manual of any specific command")
    time.sleep(1)
    print("\t\t 5. Get help of any specific command ")
    time.sleep(1)
    print("\t\t 6. Check all currently running  process")
    time.sleep(1)
    print("\t\t 7. Check the CRON-JOBs for logged in User")
    time.sleep(1)
    print("\t\t 8. Schedule CRON-JOBs")
    time.sleep(1)
    print("\t\t 9. Get summary of every logged in Users")
    time.sleep(1)
    print("\t\t 10. Exit from this SECTION\n")

def menu5_blank():
    os.system("clear")
    print("\n\t\t This RHEL8 Packages & Processes related Section provides you the following options...\n")
    os.system("tput setf 5")
    print("\n \t\t 1. Check if a package is installed or not")
    print("\t\t 2. Download & install a package ")
    print("\t\t 3. Check the memory of your Linux OS")
    print("\t\t 4. Check the manual of any specific command")
    print("\t\t 5. Get help of any specific command ")
    print("\t\t 6. Check all cureently running process")
    print("\t\t 7. Check the CRON-JOBs for logged in User")
    print("\t\t 8. Schedule CRON-JOBs")
    print("\t\t 9. Get summary of every logged in Users")
    print("\t\t 10. Exit from this SECTION\n")

menu5()
while True:
    menu5_blank()
    os.system("tput setf 2")
    print("\t \t\t Enter your choice :", end=" ")
    ch5 = int(input())

    if ch5 == 1:
        time.sleep(1)
        print("\n\t Enter the package name :", end=" ")
        pack1 = input()
        os.system("rpm -q " + pack1)
        input("\n\t press enter to continue... ")
    elif ch5 == 2:
        time.sleep(1)
        print("\n\t Enter the package name :", end=" ")
        pack2 = input()
        os.system("dnf install  " + pack2 + "  -y ")
        input("\n\t press enter to continue... ")
    elif ch5 == 3:
        time.sleep(1)
        os.system("free -mh")
        input("\n\t press enter to continue... ")
    elif ch5 == 4:
        time.sleep(1)
        print("\n\t Enter the COMMAND whose manual you wanna visit :", end=" ")
        cmd4 = input()
        print("\n\t Press 'Q' to quit from manual page ...")
        time.sleep(2)
        os.system("man " + cmd4 + " | less")
        input("\n\t press enter to continue... ")
    elif ch5 == 5:
        time.sleep(1)
        print("\n\t Enter the command to get help :", end=" ")
        cmd5 = input()
        print("\n\t Press 'Q' to quit ...")
        time.sleep(2)
        os.system(cmd5 + "  --help | less")
        input("\n\t press enter to continue... ")
    elif ch5 == 6:
        time.sleep(1)
        print("\n\t Press 'Q' to quit...")
        time.sleep(2)
        os.system("ps -a | less")
        input("\n\t press enter to continue... ")
    elif ch5 == 7:
        time.sleep(1)
        os.system("crontab -l")
        input("\n\t press enter to continue... ")
    elif ch5 == 8:
        time.sleep(1)
        print("\n\t Enter the Min-Hour-DayOfMonth-Month-DayOfWeek (separated by a space) :", end=" ")
        timing8 = input()
        print("\n\t Enter the task you wanna schedule (give full path) : ", end="")
        task8 = input()
        timingNtask8 = timing8 + " " + task8
#        cmd8 = ''' { crontab -l; echo " ''' + timingNtask8 + ''' "; } | crontab -  '''
        cmd8 = ''' { echo " ''' + timingNtask8 + ''' "; } | crontab -  '''
        os.system(cmd8)
        time.sleep(1)
        print(result)
        input("\n\t press enter to continue... ")
    elif ch5 == 9:
        time.sleep(1)
        os.system("w ")
        input("\n\t press enter to continue... ")
    elif ch5 == 10:
        os.system("tput sgr0")
        time.sleep(1)
        print("\n")
        break
    else:
        print("\n\t You have entered wrong choice bro, plz. try again ..")
        time.sleep()
        input("\n\t press enter to continue... ")




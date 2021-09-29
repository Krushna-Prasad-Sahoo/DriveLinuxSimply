
import os
import time
import pyfiglet as pf

result = pf.figlet_format("          DONE", font = "bubble" )

def menuWeb():
    os.system("clear")
    print("\n\t\t\t Welcome to the WebServer Configuration Section...\n")
    time.sleep(1)
    os.system("tput setf 5")
    print("\n \t\t 1. Configure yum repository for Web Server")
    time.sleep(1)
    print("\t\t 2. Download & install Web Server Package")
    time.sleep(1)
    print("\t\t 3. Set the document root")
    time.sleep(1)
    print("\t\t 4. Start the Server")
    time.sleep(1)
    print("\t\t 6. Visit your website..")
    print("\t\t 5. Exit from this SECTION\n")

def menuWeb_blank():
    os.system("clear")
    print("\n\t\t\t Welcome to the WebServer Configuration Section...\n")
    os.system("tput setf 5")
    print("\n \t\t 1. Configure yum repository for Web Server")
    print("\t\t 2. Download & install Web Server Package")
    print("\t\t 3. Set the document root")
    print("\t\t 4. Start the Server")
    print("\t\t 5. Visit your website ..")
    print("\t\t 6. Exit from this SECTION\n")

menuWeb()
while True:
    menuWeb_blank()
    os.system("tput setf 2")
    print("\t \t\t Enter your choice :", end=" ")
    chW = int(input())

    if chW == 1:
        time.sleep(1)
        print("\n\t Yum Configured .. go ahead")
        time.sleep(1)
        input("\n\t press enter to continue... ")
    elif chW == 2:
        time.sleep(1)
        os.system("sudo yum reinstall httpd -y")
        input("\n\t press enter to continue... ")
    elif chW == 3:
        time.sleep(1)
        print("\n\t Give a sample html page(named as index.html) :", end=" ")
        page3 = input()
        os.system("cp -f " + page3 + "   /var/www/html/")
        time.sleep(1)
        print(result)
        input("\n\t press enter to continue... ")
    elif chW == 4:
        time.sleep(1)
        os.system("sudo systemctl start httpd")
        os.system("systemctl status httpd | grep Active")
        time.sleep(1)
        print("\n\t\t Now you can access your Website by pressing 5 next ..")
        time.sleep(1)
        input("\n\t press enter to continue... ")
    elif chW == 5:
        time.sleep(1)
        os.system("curl  localhost:80")
        time.sleep(1)
        input("\n\t press enter to continue ...")
    elif chW == 6:
        os.system("tput sgr0")
        time.sleep(1)
        print("\n")
        break
    else :
        print("\n\t You have entered wrong choice bro, plz try again ..")
        time.sleep(1)
        input("\n\t press enter to continue... ")





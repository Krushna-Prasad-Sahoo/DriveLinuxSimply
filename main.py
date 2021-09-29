#!/usr/bin/python3

import os
import art
import time
import getpass

os.system("clear")
os.system("tput setf 1 ")
print("\n \t\t\t\t (: ..Manage Linux using Numbers & Alphabets Only.. :)  \n")
time.sleep(1)
os.system("tput setf 4")
print("\n \t\t\t\t   (: Please Enter your nick name ... ", end=" ")
name = input()
time.sleep(1)
os.system("tput setf 2")
art.tprint("   Hello _ " + name + " _!! ")
os.system("tput setf 1")
passwd = getpass.getpass("\n \t\t Please Enter Your Password with a smile : \n")
if passwd != "kp":
        os.system("tput setf 4")
        art.tprint("  :(  ")
        print("\n \t\t Authentication Failed .... \n")
        time.sleep(1)
        os.system("tput sgr0 ")
else :
        os.system("tput setf 2")
        art.tprint(" ~:)")
        print("\n \t\t Authentication Successful .... \n")
        time.sleep(1)
        def menu():
          os.system("clear")
          os.system("tput setf 5")
          time.sleep(1)
          print("\n \t\t\t\t   (: This application offers you the following facilities. :) ")      
          print(" \t\t\t\t    ---------------------------------------------------------    \n")
          time.sleep(1)
          print("\n \t\t Press the numbers to go the respective section, see the hints to get some idea ...\n")
          time.sleep(2)
          os.system("tput setf 3")
          print("\n \t\t 1. Basic System Utility Section [To see date,calendar,hostname,terminal,network connectivity etc.]\n")
          time.sleep(2)
          print("\t\t 2. User & Permission Management Section [To check user, create & delete user, permissions etc.]\n")
          time.sleep(2)
          print("\t\t 3. File Management Section [To list, create, delete, copy, move files & directoties.]\n")
          time.sleep(2)
          print("\t\t 4. File System based Section [To work with disk, mounting & unmounting,lvm & fstab etc.]\n")
          time.sleep(2)
          print("\t\t 5. RHEL8 Packages & Process based Section [To install package, check memory, kill process etc.]\n")
          time.sleep(2)
          print("\t\t 6. Exclusive Section [To setup basic WebServer & work with Docker Containers]\n")
          time.sleep(1)
          print("\t\t 7. Exit from the Application\n")


        def menu_blank():
          os.system("clear")
          os.system("tput setf 5")
          print("\n \t\t\t\t   (: This application offers you the following facilities. :) ")
          print(" \t\t\t\t    ---------------------------------------------------------    \n")
          print("\n \t\t Press the numbers to go the respective section, see the hints to get some idea ...\n")
          os.system("tput setf 3")
          print("\n \t\t 1. Basic System Utility Section [To see date,calendar,hostname,terminal,network connectivity etc.]\n")
          print("\t\t 2. User & Permission Management Section [To check user, create & delete user, permissions etc.]\n")
          print("\t\t 3. File Management Section [To list, create, delete, copy, move files & directoties.]\n")
          print("\t\t 4. File System based Section [To work with disk, mounting & unmounting,lvm & fstab etc.]\n")
          print("\t\t 5. RHEL8 Packages & Process based Section [To install package, check memory, kill process etc.]\n")
          print("\t\t 6. Exclusive Section [To setup basic WebServer & work with Docker Containers\n")
          print("\t\t 7. Exit from the Application\n")

        menu()
        while True:
          menu_blank()
          os.system("tput setf 2")
          print("\n \t\t Enter your choice : ", end=" ")
          choice = int(input())
        
  
          if choice == 1:
              os.system("python3 1.py")
              os.system("tput setf 1")
              input("Press enter to continue ..\n")
              time.sleep(1)
          elif choice == 2:
              os.system("python3 2.py")
              os.system("tput setf 1")
              input("Press enter to continue ..\n")
              time.sleep(1)
          elif choice == 3:
              os.system("python3 3.py")
              os.system("tput setf 1")
              input("Press enter to continue ..\n")
              time.sleep(1)
          elif choice == 4:
              os.system("python3 4.py")
              os.system("tput setf 1")
              input("Press enter to continue ..\n")
              time.sleep(1)
          elif choice == 5:
              os.system("python3 5.py")
              os.system("tput setf 1")
              input("Press enter to continue ..\n")
              time.sleep(1)
          elif choice == 6:
              os.system("python3 6.py")
              os.system("tput setf 1")
              input("Press enter to continue ..\n")
              time.sleep(1)
          elif choice == 7:
              os.system("tput setf 6")
              art.tprint("   _BYE _" + name +" _!!")
              time.sleep(1)
              input("Press enter to continue ..\n")
              os.system("tput sgr0 ")
              time.sleep(1)
              break
          else:
              os.system("tput setb 6 ")
              os.system("tput setf 4")
              print("\n \t\t Dear " + name + " You have entered a wrong choice, please try again ...\n")
              time.sleep(1)
              os.system("tput setab 0")
              os.system("tput setf 2")
              input("Press enter to continue ..\n")
              time.sleep(1)






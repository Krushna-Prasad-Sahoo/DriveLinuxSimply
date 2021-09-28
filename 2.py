
import os
import time
import pyfiglet as pf

result = pf.figlet_format("          DONE", font = "bubble" )

def menu2():
    os.system("clear")
    print("\n\t\t This User/Group & Permission Management Section provides you with the following options...\n")
    time.sleep(1)
    os.system("tput setf 5")
    print("\n \t\t 1. Check a user, if exists or not")
    time.sleep(1)
    print("\t\t 2. Check current logged in user")
    time.sleep(1)
    print("\t\t 3. Create a User & set password")
    time.sleep(1)
    print("\t\t 4. Delete a User(only possible if you are root)")
    time.sleep(1)
    print("\t\t 5. Create a group ")
    time.sleep(1)
    print("\t\t 6. Add an existing User to an existing group")
    time.sleep(1)
    print("\t\t 7. Check permission of a file")
    time.sleep(1)
    print("\t\t 8. Check permission of a directory")
    time.sleep(1)
    print("\t\t 9. Change ownership of a file/directory")
    time.sleep(1)
    print("\t\t 10. Change permission of a file/directory")
    time.sleep(1)
    print("\t\t 11. Exit from this SECTION\n")

def menu2_blank():
    os.system("clear")
    print("\n\t\t This User/Group & Permission Management Section provides you with the following options...\n")
    os.system("tput setf 5")
    print("\n \t\t 1. Check a user, if exists or not")
    print("\t\t 2. Check current logged in user")
    print("\t\t 3. Create a User & set password")
    print("\t\t 4. Delete a User(only possible if you are root)")
    print("\t\t 5. Create a group ")
    print("\t\t 6. Add an existing User to an existing group")
    print("\t\t 7. Check permission of a file")
    print("\t\t 8. Check permission of a directory")
    print("\t\t 9. Change ownership of a file/directory")
    print("\t\t 10. Change permission of a file/directory")
    print("\t\t 11. Exit from this SECTION\n")

menu2()
while True:
    menu2_blank()
    os.system("tput setf 2")
    print("\t \t\t Enter your choice :", end=" ")
    ch2 = int(input())

    if ch2 == 1:
        time.sleep(1)
        print("\n\t Enter the username you want to search : ", end="")
        username1 = input()
        os.system("id " + username1 )
        input("\n\t press enter to continue... ")
    elif ch2 == 2:
        time.sleep(1)
        os.system("whoami ")
        input("\n\t press enter to continue... ")
    elif ch2 == 3:
        time.sleep(1)
        print("\n\t Enter the new username you want to create :", end=" ")
        username3 = input()
        os.system("useradd  " + username3 )
        os.system("passwd  " + username3)
        time.sleep(1)
        input("\n\t press enter to continue... ")
    elif ch2 == 4:
        time.sleep(1)
        print("\n\t Enter the username you want to delete :", end=" ")
        username4 = input()
        os.system("userdel  " + username4)
        time.sleep(1)
        print(result)
        input("\n\t press enter to continue... ")
    elif ch2 == 5:
        time.sleep(1)
        print("\n\t Enter the new groupname you want to create :", end=" ")
        groupname5 = input()
        os.system("groupadd  " + groupname5)
        time.sleep(1)
        print(result)
        input("\n\t press enter to continue... ")
    elif ch2 == 6:
        time.sleep(1)
        print("\n\t Enter the username whom you want to add to the group :", end=" ")
        uname6 = input()
        print("\n\t Enter the groupname for the user :", end=" ")
        gname6 = input()
        os.system("sudo usermod -a  -G " + gname6 + "  " + uname6 )
        time.sleep(1)
        print(result)
        input("\n\t press enter to continue... ")
    elif ch2 == 7:
        time.sleep(1)
        print("\n\t Enter the file name (give absolute path) :", end=" ")
        fname7 = input()
        os.system("ls -l " + fname7)
        input("\n\t press enter to continue... ")
    elif ch2 == 8:
        time.sleep(1)
        print("\n\t Enter the directory name (give absolute path) :", end=" ")
        dirname8 = input()
        os.system("ls -ld " + dirname8)
        input("\n\t press enter to continue... ")
    elif ch2 == 9:
        time.sleep(1)
        print("\n \t Enter the file/directory name : ", end="")
        fd9 = input()
        print("\n\t Enter the username for ownership of this file :", end=" ")
        u9 = input()
        os.system("chown " + u9 + " " + fd9)
        time.sleep(1)
        print(result)
        input("\n\t press enter to continue... ")
    elif ch2 == 10:
        time.sleep(1)
        print("\n \t Enter the file/directory name : ", end="")
        fd10 = input()
        print("\n \t Enter the permission in numbers (example: 777): ", end="")
        permi = input()
        os.system("chmod  " + permi + " " + fd10)
        time.sleep(1)
        print(result)
        input("\n\t press enter to continue... ")
    elif ch2 == 11:
        os.system("tput sgr0")
        time.sleep(1)
        print("\n")
        break
    else:
        print("\n\t You have entered wrong choice bro, plz try again..")
        time.sleep(1)
        input("\n\t press enter to continue... ")





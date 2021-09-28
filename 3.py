
import os
import time
import pyfiglet as pf

result = pf.figlet_format("          DONE", font = "bubble" )

def menu3():
    os.system("clear")
    print("\n\t\t\t This Files & Directory Management Section provides you the following options...\n")
    time.sleep(1)
    os.system("tput setf 5")
    print("\n \t\t 1. Check if a file is present or not")
    time.sleep(1)
    print("\t\t 2. Check if a directory is present or not")
    time.sleep(1)
    print("\t\t 3. Create a directory")
    time.sleep(1)
    print("\t\t 4. Delete a file/directory")
    time.sleep(1)
    print("\t\t 5. Create an empty file ")
    time.sleep(1)
    print("\t\t 6. Add data into an existing file ")
    time.sleep(1)
    print("\t\t 7. See the contents of a file")
    time.sleep(1)
    print("\t\t 8. Copy a file/directory from soruce to destination")
    time.sleep(1)
    print("\t\t 9. Move a file/directory from source to destination")
    time.sleep(1)
    print("\t\t 10. Download a file from URL")
    time.sleep(1)
    print("\t\t 11. Exit from this SECTION\n")

def menu3_blank():
    os.system("clear")
    print("\n\t\t\t This Files & Directory Management Section provides you the following options...\n")
    os.system("tput setf 5")
    print("\n \t\t 1. Check if a file is present or not")
    print("\t\t 2. Check if a directory is present or not")
    print("\t\t 3. Create a directory")
    print("\t\t 4. Delete a file/directory")
    print("\t\t 5. Create an empty file ")
    print("\t\t 6. Add data into an existing file ")
    print("\t\t 7. See the contents of a file")
    print("\t\t 8. Copy a file/directory from soruce to destination")
    print("\t\t 9. Move a file/directory from source to destination")
    print("\t\t 10. Download a file from URL")
    print("\t\t 11. Exit from this SECTION\n")
  


menu3()
while True:
    menu3_blank()
    os.system("tput setf 2")
    print("\t \t\t Enter your choice :", end=" ")
    ch3 = int(input())

    if ch3 == 1:
        time.sleep(1)
        print("\n\t Enter the file name (give absolute path) :", end=" ")
        f1 = input()
        os.system("ls -l " + f1)
        input("\n\t press enter to continue... ")
    elif ch3 == 2:
        time.sleep(1)
        print("\n\t Enter the directory name (give absolute path) :", end=" ")
        d2 = input()
        os.system("ls -ld " + d2)
        input("\n\t press enter to continue... ")
    elif ch3 == 3:
        time.sleep(1)
        print("\n\t Enter the directory name (give absolute path) :", end=" ")
        d3 = input()
        os.system("mkdir " + d3)
        time.sleep(1)
        print(result)
        input("\n\t press enter to continue... ")
    elif ch3 == 4:
        time.sleep(1)
        print("\n\t Enter the directory name (give absolute path) :", end=" ")
        d4 = input()
        os.system("rm -rf " + d4)
        time.sleep(1)
        print(result)
        input("\n\t press enter to continue... ")
    elif ch3 == 5:
        time.sleep(1)
        print("\n\t Enter the file name (give absolute path) :", end=" ")
        f5 = input()
        os.system("touch " + f5)
        time.sleep(1)
        print(result)
        input("\n\t press enter to continue... ")
    elif ch3 == 6:
        time.sleep(1)
        print("\n\t Enter the file name where U wanna keep data :", end=" ")
        f6 = input()
        print("\n\t Enter the data :", end=" ")
        data6 = input()
        os.system("echo " + data6 + " >> " + f6)
        time.sleep(1)
        print(result)
        input("\n\t press enter to continue... ")
    elif ch3 == 7:
        time.sleep(1)
        print("\n\t Enter the file name (give absolute path) :", end=" ")
        f7 = input()
        os.system("cat " + f7)
        input("\n\t press enter to continue... ")
    elif ch3 == 8:
        time.sleep(1)
        print("\n\t Enter the file/directory name (give absolute path) :", end=" ")
        fd8 = input()
        print("\n \t Enter the destination :", end=" ")
        dest8 = input()
        os.system("sudo cp -rf " + fd8 + " " + dest8)
        time.sleep(1)
        print(result)
        input("\n\t press enter to continue... ")
    elif ch3 == 9:
        time.sleep(1)
        print("\n\t Enter the file/directory name (give absolute path) :", end=" ")
        fd9 = input()
        print("\n\t Enter the destination :", end=" ")
        dest9 = input()
        os.system("sudo mv -f " + fd9 + " " + dest9)
        time.sleep(1)
        print(result)
        input("\n\t press enter to continue... ")
    elif ch3 == 10:
        time.sleep(1)
        print("\n\t Enter the URL of the file you want to download :", end=" ")
        url10 = input()
        os.system("wget --progress=dot  " + url10)
        input("\n\t press enter to continue... ")
    elif ch3 == 11:
        os.system("tput sgr0")
        time.sleep(1)
        print("\n")
        break
    else:
        print("\n\t You have entered wrong choice bro, plz try again")
        time.sleep(1)
        input("\n\t press enter to continue... ")




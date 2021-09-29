
import os
import time
import pyfiglet as pf

result = pf.figlet_format("          DONE", font = "bubble" )

def menud():
    os.system("clear")
    print("\n\t\t\t Welcome to the DOCKER container world ...\n")
    time.sleep(1)
    os.system("tput setf 5")
    print("\n \t\t 1. Check if Docker daemon is running or not")
    time.sleep(1)
    print("\t\t 2. Start Docker Service")
    time.sleep(1)
    print("\t\t 3. Stop Docker Service")
    time.sleep(1)
    print("\t\t 4. Check the details about your Docker Server")
    time.sleep(1)
    print("\t\t 5. List the running Docker Containers")
    time.sleep(1)
    print("\t\t 6. List all the docker images available")
    time.sleep(1)
    print("\t\t 7. Launch a container yourself")
    time.sleep(1)
    print("\t\t 8. Start a stopped container")
    time.sleep(1)
    print("\t\t 9. Build a Docker image from Dockerfile")
    time.sleep(1)
    print("\t\t 10. Exit from this SECTION\n")

def menud_blank():
    os.system("clear")
    print("\n\t\t\t Welcome to the DOCKER container world ...\n")
    os.system("tput setf 5")
    print("\n \t\t 1. Check if Docker daemon is running or not")
    print("\t\t 2. Start Docker Service")
    print("\t\t 3. Stop Docker Service")
    print("\t\t 4. Check the details about your Docker Server")
    print("\t\t 5. List the running Docker Containers")
    print("\t\t 6. List all the docker images available")
    print("\t\t 7. Launch a container yourself in background")
    print("\t\t 8. Start a stopped container")
    print("\t\t 9. Build a Docker image from Dockerfile")
    print("\t\t 10. Exit from this SECTION\n")

menud()
while True:
    menud_blank()
    os.system("tput setf 2")
    print("\t \t\t Enter your choice :", end=" ")
    chd = int(input())

    if chd == 1:
        time.sleep(1)
        os.system("systemctl status docker | grep Active")
        input("\n\t press enter to continue... ")
    elif chd == 2:
        time.sleep(1)
        os.system("systemctl start docker")
        time.sleep(1)
        print(result)
        input("\n\t press enter to continue... ")
    elif chd == 3:
        time.sleep(1)
        os.system("systemctl stop docker")
        time.sleep(1)
        print(result)
        input("\n\t press enter to continue... ")
    elif chd == 4:
        time.sleep(1)
        os.system("docker info")
        input("\n\t press enter to continue... ")
    elif chd == 5:
        time.sleep(1)
        os.system("docker  ps")
        input("\n\t press enter to continue... ")
    elif chd == 6:
        time.sleep(1)
        os.system("docker images ")
        input("\n\t press enter to continue... ")
    elif chd == 7:
        time.sleep(1)
        print("\n\t Enter the Image from where you want to launch container : ", end=""
)
        img7 = input()
        print("\n\t What name you want to give to the tiny OS :", end=" ")
        name7 = input()
        os.system("docker run -it --name " + name7 + "  " + img7 )
        input("\n\t press enter to continue... ")
    elif chd == 8:
        time.sleep(1)
        print("\n\t Enter the name or container ID which you want to start : ", end="")
        nid8 = input()
        os.system("docker start " + nid8)
        input("\n\t press enter to continue... ")
    elif chd == 9:
        time.sleep(1)
        print("\n\t Just give path of your Dockerfile (example: /root/myDocker/) : ", end="")
        path9 = input()
        print("\n\t What name you want to give to your new Container Image ? ", end="")
        name9 = input()
        os.system("docker build -t " + name9 + " " + path9)
        input("\n\t press enter to continue... ")
    elif chd == 10:
        os.system("tput sgr0")
        time.sleep(1)
        print("\n")
        break
    else:
        print("\n\t You have entered wrong choice bro, plz try again ..")
        time.sleep(1)
        input("\n\t press enter to continue... ")




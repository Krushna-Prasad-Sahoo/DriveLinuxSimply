
import os
import time
import pyfiglet as pf

result = pf.figlet_format("          DONE", font = "bubble" )

def menu4():
    os.system("clear")
    print("\n\t\t\t This Linux Files System based Section provides you the following options...\n")
    time.sleep(1)
    os.system("tput setf 5")
    print("\n \t\t 1. Check the file system disk space statistics")
    time.sleep(1)
    print("\t\t 2. Check the partition & other details of specific HD")
    time.sleep(1)
    print("\t\t 3. Get information about all available block devices")
    time.sleep(1)
    print("\t\t 4. Get UUID of all mounted partitions in this OS")
    time.sleep(1)
    print("\t\t 5. Format a disk partition ")
    time.sleep(1)
    print("\t\t 6. Mount file system to a drive/directory")
    time.sleep(1)
    print("\t\t 7. Perform a smooth Unmount operation")
    time.sleep(1)
    print("\t\t 8. Make your mount persistent at boot time (using fstab)")
    time.sleep(1)
    print("\t\t 9. Logical Volume Managemnt")
    time.sleep(1)
    print("\t\t 10. Exit from this SECTION\n")

def menu4_blank():
    os.system("clear")
    print("\n\t\t\t This Files & Directory Management Section provides you the following options...\n")
    os.system("tput setf 5")
    print("\n \t\t 1. Check the file system disk space statistics")
    print("\t\t 2. Check the partition & other details of specific HD")
    print("\t\t 3. Get information about all available block devices")
    print("\t\t 4. Get UUID of all mounted partitions in this OS")
    print("\t\t 5. Format a disk partition ")
    print("\t\t 6. Mount file system to a drive/directory")
    print("\t\t 7. Perform a smooth Unmount operation")
    print("\t\t 8. Make your mount persistent at boot time (using fstab)")
    print("\t\t 9. Logical Volume Managemnt")
    print("\t\t 10. Exit from this SECTION\n")
  


menu4()
while True:
    menu4_blank()
    os.system("tput setf 2")
    print("\t \t\t Enter your choice :", end=" ")
    ch4 = int(input())

    if ch4 == 1:
        time.sleep(1)
        os.system("df  -hT")
        input("\n\t press enter to continue... ")
    elif ch4 == 2:
        time.sleep(1)
        print("\n\t Enter the Disk name (example: /dev/sda) : ", end="")
        disk2 = input()
        os.system("fdisk  -l  " + disk2)
        input("\n\t press enter to continue... ")
    elif ch4 == 3:
        time.sleep(1)
        os.system("lsblk")
        input("\n\t press enter to continue... ")
    elif ch4 == 4:
        time.sleep(1)
        os.system("blkid")
        input("\n\t press enter to continue... ")
    elif ch4 == 5:
        time.sleep(1)
        print("\n\t Enter the name of disk partition (example /dev/sda1): ", end="")
        part5 = input()
        print("\n\t Enter the File System type for formatting (example: ext4): ", end="")
        fs5 = input()
        os.system("sudo mkfs -t " + fs5 + "  " + part5)
        time.sleep(1)
        print(result)
        input("\n\t press enter to continue... ")
    elif ch4 == 6:
        time.sleep(1)
        print("\n\t Enter the file system name (example: /dev/sda1) : ", end="")
        fs6 = input()
        print("\n\t Enter the mount point or drive name :", end=" ")
        mp6 = input()
        os.system("sudo mount " + fs6 + " " + mp6)
        time.sleep(1)
        print(result)
        input("\n\t press enter to continue... ")
    elif ch4 == 7:
        time.sleep(1)
        print("\n\t Enter the directory or mount point name : ", end="")
        mp7 = input()
        os.system("sudo umount -l  " + mp7)
        time.sleep(1)
        print(result)
        input("\n\t press enter to continue... ")
    elif ch4 == 8:
        time.sleep(1)
        print("\n\t Enter the disk partition name : ", end="")
        dp8 = input()
        print("\n\t Enter the mount point : ", end="")
        mp8 = input()
        print("\n\t Enter the format type (example: ext4) :", end=" ")
        ft8 = input()
        print("\n\t Enter the options for modes (example: defaults) :", end=" ")
        mode8 = input()
        cmd = dp8 + "   " + mp8 + "     " + ft8 + "     " + mode8 + "   0   0   "
        os.system("echo  " + cmd  + " >> /etc/fstab ")
        time.sleep(1)
        print(result)
        input("\n\t press enter to continue... ")
    elif ch4 == 9:
        time.sleep(1)
        print("\n\t Enter your first HD name : ", end=" ")
        fhd9 = input()
        print("\n\t Enter your second HD name : ", end=" ")
        shd9 = input()
        print("\n\t Enter the volume group name you want : ", end=" ")
        vg9 = input()
        print("\n\t Enter the logical volume name you want : ", end=" ")
        lv9 = input()
        print("\n\t Enter the size of the logical volume you want (example: 15G): ", end=" ")
        size9 = input()
        print("\n\t Enter your mount point name : ", end=" ")
        mp9 = input()

        time.sleep(1)
        print("\n\t .. your LV is on th way ...\n")
        os.system("pvcreate  " + fhd9)
        os.system("pvcreate  " + shd9)
        os.system("vgcreate  " + vg9 + "  " + fhd9 + "  " + shd9)
        os.system("lvcreate  --size  " + size9 + "  --name  " + lv9 + "  " + vg9)
        os.system("mkfs.ext4  /dev/" + vg9 + "/" +lv9)
        os.system("mount  /dev/" + vg9 + "/" +lv9 + "  " + mp9)
        os.system("lvdisplay   " + vg9 + "/" +lv9)
        time.sleep(1)
        print(result)
        input("\n\t press enter to continue... ")
    elif ch4 == 10:
        os.system("tput sgr0")
        time.sleep(1)
        print("\n")
        break
    else :
        print("\n\t You have entered wrong choice bro, plz try again...")
        time.sleep()
        input("\n\t press enter to continue... ")




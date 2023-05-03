import subprocess, json

out = subprocess.getoutput("PowerShell -Command \"& {Get-PnpDevice | Select-Object Status,Class,FriendlyName,InstanceId | ConvertTo-Json}\"")
j = json.loads(out)
for dev in j:
    print(dev['Status'], dev['Class'], dev['FriendlyName'], dev['InstanceId'] )


'''import os
import win32api
import win32file
os.system("cls")
drive_types = {
                win32file.DRIVE_UNKNOWN : "Unknown\nDrive type can't be determined.",
                win32file.DRIVE_REMOVABLE : "Removable\nDrive has removable media. This includes all floppy drives and many other varieties of storage devices.",
                win32file.DRIVE_FIXED : "Fixed\nDrive has fixed (nonremovable) media. This includes all hard drives, including hard drives that are removable.",
                win32file.DRIVE_REMOTE : "Remote\nNetwork drives. This includes drives shared anywhere on a network.",
                win32file.DRIVE_CDROM : "CDROM\nDrive is a CD-ROM. No distinction is made between read-only and read/write CD-ROM drives.",
                win32file.DRIVE_RAMDISK : "RAMDisk\nDrive is a block of random access memory (RAM) on the local computer that behaves like a disk drive.",
                win32file.DRIVE_NO_ROOT_DIR : "The root directory does not exist."
              }

drives = win32api.GetLogicalDriveStrings().split('\x00')[:-1]

for device in drives:
    type = win32file.GetDriveType(device)
    
    print("Drive: %s" % device)
    print(drive_types[type])
    print("-"*72)

os.system('pause')
'''



'''import os
import wmi
c = wmi.WMI()

for item in c.Win32_PhysicalMedia():
    print(item)

for drive in c.Win32_DiskDrive():
    print(drive)

for disk in c.Win32_LogicalDisk():
    print(disk)

os.system('pause')'''
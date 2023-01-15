import os 
# detect USB storage function on linux

def detect_usb_storage():
    devices=[]
    for device in os.listdir("/sys/block"):
        if device.startswith("sd"):
            device_path=os.path.join("/sys/block",device)
            with open(os.path.join(device_path,"removable"),'r') as f:
                 if f.read().strip()=="1":
                    devices.append(device)
    return devices

print (detect_usb_storage)


#Function to detect and block USB devices on windows


'''
The function used the win32api module to get a list of 
all the logical drives on the computer. It then iterates through
the list and checks if the drive letter is 'F', which is typically 
assigned to USB drives.If the drive is a USB drive, the function uses
the win32api.SetVolumeMountPoint method to block the drive. If the 
drive is not a USB drive the function allows it.

****Note***WORK IN PROGRESSS***
There are some issues with this code.
 if you only have drive C so far and you plug a USB drive in.
The Drive will get the letter 'D'.
Therefore it will print  
C:\is not a USB drive.. Allowing...
D:\is not a USB drive.. Allowing...
'''

import win32api

def detect_and_block_usb_devices():
    drives=win32api.GetLogicalDriveStrings()
    drives=drives.split('\000')[:-1]
    for drive in drives:
        if drive[0]=='F':
            print(drive + "is a USB drive. Blocking...")
            win32api.SetVolumeMountPoint(None,drive,0x00001000)
        else: print(drive+ "is not a USB drive.. Allowing...")

detect_and_block_usb_devices()







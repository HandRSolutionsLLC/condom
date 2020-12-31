from subprocess import getoutput as cmd
from os import system as cmd_
from time import sleep
import platform as pl
import threading



# NOTICE OF FALSE POSITIVE
# External Hard Disks are also recognised as Local Fixed Disk.
# I suggest the software logs the serial numbers of the current disks(if more than one) and
# their total number. If the number of disks detected exceed the total number we automatically
# know it's foreign even if it is an external HDD and it reads as "Local Fixed Disk"   



class Timer(threading.Thread):
	def __init__(_,time):
		threading.Thread.__init__(_)
		_.secs=time

	def run(_):
		time = _.secs 
		while _.secs != 0: 
			sleep(1)
			_.secs -= 1
		else: 
			print("Time UP! Foreign drive has been successfully ejected!")

class CMD:
	def __init__(_):
		_.getID = "wmic diskdrive get pnpdeviceid"
	 


def DeviceIsCompatible():
	'''This ensures the OS is Windows 10 or Linux'''
	return True if (pl.system() == "Windows" and pl.release() == "10") or pl.system() == "Linux" else False 


def driveDetected():
	#The first output is a header so we skip it
	#If more than one drive is detected it returns true
	if pl.system() == "Windows": numOfDrives=len(cmd(shell.getID).split()[1:])
	elif pl.system() == "Linux": numOfDrives=len(cmd('lsblk -S').split('\n')[1:])
	return numOfDrives > 1 

def ejectForeignDrive():
	print('Ejecting......')

	print('Ejecting Complete!')





if not DeviceIsCompatible(): print("Sorry! Your device is not compatible with this software.\nYou need a Windows 10 or Linux machine, Thank You."),exit()

shell = CMD()


while True:
	sleep(1)
	if driveDetected():
		clock = Timer(10)
		clock.start()
		while clock.secs > 0: sleep(1),print(f"Drive Detected! Enter password else drive will eject in {clock.secs} seconds: ")
		else: ejectForeignDrive()

	else: print('No drive detected!')

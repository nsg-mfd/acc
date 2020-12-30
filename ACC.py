# ACC.py for creating accounts in BA. instanceForIOWhenConnectNil when no available online data is available
# by NSG and OBjisGay 19/04/2020

# Jump to line for function
# L  |   FuncName   |  l
# -----------------------
# 34   createFile()  16  l
# 52   load()        12  l
# 68   load2()		 12  l
# 82   main()		 103 l
# 188  signIn()		 61  l
# 252  signUp()		 266 l

# libraries #
import json
import time
import os
import colorama
from colorama import Fore,Back,Style
import random
from random import randrange
############

# Init colorama #
colorama.init()
#################

# Custom functions #
clear = lambda: os.system('cls')
lo = lambda: os.system('python ACC.py')
####################

# Globals #
p = ["f","g"]
iD = 0
###########

#If it's first time, you deleted file or file is corrupt
def createFile():
	# iD = randrange(0,1000000)
	default = {"Name":0,"userName":0,"Email":0,"Password":0,"iD":iD,"settingsProtectCode":0,"settingsProtected":False,"isIn":False,"hexOfIdOf4":hex(iD)}
	print(Fore.CYAN,type(default))
	with open("account.json","w") as f:
		print(Fore.WHITE+"Creating", Fore.RED + "account.json\n",Fore.CYAN,type(f))
		f.write(json.dumps(default,indent = 2))
		f.close()
	#create backup if main is possibly corrupt
	with open("account_backup.json","w") as f:
		print(Fore.WHITE+"Creating", Fore.RED + "account_backup.json\n",Fore.CYAN,type(f))
		f.write(json.dumps(default,indent = 2))
		print(Fore.GREEN + "Finished, continuing to signin/signup page\n\n\n"+Fore.WHITE)
		f.close()
		print(json.dumps(default,indent = 2))
		lo()

#When logging out
def load():
	for i in range(2):
		clear()
		print("Logging out.")
		time.sleep(0.5)
		clear()
		print("Logging out..")
		time.sleep(0.5)
		clear()
		print("Logging out...")
		time.sleep(0.5)
		clear()

#When logging in
def load2():
	for i in range(2):
		clear()
		print("Logging in.")
		time.sleep(0.5)
		clear()
		print("Logging in..")
		time.sleep(0.5)
		clear()
		print("Logging in...")
		time.sleep(0.5)
		clear()

#Main interface
def Main():
	try:
		with open("account.json") as file:
			data = json.load(file)
			if data["isIn"] == False:
				ipu = input("Would you like to 1) sign in or 2) sign up\n")
				if ipu == "1":
					signIn()
					file.close()
				elif ipu == "2":
					signUp()
					file.close()
				elif ipu == "3":
					file.close()
					os.system("python del.py")
			else:
				print("Welcome " + data["Name"] + " (" + data["userName"] + ") To battle arenas offline (Or corrupt! ;))\nPlease select one of the options from below:")
				ins = input("1.Change Name\n2.Change Password\n3.Logout\nInt: ")
				if ins == "1":
					ins1 = input("Enter a new name! ")
					with open("account.json","r") as f:
						data = json.load(f)
						f.close()
						data["Name"] = ins1
						with open("account.json","w+") as fa:
							fa.write(json.dumps(data,indent = 2))
							fa.close()
					with open("account_backup.json","r") as f:
						data = json.load(f)
						f.close()
						data["Name"] = ins1
						with open("account_backup.json","w+") as fa:
							fa.write(json.dumps(data,indent = 2))
							fa.close()
							clear()
							lo()
				elif ins == "2":
					passwconf = input("Enter your password: ")
					with open("account_backup.json","r") as f:
						data = json.load(f)
						f.close()
						if passwconf == data["Password"]:
							print(Fore.GREEN+"Correct password, continuing."+Fore.WHITE)
							time.sleep(1)
						else:
							print(Fore.RED+"Incorrect password"+Fore.WHITE)
							time.sleep(1)
							Main()
					passw = input("Enter a new password 8 or more characters in length: ")
					if len(passw) < len("password"):
						print("Please choose a longer Password")
						time.sleep(2)
						Main()
					else:
						print("Password:" + passw)
						with open("account.json","r") as f:
							data = json.load(f)
							f.close()
							data["Password"] = passw
							with open("account.json","w+") as fa:
								fa.write(json.dumps(data,indent = 2))
								fa.close()
						with open("account_backup.json","r") as f:
							data = json.load(f)
							f.close()
							data["Password"] = passw
							with open("account_backup.json","w+") as fa:
								fa.write(json.dumps(data,indent = 2))
								fa.close()
								clear()
								lo()
				elif ins == "3":
					default = {"Name":0,"userName":0,"Email":0,"Password":0,"iD":iD,"settingsProtectCode":0,"settingsProtected":False,"isIn":False,"hexOfIdOf4":hex(iD)}
					with open("account.json","w") as f:
						f.write(json.dumps(default,indent = 2))
					with open("account_backup.json","r") as fl:
						data = json.load(fl)
						fl.close()
						data["isIn"] = False
						with open("account_backup.json","w+") as fla:
							fla.write(json.dumps(data,indent = 2))
							fla.close()
							load()
							print(Fore.GREEN+"Successfuly logged out!"+Fore.WHITE)
							lo()
				elif ins == "4":
					default = {"Name":0,"userName":0,"Email":0,"Password":0,"iD":iD,"settingsProtectCode":0,"settingsProtected":False,"isIn":False,"hexOfIdOf4":hex(iD)}
					with open("account.json","w") as f:
						f.write(json.dumps(default,indent = 2))
					with open("account_backup.json","r") as fl:
						data = json.load(fl)
						fl.close()
						data["isIn"] = False
						with open("account_backup.json","w+") as fla:
							fla.write(json.dumps(data,indent = 2))
							fla.close()
							print(Fore.GREEN+"Successfuly logged out!"+Fore.WHITE)
							lo()
	except IOError:
		print("Unexpected error, file", Fore.RED + "account.json, account_backup.json", Fore.WHITE + "does not exist in the current context\n")
		print("Creating new file...")
		time.sleep(3)
		createFile()

# SignIn
def signIn():
	######################################################################
	# UserNameIn input chunk
	unamein = input("Enter your account User Name or E-Mail: ")
	with open("account_backup.json","r") as f:
		data = json.load(f)
		f.close()
		if unamein == data["userName"] or data["Email"]:
			print(Fore.GREEN + unamein + " exists in current context"+Fore.WHITE)
		else:
			# This will run if any val is an int or null or you put wrong data in
			print(Fore.RED+"No account exists with the name/email "+unamein+" in the current context"+Fore.WHITE)
			time.sleep(1)
			signIn()

	######################################################################
	# PasswordIn input chunk
	passwin = input("Enter password for account "+unamein+": ")
	with open("account_backup.json","r") as f:
		data = json.load(f)
		f.close()
		if passwin == data["Password"]:
			print(Fore.GREEN+"Correct password"+Fore.WHITE)
			time.sleep(1)
		else:
			print(Fore.RED+"Incorrect password for "+unamein+Fore.WHITE)
			time.sleep(1)
			signIn()

	######################################################################
	# DataChangInFieldOrNot chunk
	with open("account_backup.json") as f:
		data = json.load(f)
		data["isIn"] = True
		with open ("account_backup.json","w+") as f2:
			f2.write(json.dumps(data,indent = 2))

	######################################################################
	# DataChangInFieldOrNot chunk
	with open("account_backup.json") as f:
		data = json.load(f)
		if data["settingsProtected"] == True:
			go = input("Enter your settingsProtectCode: ")
			if go == data["settingsProtectCode"]:
				######################################################################
				# DataChangInFieldOrNot2 chunk
				with open("account_backup.json") as f:
					with open("account.json","w") as f1:
						for line in f:
							f1.write(line)
				load2()
				lo()
			else:
				exit("wrong settingsProtectCode")
		else:
			with open("account_backup.json") as f:
					with open("account.json","w") as f1:
						for line in f:
							f1.write(line)
			load2()
			lo()
	


# SignUp
def signUp():
	######################################################################
	# FullName input chunk
	fName=input("Enter your Full name: ")
	if fName in p:
		clear()
		print("How the hell is your name that short?")
		time.sleep(3)
		signUp()
	else:
		with open("account.json","r") as f:
			data = json.load(f)
			f.close()
			data["Name"] = fName
			with open("account.json","w+") as fa:
				fa.write(json.dumps(data,indent = 2))
				fa.close()
		with open("account_backup.json","r") as f:
			data = json.load(f)
			f.close()
			data["Name"] = fName
			with open("account_backup.json","w+") as fa:
				fa.write(json.dumps(data,indent = 2))
				fa.close()

	######################################################################
	# Username input chunk
	uname = input("Enter a UserName with 3 or more characters: ")
	if len(uname) < len("eee"):
		print("Enter a userName with more than 3 or more characters!")
		time.sleep(2)
		signUp()
	else:
		print("Name is long enough")
		with open("account.json","r") as f:
			data = json.load(f)
			f.close()
			data["userName"] = uname
			with open("account.json","w+") as fa:
				fa.write(json.dumps(data,indent = 2))
				fa.close()
		with open("account_backup.json","r") as f:
			data = json.load(f)
			f.close()
			data["userName"] = uname
			with open("account_backup.json","w+") as fa:
				fa.write(json.dumps(data,indent = 2))
				fa.close()

	######################################################################
	# Email input chunk
	emailio = input("Enter a Email: ")
	# EmailData postfix = @gmail.com
	if "@gmail.com" in emailio:
		print(emailio, " is allowed!")
		# Make EMail = emailio
		with open("account.json","r") as f:
			data = json.load(f)
			f.close()
			data["Email"] = emailio
			# apply data to account.json
			with open("account.json","w+") as fa:
				fa.write(json.dumps(data,indent = 2))
				fa.close()
		# Make EMail = emailio
		with open("account_backup.json","r") as f:
			data = json.load(f)
			f.close()
			data["Email"] = emailio
			# apply data to account_backup.json
			with open("account_backup.json","w+") as fa:
				fa.write(json.dumps(data,indent = 2))
				fa.close()
	# EmailData postfix = @outlook.com
	elif "@outlook" in emailio:
		print(emailio, " is allowed!")
		# Make EMail = emailio
		with open("account.json","r") as f:
			data = json.load(f)
			f.close()
			data["Email"] = emailio
			# apply data to account.json
			with open("account.json","w+") as fa:
				fa.write(json.dumps(data,indent = 2))
				fa.close()
		# Make EMail = emailio
		with open("account_backup.json","r") as f:
			data = json.load(f)
			f.close()
			data["Email"] = emailio
			# apply data to account_backup.json
			with open("account_backup.json","w+") as fa:
				fa.write(json.dumps(data,indent = 2))
				fa.close()
	else:
		print(emailio, " does not fit our class of \"Email\"")
		signUp()
	

	######################################################################
	# Password input chunk
	passw = input("Enter a password 8 or more characters in length: ")
	if len(passw) < len("password"):
		print("Please choose a longer Password")
		time.sleep(2)
		signUp()
	else:
		# Make password = passw
		with open("account.json","r") as f:
			data = json.load(f)
			f.close()
			data["Password"] = passw
			# apply data to account.json
			with open("account.json","w+") as fa:
				fa.write(json.dumps(data,indent = 2))
				fa.close()
		# Make password = passw
		with open("account_backup.json","r") as f:
			data = json.load(f)
			f.close()
			data["Password"] = passw
			# apply data to account_backup.json
			with open("account_backup.json","w+") as fa:
				fa.write(json.dumps(data,indent = 2))
				fa.close()

	######################################################################
	# settingsProtected input chunk
	ans = input("Do you want to enable settingsProtected? y or n? ")
	if ans == "y":
		# make settingsProtected = True
		with open("account.json","r") as f:
			data = json.load(f)
			f.close()
			data["settingsProtected"] = True
			odj = randrange(1000,9999)
			odj_s = str(odj)
			data["settingsProtectCode"] = odj_s
			# apply data to account.json
			with open("account.json","w+") as fa:
				fa.write(json.dumps(data,indent = 2))
				fa.close()
		# make settingsProtected = True
		with open("account_backup.json","r") as f:
			data = json.load(f)
			f.close()
			data["settingsProtected"] = True
			#set this to this
			with open("account.json","r") as b:
				data1 = json.load(b)
				data["settingsProtectCode"] = data1["settingsProtectCode"]
				# apply data to account_backup.json
				with open("account_backup.json","w+") as fa:
					fa.write(json.dumps(data,indent = 2))
					fa.close()

	######################################################################
	# Make "isIn" = True 
	with open("account.json","r") as l:
		data = json.load(l)
		l.close()
		data["isIn"] = True
		# apply data to account.json
		with open("account.json","w+") as la:
			la.write(json.dumps(data,indent = 2))
			la.close()

	######################################################################
	# Make "isIn" = True 
	with open("account_backup.json","r") as l:
		data = json.load(l)
		l.close()
		data["isIn"] = True
		# apply data to account_backup.json
		with open("account_backup.json","w+") as la:
			la.write(json.dumps(data,indent = 2))
			la.close()

	######################################################################
	# Make "id" = ranInt 
	with open("account.json","r") as l:
		data = json.load(l)
		l.close()
		data["iD"] = randrange(1, 10000000)
		# apply data to account.json
		with open("account.json","w+") as la:
			la.write(json.dumps(data,indent = 2))
			la.close()

	######################################################################
	# Make "id" = ranInt 
	with open("account_backup.json","r") as l:
		data = json.load(l)
		l.close()
		# Set this to this
		with open("account.json","r") as b:
			data1 = json.load(b)
			data["iD"] = data1["iD"] 
			# apply data to account_backup.json
			with open("account_backup.json","w+") as la:
				la.write(json.dumps(data,indent = 2))
				la.close()

	######################################################################
	# Update hexOfIdOf4 
	with open("account.json","r") as l:
		data = json.load(l)
		l.close()
		data["hexOfIdOf4"] = hex(data["iD"])
		# apply data to account.json
		with open("account.json","w+") as la:
			la.write(json.dumps(data,indent = 2))
			la.close()

	######################################################################
	# Update hexOfIdOf4 
	with open("account_backup.json","r") as l:
		data = json.load(l)
		l.close()
		data["hexOfIdOf4"] = hex(data["iD"])
		# apply data to account_backup.json
		with open("account_backup.json","w+") as la:
			la.write(json.dumps(data,indent = 2))
			la.close()
			clear()
			lo()
Main()
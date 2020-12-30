import os
import colorama
from colorama import Fore,Back,Style
colorama.init()
try:
	os.remove("account.json")
	print(Fore.RED+"account.json"+Fore.WHITE+" deleted.")
except IOError:
	print(Fore.GREEN+"account.json"+Fore.RED+" are index null, exiting code with [0]"+Fore.WHITE)
try:
	os.remove("account_backup.json")
	print(Fore.RED+"account_backup.json"+Fore.WHITE+" deleted.")
except IOError:
	print(Fore.GREEN+"account_backup.json"+Fore.RED+" are index null, exiting code with [0]"+Fore.WHITE)
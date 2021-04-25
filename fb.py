# Coded by R-A-N-A MZ
import os, re
from time import sleep
try:
	from bs4 import BeautifulSoup as ser
except ImportError:
	os.system("python3 -m pip install -q bs4")
	from bs4 import BeautifulSoup as ser
try:
	import requests as get
except ImportError:
	os.system("python3 -m pip install -q requests")
	import requests as get

class Nomor:
	def __init__(self):
		os.system('cls' if os.name == 'nt' else 'clear')
		logo()
		url = "https://www.temp-mails.com/lan/id/number"
		self.get_1(url)

	def get_1(self, url):
		ambil = ser(get.get(url).text, "html.parser")
		parser = ambil.find("div", id="content")
		fnomor = parser.find_all("div", class_="own-num")
		nom = [res.text for res in fnomor]
		print("="*31)
		for me in nom:
			num = me.replace("\n", "")
			print(f' \x1b[1;92m¹116 see q(\x1b[1;91m+\x1b[1;92m)\x1b[1;96m>> \x1b[1;97m{num}\t✓ \x1b[1;94mON\x1b[1;91m')
		print("="*31)
		print(" \x1b[1;96m USE THE NUMBER AVAILABLE")
		print(" \x1b[1;96m DO NOT FORGET TO CHECK THE SIGN IN CONTACTS")
		print("\x1b[1;91m="*31)
		print(" \x1b[1;92m(\x1b[1;96mA\x1b[1;92m) \x1b[1;97m CONTACT IN")
		print(" \x1b[1;92m(\x1b[1;96mB\x1b[1;92m) \x1b[1;97m ABOUT US")
		print(" \x1b[1;92m(\x1b[1;91mE\x1b[1;92m) \x1b[1;97m EXIT")
		print("\x1b[1;91m="*31)
		pil = input(" \x1b[1;96m SELECT : \x1b[1;92m")
		print("\x1b[1;91m="*31)
		if pil == "A" or pil == "a":
			self.pesan(url)
		elif pil == "B" or pil == "b":
			os.system('cls' if os.name == 'nt' else 'clear')
			logo()
			tentang()
		else:
			exit("\n \x1b[1;97m THANK YOU ..")

	def pesan(self, url):
		print("\n \x1b[1;96m WAITING FOR MESSAGE IN ...")
		while True:
			try:
				ambi = ser(get.get(url).content, "html.parser")
				tabl = ambi.find("div", id="tablenumber")
				tim = tabl.find("td", class_="sms-date").text
				fro = tabl.find("td", class_="sms-from").text
				to = tabl.find("td", class_="sms-to").text
				sear = tabl.find("button", attrs={"class":"btn btn-primary open-msg-btn"})
				pes = re.findall("data-text=\"(.*?)\"", str(sear))
				if str(tim) == "1 seconds ago ":
					print("\n\x1b[1;91m>>>>>>>>>\x1b[1;92m(\x1b[1;94m INCOMING MESSAGES\x1b[1;92m)\x1b[1;91m<<<<<<<<<\n")
					print(" \x1b[1;96mDATE  : \x1b[1;97m"+tim)
					print(" \x1b[1;96mFROM  : \x1b[1;97m"+fro)
					print(" \x1b[1;96mTO    : \x1b[1;97m+"+to)
					print(" \x1b[1;96m MESSAGE : \x1b[1;97m"+pes[0].replace("&amp;lt#&amp;gt",""))
					print("\n\x1b[1;91m>>>>>>>>>\x1b[1;92m(    \x1b[1;94mEND    \x1b[1;92m)\x1b[1;91m<<<<<<<<<\n")
					sleep(1)
					continue
				else:
					continue
			except IndexError:
				continue

def logo():
	print('''
\x1b[1;94m RANA MZ                            
\x1b[1;94m FOLOW ME ON FACEBOOK 
\x1b[1;94m SUBCRBE NY YOU TUBE CHNAL
\x1b[1;94mUSE FAST SPEED INTERNET
\x1b[1;94m DONT USE FOR ILLGEL
\x1b[1;94m IM THE ONE 
  \x1b[105m\x1b[37;1mCODED BY RANA MZ\x1b[0m''')

def tentang():
	print("\x1b[1;91m="*31)
	print('''\x1b[1;96m AUTHOR   : \x1b[1;97mRANA MZ
\x1b[1;96m GITHUB   : \x1b[1;97mhttps://github.com/RANAMZ-zeshi
\x1b[1;96m FACEBOOK : \x1b[1;97mhttps://www.facebook.com/RanaMZ.zeshi''')
	print("\x1b[1;91m="*31)
	input("\n\x1b[1;92m ENTER TO BACK ()> ")
	Nomor()

if __name__=="__main__":
	try:
		Nomor()
	except KeyboardInterrupt:
		print("\n \x1b[1;97m SHUKRAN ..")

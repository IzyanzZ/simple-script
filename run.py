import os,sys,time

x = 'S'
y = 'C'


def b():
  os.system("clear")
  
def login():
  usr = raw_input("\033[1;95mUsername $ \033[1;37m")
  passw = raw_input("\033[1;39mPassword $ \033[1;37m")
  if usr ==x and passw ==y:
    print("\033[1;31mAcces Granted!")
    time.sleep(2)
  else:
    print("\033[1;31mAcces Denied!")
    os.system("python2 run.py")
    time.sleep(2)
    
def menu():
  print("\033[1;33m     xxxxxxx    ")
  print("\033[1;33m   xxxxxxxxxxx  ")  
  print("\033[1;33m xxxxx    xxxxx ")
  print("\033[1;33mxxxx        xxxx")
  print("\033[1;33mxxx          xxx")
  print("\033[1;33mxxx          xxx")
  print("\033[1;33m xxxxx    xxxxx ")
  print("\033[1;33m  xxxxxxxxxxxx  ")

b()
login()
menu()

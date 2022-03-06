# ---------- Packages -----------


import os
import time


# --------- Functions -----------


# Main Function

def main():
    print("Enter 1 for USA")
    print("Enter 2 for Oceania")
    print("Enter 3 for Europe")
    print("Enter 4 for Russia")
    print("Enter 5 for Asia")
    print("Enter 6 for South America")
    print("Enter 7 for Middle East")
    n = input("Enter Server: ")

    if n=='1':
        usa()
    elif n=='2':
        oce()
    elif n=='3':
        eur()
    elif n=='4':
        rus()
    elif n=='5':
        asia()
    elif n=='6':
        sam()
    elif n=='7':
        me()
    else:
        print("Invalid choice")
        quit()
    

# USA

def usa():
    dump = [['Atlanta','185.93.0.83'],['Beauharnois','51.161.118.44'],['California','45.35.136.14'],['Chicago','108.62.107.8'],['Dallas','172.241.25.143'],['Denver','84.17.63.82'],['Miami','23.82.136.213'],['NewYork','89.187.178.79'],['Seattle','23.19.87.236'],['Washington DC','5.188.124.11']] 
    al = len(dump)
    for ip in range(al):
        os.system('cls')
        print('-'*60)
        print('Pinging now: ', dump[ip][0])
        print('-'*60)
        os.system('ping -n 3 {}'.format(dump[ip][1]))
        print('-'*60)
        time.sleep(5)


# Oceania

def oce():
    dump = [['Australia','103.101.129.122']] 
    al = len(dump)
    for ip in range(al):
        os.system('cls')
        print('-'*60)
        print('Pinging now: ', dump[ip][0])
        print('-'*60)
        os.system('ping -n 3 {}'.format(dump[ip][1]))
        print('-'*60)
        time.sleep(5)


# Europe

def eur():
    dump = [['Austria,185.180.12.85],[Bratislava','156.146.40.72'],['Bucharest','185.102.217.153'],['Czech','89.187.191.202'],['Europe','78.138.127.150'],['Finland','95.216.45.93'],['France','92.204.161.26'],['Germany','176.57.181.239'],['London','51.89.235.21'],['Netherlands','81.171.15.112']]
    al = len(dump)
    for ip in range(al):
        os.system('cls')
        print('-'*60)
        print('Pinging now: ', dump[ip][0])
        print('-'*60)
        os.system('ping -n 3 {}'.format(dump[ip][1]))
        print('-'*60)
        time.sleep(5)


# Russia

def rus():
    dump = [['Ekaterinburg','92.223.91.8'],['Kazakhstan','5.189.202.7'],['Khabarovsk','92.38.191.135'],['Krasnoyarsk','92.223.87.6'],['Moscow','176.99.3.55'],['Novosibirsk','5.8.42.6'],['Saint Petersburg','5.8.78.114']]
    al = len(dump)
    for ip in range(al):
        os.system('cls')
        print('-'*60)
        print('Pinging now: ', dump[ip][0])
        print('-'*60)
        os.system('ping -n 3 {}'.format(dump[ip][1]))
        print('-'*60)
        time.sleep(5)


# Asia

def asia():
    dump = [['Hong Kong','43.249.37.109'],['Japan','103.208.221.211'],['Seoul','92.38.165.133'],['Singapore','23.106.120.84'],['Taiwan','43.251.182.44'],['Tokyo','5.188.71.31']]
    al = len(dump)
    for ip in range(al):
        os.system('cls')
        print('-'*60)
        print('Pinging now: ', dump[ip][0])
        print('-'*60)
        os.system('ping -n 3 {}'.format(dump[ip][1]))
        print('-'*60)
        time.sleep(5)


# South America

def sam():
    dump = [['San Paulo','92.38.150.27']]
    al = len(dump)
    for ip in range(al):
        os.system('cls')
        print('-'*60)
        print('Pinging now: ', dump[ip][0])
        print('-'*60)
        os.system('ping -n 3 {}'.format(dump[ip][1]))
        print('-'*60)
        time.sleep(5)


# Middle East

def me():
    dump = [['Israel','5.188.95.8'],['Tel Aviv','5.188.95.64'],['Turkey','92.38.180.18']]
    al = len(dump)
    for ip in range(al):
        os.system('cls')
        print('-'*60)
        print('Pinging now: ', dump[ip][0])
        print('-'*60)
        os.system('ping -n 3 {}'.format(dump[ip][1]))
        print('-'*60)
        time.sleep(5)


# ------------ Start Execution -------------


main()
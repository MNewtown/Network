import pyautogui
import time

def main():
    option = input("(1) Switch ### (2) Access Port ### (3) Trunk Port:\n")
    if option == "1":
        time.sleep(1)
        switchsetup()
    if option == "2":
        accessPortSetup()
    if option == "3":
        time.sleep(1)
        trunkPortSetup()
def wr(word):
    pyautogui.write(word)
    pyautogui.press('enter')
    time.sleep(0.02)

def switchsetup():
    pyautogui.press('enter')
    wr("en")
    wr("conf t")
    wr('service password-encryption')
    wr('username admin secret cisco')
    wr('line con 0')
    wr('password cisco')
    wr('login')
    wr('exit')
    wr('line vty 0 15')
    wr('password cisco')
    wr('login')
    wr('exit')
    #wr('banner motd') # DO THIS THING
    wr('vlan 10')
    wr('in vlan 10')
    wr('vlan 20')
    wr('in vlan 20')
    wr('vlan 30')
    wr('in vlan 30')
    wr('exit')
    wr('lldp run')
    wr('spanning-tree mode rapid-pvst')
    wr('exit')
    wr('copy run start')
    pyautogui.press('enter')
    print("###\n###\nRemember to config SVIs!\n###\n###")

def accessPortSetup():
    option = input("Interface(s) <e.g. f0/1-f0/3>:\n")
    time.sleep(1)
    range = False
    for i in option:
        if i == "-" or ",":
            range = True
            break
    if range:
        wr(f'in range {option}')
    else:
        wr(f'in {option}')
    wr('switchport mode access')
    wr('spanning-tree portfast')
    wr('spanning-tree guard root')
    wr('exit')

def trunkPortSetup():
    pass

if __name__ == "__main__":
    main()
# !/usr/bin/python3

import re, sys, subprocess
from termcolor import colored

if len(sys.argv) != 2:
    print(colored("\n[!] Uso: python3 ScanOs.py <ip_addres> [!]", 'red'))
    sys.exit(0)

def is_valid_IP(str):
    return bool(re.match(r'^((0|[1-9][0-9]?|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(\.|$)){4}$', str))

def scan_ttl(ip_machine):
    
    print(colored("\n[*] Escaneando SO [*]", "blue"))
    try: 
        ping_proc = subprocess.Popen(["/usr/bin/ping -c 1 %s" % ip_machine, ""], stdout=subprocess.PIPE, shell=True)
        (out,err) = ping_proc.communicate()

        out = out.split()
        out = out[12].decode('utf-8')

        ttl = re.findall(r"\d{1,3}", out)[0]
        return ttl

    except: 
        print("\n[!] Algo salio mal :C")
    
def scanOs(ttl):

    ttl_os = int(ttl)

    print(f"\n[*] TTL: {ttl}")
    
    if ttl_os >= 0 and ttl_os <= 64:
        print("[*] OS: Linux\n")
    elif ttl_os >=65 and ttl_os <= 128:
        print("[*] OS: Windows\n")
    else:
        print("[!] OS: no identificado\n")

    print(colored("[*] Escaneo terminado :) [*]\n", 'yellow'))

if __name__ == "__main__":
    
    ip = sys.argv[1]
    try:
        if is_valid_IP(ip):
            ttl = scan_ttl(ip)
            scanOs(ttl)
        else:
            print(colored("[!] IP invalida [!]", 'red'))
            print(colored("\n[*] Ejemplo: IP: 10.10.10.70", 'yellow'))
    except:
        print(colored("[!] Algo salio mal :c [!]", 'red'))



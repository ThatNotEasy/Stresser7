def proxysocks():
    try:
        sock_api = [
            "https://api.proxyscrape.com/v2/?request=getproxies&protocol=socks5&timeout=10000&country=all&simplified=true",
            "https://www.proxy-list.download/api/v1/get?type=socks5",
            "https://www.proxyscan.io/download?type=socks5",
            "https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks5.txt",
            "https://raw.githubusercontent.com/hookzof/socks5_list/master/proxy.txt",
            "https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/socks5.txt",
            "https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks5.txt",
            "https://api.openproxylist.xyz/socks5.txt",
            "https://api.proxyscrape.com/v2/?request=getproxies&protocol=socks5",
            "https://openproxylist.xyz/socks5.txt",
            "https://proxyspace.pro/socks5.txt",
            "https://raw.githubusercontent.com/B4RC0DE-TM/proxy-list/main/SOCKS5.txt",
            "https://raw.githubusercontent.com/manuGMG/proxy-365/main/SOCKS5.txt",
            "https://raw.githubusercontent.com/mmpx12/proxy-list/master/socks5.txt",
            "https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS5_RAW.txt",
            "https://raw.githubusercontent.com/saschazesiger/Free-Proxies/master/proxies/socks5.txt",
            "https://api.proxyscrape.com/v2/?request=getproxies&protocol=socks4",
            "https://openproxylist.xyz/socks4.txt",
            "https://proxyspace.pro/socks4.txt",
            "https://raw.githubusercontent.com/B4RC0DE-TM/proxy-list/main/SOCKS4.txt",
            "https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks4.txt",
            "https://raw.githubusercontent.com/mmpx12/proxy-list/master/socks4.txt",
            "https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS4_RAW.txt",
            "https://raw.githubusercontent.com/saschazesiger/Free-Proxies/master/proxies/socks4.txt",
            "https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/socks4.txt",
            "https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks4.txt",
            "https://www.proxy-list.download/api/v1/get?type=socks4",
            "https://www.proxyscan.io/download?type=socks4",
            "https://api.proxyscrape.com/?request=displayproxies&proxytype=socks4&country=all",
            "https://api.openproxylist.xyz/socks4.txt",
        ]
        ips = []
        print(f"{Fore.GREEN}\n[w00t!] - Downloading proxies, this might take a while!")
        print(f"{Fore.GREEN}[w00t!] - This is SOCK4 & 5 Proxy. Use Mix Proxy for bigger proxy list.")
        for api in sock_api:
            try:
                r = requests.get(api, timeout=15)
                ips += re.findall(r"(?:\d{1,3}[\.:]){3}\d{1,3}:\d+", r.text)
            except:
                pass
        with open("proxy.txt", "w") as f:
            for ip in set(ips):
                f.write(ip + "\n")
        print(f"{Fore.GREEN}\n[w00t!] - Successful with no problemo!")
    except:
        print("\nERROR!\n")
    proxylist()

def proxysmall():
    try:
        http_api = [
            "https://api.proxyscrape.com/?request=displayproxies&proxytype=http",
            "https://www.proxy-list.download/api/v1/get?type=http",
            "https://www.proxyscan.io/download?type=http",
            "https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt",
            "https://api.openproxylist.xyz/http.txt",
        ]
        ips = []
        print(f"{Fore.GREEN}\n[w00t!] - Downloading proxies, please wait!")
        print(f"{Fore.GREEN}[w00t!] - Fast internet speed? Use bigger List Proxy.")
        for api in http_api:
            try:
                r = requests.get(api, timeout=15)
                ips += re.findall(r"(?:\d{1,3}[\.:]){3}\d{1,3}:\d+", r.text)
            except:
                pass
        with open("proxy.txt", "w") as f:
            for ip in set(ips):
                f.write(ip + "\n")
        print(f"{Fore.GREEN}[w00t!] - Successful with no problemo!")
    except:
        print("\nERROR!\n")
    proxylist()

def proxybig():
    try:
        http_api = [
            "https://api.proxyscrape.com/?request=displayproxies&proxytype=all",
            "https://www.proxy-list.download/api/v1/get?type=http",
            "https://www.proxyscan.io/download?type=http",
            "https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt",
            "https://api.openproxylist.xyz/http.txt",
            "https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/proxy.txt",
            "http://alexa.lr2b.com/proxylist.txt",
            "https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies.txt",
            "https://raw.githubusercontent.com/sunny9577/proxy-scraper/master/proxies.txt",
            "https://multiproxy.org/txt_all/proxy.txt",
            "https://raw.githubusercontent.com/roosterkid/openproxylist/main/HTTPS_RAW.txt",
            "https://raw.githubusercontent.com/UserR3X/proxy-list/main/online/http.txt",
            "https://raw.githubusercontent.com/UserR3X/proxy-list/main/online/https.txt",
            "https://openproxylist.xyz/http.txt",
            "https://proxyspace.pro/http.txt",
            "https://proxyspace.pro/https.txt",
            "https://raw.githubusercontent.com/aslisk/proxyhttps/main/https.txt",
            "https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data.txt",
            "https://raw.githubusercontent.com/mmpx12/proxy-list/master/http.txt",
            "https://raw.githubusercontent.com/mmpx12/proxy-list/master/https.txt",
            "https://raw.githubusercontent.com/proxy4parsing/proxy-list/main/http.txt",
            "https://raw.githubusercontent.com/saisuiu/uiu/main/free.txt",
            "https://raw.githubusercontent.com/saisuiu/uiu/main/cnfree.txt",
            "https://rootjazz.com/proxies/proxies.txt",
            "https://www.proxy-list.download/api/v1/get?type=https",
        ]
        ips = []
        print(f"{Fore.GREEN}\n- Downloading proxies, please wait!")
        print(f"{Fore.GREEN}- Huge proxy list, this might take a while.")
        for api in http_api:
            try:
                r = requests.get(api, timeout=15)
                ips += re.findall(r"(?:\d{1,3}[\.:]){3}\d{1,3}:\d+", r.text)
            except:
                pass
        with open("proxy.txt", "w") as f:
            for ip in set(ips):
                f.write(ip + "\n")
        print(f"{Fore.GREEN}\n[w00t!] - Successful with no problemo!")
    except:
        print("\nERROR!\n")
    proxylist()

def proxylist():
    global proxies
    print(f"{Fore.CYAN}\nPress enter to save filename! {Fore.RED}")
    out_file = str(input(f"{Fore.YELLOW}#OpsPetir@CyberTroopers:- {Fore.RED}"))
    if out_file == "":
        out_file = "proxy.txt"
    proxies = open(out_file).readlines()
    numthreads()

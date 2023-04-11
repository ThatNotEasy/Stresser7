import requests

options = {
    1: {"country": "all", "timeout": "750"},
    2: {"country": "US", "timeout": "750"},
    3: {"country": "RU", "timeout": "1000"},
    4: {"country": "UA", "timeout": "1000"},
    5: {"country": "IN", "timeout": "1000"},
    6: {"country": "IT", "timeout": "1000"},
    7: {"country": "CA", "timeout": "1000"},
    8: {"country": "FR", "timeout": "1000"},
    9: {"country": "TH", "timeout": "1000"},
    10: {"country": "PL", "timeout": "1000"},
    11: {"country": "NL", "timeout": "2100"},
    12: {"country": "MX", "timeout": "1500"},
    13: {"country": "KZ", "timeout": "1500"},
    14: {"country": "IR", "timeout": "1500"},
    15: {"country": "EG", "timeout": "1500"},
    16: {"country": "HK", "timeout": "2250"},
    17: {"country": "DE", "timeout": "1500"},
    18: {"country": "VN", "timeout": "1500"},
    19: {"country": "HU", "timeout": "1500"},
    20: {"country": "BR", "timeout": "1500"},
    21: {"country": "JP", "timeout": "1500"},
    22: {"country": "KH", "timeout": "1500"},
    23: {"country": "CN", "timeout": "1250"}
}

while True:
    country_code = input("Enter a country code (type 'all' for all countries): ")
    if country_code == "all" or country_code.upper() in options.values():
        break
    print("Invalid country code, please try again.")

while True:
    try:
        op = int(input("Enter an option: "))
        if op in options:
            break
        print("Invalid option, please try again.")
    except ValueError:
        print("Invalid input, please try again.")

url = f"https://api.proxyscrape.com/v2/?request=displayproxies&protocol=all&timeout={options[op]['timeout']}&country={options[op]['country']}"
proxies = requests.get(url).text

with open("proxy.txt", "w") as f:
    f.write(proxies)

print("Proxies saved to 'proxy.txt'.")
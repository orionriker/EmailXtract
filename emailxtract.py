import re
import requests
import time
import random
from datetime import datetime
from bs4 import BeautifulSoup

# Text styling
class textstylez:
    reset="\x1B[0m"
    dim="\x1B[2m"
    blink="\x1B[5m"
    negative="\x1B[7m"
    bigunderline="\x1B[21m"
    overline="\x1B[53m"
    bold="\x1B[1m"
    italic="\x1B[3m"
    underline="\x1B[4m"
    strike="\x1B[9m"
    fg_black="\x1B[30m"
    fg_red="\x1B[31m"
    fg_green="\x1B[32m"
    fg_yellow="\x1B[33m"
    fg_blue="\x1B[34m"
    fg_magenta="\x1B[35m"
    fg_cyan="\x1B[36m"
    fg_white="\x1B[37m"
    fg_stblack="\x1B[90m"
    fg_stred="\x1B[91m"
    fg_stgreen="\x1B[92m"
    fg_styellow="\x1B[93m"
    fg_stblue="\x1B[94m"
    fg_stmagenta="\x1B[95m"
    fg_stcyan="\x1B[96m"
    fg_stwhite="\x1B[97m"
    bg_black="\x1B[40m"
    bg_red="\x1B[41m"
    bg_green="\x1B[42m"
    bg_yellow="\x1B[43m"
    bg_blue="\x1B[44m"
    bg_magenta="\x1B[45m"
    bg_cyan="\x1B[46m"
    bg_white="\x1B[47m"
    bg_stblack="\x1B[100m"
    bg_stred="\x1B[101m"
    bg_stgreen="\x1B[102m"
    bg_styellow="\x1B[103m"
    bg_stblue="\x1B[104m"
    bg_stmagenta="\x1B[105m"
    bg_stcyan="\x1B[106m"
    bg_stwhite="\x1B[107m"

# Argument parser
class ArgumentParser:
    def __init__(self):
        self.args = {}
        self.parse_args()

    def parse_args(self):
        import sys
        args = sys.argv[1:]
        i = 0
        while i < len(args):
            arg = args[i]
            if arg.startswith('--'):
                key = arg[2:]
                value = True
                if i + 1 < len(args) and not args[i + 1].startswith('--'):
                    value = args[i + 1]
                    if ',' in value:
                        value = value.split(',')
                        value = [re.sub(r"['\"]", "", val) for val in value]
                    i += 1
                self.args[key] = value
            i += 1

    def get(self, key, default=None):
        return self.args.get(key, default)

# CloudFlare email protection decoder
def cfDecodeEmail(encodedString):
    r = int(encodedString[:2], 16)
    email = ''.join([chr(int(encodedString[i:i+2], 16) ^ r) for i in range(2, len(encodedString), 2)])
    return email

# Format time
def format_time(seconds):
    if seconds < 60:
        return f"{seconds:.2f}s"
    elif seconds < 3600:
        minutes = seconds / 60
        return f"{minutes:.2f}mins"
    elif seconds < 86400:
        hours = seconds / 3600
        return f"{hours:.2f}hrs"
    else:
        days = seconds / 86400
        return f"{days:.2f}days"


print(f"{textstylez.fg_blue}{textstylez.bold} ______                 _ ___   ___                  _   ")
print("|  ____|               (_) \ \ / / |                | |  ")
print("| |__   _ __ ___   __ _ _| |\ V /| |_ _ __ __ _  ___| |_ ")
print("|  __| | '_ ` _ \ / _` | | | > < | __| '__/ _` |/ __| __|")
print("| |____| | | | | | (_| | | |/ . \| |_| | | (_| | (__| |_ ")
print("|______|_| |_| |_|\__,_|_|_/_/ \_\\\__|_|  \__,_|\___|\__|")
print("")

print("EmailXtract Email Scraper 1.0.0")
print(f"Copyright (c) 2023 gamemaster123356, All rights reserved.{textstylez.reset}")
print("")

print(f"{textstylez.fg_styellow}{textstylez.blink}[!] Legal Disclaimer: EmailXtract is intended for ethical security research and vulnerability assessment purposes only.")
print(f"Using EmailXtract to attack targets without explicit mutual consent is illegal and strictly prohibited. End users are solely responsible for complying with all relevant laws and regulations. The developer(s) assume no liability for misuse or damage caused by EmailXtract. Use responsibly and lawfully.{textstylez.reset}")
print("")

argparser = ArgumentParser()

# Parse Arguments
proxies = None
if argparser.get('proxies'):

    proxies_list = argparser.get('proxies')
    if isinstance(proxies_list, str):
        proxies_list = [proxies_list]

    proxies = {}
    for proxy in proxies_list:
        proxy = re.sub("[$@&']","",proxy)
        proxy_parts = proxy.split(':')
        proxy_type = proxy_parts[0]
        proxy_address = ':'.join(proxy_parts[1:])
        proxy = re.sub(r'^https?://', '', proxy)
        proxies[proxy_type] = proxy
        if proxy_type == 'http':
            proxies['https'] = proxy

if proxies:
    print(f"[*] Using proxies. Please beware that proxies may slow down scraping speeds.")
    print("")

emailxtract_tips = [
    "Use the --proxies parameter to scrape with proxies for enhanced privacy and anonymity.",
    "Consider allowing redirects for a more comprehensive scraping experience.",
    "Remember to include the URL scheme (http:// or https://) in the URL input.",
    "Be cautious when using proxies, as they might slow down scraping speeds.",
    "Fun Fact: EmailXtract can bypass CloudFlare's email protection.",
    "When scraping, always respect website terms of use and be aware of any scraping restrictions.",
    "Regularly check for updates to ensure you're using the latest version of EmailXtract.",
]
random_tip = random.choice(emailxtract_tips)
print(f"[*] Tip: {random_tip}")
print("")

while True:
    # Get user input for url
    print("Enter the URL to scrape emails from or type exit() to exit")
    print("the URL MUST start with the scheme (http:// or https://)")
    prompt = ''
    while prompt == '':
        prompt = input(f">> ")

    # Check if the prompt is exit() and then break the loop
    if prompt == 'exit()':
        break

    # Check if the prompt has a URL scheme (http:// or https://)
    if not re.match(r'^https?://', prompt):
        print("")
        print(f"{textstylez.fg_stred}Error: Please include the URL scheme (http:// or https://){textstylez.reset}")
        print("")
        continue
    else:
        url = prompt

    # Get user input for allowing redirects
    print("")
    prompt = input(f"Allow redirects? (Y/n): ")
    print("")

    if prompt == 'exit()':
        break

    allow_redirects = False if (prompt.lower() in ["n", "no"]) else True

    # Scrape emails
    current_datetime = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
    print(f"{textstylez.fg_styellow}[*] [{textstylez.fg_stblue}{current_datetime}{textstylez.fg_styellow}] Scraping Emails...{textstylez.reset}")

    # Make a request to the URL
    elapsed_time = time.time()
    try:
        response = requests.get(url, allow_redirects=allow_redirects, proxies=proxies)
    except requests.exceptions.RequestException as e:
        print(f"{textstylez.fg_stred}Error: Unable to retrieve content from {url}: {e}{textstylez.reset}")
        print("")
        continue

    content = response.text

    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(content, 'html.parser')

    email_pattern  = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
    email_elements = ['p', 'div', 'b', 'i', 'li', 'a', 'span', 'script']

    all_emails = set()
    for element in email_elements:
        for tag in soup.find_all(element):
            text = tag.get_text()
            emails = re.findall(email_pattern, text)

            # Bypass CloudFlare email protection
            if tag.has_attr('data-cfemail'):
                encoded_email = tag['data-cfemail']
                decoded_email = cfDecodeEmail(encoded_email)
                emails.append(decoded_email)

            all_emails.update(emails)

    elapsed_time = format_time(time.time() - elapsed_time)

    # Print the scraped emails and save to file if found. Else throw error
    if not all_emails:
        print(f"{textstylez.fg_stred}Error: No emails to retrieve from {url}{textstylez.reset}")
        print("")
        continue
    else:
        print(f"Done in {elapsed_time}")
        print("")

        with open("scraped_emails.txt", "w") as f:
            for email in all_emails:
                f.write(email + "\n")
            current_datetime = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
            print(f"{textstylez.fg_styellow}[*] [{textstylez.fg_stblue}{current_datetime}{textstylez.fg_styellow}] Scraped emails saved to 'scraped_emails.txt'{textstylez.reset}")

        current_datetime = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
        print(f"{textstylez.fg_styellow}[*] [{textstylez.fg_stblue}{current_datetime}{textstylez.fg_styellow}] Scraped emails:{textstylez.reset}")
        for email in all_emails:
            print(email)

    break

exit()
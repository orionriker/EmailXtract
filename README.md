# EmaiXtract
This Python script is designed for fast, efficient email scraping from websites. It offers a range of features, including proxy support for enhanced privacy, a CloudFlare email protection bypass function, and the ability to scrape email addresses from web content. Scraped emails will be stored in a "scraped_emails.txt" file and displayed on the console. Additionally, users have the option to enable or disable redirects when making requests to the specified URL.

**[!] Legal Disclaimer: EmailXtract is intended for ethical security research and vulnerability assessment purposes only.
Using EmailXtract to attack targets without explicit mutual consent is illegal and strictly prohibited. End users are solely responsible for complying with all relevant laws and regulations. The developer(s) assume no liability for misuse or damage caused by EmailXtract. Use responsibly and lawfully.**

<br>
## ⭐ Features
- **Proxy Support**: The script supports the use of proxies for enhanced privacy and anonymity during scraping. Proxies can be specified through the --proxies parameter.

- **CloudFlare Email Protection Bypass**: The script includes a function, cfDecodeEmail, which decodes email addresses protected using CloudFlare's email obfuscation techniques.

- **Email Scraping**: The script uses the requests library to fetch the content from the specified URL. It then uses the BeautifulSoup library to parse the HTML content and extract email addresses.

- **Scraped Email Storage**: The script saves the scraped email addresses to a file named "scraped_emails.txt" and displays the scraped emails on the console.

- **Enable/Disable Redirects**: The script allows users to choose whether to enable or disable redirects when making requests to the specified URL.

<br>
## 📦 Dependencies
BS4 (Required):<br>
`pip install bs4`<br>

PySOCKS (Optional. Should be installed when using a SOCKS Proxy)<br>
`pip install pysocks`

<br>
## 🔧 Usage
**Normal usage:**<br>
`python emailxtract.py`

**With proxy usage:**<br>
`python emailxtract.py --proxies http://<proxy type>://<proxy address>:<proxy port>`<br>
example(s):<br>
`python emailxtract.py --proxies http://socks5://127.0.0.1:9050`

**With Multiple proxy usage:**<br>
`python emailxtract.py --proxies http://<proxy type>://<proxy address>:<proxy port>,http://<proxy type>://<proxy address>:<proxy port>`<br>
example(s):<br>
`python emailxtract.py --proxies http://socks5://127.0.0.1:9050,http://socks5://127.0.0.1:2020`

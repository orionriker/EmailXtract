c='data-cfemail'
b='exit()'
a='^https?://'
Z='proxies'
Y=input
R='%d-%m-%Y %H:%M:%S'
Q=True
P=len
C=''
A=print
import re as F,requests as S,time as T,random as d
from datetime import datetime as K
from bs4 import BeautifulSoup as e
class B:reset='\x1b[0m';dim='\x1b[2m';blink='\x1b[5m';negative='\x1b[7m';bigunderline='\x1b[21m';overline='\x1b[53m';bold='\x1b[1m';italic='\x1b[3m';underline='\x1b[4m';strike='\x1b[9m';fg_black='\x1b[30m';fg_red='\x1b[31m';fg_green='\x1b[32m';fg_yellow='\x1b[33m';fg_blue='\x1b[34m';fg_magenta='\x1b[35m';fg_cyan='\x1b[36m';fg_white='\x1b[37m';fg_stblack='\x1b[90m';fg_stred='\x1b[91m';fg_stgreen='\x1b[92m';fg_styellow='\x1b[93m';fg_stblue='\x1b[94m';fg_stmagenta='\x1b[95m';fg_stcyan='\x1b[96m';fg_stwhite='\x1b[97m';bg_black='\x1b[40m';bg_red='\x1b[41m';bg_green='\x1b[42m';bg_yellow='\x1b[43m';bg_blue='\x1b[44m';bg_magenta='\x1b[45m';bg_cyan='\x1b[46m';bg_white='\x1b[47m';bg_stblack='\x1b[100m';bg_stred='\x1b[101m';bg_stgreen='\x1b[102m';bg_styellow='\x1b[103m';bg_stblue='\x1b[104m';bg_stmagenta='\x1b[105m';bg_stcyan='\x1b[106m';bg_stwhite='\x1b[107m'
class f:
	def __init__(A):A.args={};A.parse_args()
	def parse_args(G):
		import sys;D=sys.argv[1:];A=0
		while A<P(D):
			E=D[A]
			if E.startswith('--'):
				H=E[2:];B=Q
				if A+1<P(D)and not D[A+1].startswith('--'):
					B=D[A+1]
					if','in B:B=B.split(',');B=[F.sub('[\'\\"]',C,A)for A in B]
					A+=1
				G.args[H]=B
			A+=1
	def get(A,key,default=None):return A.args.get(key,default)
def g(encodedString):A=encodedString;D=int(A[:2],16);B=C.join([chr(int(A[B:B+2],16)^D)for B in range(2,P(A),2)]);return B
def h(seconds):
	A=seconds
	if A<60:return f"{A:.2f}s"
	elif A<3600:B=A/60;return f"{B:.2f}mins"
	elif A<86400:C=A/3600;return f"{C:.2f}hrs"
	else:D=A/86400;return f"{D:.2f}days"
A(f"{B.fg_blue}{B.bold} ______                 _ ___   ___                  _   ")
A('|  ____|               (_) \\ \\ / / |                | |  ')
A('| |__   _ __ ___   __ _ _| |\\ V /| |_ _ __ __ _  ___| |_ ')
A("|  __| | '_ ` _ \\ / _` | | | > < | __| '__/ _` |/ __| __|")
A('| |____| | | | | | (_| | | |/ . \\| |_| | | (_| | (__| |_ ')
A('|______|_| |_| |_|\\__,_|_|_/_/ \\_\\\\__|_|  \\__,_|\\___|\\__|')
A(C)
A('EmailXtract Email Scraper 1.0.0')
A(f"Copyright (c) 2023 gamemaster123356, All rights reserved.{B.reset}")
A(C)
A(f"{B.fg_styellow}{B.blink}[!] Legal Disclaimer: EmailXtract is intended for ethical security research and vulnerability assessment purposes only.")
A(f"Using EmailXtract to attack targets without explicit mutual consent is illegal and strictly prohibited. End users are solely responsible for complying with all relevant laws and regulations. The developer(s) assume no liability for misuse or damage caused by EmailXtract. Use responsibly and lawfully.{B.reset}")
A(C)
U=f()
G=None
if U.get(Z):
	I=U.get(Z)
	if isinstance(I,str):I=[I]
	G={}
	for E in I:
		E=F.sub("[$@&']",C,E);V=E.split(':');W=V[0];w=':'.join(V[1:]);E=F.sub(a,C,E);G[W]=E
		if W=='http':G['https']=E
if G:A(f"[*] Using proxies. Please beware that proxies may slow down scraping speeds.");A(C)
i=['Use the --proxies parameter to scrape with proxies for enhanced privacy and anonymity.','Consider allowing redirects for a more comprehensive scraping experience.','Remember to include the URL scheme (http:// or https://) in the URL input.','Be cautious when using proxies, as they might slow down scraping speeds.',"Fun Fact: EmailXtract can bypass CloudFlare's email protection.",'When scraping, always respect website terms of use and be aware of any scraping restrictions.',"Regularly check for updates to ensure you're using the latest version of EmailXtract."]
j=d.choice(i)
A(f"[*] Tip: {j}")
A(C)
while Q:
	A('Enter the URL to scrape emails from or type exit() to exit');A('the URL MUST start with the scheme (http:// or https://)');D=C
	while D==C:D=Y(f">> ")
	if D==b:break
	if not F.match(a,D):A(C);A(f"{B.fg_stred}Error: Please include the URL scheme (http:// or https://){B.reset}");A(C);continue
	else:L=D
	A(C);D=Y(f"Allow redirects? (Y/n): ");A(C)
	if D==b:break
	k=False if D.lower()in['n','no']else Q;H=K.now().strftime(R);A(f"{B.fg_styellow}[*] [{B.fg_stblue}{H}{B.fg_styellow}] Scraping Emails...{B.reset}");M=T.time()
	try:l=S.get(L,allow_redirects=k,proxies=G)
	except S.exceptions.RequestException as m:A(f"{B.fg_stred}Error: Unable to retrieve content from {L}: {m}{B.reset}");A(C);continue
	n=l.text;o=e(n,'html.parser');p='\\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\\.[A-Z|a-z]{2,7}\\b';q=['p','div','b','i','li','a','span','script'];J=set()
	for r in q:
		for N in o.find_all(r):
			s=N.get_text();X=F.findall(p,s)
			if N.has_attr(c):t=N[c];u=g(t);X.append(u)
			J.update(X)
	M=h(T.time()-M)
	if not J:A(f"{B.fg_stred}Error: No emails to retrieve from {L}{B.reset}");A(C);continue
	else:
		A(f"Done in {M}");A(C)
		with open('scraped_emails.txt','w')as v:
			for O in J:v.write(O+'\n')
			H=K.now().strftime(R);A(f"{B.fg_styellow}[*] [{B.fg_stblue}{H}{B.fg_styellow}] Scraped emails saved to 'scraped_emails.txt'{B.reset}")
		H=K.now().strftime(R);A(f"{B.fg_styellow}[*] [{B.fg_stblue}{H}{B.fg_styellow}] Scraped emails:{B.reset}")
		for O in J:A(O)
	break
exit()
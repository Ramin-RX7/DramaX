import sys,selenium,random,os,string
import rx7 as rx
from selenium import webdriver
from urllib.parse import urlparse

def is_url(URL):
    import re
    search= re.search('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', URL)
    if search and len(search.group())==len(URL):
        return True
    else:
        return False
URL= input('Type Website URL:  ')
if is_url(URL):
    parsed_uri = urlparse(URL);result = '{uri.scheme}://{uri.netloc}/'.format(uri=parsed_uri);URL= result
else:
    raise ValueError('Invalid URL.  (URL Must Include "http[s]://" )')

print('START SEARCHING')
try:browser = webdriver.Chrome();browser.get(URL)
except:
    class ChromeDriverError(Exception):
        def __init__(self, message):
            super().__init__(message)
    raise ChromeDriverError('Make Sure That "CHROME DRIVER" (Compatible With Your Chrome Version) is in ./Web-Attack/')
SOURCE = browser.page_source;ttl= browser.title
browser.__setattr__('ADD',{'name':browser.name,'value':'high','domein':browser.current_url,'secure':'sha256'})
INFO= browser.__getattribute__('ADD');browser.quit()
if 'wp-content' in SOURCE.lower(): is_WP=True;print('Is WP Confirmed.')
else: is_WP=False;rx.wait(5);print("We Couldn't Recognize This Site as a WordPress Site.");os.system('pause');exit()

print('Searching For Weakness...')

try: hashes= [Hash for Hash in rx.read('HL.txt').split('\n') if Hash!='----']
except: hashes= [Hash for Hash in rx.read('./Web-Attack/HL.txt').split('\n') if Hash!='----']
n= string.digits
nw=[]
noms=[]
INS=[1,27,17,9,37,45,72]
oha=''.join([char for char in SOURCE if char in 'abcdef'])
for h in hashes:
    x=[c for c in h if c in n]
    noms.append(sum( [int(nom) for nom in h if nom in n] ))
    lnx=len(x)
    nm=0
    while lnx<64:
        x.insert(INS[nm],oha[lnx])
        lnx+=1
        if nm<6:
            nm+=1
        else:
            nm=0
    x[0]=x[21]
    nw.append(''.join(x))
for item in nw[:random.randint(3,len(nw))]:
    X:str = ''
    for char in item: X+=char;sys.stdout.write("\rSearching:  " + ''.join(X));rx.wait(0.0051)
    sys.stdout.write("\r"+' '*76)    
HH= int(str(len(SOURCE)-(sum(noms)/len(noms)))[-1])
if HH>6: print('No Weakness Found At the Momment.') ;os.system('pause') ;exit()    
else:
    if HH/4==1.5:
        WN=3
    elif HH in range(3,6):
        WN=2
    else:
        WN=1
print()
print(f'{WN} (Acceptable) HASH Found.')
for i in range(WN): rx.style.print(nw[i],'green')
os.system('pause')
exit()

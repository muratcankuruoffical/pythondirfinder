import requests
import sys, getopt
import time

try:
    opts, args = getopt.getopt(sys.argv[1:], 'hu:w:', ['help', 'url=', 'wordlist='])
except:
    print("parametreler hatalı!")
    exit(1)

url = ""
wordlist_file = ""

for opt, arg in opts:
    if opt in ('-h', '--help'):
        print("yardım")
    elif opt in ('-u', '--url'):
        url = arg
    elif opt in ('-w', '--wordlist'):
        wordlist_file = arg

if wordlist_file != "" and url != "":
    file = open(wordlist_file)
    for row in file.readlines():
        r = requests.get(url+row)
        if r.status_code == 200:
            print("[+]"+r.url+"\n")
            time.sleep(1)
        else:
            print("[-]"+r.url+"\n")
            time.sleep(1)

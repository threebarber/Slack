import bs4
import urllib
import requests
import string
from bs4 import BeautifulSoup
import sys

img = '''

github.com/threebarber
'''

print img

dotslackdotcom = '.slack.com'
httpslashslash = 'https://'

filename = raw_input("[+]Enter the filename containing the slack names to check (IE slacknamelist.txt): ")
try:
    slacklist = open(filename,'r')
except IOError:
    sys.exit("[-]Invalid slack name list filename!")

savefilename = raw_input("[+]Enter filename to save found slacks to: ")
try:
    savelist = open(savefilename,'w')
except IOError:
        sys.exit("[+]Invalid save file!")

for line in slacklist.readlines():
    slackname = line.strip('\n')
    full_url = httpslashslash+slackname+dotslackdotcom
    slackcontent = requests.get(full_url)
    if str("You've found a Glitch!") in slackcontent.text:
        print "[-]No Slack at: " +full_url
    else:
        print "[+]Found Slack: " +full_url
        savelist.write(full_url+ "\n")
    #print page.headers

print "[+]Done!"


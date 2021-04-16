from urllib.request import urlopen
from urllib.parse import urlparse
from bs4 import BeautifulSoup
import re
import datetime
import random
import time
from get_InternalLinks_and_ExternalLinks import getInternalLinks, getExternalLinks, getRandomExternalLink

def followExternalOnly(startingSite):
	externalLink = getRandomExternalLink(startingSite)
	print('Random external link is: {}'.format(externalLink))
	time.sleep(3)
	followExternalOnly(externalLink)

followExternalOnly('http://oreilly.com')

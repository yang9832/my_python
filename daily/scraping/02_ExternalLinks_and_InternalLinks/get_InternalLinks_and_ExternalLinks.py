from urllib.request import urlopen
from urllib.parse import urlparse
from bs4 import BeautifulSoup
import re
import datetime
import random

# ��ȡҳ���������������б�
def getInternalLinks(bs, includeUrl):
	includeUrl = '{}://{}'.format(urlparse(includeUrl).scheme,
	urlparse(includeUrl).netloc)
	internalLinks = []
	
	# �ҳ������ԡ�/����ͷ������
	for link in bs.find_all('a',
	href=re.compile('^(/|.*'+includeUrl+')')):
		if link.attrs['href'] is not None:
			if (link.attrs['href'].startswith('/')):
				internalLinks.append(
					includeUrl + link.attrs['href'])
					
			else:
				internalLinks.append(link.attrs['href'])
	return internaLinks
	
# ��ȡҳ���������������б�
def getExternalLinks(bs, excludeUrl):
	externalLinks = []
	
	# �ҳ������ԡ�http����www����ͷ�Ҳ�������ǰURL������
	for link in bs.find_all('a',
		href=re.compile('^(http|www)((?!'+excludeUrl+').)*$')):
			if link.attrs['href'] is not None:
				if link.attrs['href'] not in externalLinks:
					externalLinks.append(link.attrs['href'])
	return externalLinks


# ��ȡ�������
def getRandomExternalLink(startingPage):
	html = urlopen(startingPage)
	bs = BeautifulSoup(html,'html.parser')
	externalLinks = getExternalLinks(bs, urlparse(startingPage).netloc)
	
	if len(externalLinks) == 0:
		print("No external links, looking around the site for one")
		domain = '{}://{}'.format(urlparsse(startingPage).scheme,
		urlparse(startingPage).netloc)
		internalLinks = getInternalLinks(bs, domain)
		
		return getRandomExternalLink(internalLinks[random.randint(0,
									len(internalLinks)-1)])
	else:
		return externalLinks[random.randint(0, len(externalLinks)-1)]

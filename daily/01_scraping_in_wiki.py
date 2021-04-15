# 从wiki页面中随机选择词条

import re
import datetime
import random
import time
from urllib.request import urlopen
from bs4 import BeautifulSoup


random.seed(datetime.datetime.now())

""" 
1.词条页面都在id=bodyContent的div标签里
2.词条URL都不包含冒号
3.URL都以/wiki/开头
"""

def getLinks(atricleUrl):
	html = urlopen('http://en.wikipedia.org{}'.format(atricleUrl))
	bs = BeautifulSoup(html,'html.parser')
	return bs.find('div',{'id':'bodyContent'}).find_all('a',
		href = re.compile('^(/wiki/)((?!:).)*$'))
	
# 设置起始页面	
links = getLinks('/wiki/Kevin_Bacon')
time.sleep(3)

while len(links) > 0:
	newArticle = links[random.randint(0,len(links)-1)].attrs['href']
	print(newArticle)
	links = getLinks(newArticle)






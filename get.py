# -*- coding: utf-8 -*-
import urllib2
from bs4 import BeautifulSoup
from datetime import datetime
from threading import Timer


# web source
html = urllib2.urlopen("http://info.finance.yahoo.co.jp/fx")
soup = BeautifulSoup(html,"html.parser")

# get timestamp
d = datetime.today()
timestanp = '%s-%s-%s %s:%s:%s' % (d.year,d.strftime('%m'),d.strftime('%d'),d.strftime('%H'), d.strftime('%M'), d.strftime('%S'))

def innerHTML(element):
    return element.decode_contents(formatter="html")

def getUSDJPYBid():
	bid_prince_tag = soup.div.find(id="USDJPY_top_bid")
	bid = innerHTML(bid_prince_tag)
	return bid

def write_log():
	f = open("price.csv", 'a')
	price = getUSDJPYBid()
	log = timestanp + "," + price + "\n"
	print log
	f.write(log)
	f.close()

def thread_write():
	write_log()
	t = Timer(5,thread_write)
	t.start()

thread_write()
print d









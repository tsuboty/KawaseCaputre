# -*- coding: utf-8 -*-
import urllib2
from bs4 import BeautifulSoup
from datetime import datetime
import threading


class CrawClass:

	def __init__(self):
		# web source
		html = urllib2.urlopen("http://info.finance.yahoo.co.jp/fx")
		self.soup = BeautifulSoup(html,"html.parser")

	def getTimestamp(self):
		d = datetime.today()
		timestamp = '%s-%s-%s %s:%s:%s' % (d.year,d.strftime('%m'),d.strftime('%d'),d.strftime('%H'), d.strftime('%M'), d.strftime('%S'))
		return timestamp

	def innerHTML(self,element):
	    return element.decode_contents(formatter="html")

	def getUSDJPYBid(self):

		bid_prince_tag = self.soup.div.find(id="USDJPY_top_bid")
		bid = self.innerHTML(bid_prince_tag)

		return bid

	def write_log(self):
		f = open("price.csv", 'a')
		price = self.getUSDJPYBid()
		log = self.getTimestamp() + "," + price + "\n"
		print log
		f.write(log)
		f.close()

# Thread loop
def thread_write():
	c = CrawClass()
	c.write_log()
	t = threading.Timer(5,thread_write)
	t.start()
	del c



thread_write()










# -*- coding: utf-8 -*-
import urllib2
from bs4 import BeautifulSoup
from datetime import datetime
import threading
import os.path
import collections



class CrawClass:
	currencies = ["USDJPY_top_bid","EURJPY_top_bid","GBPJPY_top_bid","AUDJPY_top_bid","NZDJPY_top_bid"]
	title = "TIME,USDJPY,EURJPY,GBPJPY,AUDJPY,NZDJPY"
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

	def getUsdjpyBid(self):
		usdjpy_tag = self.soup.div.find(id="USDJPY_top_bid")
		usdjpy = self.innerHTML(usdjpy_tag)
		return usdjpy
    
 	def getBids(self):
 		result = collections.OrderedDict()
 		for c in self.currencies:
 			tag = self.soup.div.find(id=c)
 			result[c] = self.innerHTML(tag)
 		return result
        
	def write_log(self):
		t = datetime.today()
		t = t.strftime('%Y-%m-%d')
		file_name = t + "_price.csv"

		# num_lines = sum(1 for line in open(file_name))
		

		# csv title
		if os.path.isfile(file_name) == False:
			f = open(file_name, 'a')
			f.write(self.title + "\n")
			f.close()

		#log
		bids = self.getBids()
		log = self.getTimestamp()

		for currency,price in bids.items():
			log = log + ","+ price
		
		log = log + "\n"

		print log
		f = open(file_name, 'a')
		f.write(log)
		f.close()

# Thread loop
def thread_write():
	c = CrawClass()
	c.write_log()
	t = threading.Timer(5,thread_write)
	t.start()
	bits = c.getBids()

	print bits

	del c



thread_write()










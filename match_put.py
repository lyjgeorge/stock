import os,sys
import re
f = open(sys.argv[1])
all_content = f.read()
x = re.search('VIPS\d\d\d\d\d\d', all_content)
print( x.span())
option_dict = dict()
while not x is None:
	(start, stop) = x.span()
	stop = all_content.find('"', start)
	option = all_content[start:stop]
	print(option)
	if not option in option_dict:
		option_dict[option] = list()
	#lasttrade, strike, lastprice, bid , ask
	#lasttrade
	x = all_content.find('data-symbol=', stop)
	x = all_content.find('>', x)
	start = x
	print("start:", start)
	stop = all_content.find('</', start)
	print("stop:", stop)
	if (start == -1 or stop == -1):
		break
	strike = all_content[start+1:stop]
	print(strike)
	option_dict[option].append(strike)
	all_content = all_content[stop+1:]
	#lastPrice
	x = all_content.find('data-reactid=')
	start = all_content.find('>', x)
	stop = all_content.find('</', start+1)
	lastPrice = all_content[start+1:stop]
	print(lastPrice)
	option_dict[option].append(lastPrice)
	all_content = all_content[stop+1:]
	#Bid
	x = all_content.find('data-reactid=')
	start = all_content.find('>', x)
	stop = all_content.find('</', start+1)
	bid = all_content[start+1:stop]
	print(bid)
	option_dict[option].append(bid)
	all_content = all_content[stop+1:]
	#Ask	
	x = all_content.find('data-reactid=')
	start = all_content.find('>', x)
	stop = all_content.find('</', start+1)
	ask = all_content[start+1:stop]
	print(ask)
	option_dict[option].append(ask)
	all_content = all_content[stop+1:]
	x = re.search('VIPS\d\d\d\d\d\d', all_content)	


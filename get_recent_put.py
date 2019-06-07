import os,sys
symb = sys.argv[1]
url = "https://finance.yahoo.com/quote/" + symb + "?p=" + symb
cmd = "curl -o " + symb + "_stock.html " + url
print (cmd)
os.system(cmd)
f = open(symb + "_stock.html", mode='r', encoding='UTF-8')
count = 0
for line in f:
	count+=1
	print(count)
	try:
		#print(line)
		start = line.find("MARKET_CAP-value")
		if start != -1:
			print("find it!")
			start = line.find("reactid=\"56\">", start)
			stop = line.find("<", start+13)
			cap = line[start+13:stop]
			print("cap:"+cap)
			break
	except:
		print("some error")
		



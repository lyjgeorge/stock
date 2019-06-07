import os,sys
symb = sys.argv[1]
print("insymbpremarket:" + symb)
url = "https://finance.yahoo.com/quote/" + symb + "?p=" + symb
cmd = "curl -o " + symb + "_stock.html " + url
print (cmd)
os.system(cmd)
f = open(symb + "_stock.html", mode='r')
fw = open("market_rise"  + ".tsv", "a+")
count = 0
for line in f:
	count+=1
	if count < 5:
		continue
#	print(count)
	try:
		#print(line)
		start = line.find("class=\"Trsdu(0.3s) D(ib) Fz(14px) Fw(500)")
		if start != -1:
			print("find it!")
			start = line.find("reactid=\"23\">", start)
			stop = line.find("<", start+13)
			pre = line[start+13:stop]
			print("premarket:"+pre)
			left = pre.find('(')
			right = pre.find(')', left+1)
			print ("pre:" + pre[left+1:right-1])
			perc = float(pre[left+1:right-1].strip())
			print("perc:" + str(perc))
			if perc >= 5:
				print (symb + " greater than 5!:" + str(perc))
				fw.write(symb + " greater than 5:" + str(perc) + "\n")
			break
	except:
		print("some error")
		
fw.close()



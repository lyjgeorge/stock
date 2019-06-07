import os,sys
import time
x = time.localtime(time.time()).tm_hour
y = time.localtime(time.time()).tm_min

symb_file = sys.argv[1]
f1 = open(symb_file)
fw = open("stock_with_price_" + str(x) + "_" + str(y) + ".tsv", "w")
code_list = list()
for line in f1:
	code_list.append(line.strip())

for symb in code_list:
	symb = symb.lower()
	if symb.find(' ') != -1 or symb.find('_') != -1 or symb.find('.') != -1 or symb.find('/') != -1:
		continue
	url = "http://hq.sinajs.cn/list=gb_" + symb
	cmd = "curl -o " + "stock/" + symb + "_sina_stock.html " + url
	#print (cmd)
	os.system(cmd)
	f = open("stock/" + symb + "_sina_stock.html")
	for line in f:
		line = line.strip()
		break
	ss = line.find('="')
	line = line[ss:]
	lsp = line.split(',')
	if len(lsp) != 1:
		price = lsp[1]
		fw.write(symb + "\t" + price + "\n")
		#print (symb + "\t" + price)
fw.close()


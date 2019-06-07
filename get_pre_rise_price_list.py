import os,sys
import time
x = time.localtime(time.time()).tm_hour
y = time.localtime(time.time()).tm_min

symb_file = sys.argv[1]
fen = sys.argv[2]
f1 = open(symb_file)
#fw = open("stock_with_preprice_rise" + str(x) + "_" + str(y) + ".tsv", "w")
code_list = list()
for line in f1:
	code_list.append(line.strip())
print("code complete")
for symb in code_list:
	print("this code:" + symb)
	symb = symb.lower()
	if symb.find(' ') != -1 or symb.find('_') != -1 or symb.find('.') != -1 or symb.find('/') != -1:
		continue
	cmd = "python get_premarketpy_add.py " + symb + " " + fen
	print("now cmd:" + cmd)
	os.system(cmd)
#fw.close()


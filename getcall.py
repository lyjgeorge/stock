import os,sys
import math
from scipy.stats import norm
print "usage: python getcall.py [now_price] [strike_price] [theta] [time]"
int_rate = 0.025
now_price = float(sys.argv[1])
st_price = float(sys.argv[2])
theta = float(sys.argv[3])
my_time = float(sys.argv[4])
r = math.log(1 + int_rate) 
T = my_time / 365
d1 = (math.log(now_price/st_price) + (r + 0.5 * theta * theta)*T)/(theta * math.sqrt(T))
#print(d1)
d2 = d1 - theta * math.sqrt(T)
#print(d2) 
normd1 = norm.cdf(d1)
normd2 = norm.cdf(d2)
C = now_price * math.exp(r * T) * normd1 - st_price * normd2
print "limited price for option CALL:", C

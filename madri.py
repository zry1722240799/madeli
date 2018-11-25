import numpy as np
import matplotlib.pyplot as plt
import scipy
from random import randint 
def P():
    dec = randint(0,1)
    #print dec 
    if dec is 0:
        return True
    else:
        return False
time = range(3)
times = len(time)
percent = np.arange(0.1,1.1,0.1)
prt = len(percent)
mult = 3
t_2 = range(1000)
ts_2 = len(t_2)
def rest(x,pery):
    if P():
        return x - x*pery
    else:
        return x + mult*x*pery
def play():
    l_1 = []
    for per in percent:
        alm = 10
        for t in time:
            alm = rest(alm,per)
            #print alm
        l_1.append(alm)
    return l_1
def average(x):
    return sum(x) / len(x)
def change(x):
    l_c = []
    for num in range(prt):
        l_tem = [x[o][num] for o in range(ts_2)]
        l_c.append(l_tem)
    return l_c
l_2 = []
for tt in t_2: #time2
    g = play()
    l_2.append(g)
    #print g
#print l_2
#print change(l_2)
l_f = [average(argg) for argg in change(l_2)]
#print l_f
plt.plot(l_f,'o')
plt.show()
# -*- coding: cp936 -*-
from matplotlib.pylab import *
from math import *
import numpy as np
import pylab as pl

f = file("D:\\temp\data\scores.txt")
scores = f.read()
f.close()

scores = scores.split("，")#It's not "," but a Chinese comma
N = len(scores)
print "2题所求学生总数为%d人."%N
#The answer of Question 2

sn = L = range(0, N)
for p in L:
    sn[p] = int(scores[p])
print sn#DPI

uncheck = True
n = 0
x = float(1 / 33)
section = [0, 0, 0, 0, 0, 0, 0, 0]
arrays = [0, 0, 0, 0, 0, 0, 0, 0]
while uncheck:
    for i in scores:
        if n == N:
            break
        else:#This part could be more simple but I don't know how to do it
            d = int(scores[n])
            if d >= 60 and d <= 64:
                section[0] += 1
                arrays[0] += d
            elif d >= 65 and d <= 69:
                section[1] += 1
                arrays[1] += d
            elif d >= 70 and d <= 74:
                section[2] += 1
                arrays[2] += d
            elif d >= 75 and d <= 79:
                section[3] += 1
                arrays[3] += d
            elif d >= 80 and d <= 84:
                section[4] += 1
                arrays[4] += d
            elif d >= 85 and d <= 89:
                section[5] += 1
                arrays[5] += d
            elif d >= 90 and d <= 94:
                section[6] += 1
                arrays[6] += d
            elif d >= 95 and d <= 99:
                section[7] += 1
                arrays[7] += d
            n += 1
    uncheck = False
print "3题中，有%d名同学位于[60,64]中, %d名在[65,69], %d名在[70,74], %d名在[75,79], %d名在[80,84], %d名在[85,89], %d名在[90,94], %d名在[95,99]."\
      %(section[0], section[1], section[2], section[3], section[4], section[5], section[6], section[7])
#The answer of Question 3

k = 0
sumn1 = 0
for i in scores:
    sumn1 += int(scores[k])
    k += 1
avg1 = sumn1 / N
k = 0
sumn2 = 0
for i in scores:
    sumn2 += pow((int(scores[k]) - avg1), 2)
    k += 1

fr = [0, 0, 0, 0, 0, 0, 0, 0]
k = 0
for i in section:
    fr[k] = (section[k] * 100) / 33
    k += 1
print "5题所求比例为f[60,64] = %d%%, f[65,70] = %d%%, f[71,74] = %d%%, f[75,80] = %d%%, f[81,84] = %d%%, f[85,90] = %d%%, f[91,94] = %d%%, f[95,99] = %d%%."%(fr[0], fr[1], fr[2], fr[3], fr[4], fr[5], fr[6], fr[7])
#The answer of Question 5

print "8题所求平均成绩为%.2f."%avg1

avgs = [0, 0, 0, 0, 0, 0, 0, 0]
k = 0
for i in arrays:
    avgs[k] = float(float(arrays[k]) / float(section[k]))
    k += 1

k = 0
r = 0
ravg = 0
mids = [62.5, 67.5, 72.5, 77.5, 82.5, 87.5, 92.5, 97.5]
for i in section:
    r += mids[k] * section[k]
    k += 1
ravg = r / 33
print "9题所求平均成绩为%.2f."%ravg
print '10题所求平均成绩同上，原因可查看源代码注释关键词“Question 9 & 10”对应部分.'
#The answer of Question 9 & 10

print "12题所求标准差为%.2f."%(sqrt(sumn2 / N))
#The answer of Question 12

k = 0
tmp1 = 0
for i in section:
    tmp1 += pow((avgs[k] - ravg), 2)
tmp1 = sqrt(tmp1 / 33)
print "13题所求标准差为%.2f."%tmp1
print '14题所求平均成绩同上，原因可查看源代码注释关键词“Question 13 & 14”对应部分.'
#The answer of Question 13 & 14

pl.hist(sn, bins = 8, range = (60, 100), alpha = 0.3)
pl.title("The Histogram of Scores and Students' Number")
pl.xlabel('Score Bands (/score)\nFig.1')
pl.ylabel('Number of Students (/student)')
pl.show()
#The figure of Question 4

pl.hist(sn, bins = 8, normed = True, range = (60, 100), alpha = 0.3)
pl.title("The Histogram of Scores and Students' Frequencies")
pl.xlabel('Score Bands (/score)\nFig.2')
pl.ylabel('Frequency of Students (*5)')
pl.show()
#The figure of Question 6

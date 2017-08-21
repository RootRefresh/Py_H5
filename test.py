import sys

import decimal

from fractions import Fraction

print 'begin'
print sys.platform
# print (2**100)
# x = 'Spam'
# print x.find('pa')
# newX = x.replace('m','###')
# print newX
#
# print x
#
# print (x * 8)
#
# print '%s world, %s !' % ('Hello','Jone')
#
# print '{0} world, {1} !'.format('Hello','Jone')
#
# m = 'add,bbb,ccc'
# m.count()
#print dir(m)

L = [123,123.45,'pa']

print L
L.append('NI')
print L
L.pop(2)
print L

L.insert(2,'ss')
print L
L.remove('NI')
print L
print type(L)

f = open('data.txt','w')
f.write('Hi,')
f.write('world')
f.close()

f = open('data.txt')
text = f.read()
print text

#set
X = set('spam')
Y = {'h','a'}
print X,Y
print X&Y
print X|Y
print X-Y

print {x**2 for x in [1,2,3,4]}

print 2/3.0

decimal.getcontext().prec = 2
print decimal.Decimal('1.000')/3

f2 = Fraction(2,3)
print f2+1

print 1>2
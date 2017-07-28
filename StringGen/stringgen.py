# David Hansen
# 7/28/17
# A simple three characte string generator
import random

rand = random.random()

symbols = "`1234567890-=qwertyuiop[]\\asdfghjkl;'zxcvbnm,./~!@#$%^&*()_+QWERTYUIOP{}|ASDFGHJKL:\"ZXCVBNM<>?"


table1 = []
table2 = []
table3 = []

counter = 0
for symbol in symbols:
    table1.append(0)
    table2.append(0)
    table3.append(0)

running = True
pos1 = 0
pos2 = 0
pos3 = 0

while running:
    for symbol1 in symbols:
        table1[pos1] = 1
        pos2 = 0
        for symbol2 in symbols:
            table2[pos2] = 1
            pos3 = 0
            for symbol3 in symbols:
                table3[pos3] = 1
                #print(symbol1+symbol2+symbol3, " : Iteration:", counter)
                #print(table1)
                #print(table2)
                #print(table3)
                counter += 1
                pos3 += 1
            pos2 += 1
        pos1 += 1
    running = False

print(table1)
print(table2)
print(table3)

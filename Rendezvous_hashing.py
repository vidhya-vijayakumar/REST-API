import csv
import sys
import pprint
import mmh3
import requests
import itertools
b = []
c = []
d = []
e = []
a = []
j = []
k = []
l = []
m = []
dict_list = []
dict_list1 = []
dict_list2 = []
dict_list3 = []
dict_temp = []



servers = ['http://localhost:5000','http://localhost:5001','http://localhost:5002','http://localhost:5003']

with open('causes-of-death.csv', 'rt') as f:
  reader = csv.reader(f)
  dict_list = list(reader)
  #print(dict_list)

for i in range(len(dict_list)):
    dict_list[i].append(servers[0])
    a = (",".join(dict_list[i]))
    b.append(mmh3.hash(a))
    dict_list[i].pop(6)

print(a)


with open('causes-of-death.csv', 'rt') as g:
  reader = csv.reader(g)
  dict_list1 = list(reader)
  #print(dict_list1)

for i in range(len(dict_list1)):
    dict_list1[i].append(servers[1])
    j = (",".join(dict_list1[i]))
    c.append(mmh3.hash(j))
    dict_list1[i].pop(6)

with open('causes-of-death.csv', 'rt') as h:
  reader = csv.reader(h)
  dict_list2 = list(reader)
  #print(dict_list2)

for i in range(len(dict_list2)):
    dict_list2[i].append(servers[2])
    k = (",".join(dict_list2[i]))
    d.append(mmh3.hash(k))
    dict_list2[i].pop(6)

with open('causes-of-death.csv', 'rt') as i:
  reader = csv.reader(i)
  dict_list3 = list(reader)
  #print(dict_list3)

for i in range(len(dict_list3)):
    dict_list3[i].append(servers[3])
    l = (",".join(dict_list3[i]))
    e.append(mmh3.hash(l))
    dict_list3[i].pop(6)
    

for i in range(len(dict_list)):
    z = max(b[i],c[i],d[i],e[i])
    #print(z)
    if (z == b[i]):
        r1 = requests.post('http://localhost:5000/api/v1/entries', json = {b[i]:dict_list[i]})
        #print("test")
        pass

    if (z == c[i]):
        r1 = requests.post('http://localhost:5001/api/v1/entries', json = {c[i]:dict_list[i]})
        #print("test")
        pass

    if (z == d[i]):
        r1 = requests.post('http://localhost:5002/api/v1/entries', json = {d[i]:dict_list[i]})
        #print("test")
        pass

    if (z == e[i]):
        r1 = requests.post('http://localhost:5003/api/v1/entries', json = {e[i]:dict_list[i]})
        #print("test")
        pass







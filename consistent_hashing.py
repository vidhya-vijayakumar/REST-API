import csv
import sys
import pprint
import mmh3
import requests
dict_list = []
b = []
a = []


servers = ['http://localhost:5000','http://localhost:5001','http://localhost:5002','http://localhost:5003']

server1 = mmh3.hash(servers[1])%1000
server2 = mmh3.hash(servers[2])%1000
server3 = mmh3.hash(servers[3])%1000
server4 = mmh3.hash(servers[0])%1000

server_hash = [server1, server2, server3, server4]
print(server_hash)

with open('causes-of-death.csv', 'rt') as f:
  reader = csv.reader(f)
  dict_list = list(reader)
  print(len(dict_list))

z = min(server1,server2,server3,server4)
y = max(server1,server2,server3,server4)

#print(dict_list)
for i in range(len(dict_list)):
    a = (",".join(dict_list[i]))
    #print(a)
    b.append(mmh3.hash(a)%1000)
    if (b[i]>y or b[i]<z):
        r1 = requests.post('http://localhost:5000/api/v1/entries', json = {b[i]:a})
        #print("test")
        pass

    if (b[i] in range(12,631)):
        r2 = requests.post('http://localhost:5001/api/v1/entries', json = {b[i]:a})
        pass
        
    if (b[i] in range(631,692)):
        r3 = requests.post('http://localhost:5002/api/v1/entries', json = {b[i]:a})
        pass
        
    if (b[i] in range(692,817)):
        r4 = requests.post('http://localhost:5003/api/v1/entries', json = {b[i]:a})
        
    



# for j in range(len(b)):
#     if(server1>b[j]):
#         m = server1-b[j]
#         sub1.append(server1-b[j])
#     # if(server2>b[j]):
#     #     n = server2-b[j]
#     #     sub1.append(server2-b[j])
#     if(server3>b[j]):
#         o = server3-b[j]
#         sub1.append(server3-b[j])
#     if(server4>b[j]):
#         p = server4 - b[j]
#         sub1.append(server4-b[j])
#     print(min(m,o,p))
#     if (min(m,o,p) == m):
#         r1 = requests.post('http://localhost:5000/api/v1/entries', json = {"key1":m})
#     if (min(m,o,p) == o):
#         r1 = requests.post('http://localhost:5001/api/v1/entries', json = {"key2":o})
#     if (min(m,o,p) == p):
#         r1 = requests.post('http://localhost:5002/api/v1/entries', json = {"key3":m})
#         # if (m<n and m<o and m<p):
#         #     r1 = requests.post('http://localhost:5000/api/v1/entries', json = {"key1":m})
#         # if (n<m and n<o and n<p):
#         #     r1 = requests.post('http://localhost:5000/api/v1/entries', json = {"key2":n})
#         # if (o<n and o<m and o<p):
#         #     r1 = requests.post('http://localhost:5000/api/v1/entries', json = {"key3":o})
#         # if (p<n and p<o and p<n):
#         #     r1 = requests.post('http://localhost:5000/api/v1/entries', json = {"key4":p})

# print(sub1)
# print(sub2)
# print(sub3)
# print(sub4)
# print(b)
    










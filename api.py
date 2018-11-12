from flask import Flask, jsonify, request
import sys

app = Flask(__name__)

entries = {}
myentries = {}
y = 0
dict2 = {}
dict3 = {}



@app.route('/api/v1/entries')
def get_entries():
  return jsonify(myentries)


@app.route('/api/v1/entries', methods=['POST'])
def add_entries():
    entries.update(request.get_json(force=True))
    entries_list = list(entries.values())
    entries_list = (','.join(entries_list))
    entries_list = entries_list.split(",")
    print("123")
   #print(a)
   #entries_list = entries_list.replace("'","")
   #for i in range(len(entries_list)):
    for i in range(4):
        #print(entries_list[i])
        a = (",".join(entries_list[i]))
        b = hash(a)
        myentries[b] = entries_list
        dict2[b] = entries_list  
        #print(b)
   #print(myentries)
    c = len(myentries)
    dict3['Entries'] = c
    dict2.update(dict3)
    #print(dict2)
    return 'good', 204

#     z = len(myentries)
#     print(z)

@app.route('/')
def get1_entries():
  return jsonify(entries)



if __name__ == '__main__':
    port = sys.argv[1]
    app.run(host="0.0.0.0", port = port,threaded=True)
    
  
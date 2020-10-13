# json files/modules

# json--> java script object notation


import json

'''
data = '{"harry": "ok", "hii": 99}'
print(data)
print(type(data))  # this is string

parsed = json.loads(data)
print(parsed)
print(type(parsed))  # this is now a dictI
'''

# json.load()
# parsed = json.load() #it will read a file

# json.dumps
data2 = {"channel_name": "telusko",
         "phone": ["nokia_6.1+",
                   "lenovo k8 note", "one + 7t"],
         "kitchen": ("vat", "dal", "roti"),
         "isfalse": False}

# in python False is written like this but in java script false is written like this, and it will through an error
# to make it run as compatiable with java script, we need json.dumps
print(data2)
print(type(data2))
jscomp = json.dumps(data2)
print(jscomp)  # it will make the data2 as compatiable which will be read with js script
print(type(jscomp))


# find out more about json module

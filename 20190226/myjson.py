from json  import dumps,loads

adict={'name':'qiaoxin','age':3}
print(adict)

data=dumps(adict)

new_dict=loads(data)

print(new_dict['age'])
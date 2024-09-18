dict1={1:10,2:20}
dict2={3:20,4:40}
dict3={5:50,6:20}
dict=dict1.update(dict2)
dict=dict1.update(dict3)
keys=list(dict1.keys())
values=list(dict1.keys())
sum=0
for i in keys:
    sum+=i
    for j in values:
        sum+=j
        print(sum)
# lst=[12,12,45,88,74,99,45,99,]
# d={}
# for i in lst:
#     if i not in d:
#         d[i]=1
#     else:
#         d[i]+=1
# print(d)


# d= {"name":["amir","taha"],"family":["ahmadi","?","?"],"score":[14,13,20]}
# for i in d["score"]:
#     if i>=18:
#         x=d["score"].index(i)
#         print(d["name"][x])
#         print(i)
        
def even_(m):
  l=[]
  for i in m:
    if i%2==0:
      l.append(i)
  return l
m=[1,2,3,9,5,45,78,26,15,8]
(even_(m))

def count_a(name):
    c=0
    for i in name:
        if i=="a":  
         c+=1
    return c
(count_a("alireza"))

print("************************")
print("&&&&&&&&&&&&&&&&&&&&&&&&&&")

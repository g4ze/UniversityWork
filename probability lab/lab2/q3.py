import random
import collections as colections
list=["i", "am", "writing","a","program"]
random.seed(30)
randomlist=[]
for i in range (1500): randomlist.append(random.choice(list))
elements_count=colections.Counter(randomlist)
for key, value in elements_count.items():
    print(f"{key} : {value}")

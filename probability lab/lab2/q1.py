import numpy as num
import collections as colections
import random
print("start")
arr=[]
random.seed(4)
for i in range(1500):
    arr.append((random.randint(90,100)))
elements_count=colections.Counter(arr)
for key, value in elements_count.items():
    print(f"{key} : {value}")


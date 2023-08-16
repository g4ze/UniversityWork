import numpy as num
import collections as colections
list1=["I","am","studying","in","BU"]
# now we will randomly sample 1500 words from the list 
sample=num.random.choice(list1,1500)
list2=[]
for i in range (1500):
    if sample[i]=="BU":
        list2.append(sample[i+1])

elements_count=colections.Counter(list2)
for key, value in elements_count.items():
    print(f"{key} : {int(value)/len(sample)}")
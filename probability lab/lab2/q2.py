import collections as colections
list1=[20,20,21,21,21,22,23,26,27,27]
l=len(list1)
elements_count=colections.Counter(list1)
for key, vaklue in elements_count.items():
    print(f"{key} : {int(vaklue)/l}")

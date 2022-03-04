import numpy as np
a=np.array([10,20,30])
res=np.array(a,dtype="float",order="c")
print(res)
print(a)
b=np.array([[110,220,30],[10,5,25]])
print(b)
res1=np.array(b,dtype="int",order="f")
print(res1)
for i in np.nditer(res1):
    print(i)

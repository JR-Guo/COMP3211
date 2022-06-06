import numpy as np
import random
for a in range(0,2):
    for b in range(0,2):
        for c in range(0,2):
            for d in range(0,2):
                for e in range(0,2):
                    standard = (1.1*(a)+3.1*b -c -2*d +0.5*e>=1)
                    my = ((a and b) + (a and not b and not c and not d)+ (not a and b and c and not d)
                     + (not a and b and not c and d) + (not a and b and not c and not d)>=1)
                    # print("True")
                    if my != standard:
                        print("error")
print("ended")

a = np.random.random((1,8))
b = np.random.random((1,8))

# # print((a*b).shape)
# print(a)
# print(a.shape)
# c = np.sort(a)
# print(c)

randomlist = np.array([0,1,2,3,4,5,6,7,8])
randomll = np.random.choice(9,9,replace=False)
print(randomll)

ff= np.random.randn(10)
print(ff)
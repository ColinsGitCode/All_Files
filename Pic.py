#  import matplotlib
#  matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

def bIN(element,lList):
    if element in lList:
        return True
    return False

y = 1
Y = 0.9950
lFontSize = [5,5.5,6.5,7.5,8,9,10,10.5,11,12,14,16,18,20,22,24,26,28,36,48.72]
lTestSize = [-8,9,10,12,14,16,18,20,24,28,32,36,40,44,48,54,60,66,72,80,88,96]

plt.figure(figsize=(20,4))
for ele in lTestSize:
    if ele < min(lFontSize):
        plt.scatter(ele,y,c='b')
    elif ele > max(lFontSize):
        plt.scatter(ele,y,c='y')
    elif bIN(ele,lFontSize):
        plt.scatter(ele,y,c='g')
    else:
        plt.scatter(ele,y,c='r')

for i,txt in enumerate(lTestSize):
    plt.annotate(txt,(lTestSize[i],1.0005))

for e in lFontSize:
    plt.scatter(e,Y,c='g',marker='+')
#  for i,txt in enumerate(lFontSize):
    #  plt.annotate(txt,(lFontSize[i],Y+0.0005))
#  plt.scatter(1,1)
#  plt.scatter(2,1)
#  x = np.linspace(0, 2*np.pi, 50)
#  plt.plot(x, np.sin(x))
#  plt.savefig('TestCase')
plt.show()


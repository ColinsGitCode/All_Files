import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 2*np.pi, 50)
#  plt.plot(x, np.sin(x),'r-o', x, np.sin(2*x),'g--')
plt.scatter(x, np.sin(x),'r-o', x, np.sin(2*x),'g--')
#  plt.show()
plt.savefig('PIC.png')

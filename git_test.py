import matplotlib.pyplot as plt
import numpy as np
import warnings
warnings.filterwarnings('ignore')

data=[i for i in range(100)]

s=np.sin(data)

plt.plot(s)
plt.show()

print(s)
print(data)

d=s*0.5*np.pi
print(s)

plt.plot(d,c='r')
plt.show()
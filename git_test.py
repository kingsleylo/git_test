import matplotlib.pyplot as plt
import numpy as np


data=[i for i in range(100)]

s=np.sin(data)

plt.plot(s)
plt.show()
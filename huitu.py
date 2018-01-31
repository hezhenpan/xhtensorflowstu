# *_*coding:utf-8 *_*

import numpy as np
import matplotlib.pyplot as plt

plt.figure(1, dpi=50)
x = np.linspace(-np.pi, np.pi, 100)
plt.plot(x, np.sin(x))
plt.show()

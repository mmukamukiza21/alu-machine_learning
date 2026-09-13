#!/usr/bin/env python3
"""Plot y as a solid red line graph, x-axis ranging from 0 to 10."""
import numpy as np
import matplotlib.pyplot as plt

y = np.arange(0, 11) ** 3

plt.plot(y, 'r-')
plt.xlim(0, 10)
plt.show()

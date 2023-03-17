# Rui Ji
# ITP 449
# HW4
# Q1

import numpy as np
import matplotlib.pyplot as plt

rand_int_x = np.random.randint(1, 201, size=200)  # to generate 1-200 integer we have to use randint
rand_int_y = np.random.randint(1, 201, size=200)  # random.rand will only generate uniform distribution between 0-1

plt.scatter(rand_int_x, rand_int_y, color='red')

plt.xlabel('Random Integer', color='blue')
plt.ylabel('Random Integer', color='blue')
plt.title('Scatter of Random Integers', color='green')

plt.show()

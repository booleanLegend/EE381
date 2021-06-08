# EE 381 Project 4
# Matthew Zaldana 027008928
# 3/22/21 - 3/29/21
# Simulates an exponential rv using the inverse transformation method

import math
import random
import matplotlib.pyplot as plt

n = 100  # Number of repetitions
x = []  # For the uniform rv
y = []  # For the exponential rv
lamda = 1

for i in range(n):
	r = random.uniform(0, 1)
	x.append(r)  # A list of uniformly distributed random numbers
	t = -(1 / lamda) * math.log(1 - r, math.e)
	y.append(t)

b = max(x)
a = min(x)
R = b - a  # This is the range
intervals = int(math.ceil(math.sqrt(n)))  # the number of bins
width = R / intervals  # The class width

plt.subplot(2, 1, 1)
plt.hist(x, intervals, density=width)
plt.subplot(2, 1, 2)
plt.hist(y, intervals, density=width)
plt.show()

import random

M = 8601
A = 4857
N = 10000

for i in range(100):
	print(round(((M * random.random() + A) % N), 4))
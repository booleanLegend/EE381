# Markov Chain
RecLoc = []  # Records the locations of the particle
N = 1000  # Number of steps
import random
p_A = float(input("Enter the probability of leaving '0' and going to '1'."))
p_B = float(input("Enter the probability of leaving '1' and going to '0'."))
S = int(input("Enter either '0' and '1' as starting state."))
RecLoc.append(5)
for i in range(N):
	r = random.uniform(0, 1)
	if S == 0 and r < p_A:
		S = 1
	elif S == 1 and r < p_B:
		S = 0
	RecLoc.append(S)
X = 0
for x in RecLoc:
	X = X + x
print("Percentage in state '1', ", X/N, '.')
print("Percentage in state '0', ", 1-(X/N), '.')
# Birthday problem
P = 1.0
K = 50
for k in range(1, K-1):
	P = P * ((365 - k + 1) / 365)
	print(k, 1-P)
# Poisson
L = float(input("Enter the value of the Poisson parameter."))
N = 25  # Number of probabilities
import math
P = math.exp(-L)
X = [0] # Horizontal axis
Y = [P] # Vertical axis
for i in range(N):
	if i > 0:
		P = P*(L/i) # Recursion
		X.append(i)
		Y.append(P)
	print(i, P)  # Poisson probabilities
import matplotlib.pyplot as plt
plt.plot(X, Y, 'r+')
plt.show()

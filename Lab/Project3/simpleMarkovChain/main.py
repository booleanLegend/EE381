# Name: Matthew Zaldana
# ID #: 027008928
# Date: 3/1/2021 

# Part 1
import random

p = float(input('Enter the probability of success. '))
T = int(input('How many trials?'))

for j in range(T):
    
    r = random.uniform(0,1)
    if r < p:
        print('1', end='')
    else:
        print('0', end='')


# Part 2
RecLoc = [] #Records the locations of the particle
p_A = float(input("\nEnter the probability of leaving '0' and going to '1'."))
q_B = float(input("Enter the probability of leaving '0' and going to '1'."))

S = int(input("Enter either '0' or '1' as a starting state." ))
RecLoc.append(S)

for i in range(24):
    r = random.uniform(0,1)
    
#--------------------------------------------------------
    if S==0 and r < p_A:
        S = 1 #Move to node one.
    elif S==1 and r<q_B:
        S = 0 #Move to node zero.
    RecLoc.append(S)
#--------------------------------------------------------
for i in RecLoc:
    print(i, end='')
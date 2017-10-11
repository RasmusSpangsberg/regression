# This was made for one of the projects in this course:
# https://www.edx.org/course/artificial-intelligence-ai-columbiax-csmm-101x-1

import sys
import matplotlib.pyplot as plt
import numpy as np
import time

#input_file = sys.argv[1]#input1.csv
#output_file = sys.argv[2]#output1.csv
input_file = "input1.csv"
output_file = "output.csv"

file = open(output_file, "w")

data = np.genfromtxt(input_file, delimiter=",")
convergence = False
iterations = 0

def f(x_i):
    s = 0
    for j in range(len(x_i)):
        s += weights[j] * x_i[j]
    if s > 0:
        return 1
    return -1

x = []
y = []

for row in data:
    x.append([1, row[0], row[1]])
    y.append(row[2])

weights = [0] * (len(x[0]))

while not convergence:
    iterations += 1
    old_weights = list(weights)

    print(int(weights[1]), int(weights[2]), ",", int(weights[0]))
    
    for i in range(len(x)):
        if y[i] * f(x[i]) <= 0:
            for j in range(len(weights)):
                weights[j] += y[i] * x[i][j] # update weights

    # plot data
    for row in data:
        if row[2] == 1:
            plt.plot(row[0], row[1], 'ob')
        else:
            plt.plot(row[0], row[1], 'or')

    # plot lines
    xx = np.linspace(0,15)
    yy = (weights[0] + weights[1] * xx) / -weights[2]
    plt.plot(xx,yy)
    plt.pause(1)
        
    if weights == old_weights:
        convergence = True
        
    file.write(str(int(weights[1])) + "," + str(int(weights[2])) +  "," + str(int(weights[0])) + "\n")


file.close()

# setup
plt.xlabel("x")
plt.ylabel("y")
plt.title("Machine Learning")
plt.grid(True)
plt.show()



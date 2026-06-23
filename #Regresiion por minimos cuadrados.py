#Regresiion por minimos cuadrados
import numpy as np


def squared_error(M, t, k):
    sse = 0.0 
    predicted = 0.0
    predicted += (M @ k)
    t = (t - predicted)
    t *= t
    for ti in t:
        sse += ti
    return sse


# data
X = np.array([[66, 5, 15, 2, 500], 
             [21, 3, 50, 1, 100], 
             [120, 15, 5, 2, 1200]])
y = np.array([250000, 60000, 525000])

#  alternative sets of coefficient values
c = np.array([[3000, -200 , -50, 5000, 100], 
             [2000, -250, -100, 150, 250], 
             [3000, -100, -250, 0, 150]])   

def find_best(X, y, c):
    smallest_error = np.inf
    best_index = -1
    for minimo , coeff in enumerate(c):
        sqe = squared_error(X, y, coeff)
        # edit here: calculate the sum of squared error with coefficient set coeff
        # and
        # keep track of the one yielding the smallest squared error
        if sqe < smallest_error:
            smallest_error = sqe
            best_index = minimo
                        
    print("the best set is set %d" % best_index)

find_best(X, y, c)

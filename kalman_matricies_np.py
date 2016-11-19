# Write a function 'filter' that implements a multi-
# dimensional Kalman Filter for the example given

from numpy import matrix
from numpy import linalg


########################################

# Implement the filter function below

def kalman_filter(x, P):
    for n in range(len(measurements)):
        
        # measurement update
        Z = measurements[n]
        y = Z - (H * x)
        S = H * P * H.T + R
        K = P * H.T * S.I
        x = x + (K * y)
        P = (I - (K * H)) * P
        
        # prediction
        x = (F * x) + u
        P = (F * P) * F.T
        
    print 'x= '
    print x
    print 'P= '
    print P

############################################
### use the code below to test your filter!
############################################

measurements = [1, 2, 3]

x = matrix([[0.], [0.]]) # initial state (location and velocity)
P = matrix([[1000., 0.], [0., 1000.]]) # initial uncertainty
u = matrix([[0.], [0.]]) # external motion
F = matrix([[1., 1.], [0, 1.]]) # next state function
H = matrix([[1., 0.]]) # measurement function
R = matrix([[1.]]) # measurement uncertainty
I = matrix([[1., 0.], [0., 1.]]) # identity matrix

kalman_filter(x, P)


# output should be:
# x: [[3.9996664447958645], [0.9999998335552873]]
# P: [[2.3318904241194827, 0.9991676099921091], [0.9991676099921067, 0.49950058263974184]]

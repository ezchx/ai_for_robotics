from numpy import matrix
from numpy import linalg


########################################

def filter(x, P):
    for n in range(len(measurements)):
        
        # prediction
        x = (F * x) + u
        P = F * P * F.T
        
        # measurement update
        Z = measurements[n]
        y = Z.T - (H * x)
        S = H * P * H.T + R
        K = P * H.T * S.I
        x = x + (K * y)
        P = (I - (K * H)) * P
    
    print 'x= '
    print x
    print 'P= '
    print P

########################################

print "### 4-dimensional example ###"

measurements = matrix([[5., 10.], [6., 8.], [7., 6.], [8., 4.], [9., 2.], [10., 0.]])
initial_xy = [4., 12.]

#measurements = [[1., 4.], [6., 0.], [11., -4.], [16., -8.]]
#initial_xy = [-4., 8.]

#measurements = [[1., 17.], [1., 15.], [1., 13.], [1., 11.]]
#initial_xy = [1., 19.]

dt = 0.1

x = matrix([[initial_xy[0]], [initial_xy[1]], [0.], [0.]]) # initial state (location and velocity)
u = matrix([[0.], [0.], [0.], [0.]]) # external motion

#### DO NOT MODIFY ANYTHING ABOVE HERE ####
#### fill this in, remember to use the matrix() function!: ####

P = matrix([[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 1000., 0], [0, 0, 0, 1000.]]) # initial uncertainty: 0 for positions x and y, 1000 for the two velocities DONE
F = matrix([[1., 0, 0.1, 0], [0, 1., 0, 0.1], [0, 0, 1., 0], [0, 0, 0, 1.]]) # next state function: generalize the 2d version to 4d - this was covered in the quiz DONE
H = matrix([[1., 0, 0, 0], [0, 1., 0, 0]]) # measurement function: reflect the fact that we observe x and y but not the two velocities DONE
R = matrix([[0.1, 0], [0, 0.1]]) # measurement uncertainty: use 2x2 matrix with 0.1 as main diagonal DONE
I = matrix([[1., 0, 0, 0], [0, 1., 0, 0], [0, 0, 1., 0], [0, 0, 0, 1.]]) # 4d identity matrix DONE

###### DO NOT MODIFY ANYTHING HERE #######

filter(x, P)

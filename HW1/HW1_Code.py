import numpy as np
import matplotlib.pyplot as plt
lam =1
def dx_dt(x, y, t):
    return -x - 2 + y*(x+1) #lam*(np.cos(np.pi*x/2))**2 *(y - (4/(lam*np.pi))*np.tan(np.pi*x/2) )#x*(1-x-2*y)#y # x*(x**2 + y**2 -1)

def dy_dt(x, y, t):
    return -x*(x+1) # lam*(np.cos(np.pi*y/2))**2 *(x - (4/(lam*np.pi))*np.tan(np.pi*y/2) )#2*y*(x-y)#-x +y*(2-3*x**2 -2*y**2)#y*(x**2 + y**2 -1)

t = np.linspace(0, 10, 1000)
x, y = np.meshgrid(np.linspace(-2, 2, 20), np.linspace(-5, 5, 20))

u, v = np.zeros(x.shape), np.zeros(y.shape)

ni, nj = x.shape
for i in range(ni):
    for j in range(nj):
        x_ = x[i, j]
        y_ = y[i, j]
        u[i, j] = dx_dt(x_, y_, t[0])
        v[i, j] = dy_dt(x_, y_, t[0])

plt.streamplot(x, y, u, v, color='r')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Phase Portrait for lam = 1')
plt.show()

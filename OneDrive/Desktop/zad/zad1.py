import numpy as np
import matplotlib.pyplot as plt
def z(x,y):
    return 2*np.exp(-((y+2)**2)-((x-2)**2)/4)*(np.cos((y**2)/4)+np.cos((3*x**2)/4))-(((y+1)**3)/4+((x+1)**3)/2)*np.exp((-(y+1)**2)/4-(x-1)**2)
def grad(x,y, h=1e-5):
    dfdx=(z(x+h,y)-z(x-h,y))/(2*h)
    dfdy=(z(x,y+h)-z(x,y-h))/(2*h)
    return np.array([dfdx,dfdy])

x,y=0.0,0.0
points=[(x,y)] 
epsilon = 1e-5
max_iter=1000
for i in range(max_iter):
    g=grad(x,y)
    if (np.linalg.norm(g)<epsilon):
        znaleziono=True
        liczba=i+1
        break;
        
    alpha=1.0 
    while z(x-alpha*g[0],y-alpha*g[1])>z(x,y):
        alpha/=2
        if (alpha < 1e-12):
            break;
    x=x-alpha*g[0]
    y=y-alpha*g[1]
    points.append((x,y))

if (znaleziono):
    print(f"znaleziono minimum po {liczba} iteracjach")
z_min=z(x,y)
print(f"\nminimum znaleziono w punkcie ({x:.4f}, {y:.4f})\n")
print(f"\nwartość funkcji w tym punkcie wynosi {z_min:.4f}\n")
x_ax=np.linspace(0,3,200)
y_ax=np.linspace(-3,1,200)
X,Y=np.meshgrid(x_val,y_val)
Z=z(X,Y)
points=np.array(points)
plt.contour(X,Y,Z, levels=35)
plt.plot(points[:,0],points[:,1])
plt.plot(x,y,'bo')
plt.show()
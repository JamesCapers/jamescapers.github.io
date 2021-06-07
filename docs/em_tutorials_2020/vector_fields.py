import numpy as np
import matplotlib.pyplot as plt

xv,yv=np.linspace(-10,10,20),np.linspace(-10,10,20)
Y,X=np.meshgrid(yv,xv)

# Plot the vector field (x, 0)
plt.figure()
plt.title("Vector Field ($x,0$)")
plt.quiver(X,Y,X,0)
plt.xlabel("$x$");plt.ylabel("$y$")

# Plot the vector field (-y, x)
plt.figure()
plt.title("Vector Field ($-y,x$)")
plt.quiver(X,Y,-Y,X)
plt.xlabel("$x$");plt.ylabel("$y$")

# Plot the vector field r rhat
plt.figure()
plt.title("Vector Field r rhat")
r=np.sqrt(X**2 + Y**2)
t=np.arctan2(Y,X)
plt.quiver(X,Y,r*np.cos(t),r*np.sin(t))
plt.xlabel("$x$");plt.ylabel("$y$")

# Plot the vector field 1/r rhat
plt.figure()
plt.title("Vector Field 1/r rhat")
r=np.sqrt(X**2 + Y**2)
t=np.arctan2(Y,X)
plt.quiver(X,Y,(1/r)*np.cos(t),(1/r)*np.sin(t))
plt.xlabel("$x$");plt.ylabel("$y$")

plt.show()

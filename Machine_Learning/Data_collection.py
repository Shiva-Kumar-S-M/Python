# from sklearn.datasets import make_circles
# import matplotlib.pyplot as plt

# X,y=make_circles(n_samples=400,shuffle=True,noise=0.1,random_state=58)
# plt.scatter(X[:,0],X[:,1],c=y)
# plt.show() 

from sklearn.datasets import make_regression 
import matplotlib.pyplot as plt

x,y=make_regression(n_samples=1000,n_features=1,noise=1,random_state=42)
plt.scatter(x,y)
plt.show()
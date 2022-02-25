import math 
import numpy as np 
import matplotlib.pyplot as plt 
 
def sigma(x):
    return 1/(1 + math.exp(-x))

def dsigma(x):
    return sigma(x)*(1 - sigma(x))

varX = np.linspace(-5,5,50)
varY = [sigma(x) for x in varX]
varZ = [dsigma(x) for x in varX]

plt.plot(varX,varY)
plt.plot(varX,varZ)
plt.grid()
plt.legend(["sigma(x)","sigma'(x)"])
plt.show()
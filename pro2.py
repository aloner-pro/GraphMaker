'''
author = @gunjitsinha
'''

import matplotlib.pyplot as plt
import numpy as np

def formalities():
    plt.xlabel('x axis')
    plt.ylabel('y axis')
    plt.grid(True, which='both')
    plt.axhline(y=0, color='k')
    plt.show()
    
def sine():
    x = np.arange(-10, 10, 0.1)
    y = np.sin(x)
    plt.plot(x, y)
    plt.title('Sin')
    formalities()

def cosine():
    x = np.arange(-10, 10, 0.1)
    y = np.cos(x)
    plt.plot(x, y)
    plt.title('Cos')
    formalities()
   

def tangent():
    x = np.arange(-2*np.pi, 2*np.pi, 0.1)
    y = np.tan(x)
    y[:-1][np.diff(y) < 0] = np.nan
    plt.ylim(-3, 3)
    plt.plot(x,y)
    plt.title('Tan')
    formalities()
    

def cotangent():
    x = np.arange(-2 * np.pi, 2 * np.pi, 0.1)
    y = 1/(np.tan(x))
    y[:-1][np.diff(y) > 0] = np.nan
    plt.ylim(-3, 3)
    plt.plot(x, y)
    plt.title('Cot')
    formalities()



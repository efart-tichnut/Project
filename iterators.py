import numpy as np
def sinx_x(x):
    if x == 0:
        return 1
    num=np.sin(x)/x
    return num
def cosx_x(x):
    if x == 0:
        return 1
    num=np.cos(x)/x
    return num
t=list(np.arange(-100,100,0.01))
sinx=list()
cosx=list()
for i in t:
    sinx.append(sinx_x(i))
    cosx.append(cosx_x(i))



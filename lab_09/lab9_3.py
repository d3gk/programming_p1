

import numpy as nmp
import matplotlib.pyplot as mpl

t = nmp.linspace(0, 40 * nmp.pi, 801)

y1 = (nmp.e ** (-0.07 * t)) * nmp.sin(t)
                                    
y2 = 1 - ((nmp.e ** (-0.07 * t)) * nmp.sin(t))             

mpl.plot(t, y1)
mpl.plot(t, y2)
mpl.show()



import numpy as np
import matplotlib.pyplot as plt
from functions_lab import func, gerar_graficos

fs = 10     # Hz
Ts = 1/fs   # s
Tmax = 1    # s
t = np.arange(0,Tmax+Ts,Ts)

y = func(t,phi=0)

gerar_graficos(t, y)
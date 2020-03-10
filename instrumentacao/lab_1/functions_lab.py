import numpy as np
import matplotlib.pyplot as plt

def func_ref(Tmax=1, f=10, t=None, phi = 0):
    T = 1/f
    t = np.arange(0,Tmax,T/100)
    y = np.sin(2*np.pi*f*t + phi) + 0.5*np.sin(2*np.pi*2*f*t + phi)
    return t, y

def func(t, phi=0):
    f = 10
    y = np.sin(2*np.pi*f*t + phi) + 0.5*np.sin(2*np.pi*2*f*t + phi)
    return y

def gerar_graficos(t, y, scatter = True, Tmax = 1, ref=False):
    #plt.plot(tr,yr)
    if scatter:
        plt.plot(t,y,'o', label="meu sinal")
    else:
        plt.plot(t,y, label="meu sinal")

    if ref:
        tr, yr = func_ref(Tmax=Tmax)
        plt.plot(tr,yr, label="referencia")
    plt.ylim(-1.5, 1.5)
    plt.legend(loc="upper left")
    plt.grid()
    plt.show()
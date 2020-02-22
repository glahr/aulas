import control
import matplotlib.pyplot as plt

m = 20  # kg
b = 150  # Ns/m
k = 3000 # N/m

num = [1]
den = [m, b, k]  # ms² + bs + k

FT = control.TransferFunction(num, den)

print(FT)

t, y = control.step_response(FT)

plt.plot(t,y) # abscissa, ordenada
plt.show()

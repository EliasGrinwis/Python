import numpy as np
from matplotlib import pyplot as plt
temperature = np.loadtxt(fname="Files_Chapter_11/temperatures.txt", dtype=int, delimiter=",")

array_days = np.array(temperature[:, 0], str)
array_temperature = np.array(temperature[:, 1])

print(array_days)
print(array_temperature)

plt.plot(array_days, array_temperature)
plt.title("Temperature measurements C°")
plt.xlabel("Days")
plt.ylabel("Temperatures")
plt.xticks(rotation=90)

plt.show()

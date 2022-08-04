import matplotlib.pyplot as plt
import numpy as np

y = np.array([15, 30, 45, 10])
my_labels = ["Cricket", "Football", "Hockey", "Formula1"]
my_colors = ["red", "yellow", "green", "blue"]

plt.title("Sports")

plt.pie(y, labels=my_labels, colors=my_colors, autopct="%.1f%%")
plt.show()

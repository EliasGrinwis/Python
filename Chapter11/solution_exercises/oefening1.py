import numpy as np

loaded_data = np.loadtxt(fname="Files_Chapter_11/student_grades_3.csv", delimiter=";", dtype=int, skiprows=1)

print("Grades analysis Python:")
print("max", np.max(loaded_data, axis=0)[0], "\t", "min", np.min(loaded_data, axis=0)[0], "\t", "mean", np.mean(loaded_data, axis=0)[0])

print("Grades analysis Linux:")
print("max", np.max(loaded_data, axis=0)[1], "\t", "min", np.min(loaded_data, axis=0)[1], "\t", "mean", np.mean(loaded_data, axis=0)[1])

print("Grades analysis Routing & Switching:")
print("max", np.max(loaded_data, axis=0)[2], "\t", "min", np.min(loaded_data, axis=0)[2], "\t", "mean", np.mean(loaded_data, axis=0)[2])

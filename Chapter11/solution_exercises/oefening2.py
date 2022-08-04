import numpy as np

points_python = np.genfromtxt(fname="Files_Chapter_11/points_python.txt", delimiter=";", dtype=int, filling_values="0")
#print(points_python)

points_networks = np.genfromtxt(fname="Files_Chapter_11/points_networks.csv", delimiter=";", dtype=int, filling_values="0")
#print(points_networks)

points_web = np.genfromtxt(fname="Files_Chapter_11/points_web.txt", delimiter=";", dtype=int, filling_values="0")
#print(points_web)

points_linux = np.genfromtxt(fname="Files_Chapter_11/points_linux.csv", delimiter=";", dtype=int, filling_values="0")
#print(points_linux)

total_array = (points_python + points_networks + points_web + points_linux) / 4
total_array[:, 1] *= 5
#print(total_array)

exam_results = "November 2021 Exam results:"
print(exam_results)
print("-" * len(exam_results))
print("The highest score this exam period is:", str(np.max(total_array, axis=0)[1]) + "%")
print("The lowest score this exam period is:", str(np.min(total_array, axis=0)[1]) + "%")

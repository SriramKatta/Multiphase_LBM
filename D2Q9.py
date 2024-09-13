import numpy as np

ni = 9
ei = np.arange(ni)
exs = np.array([0, 1, 0,-1, 0, 1,-1,-1, 1])
eys = np.array([0, 0, 1, 0,-1, 1, 1,-1,-1])
ws = np.array([4/9, 1/9, 1/9, 1/9, 1/9, 1/36, 1/36, 1/36, 1/36])
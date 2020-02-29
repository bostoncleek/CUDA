import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


def plot(obstacles, graph):
	fig, ax = plt.subplots()
	plt.plot()
	plt.xlim((0,11))
	plt.ylim((0,11))

	for i in range(obstacles.shape[0]):
		circ = obstacles.iloc[i, :].to_numpy()
		circle = plt.Circle((circ[0],circ[1]), circ[2], color='k')
		ax.add_artist(circle)

	for i in range(graph.shape[0]):
		edge = graph.iloc[i, :].to_numpy()
		if (edge[-1] == -1): #root case
			plt.scatter(edge[0], edge[1], color='yellow', marker='X')
		elif (edge[-1] == 1): #goal case
			plt.scatter(edge[0], edge[1], color='red', marker='P')
		else:
			plt.plot([edge[0], edge[1]],[edge[2], edge[3]], '-ob')


def main():
	obstacles = pd.read_csv("rrtout/obstacles.csv", header = None, index_col = False)
	print(obstacles)
	graph = pd.read_csv("rrtout/graph.csv", header = None, index_col = False)
	print(graph)
	plot(obstacles, graph)
	# print(obstacles.shape[0])
	# graph = pd.read_csv("rrtout/graph.csv")


if __name__ == '__main__':
	main()
	plt.show()

import math

from aco import ACO, Graph
from plot import plot
import matplotlib.pyplot as plt

def distance(city1: dict, city2: dict):
    return math.sqrt((city1['x'] - city2['x']) ** 2 + (city1['y'] - city2['y']) ** 2)


def run(num_cities):
    cities = []
    points = []
    with open('./data/chn31.txt') as f:
        counter = 0
        for line in f.readlines():
            if counter< num_cities:
                city = line.split(' ')
                cities.append(dict(index=int(city[0]), x=int(city[1]), y=int(city[2])))
                points.append((int(city[1]), int(city[2])))
                counter +=1
    cost_matrix = []
    rank = len(cities)
    for i in range(rank):
        row = []
        for j in range(rank):
            row.append(distance(cities[i], cities[j]))
        cost_matrix.append(row)
    aco = ACO(10, 100, 1.0, 10.0, 0.5, 10, 2)
    graph = Graph(cost_matrix, rank)
    path, cost = aco.solve(graph)
    print('number cities: {},cost: {}, path: {}'.format(num_cities,cost, path))
    plot(points, path)
    return path,cost

ans = []
for i in range(5,51):
    ans.append(run(i))
plt.show()

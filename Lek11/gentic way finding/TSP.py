"""
Created on Wed Mar 3 16:39:18 2021
@author: Sila
"""

# Gettting started methods for TSP GA algorithm
# - Read cities from file
#

import pandas as pd
import random
import math

data = pd.read_csv('TSPcities1000.txt', sep='\s+', header=None)
data = pd.DataFrame(data)

import matplotlib.pyplot as plt

x = data[1]
y = data[2]
plt.plot(x, y, 'r.')
plt.show()


def createRandomRoute():
    tour = [[i] for i in range(1000)]
    print(tour)
    random.shuffle(tour)
    return tour


# plot the tour - Adjust range 0..len, if you want to plot only a part of the tour.
def plotCityRoute(route):
    for i in range(0, len(route)):
        plt.plot(x[i:i + 2], y[i:i + 2], 'ro-')
    plt.show()


# Alternativ kode:
#  for i in range(0, len(route)-1):              
#     plt.plot([x[route[i]],x[route[i+1]]], [y[route[i]],y[route[i+1]]], 'ro-')

tour = createRandomRoute()
plotCityRoute(tour)


# calculate distance between cities
def distancebetweenCities(city1x, city1y, city2x, city2y):
    xDistance = abs(city1x - city2x)
    yDistance = abs(city1y - city2y)
    distance = math.sqrt((xDistance * xDistance) + (yDistance * yDistance))
    return distance


def costFunction():
    cost = 0
    for i in range(1, len(x)):
        cost += distancebetweenCities(x[i - 1], y[i - 1], x[i], y[i])
    return cost


# distance between city number 100 and city number 105
dist = distancebetweenCities(x[100], y[100], x[105], y[105])
print('Distance, % target: ', dist)

best_score_progress = []  # Tracks progress

# replace with your own calculations
fitness_gen0 = costFunction()  # replace with your value
print('Starting best score, % target: ', fitness_gen0)

best_score = fitness_gen0
# Add starting best score to progress tracker
best_score_progress.append(best_score)


# Here comes your GA program...
# def generate_population():


def fill_with_parent1_genes(child, parent, genes_n):
    start_at = random.randint(0, len(parent.genes) - genes_n - 1)
    finish_at = start_at + genes_n
    for i in range(start_at, finish_at):
        child.genes[i] = parent.genes[i]


def fill_with_parent2_genes(child, parent):
    j = 0
    for i in range(0, len(parent.genes)):
        if child.genes[i] is None:
            while parent.genes[j] in child.genes:
                j += 1
            child.genes[i] = parent.genes[j]
            j += 1


best_score = 980
best_score_progress.append(best_score)
best_score = 960
best_score_progress.append(best_score)

# GA has completed required generation
print('End best score, % target: ', best_score)

plt.plot(best_score_progress)
plt.xlabel('Generation')
plt.ylabel('Best Fitness - route length - in Generation')
plt.show()

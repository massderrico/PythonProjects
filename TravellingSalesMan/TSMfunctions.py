
# coordinates of cites (list of x coor and list of y coord)
# func that calculates the distance from one city to another
# func that reapeats it N factorials amount of times.
import itertools
import random as rnd
import math
import time
import matplotlib.pyplot as plt
import numpy as np

 #the number of cities to be generated

nearneigh_citynum= []
nearneigh_times = []
nearneigh_shortest_dist_list = []
brute_times=[]
brute_citynum = []
brute_shortest_dist_list = []


def create_x(city):#funtion generates a list of random x values for cites
    x = []
    for i in range (0,city):
        ran_x = rnd.randint(0, 1000)
        x.append(ran_x)
    return x

def create_y(city): #funtion generates a list of random y values for cites
    y = []
    for i in range (0,city):
        ran_y = rnd.randint(0, 1000)
        y.append(ran_y)
    return y

def calcDist(x1,x2,y1,y2):
    dist = (math.sqrt((x1-x2)**2+(y1-y2)**2))
    return dist

class Algo()
    def brute_force_alg(city, x_list,y_list):
        brute_distances = []
        i = 0
        x_perm = list(itertools.permutations(x_list))#generate a list with all permutations(all the different paths) for the x values 'note: each element in this list is a tuple'
        y_perm = list(itertools.permutations(y_list))#generate a list with all permutations(all the different paths) for the y values

        while i < math.factorial(city):
            total_dist = 0
            x_tour = []
            y_tour = []
            x_dist = x_perm[i] #takes one element(a tuple) from the x list and sets an an individual element
            y_dist = y_perm[i] #same as ^^^^ except for the y_list

            for k in range(0,city):
                x_tour.append(x_dist[k]) #takes each element in the tuple and appends it to a list
                y_tour.append(y_dist[k])
            x_tour.append(x_dist[0]) # adds the first element of the list to the end to complete the tour
            y_tour.append(y_dist[0])

            for j in range(0,city): #
                dist = calcDist(x_tour[j],x_tour[j+1],y_tour[j] ,y_tour[j+1]) #finds the distance from from one point to another
                total_dist += dist #adds the distance from one point to another to the total distance
            brute_distances.append(total_dist)
            i += 1
        shortest_brute = min(brute_distances)
        return shortest_brute

    def nearest_neigh_alg(city, x_list,y_list):
        nn_distances = []
        z = 0
        while (z < city): # the coordinates of the starting city has the index z
            unvisited_x= []
            unvisited_y = []
            visited_x= []
            visited_y = []
            total_distance = 0

            for i in range(0,city):
                if i != z:
                    unvisited_x.append(x_list[i])  #creates an x and y list with the coordinates with all the unvisited cities
                    unvisited_y.append(y_list[i])
                else:
                    visited_x.append(x_list[i])    #creates an x and y list with the coordinates of the starting city
                    visited_y.append(y_list[i])
            i = 0
            while i < (city-1):
                potential_paths = []

                for j in range(0,len(unvisited_x)): #find the distances from the starting to all the unvisited cities
                    dist= calcDist(unvisited_x[j],visited_x[-1],unvisited_y[j],visited_y[-1])
                    potential_paths.append(dist)           #appends the distances to a list

                shortest_path = min(potential_paths) #find the shortest distance in the list "potential_paths"
                total_distance += shortest_path                 #adds the shortest path to the total distace
                index_short = potential_paths.index(shortest_path)
                visited_x.append(unvisited_x[index_short]) #adds the city with the shortest distance to the visited city list(this sets it as the new starting city)
                visited_y.append(unvisited_y[index_short]) #
                unvisited_x.pop(index_short)  #revoves the
                unvisited_y.pop(index_short)  #
                i += 1

            last_dist = calcDist(visited_x[0], visited_x[-1], visited_y[0], visited_y[-1]) #finds the distance from the last visited city to the first city
            total_distance += last_dist  # adds the last distance to the total distance to complete the tour
            nn_distances.append(total_distance)
            z+=1

        shortest_nn = min(nn_distances) #return the shortest path for the nearest neighbor algorithm
        return shortest_nn


num_of_city = 150 #max number of cities to compute
for i in range(3,(num_of_city+1)):
    x_val = create_x(i) #creates a list of x and y values
    y_val = create_y(i)

    start_time_nn = time.time() #sets the start time
    shortest_dist_nn =nearest_neigh_alg(i, x_val, y_val)
    nn_time_to_complete = ((time.time() - start_time_nn))  #find the execution time of the nearest neighbor algorithm(in seconds)
    nearneigh_times.append(nn_time_to_complete)  # appends the times to a list
    nearneigh_shortest_dist_list.append(shortest_dist_nn) #appends distances calculated by the nearest neighbor algorithm to a list
    nearneigh_citynum.append(i) #appends the number of cities used to a list

    if i < 10:  # this loop limit the number of cities used by the brute force algorithm to 9 because it cannot compute more than 9 cites
        start_time_brute = time.time()
        shortest_dist_brute = brute_force_alg(i, x_val, y_val)
        brute_time_to_complete = ((time.time() - start_time_brute))#finds the execution time of the nearest brute force algorithm (in seconds)
        brute_times.append(brute_time_to_complete) # appends the times to a list
        brute_shortest_dist_list.append(shortest_dist_brute)#appends distances calculated by the brute force algorithm to a list
        brute_citynum.append(i) #appends the number of cities used to a list
    else:
        pass

"""Setting up the bar graph"""

# Plots the distances calculated by both algorithms in a bar graph

def round_func(list_to_round): #this function is used to round the distances for the bar graph so that it looks better
    rounded_list=[]
    for i in list_to_round:
        rounded_num = round(i,2)
        rounded_list.append(rounded_num)
    return rounded_list

nearneigh_shortest_dist_list_mod = nearneigh_shortest_dist_list[0:len(brute_shortest_dist_list)]
x = np.arange(len(brute_citynum))  # the label locations
width = 0.45  # the width of the bars
fig, ax = plt.subplots(2, figsize=(10,7),)
rects1 = ax[0].bar(x - width/2, round_func(brute_shortest_dist_list), width, label='Brute force')
rects2 = ax[0].bar(x + width/2, round_func(nearneigh_shortest_dist_list_mod), width, label='Nearest neighbor')

ax[0].set_xlabel("Number of Cities")
ax[0].set_ylabel('Distances')
ax[0].set_title('Distances calculated by BF and NN algorithm')
ax[0].set_xticks(x)
ax[0].set_xticklabels(brute_citynum)
ax[0].legend(loc= "upper left", facecolor= "#FFFFFF")

def autolabel(rects):
    for rect in rects:
        height = rect.get_height()
        text = ax[0].annotate('{}'.format(height),
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 0),  # 3 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom')
        text.set_fontsize(6)

autolabel(rects1)
autolabel(rects2)
fig.tight_layout()

"""Setting up the line graph"""
#plots the runtime vs the number of cites for both algorithms

ax[1].plot(brute_citynum, brute_times, label='Brute Force')
ax[1].plot(nearneigh_citynum, nearneigh_times , label= 'Nearest Neighbor')
x_axis = []
for i in range(5,num_of_city+1,5):
    x_axis.append(i)
ax[1].set_xticks(x_axis)
ax[1].set_xlabel('Number of Cities')
ax[1].set_ylabel('Time to Compute(in seconds)')
ax[1].set_title("Code Execution Time Comparison of BF and NN algorithms")
ax[1].legend()
plt.show()


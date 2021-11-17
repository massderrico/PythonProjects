

from TSM import calcDist,create_x,create_y
import time

initialcity_x = 0
initialcity_y = 0


x = [2,9,5,10,65]
y= [1,34,5,7,50]

def shortest_dist(a_list): #returns the shortest distance in a list
    short_dist = (min(a_list))
    return short_dist


def shortest_dist_index(a_list): #returns the index of the shortest distance in a list
    index_short = a_list.index((min(a_list)))
    return index_short




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
        total_distance += last_dist  # add the distance to the total distance to complete the tour
        nn_distances.append(total_distance)
        z+=1
    print(visited_x, visited_y)
    print(nn_distances)
    shortest_nn = min(nn_distances)
    print(shortest_nn)


f = 5
start_time = time.time()
nearest_neigh_alg(f,create_x(f),create_y(f))
time_to complete = (time.time() - start_time)


class Algo():
    def __init__(self):
        

city_num = 100
x_axis = []
for i in range(0,city_num+1,2):
    x_axis.append(i)

print(x_axis)
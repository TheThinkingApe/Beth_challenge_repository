# CHALLENGE PROBLEMS
# YOU MAY NOT USE ANY ADDITIONAL LIBRARIES OR PACKAGES TO COMPLETE THIS CHALLENGE

# Divvy is Chicago's bike share system, which consists of almost 600 stations scattered
# around the city with blue bikes available for anyone to rent. Users begin a ride by removing
# a bike from a dock, and then they can end their ride by returning the bike to a dock at any Divvy 
# station in the city. You are going to use real data from Divvy collected at 1:30pm on 4/7/2020 
# to analyze supply and demand for bikes in the system. 

# NOTE ** if you aren't able to run this, type "pip install json" into your command line
import json

# do not delete; this is the data you'll be working with
divvy_stations = json.loads(open('C:/Users/bethk/Desktop/Programming/Harris-Challenge-1/divvy_stations.txt').read())

# PROBLEM 1
# find average number of empty docks (num_docks_available) and 
# available bikes (num_bikes_available) at all stations in the system

    # Make list out of values for the same key in all the dictionaries in divvy_stations
availabikes = []
for number in range(len(divvy_stations)):
    x = divvy_stations[number]['num_bikes_available']
    availabikes.append(x)
availadocks = []
for number in range(len(divvy_stations)):
    x = divvy_stations[number]['num_docks_available']
    availadocks.append(x)
   # Take averages and round to the nearest 2 decimal points
availabikes_avg = round(sum(availabikes)/len(availabikes), 2)
availadocks_avg = round(sum(availadocks)/len(availadocks), 2)
    # Print result
print('The average number of available bikes is {} and the average number of empty docks is {}.'.format(availabikes_avg, availadocks_avg))


# PROBLEM 2
# find ratio of bikes that are currently rented to total bikes in the system (ignore ebikes)

rented_over_total = round(sum(availadocks)/(sum(availadocks)+sum(availabikes)), 2)
print('The ratio of currently rented bikes to total bikes in the system is {}.'.format(rented_over_total))


# PROBLEM 3 
# Add a new variable for each divvy station's entry, "percent_bikes_remaining", that shows 
# the percentage of bikes available at each individual station (again ignore ebikes). 
# This variable should be formatted as a percentage rounded to 2 decimal places, e.g. 66.67%

percent_bikes_remaining = []
for number in range(0,len(divvy_stations)):
    bikes = divvy_stations[number]['num_bikes_available']
    docks = divvy_stations[number]['num_docks_available']
    total = bikes + docks
    ratio = bikes/total
    ratio100 = round(ratio*100, 2)
    percent = str(ratio100)+'%'
    percent_bikes_remaining.append(percent)
    divvy_stations[number]['percent_bikes_remaining'] = percent_bikes_remaining[number] 

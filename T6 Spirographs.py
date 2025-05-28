# Importing the relevant modules
from matplotlib import pyplot as plt
import tkinter as tk
import math
from numpy import *

# Data
planets = [
    # ['Planet', Semi-Major Axis, Semi-Minor Axis, Orbital Periods]
    ['Mercury', 0.387, 0.37870, 0.241],
    ['Venus', 0.723, 0.72298, 0.615],
    ['Earth', 1.00, 0.99986, 1.000],
    ['Mars', 1.523, 1.51740, 1.881],
    ['Jupiter', 5.20, 5.19820, 11.859],
    ['Saturn', 9.58, 9.56730, 29.428],
    ['Uranus', 19.29, 19.19770, 83.760],
    ['Neptune', 30.25, 30.10870, 163.746],
    ['Pluto', 39.51, 39.482, 247.974]
]

# Functions

def eccentricity_calc(s_major, s_minor): # Calculates the Eccentricity of the Ellipse
    s_minor = s_minor ** 2
    s_major = s_major ** 2
    ecc = (1 - s_minor/s_major) ** 0.5
    del s_major, s_minor
    return(ecc)


eccentricity_of_ellipse = [] # Calculating all Eccentricities

for planet in range(len(planets)):
    ecc_temp = eccentricity_calc(planets[planet][1], planets[planet][2])
    eccentricity_of_ellipse.append(ecc_temp)
    del ecc_temp



def planet_ylimit(chosen_planets): # Defining Graph Y-Axis Limit
    temp_list = []
    for i in range(len(chosen_planets)):
        temp_list.append(planets[chosen_planets[i]][2])
    return(max(temp_list))

def planet_xlimit(chosen_planets): # Defining Graph X-Axis Limit
    temp_list = []
    for i in range(len(chosen_planets)):
        temp_list.append(planets[chosen_planets[i]][1])
        pl = i
    return([max(temp_list), pl])

## Plotting Both Axis

# Constant/Fixed Sun 
Sun=[0]
plt.plot(Sun, c= "Yellow", marker="o")

chosen_planets = []

for i in range(2): # Loop for choosing planets
    allow = False
    while allow == False:
        try:
            chosen_p = int(input("Choose Planets: ")) -1
            allow = True
        except:
            print("Please Try Again.")
    chosen_planets.append(chosen_p)
    del chosen_p

planet1 = chosen_planets[0]
planet2 = chosen_planets[1]

# Ellipses of Chosen Planets
for i in range(len(chosen_planets)): # Plotting orbits normally
    cur_t = linspace(0, 360, 180)
    x = planets[chosen_planets[i]][1] * cos(radians(cur_t)) + eccentricity_of_ellipse[chosen_planets[i]]
    y = planets[chosen_planets[i]][2] * sin(radians(cur_t))

    plt.plot(x,y, label=planets[chosen_planets[i]][0])
    del cur_t


for theta in range(360): # Creating Spyrograph
    
    xvalue = []
    yvalue = []

    x = planets[planet1][1] * cos(theta / planets[planet1][3]) + eccentricity_of_ellipse[planet1]
    y = planets[planet1][2] * sin(theta / planets[planet1][3])

    x2 = planets[planet2][1] * cos(theta / planets[planet2][3]) + eccentricity_of_ellipse[planet2]
    y2 = planets[planet2][2] * sin(theta / planets[planet2][3])
    if planet1 >= 6 or planet2 >= 6:
        if theta % 3 == False:
            theta -= 2

    xvalue.append(x)
    xvalue.append(x2)
    yvalue.append(y)
    yvalue.append(y2)
    plt.plot(xvalue, yvalue, color='black', linewidth=0.3)


# Defining Graph Limits
ylimit = planet_ylimit(chosen_planets)
xlimit = planet_xlimit(chosen_planets)

plt.xlim(-xlimit[0], xlimit[0] + eccentricity_of_ellipse[chosen_planets[xlimit[1]]])
plt.ylim(-ylimit, ylimit)


# Plotting Info & Misc

plt.xlabel('x/AU')
plt.ylabel('y/AU')
plt.title(f'Spyrograph of {planets[planet1][0]}, and {planets[planet2][0]}')
plt.legend()
plt.grid()

# Making Graph Circular 
fig = plt.gcf()
fig.gca().set_aspect('equal')

# Displaying Graph
plt.show()
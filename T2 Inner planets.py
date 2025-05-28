# Importing the relevant modules
from matplotlib import pyplot as plt, animation as  anim
from functools import partial
import math
from numpy import *
# Data

planets = [
    # ['Planet', Semi-Major Axis, Semi-Minor Axis, Tilts, Orbital Frequencies]
    ['Mercury', 0.387, 0.37870, 7.00, 6],
    ['Venus', 0.723, 0.72298, 3.39, 3],
    ['Earth', 1.00, 0.99986, 0.00, 2],
    ['Mars', 1.523, 1.51740, 1.85, 1],
    ['Jupiter', 5.20, 5.19820, 1.31, 0.9],
    ['Saturn', 9.58, 9.56730, 2.49, 0.5],
    ['Uranus', 19.29, 19.19770, 0.77, 0.3],
    ['Neptune', 30.25, 30.10870, 1.77, 0.7],
    ['Pluto', 39.51, 39.482, 17.5, 0.9]
]
# Calculations

# Functions
def eccentricity_calc(s_major, s_minor): # Calculates the Eccentricity of the Ellipse
    s_minor = s_minor ** 2
    s_major = s_major ** 2
    ecc = (1 - s_minor/s_major) ** 0.5
    return(ecc)

eccentricity_of_ellipse = [] # Calculating all Eccentricities
for planet in range(len(planets)):
    ecc_temp = eccentricity_calc(planets[planet][1], planets[planet][2])
    eccentricity_of_ellipse.append(ecc_temp)

def planet_ylimit(): # Defining Graph Y-Axis Limit
    temp_list = []
    for i in range(0, 4):
        temp_list.append(planets[i][2])
    return(max(temp_list))

def planet_xlimit(): # Defining Graph X-Axis Limit
    temp_list = []
    for i in range(0, 4):
        temp_list.append(planets[i][1])
        planet = i
    return([max(temp_list), i])



## Defining Figure
fig, ax = plt.subplots()

# Constant/Fixed Sun 
Sun=[0]
plt.plot(Sun, c="orange", marker="o", markersize=10)  # Star marker

# Ellipses of planets
for planet in range(0, 4):
    t = linspace(0, 360, 180) # Start point of revolution, End point, Num of points
    x = planets[planet][1] * cos(radians(t)) + eccentricity_of_ellipse[planet]
    y = planets[planet][2] * sin(radians(t))
    plt.plot(x,y, label=planets[planet][0])

plt.plot(width = 2, edgecolor="black")
point = []
point.append(x[0])
point.append(y[0])
pointb = [0,0]

# Defining Graph Limits
ylimit = planet_ylimit()
xlimit = planet_xlimit()

# Plotting Graph Limits

plt.ylim(-ylimit, ylimit)
plt.xlim(- (xlimit[0] - eccentricity_of_ellipse[xlimit[1]]), xlimit[0] + eccentricity_of_ellipse[xlimit[1]])

# Plotting Info & Misc
plt.xlabel('x/AU')
plt.ylabel('y/AU')
plt.title('Solar System')
plt.legend()
plt.grid()
plt.show()
from matplotlib import pyplot as plt, animation as  anim
import matplotlib
from functools import partial
import math
from numpy import *
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.animation import FuncAnimation
print(plt.style.available)
print("____")
print(matplotlib.get_configdir())
plt.style.use('classic')

# Data

planets = [
    # ['Planet', Semi-Major Axis, Semi-Minor Axis, Tilts, Orbital Periods]
    ['Mercury', 0.387, 0.37870, 7.00, 0.2],
    ['Venus', 0.723, 0.72298, 3.39, 0.6],
    ['Earth', 1.00, 0.99986, 0.00, 1],
    ['Mars', 1.523, 1.51740, 1.85, 1.9],
    ['Jupiter', 5.20, 5.19820, 1.31, 11.9],
    ['Saturn', 9.58, 9.56730, 2.49, 29.4],
    ['Uranus', 19.29, 19.19770, 0.77, 83.8],
    ['Neptune', 30.25, 30.10870, 1.77, 163.7],
    ['Pluto', 39.51, 39.482, 17.5, 248]
]
# Calculations

# Functions
def eccentricity_calc(s_major, s_minor): # Calculates the Eccentricity of the Ellipse
    s_minor = s_minor ** 2
    s_major = s_major ** 2
    ecc = (1 - s_minor/s_major) ** 0.5
    return(ecc)

def polar_equation_ellipse_calc(planet, theta): # Self explanatory
    from math import cos
    semi_major = planets[planet][1]
    ecc = eccentricity_of_ellipse[planet]
    top_eq = semi_major * (1 - (ecc ** 2))
    bottom_eq = 1 - (ecc * cos(theta))

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
eccentricity_of_ellipse = [] # Calculating all Eccentricities
for planet in range(len(planets)):
    ecc_temp = eccentricity_calc(planets[planet][1], planets[planet][2])
    eccentricity_of_ellipse.append(ecc_temp)

#ax = plt.figure().add_subplot(projection='3d')


fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

plt.plot(0, 0, 1, c='yellow', marker='o', markersize=10)
"""  
t = linspace(0, 360, 180) # Start point of revolution, End point, Num of points
orbit_dot = array([planets[planet][1] * cos(radians(t)) + eccentricity_of_ellipse[planet]*cos(radians(planets[planet][3])),
                    planets[planet][2] * sin(radians(t)),
                    (planets[planet][1] * cos(radians(t)) + eccentricity_of_ellipse[planet]*cos(radians(planets[planet][3])))*sin(radians(planets[planet][3]))+1
                    ])

"""

dotting = []
for planet in range(5, 9):
    t = linspace(0, 360, 18000) # Start point of revolution, End point, Num of points
    orbit_dot = array([planets[planet][1] * cos(radians(t)) + eccentricity_of_ellipse[planet]*cos(radians(planets[planet][3])),
                       planets[planet][2] * sin(radians(t)),
                       (planets[planet][1] * cos(radians(t)) + eccentricity_of_ellipse[planet]*cos(radians(planets[planet][3])))*sin(radians(planets[planet][3]))+1
                        ])
    dotting.append(orbit_dot)
    orbit_dot_plot, = ax.plot(*orbit_dot, label=planets[planet][0])

    #ax.plot(x, y, z, label=planets[planet][0])

#ax.set_facecolor('black')#ax.grid(False)
ax.xaxis.pane.fill = False
ax.yaxis.pane.fill = False
ax.zaxis.pane.fill = False

#ylimit = planet_ylimit()
#xlimit = planet_xlimit()

#ax.set_xlim(- (xlimit[0] - eccentricity_of_ellipse[xlimit[1]]), xlimit[0] + eccentricity_of_ellipse[xlimit[1]])
#ax.set_ylim(-ylimit, ylimit)

ax.set_xlim(-40, 50)
ax.set_ylim(-40, 40)
ax.set_zlim(-20, 20)

# Planet Artist
ani_planets = []
ani_planet1, = plt.plot([], [], [], marker='o')
ani_planet2, = plt.plot([], [], [], marker='o')
ani_planet3, = plt.plot([], [], [], marker='o')
ani_planet4, = plt.plot([], [], [], marker='o')
ani_planet5, = plt.plot([], [], [], marker='o')
ani_planet6, = plt.plot([], [], [], marker='o')
ani_planet7, = plt.plot([], [], [], marker='o')
ani_planet8, = plt.plot([], [], [], marker='o')
ani_planet9, = plt.plot([], [], [], marker='o')
orbits = [ani_planet1, ani_planet2, ani_planet3, ani_planet4, ani_planet5, ani_planet6, ani_planet7, ani_planet8, ani_planet9]
"""
def update(i, planet):
    theta = deg2rad(i)
    x = planets[planet][1] * cos(radians(theta)) + eccentricity_of_ellipse[planet]
    y = planets[planet][2] * sin(radians(theta))
    x = x*cos(radians(planets[planet][3]))
    z = x*sin(radians(planets[planet][3]))+1
    orbits[i].set_data(x, y)
    orbits[i].set_3d_properties(z)
#an1 = anim.FuncAnimation(ax, partial(update, planet=6), frames=1080, interval=1)

"""
def update(frame):
    for planet in range(5, 9):
        orbitalperiods = planets[planet][4] / 365.2
        x = planets[planet][1] * cos(radians(frame / orbitalperiods)) + eccentricity_of_ellipse[planet]*cos(radians(planets[planet][3]))
        y = planets[planet][2] * sin(radians(frame / orbitalperiods))
        z = x*sin(radians(planets[planet][3]))+1
        orbits[planet].set_data(x, y)
        orbits[planet].set_3d_properties(z)

orbit_marker, = ax.plot([orbit_dot[0, 0]], [orbit_dot[1, 0]], [orbit_dot[2, 0]], marker='o')
ani = FuncAnimation(fig, partial(update), frames=len(t), interval = 0)
an1 = anim.FuncAnimation(fig, partial(update), frames=1080, interval = 0)

ax.set_xlabel("x/AU")
ax.set_ylabel("y/AU")
ax.set_zlabel("z/AU")
ax.legend()
plt.show()
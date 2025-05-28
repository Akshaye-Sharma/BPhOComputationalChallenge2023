from matplotlib import pyplot as plt, animation as  anim
from numpy import *

# Data
planets = [
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

# Calculations
def eccentricity_calc(s_major, s_minor): # Calculates the Eccentricity of the Ellipse
    s_minor = s_minor ** 2
    s_major = s_major ** 2
    ecc = (1 - s_minor/s_major) ** 0.5
    return(ecc)

def planet_ylimit(): # Defining Graph Y-Axis Limit
    temp_list = []
    for i in range(0, 4):
        temp_list.append(planets[i][2])
    return(max(temp_list))

def planet_xlimit(): # Defining Graph X-Axis Limit
    temp_list = []
    for i in range(0, 4):
        temp_list.append(planets[i][1])
    return([max(temp_list), i])

eccentricity_of_ellipse = [] # Calculating all Eccentricities
for planet in range(len(planets)):
    ecc_temp = eccentricity_calc(planets[planet][1], planets[planet][2])
    eccentricity_of_ellipse.append(ecc_temp)


## Defining Figure
fig, ax = plt.subplots()

# Constant/Fixed Sun 
Sun=[0]
plt.plot(Sun, c= "orange", marker="o", markersize=10)

# Ellipses of First 5 Planets
for planet in range(0, 4):
    t = linspace(0, 360, 180) # Start point of revolution, End point, Num of points
    x = planets[planet][1] * cos(radians(t)) + eccentricity_of_ellipse[planet]
    y = planets[planet][2] * sin(radians(t))
    plt.plot(x,y, label=planets[planet][0])

plt.plot(width = 2, edgecolor="black")

# Defining Graph Limits
ylimit = planet_ylimit()
xlimit = planet_xlimit()

# Plotting Graph Limits
plt.ylim(-ylimit, ylimit)
plt.xlim(- (xlimit[0] - eccentricity_of_ellipse[xlimit[1]]), xlimit[0] + eccentricity_of_ellipse[xlimit[1]])

# Planet Artist
orbits = []
for _ in range(4):
    planet_dot, = plt.plot([], [], marker='o')
    orbits.append(planet_dot)

# Animation Function
def update(frame):
    theta = deg2rad(frame)
    for idx in range(4):  # Animate first 4 planets
        x = planets[idx][1] * cos(theta / planets[idx][3]) + eccentricity_of_ellipse[idx]
        y = planets[idx][2] * sin(theta / planets[idx][3])
        orbits[idx].set_data([x], [y])

    return orbits

# Animation
an1 = anim.FuncAnimation(fig, update, frames=1080, interval=30, blit=True)

# Plotting Info & Misc
plt.xlabel('x/AU')
plt.ylabel('y/AU')
plt.title('Solar System')
plt.legend()
plt.grid()
plt.show()
# Importing the relevant modules
import matplotlib.pyplot as plt

# Data
planets = ['Earth', 'Mercury', 'Venus', 'Mars', 'Pluto', 'Neptune', 'Jupiter', 'Uranus', 'Saturn']
sunDistanceAU = [1.00, 0.387, 0.723, 1.523, 39.51, 30.25, 5.20, 19.29, 9.58]

orbitalperiodYears = [1.00, 0.24, 0.62, 1.88, 248.35, 166.34, 11.86, 84.75, 29.63]
#sunDistanceAU = [23, 16, 38, 37, 29, 19, 16, 13, 9]

# orbitalperiodYears = [-0.4, -46.4, 45.6, 17.9, 9, -18.7, -28.1, -37, -9.3]
# Calculating semi major axis cube and orbital period squared

sunAUCube = []
for i in range(len(planets)):
   value = sunDistanceAU[i]
   value = value ** (3/2)
   sunAUCube.append(value)

# Plotting both axes

plt.plot(sunAUCube, orbitalperiodYears, label = 'Keplar\'s III law relationship', color="red")
plt.plot(sunAUCube, orbitalperiodYears, c="red", linewidth=2, marker="o", markerfacecolor="black")

plt.xlim(0, 300)
plt.ylim(0, 300)
plt.xlabel('(a/AU)^3/2')
plt.ylabel('T/Yr')
plt.title('Kepler\'s Third Law')
plt.show()
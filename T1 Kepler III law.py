import matplotlib.pyplot as plt

# Data
planets = ['Earth', 'Mercury', 'Venus', 'Mars', 'Pluto', 'Neptune', 'Jupiter', 'Uranus', 'Saturn']
sunDistanceAU = [1.00, 0.387, 0.723, 1.523, 39.51, 30.25, 5.20, 19.29, 9.58]
orbitalperiodYears = [1.00, 0.24, 0.62, 1.88, 248.35, 166.34, 11.86, 84.75, 29.63]

sunAUCube = []
for i in range(len(planets)):
   value = sunDistanceAU[i]
   value = value ** (3/2)
   sunAUCube.append(value)

# Plotting both axes
plt.plot(sunAUCube, orbitalperiodYears, label = 'Keplar\'s III law relationship', color="red")
plt.plot(sunAUCube, orbitalperiodYears, c="purple", linewidth=2, marker="o", markerfacecolor="black")

# Plotting Info & Misc
plt.xlim(-25, 275)
plt.ylim(-25, 275)
plt.xlabel('(a/AU)^3/2')
plt.ylabel('T/Yr')
plt.grid()
plt.title('Kepler\'s Third Law')
plt.show()
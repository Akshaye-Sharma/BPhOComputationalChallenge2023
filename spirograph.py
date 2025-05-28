from matplotlib import pyplot as plt
import math
from numpy import linspace, cos, sin



# Data
planets = [
    # ['Planet', Semi-Major Axis, Semi-Minor Axis, Orbital Period (years)']
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

# Function to calculate eccentricity
def eccentricity_calc(s_major, s_minor):
    return math.sqrt(1 - (s_minor ** 2) / (s_major ** 2))

# Calculate eccentricities
eccentricities = [eccentricity_calc(p[1], p[2]) for p in planets]


# NOTE:
# This spirograph visualization generally works best when choosing two INNER planets
# (e.g., Mercury, Venus, Earth, Mars) or two OUTER planets (e.g., Uranus, Neptune, Pluto).

# Get user input for planets
chosen_planets = []
for i in range(2):
    while True:
        try:
            chosen_p = int(input(f"Choose planet #{i + 1} (1-9): ")) - 1
            if 0 <= chosen_p < len(planets):
                chosen_planets.append(chosen_p)
                break
            else:
                print("Please enter a number between 1 and 9.")
        except ValueError:
            print("Invalid input. Please enter an integer.")

planet1 = chosen_planets[0]
planet2 = chosen_planets[1]

# Plot Sun
plt.plot([0], [0], c="yellow", marker="o", label="Sun")

# Plot orbits as ellipses
theta = linspace(0, 2 * math.pi, 360)
for i in chosen_planets:
    a = planets[i][1]
    b = planets[i][2]
    e = eccentricities[i]
    x = a * cos(theta) + a * e  # Offset ellipse to place Sun at one focus
    y = b * sin(theta)
    plt.plot(x, y, label=planets[i][0])

# Generate spirograph
omega1 = 2 * math.pi / planets[planet1][3]
omega2 = 2 * math.pi / planets[planet2][3]
a1, b1, e1 = planets[planet1][1], planets[planet1][2], eccentricities[planet1]
a2, b2, e2 = planets[planet2][1], planets[planet2][2], eccentricities[planet2]

t_values = linspace(0, 200 * math.pi, 500)  # Enough steps to show pattern

for t in t_values:
    x1 = a1 * cos(omega1 * t) + a1 * e1
    y1 = b1 * sin(omega1 * t)
    x2 = a2 * cos(omega2 * t) + a2 * e2
    y2 = b2 * sin(omega2 * t)

    plt.plot([x1, x2], [y1, y2], color='black', linewidth=0.2)

# Set graph limits
max_x = max(planets[planet1][1] + a1 * e1, planets[planet2][1] + a2 * e2)
max_y = max(planets[planet1][2], planets[planet2][2])
plt.xlim(-max_x * 1.1, max_x * 1.1)
plt.ylim(-max_y * 1.1, max_y * 1.1)

# Plotting info
plt.xlabel('x (AU)')
plt.ylabel('y (AU)')
plt.title(f'Spirograph of {planets[planet1][0]} and {planets[planet2][0]}')
plt.legend()
plt.grid()

# Circular plot
plt.gca().set_aspect('equal')

# Show plot
plt.show()
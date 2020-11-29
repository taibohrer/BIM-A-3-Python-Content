import math

# General Information
print("Taiane Bohrer - Polygon Assignment")
print("BIM A+3")
print()

# Set the points that will become n
n = int(input ('Enter the number of points: '))
print()

# Define how many coordinates each point have
x = []
y = []

# Input for the coordinates of each point
for i in range(n):
    CoordinateX = float (input(f'x{i + 1}: '))
    CoordinateY = float (input(f'y{i + 1}: '))
    
    x.append(CoordinateX)
    y.append(CoordinateY)
    
print()
    
# Print Table of Points and Coordinates
print(f'{"Point":10} {"x":10} {"y":10}')
print("-"*30)

for i in range(n):
    print(f'{i+1}{x[i]:13}{y[i]:10}')
    
print()
print("Geometrical Characteristics of The Polygon:")
print("-"*30)

# Calculating the area Ax
t1 = 0
for i in range(n):
    a = x[i] + x[i-1]
    b = y[i] - y[i-1]
    d = a * b
    t1 = t1 + d
Ax = (0.5) * t1
print(f'{"Ax:":6}{Ax:10.2f}')

# Calculating Sx
t2 = 0
for i in range(n):
    a = x[i] - x[i-1]
    b = y[i]**2 + y[i] * y[i-1] + y[i-1]**2
    d = a * b
    t2 = t2 + d
Sx = -(1/6) * t2 
print(f'{"Sx:":6}{Sx:10.2f}')

# Calculating Sy
t3 = 0
for i in range(n):
    a = y[i] - y[i-1]
    b = x[i]**2 + x[i] * x[i-1] + x[i-1]**2
    d = a * b
    t3 = t3 + d

Sy = (1/6) * t3
print(f'{"Sy:":6}{Sy:10.2f}')


# Calculating Ix
t4 = 0
for i in range(n):
    a = x[i] - x[i-1]
    b = y[i]**3 + (y[i]**2) * y[i-1] + y[i] * (y[i-1]**2) + y[i-1]**3
    d = a * b
    t4 = t4 + d
Ix = -(1/12) * t4
print(f'{"Ix:":6}{Ix:10.2f}')

# Calculating Iy
t5 = 0
for i in range(n):
    a = y[i] - y[i-1]
    b = x[i]**3 + (x[i]**2) * x[i-1] + x[i] * (x[i-1]**2) + x[i-1]**3
    d = a * b
    t5 = t5 + d
Iy = (1/12) * t5
print(f'{"Iy:":6}{Iy:10.2f}')

# Calculating Ixy
t6 = 0
for i in range(n):
    a = y[i] - y[i-1]
    b = (y[i] * (3 * x[i]**2 + 2 * x[i] * x[i-1] + x[i-1]**2)) + y[i-1] * (3 * x[i-1]**2 + 2 * x[i] * x[i-1] + x[i]**2)
    d = a * b
    t6 = t6 + d
Ixy = -(1/24) * t6
print(f'{"Ixy:":6}{Ixy:10.2f}')


# Remaining Calculation

xt = Sy / Ax
print(f'{"xt:":6}{xt:10.2f}')

yt = Sx / Ax
print(f'{"yt:":6}{yt:10.2f}')

Ixt = Ix - (yt**2) * Ax
print(f'{"Ixt:":6}{Ixt:10.2f}')

Iyt = Iy - (xt**2) * Ax
print(f'{"Iyt:":6}{Iyt:10.2f}')

Ixyt = Ixy + xt * yt * Ax
print(f'{"Ixyt:":6}{Ixyt:10.2f}')
print("-"*30)

print()

# General Information
print("Taiane Bohrer - Polygon Assignment")
print("BIM A+3")
print("End")




   


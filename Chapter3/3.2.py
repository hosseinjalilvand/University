import math

x1,y1 = eval(input("Enter the latitude and longitude of the first point (in degrees): "))
x2,y2 = eval(input("Enter the latitude and longitude of the second point (in degrees): "))


x1, y1, x2, y2 = map(math.radians, [x1,y1,x2,y2])
radius = 6371.01

d = radius * math.acos(math.sin(x1) * math.sin(x2) + math.cos(x1) * math.cos(x2) * math.cos(y1 - y2))


print("The distance between the two points is", d, "km.")
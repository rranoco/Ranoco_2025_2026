import math

angle= int(input("Enter launch angle (degrees):"))
R = int(input("Enter maximum distance (meters):"))
grav = 9.8

angle_radians= math.radians(angle)
speed = math.sqrt((R*grav)/math.sin(2 * angle_radians))
speed = round(speed,2)


print("Required launch speed:", speed, "m/s")
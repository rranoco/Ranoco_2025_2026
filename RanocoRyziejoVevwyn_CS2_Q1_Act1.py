speed= float(input("Enter speed:"))
distance= 42.195

def estimated_time(distance,speed):
    time= distance/speed
    return time


def exact_hours(total_time):
    hours= int(total_time)
    mins= total_time - hours
    minute= int(mins*60)
    return hours,minute

total_time= estimated_time(distance,speed)
hours, minute = exact_hours(total_time)
print("At",speed,"km/h, it will take approximately",hours,"hours and",minute,"minutes to finish a marathon.")

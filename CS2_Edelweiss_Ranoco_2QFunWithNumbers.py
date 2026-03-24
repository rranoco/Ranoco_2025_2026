# Welcome to fun with numbers!
age = int(input("Hi there! Please enter your age:"))


if age <= 0:
    print("Please enter a positive number for your age.")

else:
    total = 0 # to store the sum
    count = 1 # starting point

    # using the while loop to add everything up until the age
    while count <= age:
        total += count
        count += 1 # adds the next number

    print("The sum of all numbers from 1 to", age, "is:", total)

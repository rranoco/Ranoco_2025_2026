Name = input("Enter Name:")
Age = input("Enter Age:")
Fav_Sub = input("Enter your favorite subject:")


student = {
   "name" : Name,
   "age" : Age,
   "favorite_subject" : Fav_Sub

}

print()
print("Student Record:")
print("Name:", (student["name"]))
print("Age:", (student["age"]))
print("Favorite Subject:", (student["favorite_subject"]))

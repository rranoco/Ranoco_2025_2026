import numpy as np

subjects_2d = np.array([
    ["Physics", "Math 2", "CS"],
])

study_data = np.array([
    [2, 3, 1, 2, 4],   
    [1, 0, 2, 1, 0],   
    [0, 1, 2, 1, 3],   
])


days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

def print_data():
    index = 0
    for row in subjects_2d:
        for subject in row:
            print(f"{subject:<15} - {study_data[index]}")
            index += 1
        print()




def select_subject():
    index = 0
    for row in subjects_2d:
        for subject in row:
             print("[", index, "]", subject)
             index += 1
    choice = int(input("Enter choice:"))
    print()
    print(subjects_2d.flatten()[choice], "-", study_data[choice].tolist())




def update_data():
    index = 0
    for i, row in enumerate(subjects_2d):
        for j, subject in enumerate(row):
            print("[", index, "]", subject)
            index += 1 
    subject_choice = int(input("Enter choice:"))

    for i, day in enumerate(days):
        print(f"[{i}] {day}")
    day_choice = int(input("Enter choice:"))

    new_value = int(input("Enter new data: "))
    study_data[subject_choice][day_choice] = new_value
    print("Updating", subjects_2d.flatten()[subject_choice], "study time on", days[day_choice], "to", new_value, "hours.")
    print()



def summarize_data():
    total = np.sum(study_data, axis=1)
    average = np.mean(study_data, axis=1)
    minimum = np.min(study_data, axis=1)
    maximum = np.max(study_data, axis=1)
    flat_subjects = subjects_2d.flatten()

    print()
    for i in range(len(flat_subjects)):
        name = flat_subjects[i]
        print("%-15s - Total Hours: %-3d | Average: %-4.1f | Min: %-2d | Max: %d" %
              (name, total[i], average[i], minimum[i], maximum[i]))
    print()



def main_menu():
    while True:
        print ("[1] Print all data.")
        print ("[2] Select subject.")
        print ("[3] Update data.")
        print ("[4] Summarize data.")
        print ("[5] Exit.")

        try:
            choice = int(input("Enter choice: "))
            if choice == 1:
                print_data()
            elif choice == 2:
                select_subject()
            elif choice == 3:
                update_data()
            elif choice == 4:
               summarize_data()
            elif choice == 5:
                break
            else:
                print("Invalid choice. Please try again")
        except ValueError:
            print("Invalid choice. Please try again")
main_menu()

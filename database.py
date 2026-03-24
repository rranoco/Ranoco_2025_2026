import json
from pathlib import Path

script_path = Path(__file__)
script_dir = script_path.parent
json_file = script_dir / "output.json"

script_path = Path(__file__)
script_dir = script_path.parent
json_file = script_dir / 'database.json'


def load_file(filename = json_file) :
    with open(filename, 'r') as file :
        return json.load(file)

def save_file(data, filename = json_file) :
        with open(filename, 'w') as file:
            json.dump(data, file, indent=4)

def initial_data():
    data = { 
            "snacks" : [{"snack_id": 1, "name": "Piattos", "category" : "chips", "price" : 20},
                   {"snack_id": 2, "name": "Nova", "category" : "chips", "price" : 18},
                   {"snack_id": 3, "name": "Oreo", "category" : "cookies", "price" : 15},
                   {"snack_id": 4, "name": "KitKat", "category" : "chocolate", "price" : 25},
                   {"snack_id": 5, "name": "Skyflakes", "category" : "crackers", "price" : 12}
    ],

    "students" : [{"student_id": 1, "name": "Alice Cruz", "grade_level" : 10},
                      {"student_id": 2, "name": "Brian Santos", "grade_level" : 9},
                      {"student_id": 3, "name": "Carla Reyes", "grade_level" : 10},
                      {"student_id": 4, "name": "David Lim", "grade_level" : 11},
                      {"student_id": 5, "name": "Ella Tan", "grade_level" : 10}
               
    ],

    "sales" : [{"sale_id": 1, "student_id": 1, "snack_id" : 1, "quantity" : 2, "total_price" : 40, "date" : "2026-03-14", "day" : "Saturday"},
                  {"sale_id": 2, "student_id": 3, "snack_id" : 3, "quantity" : 1, "total_price" : 15, "date" : "2026-03-14", "day" : "Saturday"},
                  {"sale_id": 3, "student_id": 2, "snack_id" : 2, "quantity" : 3, "total_price" : 54, "date" : "2026-03-15", "day" : "Sunday"},
                  {"sale_id": 4, "student_id": 5, "snack_id" : 4, "quantity" : 1, "total_price" : 25, "date" : "2026-03-15", "day" : "Sunday"},
                  {"sale_id": 5, "student_id": 1, "snack_id" : 1, "quantity" : 1, "total_price" : 20, "date" : "2026-03-16", "day" : "Monday"},
                  {"sale_id": 6, "student_id": 4, "snack_id" : 5, "quantity" : 2, "total_price" : 24, "date" : "2026-03-16", "day" : "Monday"}
           
    ]

    }
    
    return data

# Save & Load
def save_data(data):
    with open(json_file, "w") as f:
        json.dump(data, f, indent=4)


def load_data():
    try:
        with open(json_file, "r") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return None


# Read Info
def read_info(data):

    chips = [s for s in data["snacks"] if s["category"] == "chips"]
    print(f"Snacks that are chips: \n{chips}\n")

    g10_ids = [st["student_id"] for st in data["students"] if st["grade_level"] == 10]
    g10_sales = [sa for sa in data["sales"] if sa["student_id"] in g10_ids]
    print(f"Grade 10 sales: \n {g10_sales}\n")

    today = "2026-03-16"
    total_today = sum(sa["quantity"] for sa in data["sales"] if sa["date"] == today)
    print(f"Total quantity sold on {today}: {total_today}\n")


#Update

def update_info(data):
    for s in data["snacks"]:
        if s["name"] == "Oreo":
            s["price"] = 18

    for st in data["students"]:
        if st["name"] == "Brian Santos":
            st["grade_level"] = 10

    for sa in data["sales"]:
        if sa["sale_id"] == 1:
            sa["quantity"] = 3
            sa["total_price"] = 60

    return data


# Delete Info
def delete_info(data):

    data["snacks"] = [s for s in data["snacks"] if s["name"] != "Skyflakes"]
    
  
    removed_student_ids = [st["student_id"] for st in data["students"] if st["name"] == "Ella Tan"]
    data["students"] = [st for st in data["students"] if st["name"] != "Ella Tan"]
    
    data["sales"] = [sa for sa in data["sales"] if sa["sale_id"] != 6 and sa["student_id"] not in removed_student_ids]
    
    return data


def answer_questions(data):

    # 1. What's the most popular snack?
    snack_counts = {}
    for sale in data["sales"]:
        snack_id = sale["snack_id"]
        snack_counts[snack_id] = snack_counts.get(snack_id, 0) + sale["quantity"]

    top_snack = None
    max_count = 0
    for snack_id in snack_counts:
        if snack_counts[snack_id] > max_count:
            max_count = snack_counts[snack_id]
            top_snack = snack_id

    snack_name = next(s["name"] for s in data["snacks"] if s["snack_id"] == top_snack)
    print(f"1. The most popular snack is {snack_name} with {max_count} sold \n")

    # 2. Which grade level spends the most money on snacks?
    grade_spending = {}
    student_to_grade = {st["student_id"]: st["grade_level"] for st in data["students"]}

    for sale in data["sales"]:
        if sale["student_id"] in student_to_grade:
            grade = student_to_grade[sale["student_id"]]
            grade_spending[grade] = grade_spending.get(grade, 0) + sale["total_price"]

    top_grade = None
    max_spent = 0
    for grade in grade_spending:
        if grade_spending[grade] > max_spent:
            max_spent = grade_spending[grade]
            top_grade = grade

    print(f"2. Grade {top_grade} spends P{max_spent} on snacks. \n")

    # 3. What day of the week has the highest number of sales?
    day_counts = {}
    for sale in data["sales"]:
        day = sale["day"]
        day_counts[day] = day_counts.get(day, 0) + 1

    top_day = None
    max_sales = 0
    for day in day_counts:
        if day_counts[day] > max_sales:
            max_sales = day_counts[day]
            top_day = day

    print(f"3. The busiest day is usually {top_day} {max_sales} transactions.\n")

    # 4. Which student has made the most purchases?
    student_counts = {}
    for sale in data["sales"]:
        student_id = sale["student_id"]
        student_counts[student_id] = student_counts.get(student_id, 0) + sale["quantity"]

    top_student = None
    max_items = 0
    for student_id in student_counts:
        if student_counts[student_id] > max_items:
            max_items = student_counts[student_id]
            top_student = student_id

    student_name = next(st["name"] for st in data["students"] if st["student_id"] == top_student)
    print(f"4. The student that has the most items purchased is {student_name} with {max_items} items purchased\n")

    # 5. What is the average amount spent per sale?
    total_sales_amount = 0
    total_transactions = len(data["sales"])

    for sale in data["sales"]:
        total_sales_amount += sale["total_price"]

    if total_transactions > 0:
        average = total_sales_amount / total_transactions
    else:
        average = 0

    print(f"5. The average amount spent per sale is ₱{average:.2f}\n")

    # 6. What trends do you notice? How could the snack shop use this information to improve sales?
    print("6. Trends / Insights:")
    print("- Chips are the most popular snacks, meaning students prefer savory food.")
    print("- Grade levels with more students (like Grade 10) tend to spend more overall.")
    print("- Certain days (like weekends) have more sales activity.")
    print("- A few students repeatedly buy snacks, contributing heavily to sales.")
    print("- The school can stock more popular items and prepare more during busy days.\n")




def main():
    data = load_data()

    if not data:
        data = initial_data()
        save_data(data)

    print("DATA:")
    read_info(data)

    data = update_info(data)

    data = delete_info(data)

    save_data(data)

    print("Questions:")
    answer_questions(data)


if __name__ == "__main__":
    main()
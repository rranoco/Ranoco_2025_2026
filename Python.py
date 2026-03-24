import json
from pathlib import Path

# locate database.json in same folder
script_path = Path(__file__)
script_dir = script_path.parent
json_file = script_dir / "database.json"


# load json
def load_file(filename=json_file):
    with open(filename, "r") as file:
        return json.load(file)


# save json
def save_file(data, filename=json_file):
    with open(filename, "w") as file:
        json.dump(data, file, indent=4)


# CREATE
def create_info(name, info):
    data = load_file()
    data[name] = info
    save_file(data)


# READ
def read_info():
    data = load_file()
    for key in data:
        print(key, data[key])


# UPDATE (add school field)
def update_info():
    data = load_file()

    for key in data:
        data[key]["school"] = "PSHS"

    save_file(data)


# DELETE (remove red, blue, yellow)
def delete_info():
    data = load_file()

    remove = []
    for key in data:
        color = data[key]["favorite_color"].lower()
        if color in ["red", "blue", "yellow"]:
            remove.append(key)

    for key in remove:
        data.pop(key)

    save_file(data)


def main():

    # CREATE students
    create_info("Zach", {
        "age":14,
        "favorite_color":"Chartreuse",
        "favorite_subject":"Math 3",
        "favorite_song":"Haus of Holbein by VI the Musical"
    })

    create_info("Leigh", {
        "age":14,
        "favorite_color":"Navy Blue",
        "favorite_subject":"Biology",
        "favorite_song":"8 by IVE"
    })

    create_info("Ryziejo", {
        "age":14,
        "favorite_color":"Blue",
        "favorite_subject":"Physics",
        "favorite_song":"Another One by Mac DeMarco"
    })

    create_info("Viel", {
        "age":14,
        "favorite_color":"Pink",
        "favorite_subject":"Math 2",
        "favorite_song":"Mundo by IV of Spades"
    })

    create_info("Karl Mata", {
        "age":13,
        "favorite_color":"Green",
        "favorite_subject":"PE",
        "favorite_song":"Transform by Daniel Caesar"
    })

    create_info("RJ", {
        "age":14,
        "favorite_color":"Yellow",
        "favorite_subject":"Math 2",
        "favorite_song":"Pag-ibig by Sponge Cola"
    })

    create_info("Chloe", {
        "age":12,
        "favorite_color":"Blue",
        "favorite_subject":"Biology",
        "favorite_song":"All of You by Syd Matters"
    })

    create_info("Sasha Kissel C. Villamora", {
        "age":14,
        "favorite_color":"Pink",
        "favorite_subject":"Physics",
        "favorite_song":"Stateside by PinkPantheress ft. Zara Larsson"
    })

    create_info("Gabriel Efien R. Orapa", {
        "age":14,
        "favorite_color":"Pink",
        "favorite_subject":"Biology",
        "favorite_song":"Paradise by Chase Atlantic"
    })

    create_info("Chira", {
        "age":14,
        "favorite_color":"Green",
        "favorite_subject":"Dismissal",
        "favorite_song":"Count on Me by Bruno Mars"
    })


    print("\nREAD:")
    read_info()

    print("\nUPDATE (add school):")
    update_info()
    read_info()

    print("\nDELETE (red, blue, yellow):")
    delete_info()
    read_info()


main()
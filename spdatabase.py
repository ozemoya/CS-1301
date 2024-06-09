characters = input("Enter a character: ")
first_appearances = input("Enter the first appearance: ")
list_of_volumes = eval(input("Enter the list of volumes: "))

scott_pilgrim_database=[ 
   {
    "characters": "Scott Pilgrim",
    "first_appearance": "Volume 1",
    "volumes": [1, 2, 3, 4, 5, 6]
   },
   {
    "characters": "Ramona Flowers",
    "first_appearance": "Volume 1",
    "volumes": [1, 2, 3, 4, 5, 6]
   }
]

def add_new_characters(character, first_appearance, volumes):
    new_character = {}
    new_character["characters"] = character
    new_character["first_appearance"] = first_appearance
    new_character["volumes"] = volumes
    scott_pilgrim_database.append(new_character)

add_new_characters(characters, first_appearances, list_of_volumes)

print(scott_pilgrim_database)
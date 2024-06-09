characters = input("Enter a character: ")
first_appearance = input("Enter the number of episodes: ")
fraudulence = input("Is they a fraud?: y/n ")
jjkdatabase = [
    {
        "character": "Yuji",
        "appearance": "Episode 1",
        "fraudulence": "Yes"
    },
    {    "character": "Gojo",
        "appearance": "Episode 1",
        "fraudulence": "Yes"
    },
]


def jjkdatabase(character,first_appearance,fraud):
    new_character ={}
    new_character["character"] = character
    new_character["appearance"] = first_appearance
    new_character["fraudulence"] = fraud

jjkdatabase(characters,first_appearance,fraudulence)

print(jjkdatabase)

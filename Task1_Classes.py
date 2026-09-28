# Create the Avenger class
class Avenger:

    # Constructor
    def __init__(self, name, age, gender, super_power, weapon):
        self.name = name
        self.age = age
        self.gender = gender
        self.super_power = super_power
        self.weapon = weapon

    # Method to display superhero information
    def get_info(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Gender:", self.gender)
        print("Super Power:", self.super_power)
        print("Weapon:", self.weapon)

    # Method to check whether the Avenger is a leader
    def is_leader(self):
        if self.name == "Captain America":
            return True
        else:
            return False


# Create Avengers objects

captain = Avenger(
    "Captain America", 100, "Male",
    "Super Strength", "Shield"
)

ironman = Avenger(
    "Iron Man", 48, "Male",
    "Technology", "Armor"
)

blackwidow = Avenger(
    "Black Widow", 35, "Female",
    "Superhuman", "Batons"
)

hulk = Avenger(
    "Hulk", 49, "Male",
    "Unlimited Strength", "No Weapon"
)

thor = Avenger(
    "Thor", 1500, "Male",
    "Super Energy", "Mjölnir"
)

hawkeye = Avenger(
    "Hawkeye", 45, "Male",
    "Fighting Skills", "Bow and Arrows"
)


# Store all Avengers in a list
super_heroes = [
    captain,
    ironman,
    blackwidow,
    hulk,
    thor,
    hawkeye
]


# Display information about each Avenger
for hero in super_heroes:
    print("\n------------------------------")
    hero.get_info()
    print("Is Leader:", hero.is_leader())

print("\n------------------------------")
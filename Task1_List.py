justice_league = [
    "Superman",
    "Batman",
    "Wonder Woman",
    "Flash",
    "Aquaman",
    "Green Lantern"
]

print("1. Members:", len(justice_league))

justice_league.extend(["Batgirl", "Nightwing"])
print("2.", justice_league)

justice_league.remove("Wonder Woman")
justice_league.insert(0, "Wonder Woman")
print("3.", justice_league)

justice_league.remove("Green Lantern")
flash_index = justice_league.index("Flash")
justice_league.insert(flash_index, "Green Lantern")
print("4.", justice_league)

justice_league = [
    "Cyborg",
    "Shazam",
    "Hawkgirl",
    "Martian Manhunter",
    "Green Arrow"
]
print("5.", justice_league)

justice_league.sort()
print("6.", justice_league)
print("New Leader:", justice_league[0])
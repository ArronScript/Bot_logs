
import random



american_names = ["Max", "Buddy", "Charlie", "Jack", "Rocky", "Duke", "Toby", "Bailey", "Tucker", "Jake",
                  "Cody", "Buster", "Duke", "Riley", "Cooper", "Harley", "Bear", "Murphy", "Lucky", "Oliver"]

british_names = ["Poppy", "Lola", "Bella", "Daisy", "Ruby", "Rosie", "Molly", "Millie", "Lucy", "Tilly",
                 "Lily", "Maggie", "Maisie", "Holly", "Jessie", "Sophie", "Amber", "Skye", "Rosie", "Ellie"]

all_dog_names = []
for _ in range(500):
    all_dog_names.append(random.choice(american_names))
    all_dog_names.append(random.choice(british_names))

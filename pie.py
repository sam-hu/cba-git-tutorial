#####DO NOT CHANGE THIS FILE#####
import matplotlib.pyplot as plt
from collections import Counter

array = []
with open("animals.txt", "r") as ins:
    for line in ins:
        if not (line[:2] == "**"):
            animal = line.split(":", 1)[1]
            strip1 = animal.strip()
            strip2 = strip1.strip("\n")
            if strip2 != "":
                array.append(strip2.lower())

counter = Counter(array)
d = dict(counter)
animals = d.keys()
counts = list(map(int, d.values()))

# Plot
plt.title("CBA's Favorite Animals")
plt.pie(counts, labels=animals, shadow=True, autopct='%1.1f%%', startangle=140)

plt.axis('equal')
plt.show()

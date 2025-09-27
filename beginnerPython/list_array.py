cats = ["Evee", "Preeti", "Querky"]

# cats[2] = "Owner"
cats.append("Owner")
cats.extend(["Cool", "Naughty"])

cats += ["mouse", "cheese"]

cats[1:1] = ["Test1", "Test2", "Test3"]

print(cats)
# print(cats[2:5])


# Tuples - they are immutable group of list means once created can't be modified

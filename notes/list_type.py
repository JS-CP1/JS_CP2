# JS, 1st, Types of Lists Notes

numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "0"]

print(numbers[3])
numbers[-1] = "10"

print(numbers)

fruit = ("apple", "orange", "peach", "kiwi", "raspberry")
home = (0, 0)
x, y = home

#fruit[3] = "pineapple"
print(x)

colors = {"orange", "purple", "green", "blue", "yellow", "red", "green", "blue"}
colors.add("pink")
colors.remove("purple")

for i in colors:
    if i == "orange":
        i = "Burgendy"
    print(i)

print(colors)
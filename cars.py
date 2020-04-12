# Practice: Showroom & Junkyard

# 1. Create an empty set named showroom.
showroom = set()

# 2. Add four of your favorite car model names to the set.
showroom.add("model X")
showroom.add("model Y")
showroom.add("RAM")
showroom.add("F1")
# print(showroom)

# 3. Print the length of your set.
# print(len(showroom))

# 4. Pick one of the items in your show room and add it to the set again.
showroom.add("RAM")
# showroom.add("Corvette")

# 5. Print your showroom. Notice how there's still only one instance of that model in there.
# print(showroom)

# 6. Using update(), add two more car models to your showroom with another set.
showroom.update({"Corvette", "Rivian"})

# 7. You've sold one of your cars. Remove it from the set with the discard() method.
showroom.discard("Corvette")
# print(showroom)


# Acquiring more cars

# 1. Now create another set of cars in a variable junkyard. Someone who owns a junkyard full 
# of old cars has approached you about buying the entire inventory. In the new set, add some 
# different cars, but also add a few that are the same as in the showroom set.
junkyard = {"Yugo", "Prius", "RAM", "Pinto", "F1"}

# 2. Use the intersection method to see which cars exist in both the showroom and that junkyard.
all_cars = showroom.intersection(junkyard)
# print(all_cars)

# 3. Now you're ready to buy the cars in the junkyard. 
# Use the union method to combine the junkyard into your showroom.
combine_cars = showroom.union(junkyard)
# print(combine_cars)

# 4. Use the discard() method to remove any cars that you acquired from the junkyard that you 
# do not want in your showroom.
combine_cars.discard("Pinto")
combine_cars.discard("Yugo")
combine_cars.discard("F1")
print(combine_cars)
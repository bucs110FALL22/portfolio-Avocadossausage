#Part A
import random

weeks = 16
print(weeks , type(weeks))
classes = 5
print(classes, type(classes))
tuition = 6000
print(tuition , type(tuition))
classes_per_week = 2
print(classes_per_week, type(classes_per_week))
cost_per_week = ((tuition / classes) / weeks)
print(cost_per_week, type(cost_per_week))
cost_per_class = (cost_per_week / classes_per_week)
print(cost_per_class, type(cost_per_class))
print("Cost per week:", cost_per_week)
print("This is the cost per class :) ", cost_per_class)


#Part B
list = ["ketchup", 20, 50.5, 1, "burger"]
random_obj = random.choice(list)
print(random_obj)
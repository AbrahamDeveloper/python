import random

# List of first names
first_names = ["Alice", "Bob", "Charlie", "David", "Emma", "Frank", "Grace", "Henry", "Ivy", "Jack"]

# List of last names
last_names = ["Smith", "Johnson", "Brown", "Lee", "Garcia", "Taylor", "Clark", "Hall", "Lewis", "Young"]

def generate_name():
    first_name = random.choice(first_names)
    last_name = random.choice(last_names)
    return first_name + " " + last_name

# Generate and print a random name
random_name = generate_name()
print("Random Name:", random_name)

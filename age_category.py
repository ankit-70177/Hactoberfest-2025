# age_category.py
# A simple program to classify a person by age.

print("🎂 Age Category Finder")

age = int(input("Enter your age: "))

if age < 0:
    print("Invalid age! 🚫")
elif age <= 12:
    print("You are a Child 👶")
elif age <= 19:
    print("You are a Teenager 🧒")
elif age <= 59:
    print("You are an Adult 🧑")
else:
    print("You are a Senior 👴")

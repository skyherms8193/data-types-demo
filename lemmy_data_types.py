"""
Project: Lemmy Data Types 🐶

Description:
A fun demonstration of Python data types using my dog Lemmy.

Covers:
- List (daily activities)
- Tuple (basic info)
- Dictionary (activity frequency)
- String (sentence + word count)
"""

# LIST: Daily activities
lemmy_activities = [
    "Morning walk",
    "Breakfast",
    "Chew toy time",
    "Afternoon walk",
    "Belly rubs",
    "Dinner",
    "Evening walk",
    "Bed"
]

print("Lemmy's Schedule:")
for activity in lemmy_activities:
    print("*", activity)


print()  # spacing


# TUPLE: Basic info (name, breed, age, weight)
lemmy_info = ("Clementine", "Dachshund", 1, "10 lbs")

print("Lemmy's details:")
print("Name:", lemmy_info[0])
print("Breed:", lemmy_info[1])
print("Weight:", lemmy_info[3])


print()


# DICTIONARY: Activity frequency
activity_frequency = {
    "Walks": "At least 3 times daily",
    "Feeding": "Twice daily",
    "Playtime": "Multiple times a day",
    "Cuddling": "Constantly"
}

print("Lemmy's daily routine:")
for activity, frequency in activity_frequency.items():
    print(f"* {activity}: {frequency}")


print()


# STRING: Sentence + word count
sentence = "Lemmy is the queen of the castle."

word_count = len(sentence.split())

print("Sentence:", sentence)
print("Word count:", word_count)

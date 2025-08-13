dictionary = {
    "title": "The Alchemist",
    "author": "Paulo Coelho",
    "year": 1988,
    "genre": "Fiction"
}

# Print the author’s name.
print(dictionary["author"])

# Update the year.
dictionary["year"] = 1977

# Add a new key rating.

dictionary["rating"] = 4.8

# print("Updated Details:", dictionary)

# for key, value in dictionary.items():
#     print(key, ": ", value)


# Create a nested dictionary for 2 students:
students = {
    "student1": {"name": "John", "marks": 85},
    "student2": {"name": "Sara", "marks": 90}
}
# print(students["student2"]["marks"])

students["student1"]["marks"] = 88

# print(students)


# You have a JSON-like dict from an AI model:


ai_output = {
    "summary": {
        "text": "Python is great for AI.",
        "word_count": 5
    },
    "keywords": ["Python", "AI", "programming"]
}


# Print the summary text.
print(ai_output["summary"]["text"])

# Print the second keyword.
print(ai_output["keywords"][1])

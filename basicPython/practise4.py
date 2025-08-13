
person = {
    "name": "Preeti",
    "age": 25,
    "is_coder": True,
}

# Accessing values
# print(person['name'])
# print(person.get("age"))
# print(person.get("city", "NAN"))  # NAN is default value

# Adding/ updating
person["city"] = "Ranchi"
person["age"] = 26

person.pop("is_coder")
del person["city"]

# print(person)

# 2️⃣ Looping Through a Dictionary

student = {"name": "John", "marks": 85}
# for key in student:
#     print("key: ", student[key])

# for key, value in student.items():
#     print(key, "=>", value)

# 3️⃣ Nested Dictionaries
data = {
    "user": {
        "name": "Alice",
        "skills": ["Python", "AI", "NLP"],
        "profile": {
            "location": "Bangalore",
            "experience": 3
        }
    }
}
print(data["user"]["skills"][0])
print(data["user"]["profile"]["location"])

response = {
    "choices": [
        {"text": "Hello, world!", "finish_reason": "stop"}
    ]
}

print(response["choices"][0]["text"])

# 4️⃣ JSON Files (AI’s Best Friend!)
import json

# writing JSON
# data = {"name": "Preeti", "skills": ["Python", "AI", "NLP"]}
# with open("profile.json", "w") as f:
#     json.dump(data, f)


# Reading JSON
# with open("profile.json", "r") as f:
#     loaded_data = json.load(f)


# print(loaded_data)
# print(loaded_data["skills"][0])


# 5️⃣ AI-Themed File Examples


# Save Chat Logs
# with open("chat_log.txt", "a") as f:
#     f.write("User: What is AI?\n")
#     f.write("Bot: AI means Artificial Intelligence")


# Load AI Configuration from JSON

# config = {
#     "model": "gpt-3.5",
#     "temperature": 0.7,
#     "max_tokens": 200
# }

# with open("config.json", "w") as f:
#     json.dump(config, f, indent=2)

# with open("config.json", "r") as f:
#     settings = json.load(f)

#     print(settings)


# profile = {
#     "name": "Preeti Sharma",
#     "age": 25,
#     "skills": ["ReactJS", "JavaScript", "Python", "MongoDB"]
# }

# # Save to me.json
# with open("me.json", 'w') as f:
#     json.dump(profile, f, indent=4)


# # Load back
# with open("me.json", "r") as f:
#     data = json.load(f)

# # Print Skills
# print("Skills: ", data["skills"])


# Q4: Write a function save_chat(user, bot) that appends this format to chat.txt:
# User: <user message>
# Bot: <bot reply>


# def save_chat(user, bot):
#     with open("chat.txt", 'a') as f:
#         f.write(f"User: {user}\n")
#         f.write(f"Bot: {bot}\n")
#         f.write("-" * 20 + "\n")


# save_chat("Hello", "Hi there!")
# save_chat("What's your name?", "I am an AI assistant.")


#  Q5: You have a dataset file data.txt with sentences like:


# with open("data.txt", 'a') as f:
#     user_inp = input("Enter sentence: ")
#     f.write(user_inp + "\n")

# count = 0
# with open("data.txt", "r") as f:

#     lines = f.readlines()
#     for line in lines:
#         if "AI" in line:
#             count += 1

# print("Number of lines containing 'AI': ", count)


# Q6: Create a JSON file ai_models.json with data:

# model_data = {
#     "models": [
#         {"name": "GPT-4", "type": "text"},
#         {"name": "Stable Diffusion", "type": "image"}
#     ]
# }

# with open("ai_models.json", 'w') as f:
#     json.dump(model_data, f, indent=2)

# with open("ai_models.json", "r") as f:
#     models = json.load(f)

# for model in models["models"]:
#     print(model["name"])
#     if model["type"] == "text":
#         print(model)


# Q7: Create a function save_summary(filename, text) that:
# Writes the original text into a file
# Also writes a fake summary (first 5 words + “…”) below it


# def save_summary(filename, text):
#     words = text.split()
#     summary = " ".join(words[:5]) + "..."

#     with open(filename, "w") as f:
#         f.write(f"Original: {text}\n")
#         f.write(f"Summary: {summary}\n")


# save_summary("summary.txt", "Python is a great programming language for AI.")


# Q8: You have a JSON file reviews.json with customer reviews:

# customer_reviews = {
#     "reviews": [
#         {"user": "Alice", "text": "AI is amazing!"},
#         {"user": "Bob", "text": "Python is tough but useful"},
#         {"user": "Charlie", "text": "AI will change the future"}
#     ]
# }

# count = 0
# for review in customer_reviews["reviews"]:
#     if "AI" in review["text"]:
#         count += 1

# print(count)

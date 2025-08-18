# 1️⃣ Conditional Statements

# age = int(input("Enter your age: "))

# if age >= 18:
#     print("You are eligible to vote.")
# elif age >= 16:
#     print("Just wait for few more years")
# else:
#     print("You are too young")


# 2️⃣ Comparison & Logical Operators

# print(5 > 3)
# print(5 == 5)
# print(5 != 3)

# Logical
x = 5
# print(x > 0 and x < 10)
# print(x > 0 or x > 10)
# print(not (x > 0))


# 3️⃣ Loops — for
# for i in range(5):
#     print(i)

words = ["AI", "Python", "NLP"]
# for word in words:
#     print(word)

# 4️⃣ Loops — while

count = 0
# while count < 3:
#     print("AI is awesome!")
#     count += 1


# 5️⃣ break, continue, pass
# for i in range(5):
#     if i == 3:
#         break
#     print(i)

# for i in range(5):
#     if i == 2:
#         continue
#     print(i)


# for i in range(5):
#     pass


# 6️⃣ AI-Themed Examples

# Example 1

# text = input("Enter a sentence: ")

# if "good" in text.lower():
#     print("Sentiment: Positive")
# elif "bad" in text.lower():
#     print("Sentiment: Negative")
# else:
#     print("Sentiment: Neutral")


# Example 2

# task = input("Enter task type (text/image): ")

# if task.lower() == "text":
#     print("Loading GPT model...")
# elif task.lower() == "image":
#     print("Loading Stable Diffusion model...")
# else:
#     print("Unknown task.")


# Day 5 Practice Challenges (AI-style) 🏋️‍♀️

# Q1:
# Ask the user for a sentence.
# If it contains "ai", print "You are talking about AI."
# If it contains "python", print "You love Python."
# Otherwise, print "General topic."

# task = input("Enter your sentence:  ")
# if task.lower() == 'ai':
#     print("You are talking about AI.")
# elif task.lower() == 'python':
#     print("You love Python.")
# else:
#     print("General topic.")


# Q2:
# Simulate a basic chatbot:
# Keep asking the user for input until they type "bye".
# If input contains "name", reply "I am an AI assistant."
# If input contains "time", reply "I can't tell time yet."
# Else, reply "Interesting..."

# Approach 1

# while True:
#     task = input("Start conversation: ")
#     if task.lower() == 'bye':
#         print("AI: Goodbye!")
#         break
#     elif "name" in task.lower():
#         print("AI: I'm an AI Assistant.")
#     elif "time" in task.lower():
#         print("I can't tell time yet.")
#     else:
#         print("AI: Intresting")

# Approach II
# while True:
#     task = input("You: ").lower()

#     match task:
#         case "bye":
#             print("AI: Goodbye!")
#             break
#         case _ if "name" in task:
#             print("AI: I'm an AI Assistant.")
#         case _ if "time" in task:
#             print("I can't tell time yet.")
#         case _:
#             print("AI: Intresting...")


# Q3 (Bonus — Loop & Condition Combo):
# Print all numbers from 1 to 50 but:
# If divisible by 3, print "AI"
# If divisible by 5, print "Python"
# If divisible by both, print "AI-Python"

for i in range(1, 50):
    if i % 3 == 0 and i % 5 == 0:
        print("AI-Python")
    elif i % 3 == 0:
        print("AI")
    elif i % 5 == 0:
        print("python")
    else:
        print(i)

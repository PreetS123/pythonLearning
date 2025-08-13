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

task = input("Enter task type (text/image): ")

if task.lower() == "text":
    print("Loading GPT model...")
elif task.lower() == "image":
    print("Loading Stable Diffusion model...")
else:
    print("Unknown task.")

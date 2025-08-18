# 1️⃣ Reading & Writing Text Files

# Writing
with open("notes.txt", "w") as f:
    f.write("AI is transforming the world.\n")
    f.write("Python makes AI easier.")


# Reading
with open("notes.txt", "r") as f:
    content = f.read()
    # print(content)


# 2️⃣ Reading Line by Line
# with open("notes.txt", "r") as f:
#     for line in f:
#         print(line.strip())

# 3️⃣ Writing Lists to a File

# sentences = ["AI is amazing.", "Python is powerful.", "Data is key."]
# with open("notes.txt", "a") as f:
#     for sentence in sentences:
#         f.write("\n" + sentence)


# Practice Challenges (More Variety) 🏋️‍♀️


# Q1: Write a program that asks the user for 3 sentences and saves them to a file called sentences.txt.

# Approach I :

# for i in range(1, 4):
#     sentence = input(f"Enter {i} sentence: ")
#     with open("sentence.txt", "a") as f:
#         f.write(sentence,"\n")

# Approach II:
# with open("sentence.txt", 'a') as f:
#     for i in range(1, 4):
#         sentence = input(f"Enter sentence {i}: ")
#         f.write(sentence + "\n")

# with open("sentence.txt", "r") as f:
#     lines = f.readlines()
#     print("Number of lines: ", len(lines))

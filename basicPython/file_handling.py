# 1️⃣ Reading & Writing Text Files

# Writing
with open("notes.txt", "w") as f:
    f.write("AI is transforming the world.\n")
    f.write("Python makes AI easier.")


# Reading
with open("notes.txt", "r") as f:
    content = f.read()
    print(content)


# 2️⃣ Reading Line by Line
with open("notes.txt", "r") as f:
    for line in f:
        print(line.strip())

# 3️⃣ Writing Lists to a File

sentences = ["AI is amazing.", "Python is powerful.", "Data is key."]
with open("notes.txt", "a") as f:
    for sentence in sentences:
        f.write("\n" + sentence)

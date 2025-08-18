# 1️⃣ Defining Functions
def greet():
    print("Hello from AI!")


# greet()


# 2️⃣ Functions with Parameters
def greet_user(name):
    print(f"Hello {name}, welcome to AI learning!")


# greet_user("Preeti")


# 3️⃣ Functions with Return Values


def add(a, b):
    return a+b


# print(add(5, 3))


# 4️⃣ Default Parameters
def introduce(name, role="Ai Assistant"):
    print(f"My name is {name}, I am a {role}")


# introduce("ChatGPT")
# introduce("Bard", role="Chatbot")


# 5️⃣ Variable Arguments

def sum_all(*numbers):
    return sum(numbers)


# print(sum_all(1, 2, 3, 4, 5))


# 6️⃣ AI-Themed Function Examples

# 🔹 Sentiment Analyzer (Keyword-based)
def analyze_sentiments(text):
    text = text.lower()
    if "good" in text or "happy" in text:
        return "Positive"
    elif "bad" in text or "sad" in text:
        return "Negative"
    else:
        return "Neutral"


# print(analyze_sentiments("AI is good"))
# print(analyze_sentiments("This is bad"))


# 🔹 Word Counter (Basic NLP Utility)

def word_count(text):
    words = text.split()
    return len(words)


# print(word_count("I love learning AI with Python"))


# 🔹 Simple AI Chat Function

def chatbot_reply(user_input):
    user_input = user_input.lower()
    if "name" in user_input:
        return "I am your AI Assistant."
    elif "python" in user_input:
        return "Python is great for AI!"
    elif "bye" in user_input:
        return "Goodbye! Have a nice day."
    else:
        return "Tell me more..."


# print(chatbot_reply("What is your name?"))
# print(chatbot_reply("I love Python"))


# <----------------------------***********----------------------------->

# Practice Challenges (AI-Utility Style) 🏋️‍♀️
# Q1:
# Write a function reverse_text(text) that:
# Takes a sentence as input
# Returns the reversed sentence

def reverse_text(text):
    return text[::-1]


# sentence = input("Enter a sentence:  ")
# output = reverse_text(sentence)
# print(output)


# Q2:
# Write a function count_keywords(text, keywords) that:
# Takes a sentence and a list of keywords
# Returns how many of the keywords appear in the text

def count_keywords(text, arr):
    count = 0
    for word in arr:
        if word in text:
            count += 1
    return count


# print(count_keywords("AI with Python is fun", ["AI", "ML", "Python"]))


# Write a function summarize(text) that:

# Returns the first 5 words + "..." (simulate a summary).

def summarize(text):
    words = text.split()
    summarized = " ".join(words[:5])
    return f"{summarized}..."


# print(summarize("Python is a great programming language for AI."))
# Output: "Python is a great programming..."


# Write a function chat_loop() that:
# Keeps asking user input until "bye"
# Uses chatbot_reply() function from above
# Prints the bot’s response


def chat_loop():
    while True:
        task = input("Say more: ")
        match task:
            case "bye":
                break


# chat_loop()

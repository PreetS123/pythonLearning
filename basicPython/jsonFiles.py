# 4️⃣ JSON Files (AI’s Best Friend!)
import json

# writing JSON
data = {"name": "Preeti", "skills": ["Python", "AI", "NLP"]}
with open("profile.json", "w") as f:
    json.dump(data, f)


# Reading JSON
with open("profile.json", "r") as f:
    loaded_data = json.load(f)


# print(loaded_data)
# print(loaded_data["skills"][0])


# 5️⃣ AI-Themed File Examples


# Save Chat Logs
with open("chat_log.txt", "a") as f:
    f.write("User: What is AI?\n")
    f.write("Bot: AI means Artificial Intelligence")


# Load AI Configuration from JSON

config = {
    "model": "gpt-3.5",
    "temperature": 0.7,
    "max_tokens": 200
}

with open("config.json", "w") as f:
    json.dump(config, f, indent=2)

with open("config.json", "r") as f:
    settings = json.load(f)

    print(settings)

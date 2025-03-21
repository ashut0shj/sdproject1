import base64

words = [ "Fearless", "Fearless", "SpeakNow", "Red", "1989", "Reputation", "Lover", "Folklore", "Evermore", "Midnights"]

# Encode words
encoded_words = base64.b64encode(",".join(words).encode()).decode()

# Save to file
with open("words.txt", "w") as file:
    file.write(encoded_words)

print("Words encoded and saved successfully!")

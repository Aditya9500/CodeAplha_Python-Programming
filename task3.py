import spacy

# Load English NLP model
nlp = spacy.load("en_core_web_sm")

# Define chatbot responses
responses = {
    "hello": "Hello! How can I assist you?",
    "hi": "Hi there! What do you need help with?",
    "how are you": "I'm just a bot, but I'm functioning as expected!",
    "your name": "I'm a chatbot created to assist you.",
    "bye": "Goodbye! Have a great day!",
}

# Function to get chatbot response
def chatbot_response(user_input):
    doc = nlp(user_input.lower())  # Process input using spaCy
    for key in responses:
        if key in doc.text:
            return responses[key]
    return "I'm not sure I understand. Can you rephrase?"

# Run chatbot
print("Chatbot: Hello! Type 'bye' to exit.")
while True:
    user_input = input("You: ")
    if user_input.lower() == "bye":
        print("Chatbot:", responses["bye"])
        break
    print("Chatbot:", chatbot_response(user_input))

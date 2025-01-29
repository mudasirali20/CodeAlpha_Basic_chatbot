import random

def basic_chatbot():
    responses = {
        "hello": ["Hi there!", "Hello!", "Hey! How can I help you?"],
        "how are you": ["I'm just a program, but I'm doing great!", "I'm fine, thank you! How about you?"],
        "bye": ["Goodbye! Have a great day!", "Bye! Take care!", "See you soon!"],
        "default": ["I'm not sure I understand. Can you rephrase?", "Interesting. Tell me more!"]
    }

    print("Chatbot: Hi! I'm your chatbot. Type 'bye' to exit.")

    while True:
        user_input = input("You: ").lower()
        if user_input == "bye":
            print("Chatbot:", random.choice(responses["bye"]))
            break

        # Check for a matching keyword in user input
        found_response = False
        for key in responses:
            if key in user_input:
                print("Chatbot:", random.choice(responses[key]))
                found_response = True
                break

        if not found_response:
            print("Chatbot:", random.choice(responses["default"]))

# Run the chatbot
basic_chatbot()
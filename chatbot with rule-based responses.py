# Simple Rule-based Chatbot
def chatbot_response(user_input):
    # Convert user input to lowercase to make matching easier
    user_input = user_input.lower()

    # Greeting responses
    if "hello" in user_input or "hi" in user_input:
        return "Hello! How can I help you today?"
    elif "how are you" in user_input:
        return "I'm just a program, but I'm here to help! How can I assist you?"
    
    # Questions about the chatbot
    elif "who are you" in user_input or "what are you" in user_input:
        return "I am a simple chatbot created to answer your questions."
    elif "what can you do" in user_input:
        return "I can chat with you, answer simple questions, and provide information based on predefined rules."

    # Questions about time or date
    elif "time" in user_input:
        from datetime import datetime
        return f"The current time is {datetime.now().strftime('%H:%M')}."
    elif "date" in user_input:
        from datetime import datetime
        return f"Today's date is {datetime.now().strftime('%B %d, %Y')}."

    # Farewell messages
    elif "bye" in user_input or "goodbye" in user_input:
        return "Goodbye! Have a nice day!"

    # Default response for unrecognized inputs
    else:
        return "Sorry, I didn't understand that. Can you please rephrase?"

# Main loop to interact with the chatbot
def chat():
    print("Chatbot: Hello! I'm your friendly chatbot. Type 'bye' to exit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["bye", "goodbye"]:
            print("Chatbot: Goodbye! Have a nice day!")
            break
        response = chatbot_response(user_input)
        print(f"Chatbot: {response}")

# Run the chat
chat()
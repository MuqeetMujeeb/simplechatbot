def chatbot():
    print("Hello! I'm a simple chatbot. How can I help you today?")
    
    while True:
        user_input = input("You: ").strip().lower()
        
        if "hello" in user_input or "hi" in user_input:
            print("Chatbot: Hello! How can I assist you today?")
        
        elif "your name" in user_input:
            print("Chatbot: I'm a simple chatbot created to assist you. What's your name?")
        
        elif "how are you" in user_input:
            print("Chatbot: I'm just a bunch of code, but I'm here to help you!")
        
        elif "weather" in user_input:
            print("Chatbot: I'm not sure about the weather right now, but you can check a weather website or app!")
        
        elif "exit" in user_input or "bye" in user_input:
            print("Chatbot: Goodbye! Have a great day!")
            break
        
        else:
            print("Chatbot: I'm sorry, I don't understand that. Can you ask something else?")
            
if __name__ == "__main__":
    chatbot()

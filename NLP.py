import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import wordnet # For more advanced matching (optional here, but useful)

def simple_chatbot():
    print("Hello! I'm a simple chatbot. How can I help you today?")
    print("Type 'quit' or 'bye' to exit.")

    while True:
        user_input = input("You: ").lower() # Get user input and convert to lowercase

        if "quit" in user_input or "bye" in user_input:
            print("Chatbot: Goodbye! Have a great day!")
            break
        elif "hello" in user_input or "hi" in user_input or "hey" in user_input:
            print("Chatbot: Hello there! Nice to talk to you.")
        elif "how are you" in user_input or "how r u" in user_input:
            print("Chatbot: I'm just a program, but I'm functioning well! Thanks for asking.")
        elif "your name" in user_input or "What is ur name" in user_input or "wt is ur name" in user_input:
            print("Chatbot: I don't have a name. I'm a simple chatbot.")
        elif "help" in user_input:
            print("Chatbot: I can answer basic questions about greetings, my name, and how I am. Try asking me something simple!")
        else:
            print("Chatbot: I'm sorry, I don't understand that yet. Can you rephrase?")

if __name__ == "__main__":
    simple_chatbot()
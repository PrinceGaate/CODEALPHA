import nltk
from nltk.chat.util import Chat, reflections

# Define a set of simple responses
pairs = [
    [
        r"my name is (.*)",
        ["Hello %1, how are you today?",]
    ],
    [
        r"hi|hey|hello",
        ["Hello", "Hey there",]
    ],
    [
        r"what is your name?",
        ["I am a chatbot created by [Your Name]. You can call me ChatBot!",]
    ],
    [
        r"how are you?",
        ["I'm doing good. How about you?",]
    ],
    [
        r"sorry (.*)",
        ["It's okay", "No problem",]
    ],
    [
        r"I am fine",
        ["Great to hear that!",]
    ],
    [
        r"quit",
        ["Bye! Have a great day!", "Goodbye! See you soon!"],
    ],
    [
        r"(.*)",
        ["I'm sorry, I don't understand that.", "Can you please clarify?",]
    ]
]

# Create the chatbot
chatbot = Chat(pairs, reflections)

def start_chat():
    print("Hello! I'm a simple chatbot. Type 'quit' to exit.")
    while True:
        user_input = input("You: ").lower()
        if user_input == 'quit':
            print("ChatBot: Bye! Have a great day!")
            break
        response = chatbot.respond(user_input)
        print(f"ChatBot: {response}")

if __name__ == "__main__":
    start_chat()

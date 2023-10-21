# importin the needed library

import nltk
from nltk.chat.util import Chat, reflections

# Define some rules for the chatbot
response = [
    (r'hi|hello|hey', ['Hello!', 'Hi there!', 'Hey!']),
    (r'how are you?', ['I am good, thanks!', 'I am just a chatbot. How can I help you?']),
    (r'what is your name?', ["hmmmmmm. You can call me Wilfred."]),
    (r'bye|goodbye', ['Goodbye!', 'See you later!', 'Have a great day!']),
    (r'what is today date|What time is it?', ["it is what it is 😂😂."]),
    (r'goodmorning', ['Morning to U!', 'What a beautiful DAy', '😊morning sunhine']),
    (r'goodnight', ['Have a sound rest..... shuttingdown!!!!!']),
]



# Create a chatbot instance
chatbot = Chat(response, reflections)


# create the logical for the bot
print("Hello! I'm your Wilfred your chatbot. You can start chatting with me. Type 'exit' to end the conversation.")
while True:
    user_input = input("You: ")
    if user_input.lower() == 'exit':
        print("Chatbot: Goodbye!")
        break
    else:
        response = chatbot.respond(user_input)
        print("Chatbot:", response)

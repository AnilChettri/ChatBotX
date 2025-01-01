import nltk
from nltk.chat.util import Chat, reflections
import random

# Ensure necessary NLTK resources are downloaded
nltk.download('punkt')
nltk.download('wordnet')

# Sample pairs of questions and responses for the chatbot
pairs = [
    (r"hi|hello|hey", ["Hello there!", "Hi, how can I help you today?", "Hey! How's it going?"]),
    (r"how are you?", ["I'm doing well, thank you!", "I'm great! How about you?"]),
    (r"what is your name?", ["I'm ChatBot, your assistant!", "I'm ChatBot. How can I assist you today?"]),
    (r"(.*) your name (.*)", ["I am ChatBot.", "My name is ChatBot, nice to meet you!"]),
    (r"happy new year", ["Happy New Year! Wishing you all the best in the coming year! 🎉", 
                         "Happy New Year! May this year bring you joy and success! 🎆"]),
    (r"(.*) (thanks|thank you)(.*)", ["You're welcome!", "Glad to be of help!"]),
    (r"myself (.*)", ["Nice to meet you, {0}!", "Hey {0}, it's a pleasure to learn more about you!"]),
    (r"(.*) (what|how) (is|are) (your|the) (.*)", ["Could you clarify that a bit?", "I'm not sure about that. Can you ask in another way?"]),
    (r"(.*)(help|assist)(.*)", ["Sure! What do you need help with?", "I'm here to assist. How can I help you today?"]),
    (r"bye|goodbye|see you", ["Goodbye! Have a great day!", "See you later! Take care!"]),
    (r"tell me a joke", ["Why don't skeletons fight each other? They don't have the guts! 😄",
                        "Why did the math book look sad? Because it had too many problems!"]),
    (r"(.*) (weather|temperature|forecast)(.*)", ["I can't check the weather right now, but you can check your local weather app!",
                                                   "Sorry, I can't provide the forecast, but I suggest checking a weather website!"]),
    (r"(.*) (like|love) (.*)", ["That's great to hear! I'm glad you like it!", "Awesome, it seems like you're really passionate about that!"]),
    (r"how can you help me?", ["I can assist you with questions, provide information, tell jokes, or just chat with you! What would you like to do?"]),
    (r"(.*)", ["Sorry, I didn't quite understand that. Could you rephrase?", 
               "I'm not sure about that. Can you ask something else?", 
               "Hmm, I don't have an answer for that. Could you try asking differently?"])
]

# Create a Chat object
chatbot = Chat(pairs, reflections)

# Function to predict the next query (basic prediction for demonstration)
def predict_next_question():
    possible_questions = [
        "How are you today?",
        "Can you tell me a joke?",
        "What's the weather like?",
        "What can you do for me?",
        "Tell me something interesting."
    ]
    return random.choice(possible_questions)

# Function to get the bot's response
def get_bot_response(user_input):
    # Handle introductions and greetings more friendly
    if "myself" in user_input.lower():
        name = user_input.lower().replace("myself", "").strip()
        response = chatbot.respond(user_input)
        response = f"Nice to meet you, {name.capitalize()}!"  # Fixing the response to sound natural
    elif user_input.lower() == "happy new year":
        response = chatbot.respond(user_input)
        next_question = predict_next_question()  # Predict next question after Happy New Year
        response += "\n\nBy the way, here's a question you might ask next: " + next_question
    else:
        response = chatbot.respond(user_input)

    # If the bot doesn't understand, offer friendly rephrasing or alternative responses
    if response is None:
        response = random.choice([
            "Oops, I didn't quite catch that. Could you rephrase it for me?",
            "Sorry, I didn't understand. Could you ask again in a different way?",
            "Hmm, that doesn't make sense to me. Can you clarify?"
        ])
    
    return response

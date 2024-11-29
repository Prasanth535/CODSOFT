import random
import datetime

def chatbot():
    # Predefined responses
    responses = {
        "greeting": ["Hello! How can I assist you today?", "Hi there! How's it going?", "Hey! What can I do for you?"],
        "farewell": ["Goodbye! Have a great day!", "See you later! Take care.", "Bye! Feel free to chat anytime."],
        "how_are_you": [
            "I'm just a program, but I'm doing great! How about you?",
            "Feeling helpful as always! How can I assist you today?",
        ],
        "name_query": ["I'm Chatbot, your friendly assistant.", "They call me Chatbot. What's your name?"],
        "weather": [
            "I can't check the weather yet, but you can try a weather app.",
            "Weather forecasting isn't my skill yet, but it's a great day to learn something new!"
        ],
        "thanks": ["You're welcome!", "Glad I could help!", "No problem at all!"],
        "time": [
            "Current time is {time}.",
            "It's currently {time}.",
            "The time right now is {time}.",
        ],
        "math": [
            "The result is {result}.",
            "Your answer is {result}.",
            "After calculating, I got {result}."
        ],
        "joke": [
            "Why don't scientists trust atoms? Because they make up everything!",
            "Why did the math book look sad? Because it had too many problems.",
            "What do you get when you cross a snowman and a vampire? Frostbite!"
        ],
        "fact": [
            "Did you know? Honey never spoils. Archaeologists have found pots of honey in ancient tombs that are over 3000 years old and still edible.",
            "Here's a fact: A day on Venus is longer than a year on Venus.",
            "Fact for you: An octopus has three hearts and blue blood."
        ],
        "unknown": [
            "I'm not sure how to respond to that. Could you try asking something else?",
            "Hmm, I didn't quite get that. Can you rephrase it?"
        ]
    }

    print("Chatbot: Hi there! I'm your advanced chatbot. Ask me anything or type 'exit' to leave the chat.")

    while True:
        user_input = input("You: ").strip().lower()
        
        # Exit condition
        if "exit" in user_input:
            print(random.choice(responses["farewell"]))
            break

        # Greeting responses
        elif any(greet in user_input for greet in ["hello", "hi", "hey"]):
            print(random.choice(responses["greeting"]))

        # How are you responses
        elif "how are you" in user_input:
            print(random.choice(responses["how_are_you"]))

        # Name query responses
        elif "your name" in user_input or "who are you" in user_input:
            print(random.choice(responses["name_query"]))

        # Weather related responses
        elif "weather" in user_input:
            print(random.choice(responses["weather"]))

        # Thanks responses
        elif any(thanks in user_input for thanks in ["thanks", "thank you"]):
            print(random.choice(responses["thanks"]))

        # Current time responses
        elif "time" in user_input:
            current_time = datetime.datetime.now().strftime("%H:%M:%S")
            print(random.choice(responses["time"]).format(time=current_time))

        # Math calculation responses
        elif any(operator in user_input for operator in ["+", "-", "*", "/"]):
            try:
                expression = ''.join([char if char in "0123456789+-*/" else '' for char in user_input])
                result = eval(expression)
                print(random.choice(responses["math"]).format(result=result))
            except Exception as e:
                print("Oops! Something went wrong while doing the math.")

        # Joke responses
        elif "joke" in user_input:
            print(random.choice(responses["joke"]))

        # Fun facts responses
        elif "fact" in user_input:
            print(random.choice(responses["fact"]))

        # Unknown responses
        else:
            print(random.choice(responses["unknown"]))


# Run the chatbot
chatbot()


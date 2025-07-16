import spacy

# Load language model
nlp = spacy.load("en_core_web_sm")

# Simple chatbot logic
def chatbot():
    print("ChatBot: Hello! Ask me anything. Type 'exit' to quit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            print("ChatBot: Goodbye!")
            break
        doc = nlp(user_input)
        if "weather" in user_input:
            print("ChatBot: I recommend checking OpenWeatherMap for the latest weather.")
        elif "name" in user_input:
            print("ChatBot: I'm a simple Python chatbot built using spaCy.")
        else:
            print("ChatBot: Sorry, I didn't understand that.")

chatbot()

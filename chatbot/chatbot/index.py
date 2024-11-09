import re
def chatbot_response(user_input):
    user_input = user_input.lower()  # Convert to lowercase to make matching case-insensitive
    if re.search(r"\bhello\b|\bhi\b|\bhey\b", user_input):
        return "Hello! "
     # Response to 'how are you?'
    elif re.search(r"\b how are you\b", user_input):
        return "I'm just a bot, but I'm doing great! How about you?"
    elif re.search(r"\bgood\b", user_input):
        return "ok :-)"
    elif re.search(r"\bwhat is your name\b", user_input):
        return "My name is chatbot!Do you like that?"
    elif re.search(r"\bno\b", user_input):
        return "ok! You can suggest me a good name"
    elif re.search(r"\balexa\b", user_input):
        return "It sounds good! My name is alexa! how can i assist you?"
    elif re.search(r"\bfeedback\b", user_input):
        return "enter 'satisfied' or 'dissatified'"
    elif re.search(r"\bsatisfied\b", user_input):
        return "Thank you for your positive feedback!Have a nice day :-)"
    elif re.search(r"\bdissatified\b", user_input):
        return "Thank you for your feedback!I am so sorry you had a bad experience with us :-("
    elif re.search(r"\bwho is the father of ai\b", user_input):
        return " John McCarthy"
    elif re.search(r"\bwhat is mean by agi\b", user_input):
        return "artificial geneal intelligence"
    elif re.search(r"\bwhat is mean by asi\b", user_input):
        return "artificial super intellience"
    elif re.search(r"\bassalamualaikum\b", user_input):
        return "walaikumassalam"
    # Response to 'what can you do?'
    elif re.search(r"\bwhat can you do\b|\bwhat do you do\b", user_input):
        return "I can help with basic queries like greetings, answering simple questions, or just having a casual chat!"
# Farewell responses
    elif re.search(r"\bbye\b|\bexit\b|\bquit\b", user_input):
        return "Goodbye! & don't forget to give feedback for our conversation for feedback review 'type' feedback "
        # Default fallback response
    else:
        return "I'm sorry, I didn't quite understand that. Could you please rephrase?"# Main function to keep the chatbot running
def chatbot():
    print("Chatbot: Hello! Type 'exit' to end the conversation.")
    while True:
        user_input = input("You: ")
        if re.search(r"\bsatisfied\b|\bdissatisfied\b", user_input.lower()):
            print("Chatbot: " + chatbot_response(user_input))
            break
        else:
            print("Chatbot: " + chatbot_response(user_input))
if __name__ == "__main__":
    chatbot()

    #import re 
    #run the code in python environment.
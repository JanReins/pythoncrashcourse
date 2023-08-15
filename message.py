def messages(text_messages, sent_messages):
    while text_messages:
        sending_message = text_messages.pop()
        print(f"Sending text message: {sent_message}")

        sent_messages.append(sending_message)
def show_message(sent_messages):
    for message in sent_messages:
        print(message)





text_messages = [
    "Hey, how's it going?",
    "I'll be there in 5 mins.",
    "Movie night this weekend?",
    "Happy to help!",
    "See you soon!",
    "Running late, sorry!",
    "Great news – promotion!",
    "Need your opinion.",
    "Check this out: 🤣",
    "Can't make it, sorry.",
]

sent_message = []

messages(text_messages, sent_message)
show_message(text_messages)
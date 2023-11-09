def send_messages(text_messages, sent_messages):
    while text_messages:
        sending_message = text_messages.pop()
        print(f"Sending text message: {sending_message}")
        sent_messages.append(sending_message)




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

send_messages(text_messages, sent_message)

print(text_messages)
print("\n", sent_message)
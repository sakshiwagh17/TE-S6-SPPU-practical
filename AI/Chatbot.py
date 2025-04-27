from tkinter import *

chat = Tk()
chat.title("Chatbot")

# Function to handle user input and bot responses
def send():
    message = "You: " + e.get()  # Get the user's message
    txt.insert(END, message + '\n')  # Display user's message in the chatbox
    user = e.get().lower()  

    # Bot's responses based on user input
    if user == 'hello':
        txt.insert(END, "Bot: Hi\n")
    elif user in ['hi', 'hii', 'hiii']:
        txt.insert(END, "Bot: Hello\n")
    elif user == 'how are you?':
        txt.insert(END, "Bot: I am fine, and you?\n")
    elif user in ['fine', 'i am good', 'i am doing good']:
        txt.insert(END, "Bot: Great! How can I help you?\n")
    else:
        txt.insert(END, "Bot: Sorry! I am not getting you\n")

# Create a Text widget for displaying chat
txt = Text(chat, height=15, width=50)
txt.grid(row=0, column=0, columnspan=2)

# Create an Entry widget for user input
e = Entry(chat, width=80)
e.grid(row=1, column=0)

send_button = Button(chat, text="Send", command=send)
send_button.grid(row=1, column=1)


chat.mainloop()

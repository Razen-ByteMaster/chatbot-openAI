import openai
import tkinter as tk
from tkinter import scrolledtext, messagebox

openai.api_key = ""  # Enter your API Key Please ❤


def chat_with_gpt(prompt):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo-0125", messages=[{"role": "user", "content": prompt}]
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")
        return "Error occurred. Please try again."


def send_message():
    user_input = user_input_field.get()
    if user_input.lower() in ["quit", "exit", "bye"]:
        root.quit()
    else:
        chat_window.config(state=tk.NORMAL)
        chat_window.insert(tk.END, f"You: {user_input}\n")
        response = chat_with_gpt(user_input)
        chat_window.insert(tk.END, f"Chatbot: {response}\n\n")
        chat_window.config(state=tk.DISABLED)
        user_input_field.delete(0, tk.END)
        chat_window.see(tk.END)


root = tk.Tk()
root.title("Chat-Bot")
root.geometry("400x500")

chat_window = scrolledtext.ScrolledText(root, state="disabled", wrap=tk.WORD)
chat_window.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

user_input_field = tk.Entry(root, width=50)
user_input_field.pack(padx=10, pady=10, side=tk.LEFT, fill=tk.X, expand=True)
user_input_field.bind("<Return>", lambda event: send_message())

send_button = tk.Button(root, text="Send", command=send_message)
send_button.pack(padx=10, pady=10, side=tk.RIGHT)

root.mainloop()

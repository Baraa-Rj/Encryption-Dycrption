import tkinter as tk
from tkinter import messagebox

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']

def encrypt(text, shift):
    encrypted_text = ""
    for letter in text:
        if letter in alphabet:
            position = alphabet.index(letter)
            new_position = (position + shift) % 26
            encrypted_text += alphabet[new_position]
        else:
            encrypted_text += letter
    return encrypted_text

def decrypt(text, shift):
    decrypted_text = ""
    for letter in text:
        if letter in alphabet:
            position = alphabet.index(letter)
            new_position = (position - shift) % 26
            decrypted_text += alphabet[new_position]
        else:
            decrypted_text += letter
    return decrypted_text

def perform_action():
    direction = action.get()
    text = input_text.get("1.0", tk.END).strip().lower()
    shift = int(shift_value.get())

    if direction == "Encode":
        result = encrypt(text, shift)
    else:
        result = decrypt(text, shift)

    output_text.delete("1.0", tk.END)
    output_text.insert(tk.END, result)

def restart_program():
    input_text.delete("1.0", tk.END)
    output_text.delete("1.0", tk.END)
    shift_value.set("")

app = tk.Tk()
app.title("Caesar Cipher")
app.configure(bg="#f5f5f5")

# Create UI components with improved design
action_label = tk.Label(app, text="Action:", bg="#f5f5f5", font=("Arial", 12))
action_label.grid(row=0, column=0, padx=10, pady=10, sticky='e')

action = tk.StringVar(value="Encode")
action_menu = tk.OptionMenu(app, action, "Encode", "Decode")
action_menu.config(bg="#e0e0e0", font=("Arial", 12))
action_menu.grid(row=0, column=1, padx=10, pady=10, sticky='w')

input_label = tk.Label(app, text="Input Text:", bg="#f5f5f5", font=("Arial", 12))
input_label.grid(row=1, column=0, padx=10, pady=10, sticky='e')

input_text = tk.Text(app, height=5, width=40, font=("Arial", 12), bg="#ffffff", relief="solid", borderwidth=1)
input_text.grid(row=1, column=1, padx=10, pady=10, sticky='w')

shift_label = tk.Label(app, text="Shift Value:", bg="#f5f5f5", font=("Arial", 12))
shift_label.grid(row=2, column=0, padx=10, pady=10, sticky='e')

shift_value = tk.StringVar()
shift_entry = tk.Entry(app, textvariable=shift_value, font=("Arial", 12), bg="#ffffff", relief="solid", borderwidth=1)
shift_entry.grid(row=2, column=1, padx=10, pady=10, sticky='w')

output_label = tk.Label(app, text="Output Text:", bg="#f5f5f5", font=("Arial", 12))
output_label.grid(row=3, column=0, padx=10, pady=10, sticky='e')

output_text = tk.Text(app, height=5, width=40, font=("Arial", 12), bg="#ffffff", relief="solid", borderwidth=1)
output_text.grid(row=3, column=1, padx=10, pady=10, sticky='w')

process_button = tk.Button(app, text="Process", command=perform_action, bg="#4CAF50", fg="#ffffff", font=("Arial", 12), relief="solid", borderwidth=1)
process_button.grid(row=4, column=0, columnspan=2, pady=10)

restart_button = tk.Button(app, text="Restart", command=restart_program, bg="#f44336", fg="#ffffff", font=("Arial", 12), relief="solid", borderwidth=1)
restart_button.grid(row=5, column=0, columnspan=2, pady=10)

# Run the application
app.mainloop()

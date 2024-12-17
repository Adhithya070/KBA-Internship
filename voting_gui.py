import tkinter as tk
from tkinter import messagebox
import requests

API_URL = "http://localhost:5000/api/vote"

def cast_vote(candidate):
    try:
        response = requests.post(API_URL, json={"candidate": candidate})
        data = response.json()
        if response.status_code == 200:
            messagebox.showinfo("Success", data["message"])
        else:
            messagebox.showerror("Error", data["message"])
    except Exception as e:
        messagebox.showerror("Error", f"Could not connect to API: {e}")

def create_gui():
    root = tk.Tk()
    root.title("Voting System")

    instruction_label = tk.Label(root, text="Choose your candidate:", font=("Arial", 14))
    instruction_label.pack(pady=10)

    candidates = ["Candidate A", "Candidate B", "Candidate C"]
    for candidate in candidates:
        button = tk.Button(root, text=candidate, font=("Arial", 12), width=20, 
                           command=lambda c=candidate: cast_vote(c))
        button.pack(pady=5)

    root.mainloop()

if __name__ == "__main__":
    create_gui()

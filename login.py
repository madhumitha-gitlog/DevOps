import tkinter as tk
from tkinter import messagebox
def validate_login():
    username = username_entry.get()
    password = password_entry.get()
    if username == "admin" and password == "password":
        messagebox.showinfo("Login Successful", "Welcome, Admin!")
    else:
        messagebox.showerror("Login Failed", "Invalid username or password")
# Create the main window
root = tk.Tk()
root.title("Login Form")
# Create and place the username label and entry
tk.Label(root, text="Username").grid(row=0, column=0)
username_entry = tk.Entry(root)
username_entry.grid(row=0, column=1)
# Create and place the password label and entry
tk.Label(root, text="Password").grid(row=1, column=0)
password_entry = tk.Entry(root, show='*')
password_entry.grid(row=1, column=1)
# Create and place the login button
login_button = tk.Button(root, text="Login", command=validate_login)
login_button.grid(row=2, columnspan=2)
# Run the application
root.mainloop()

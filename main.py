import os
import tkinter as tk
from tkinter import messagebox

def shutdown(seconds):
    os.system(f"shutdown -s -t {seconds}")

def start_timer():
    try:
        time_amount = int(time_amount_var.get())
        time_unit = time_unit_var.get()

        if time_unit == "Minutes":
            seconds = time_amount * 60
        elif time_unit == "Hours":
            seconds = time_amount * 3600

        shutdown(seconds)
        messagebox.showinfo("Shutdown Timer", f"Your computer will shut down in {time_amount} {time_unit.lower()}(s).")
    except ValueError:
        messagebox.showerror("Invalid Input", "Please select a valid time amount and unit.")

def cancel_shutdown():
    os.system("shutdown -a")
    messagebox.showinfo("Shutdown Timer", "Shutdown has been canceled.")

# Create the main window
root = tk.Tk()
root.title("Shutdown Timer")
root.geometry("300x200")

# Create the input label
label = tk.Label(root, text="Select time until shutdown:")
label.pack(pady=10)

# Create the time amount dropdown menu
time_amount_var = tk.StringVar(root)
time_amount_var.set("1")  # Default value
time_amount_menu = tk.OptionMenu(root, time_amount_var, *[str(i) for i in range(1, 61)])
time_amount_menu.pack(pady=5)

# Create the time unit dropdown menu
time_unit_var = tk.StringVar(root)
time_unit_var.set("Minutes")  # Default value
time_unit_menu = tk.OptionMenu(root, time_unit_var, "Minutes", "Hours")
time_unit_menu.pack(pady=5)

# Create the start button
start_button = tk.Button(root, text="Start Timer", command=start_timer)
start_button.pack(pady=5)

# Create the cancel button
cancel_button = tk.Button(root, text="Cancel Shutdown", command=cancel_shutdown)
cancel_button.pack(pady=5)

# Run the application
root.mainloop()

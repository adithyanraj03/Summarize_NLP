import tkinter as tk
from tkinter import ttk
import time

def simulate_loading():
    for i in range(1, 11):
        progress_bar['value'] = i * 10
        loading_label.config(text=f"Loading... {i * 10}%")
        root.update_idletasks()
        time.sleep(1)

    loading_label.config(text="Loading Complete")
    root.update_idletasks()
    time.sleep(1)
    root.destroy()

# Create the main window
root = tk.Tk()
root.title("Loading Screen")

# Create a progress bar
progress_bar = ttk.Progressbar(root, orient="horizontal", mode="determinate", length=300)
progress_bar.pack(pady=20)

# Create a label for displaying the loading status
loading_label = tk.Label(root, text="Loading... 0%")
loading_label.pack()

# Start loading simulation
simulate_loading()

# Start the GUI main loop
root.mainloop()
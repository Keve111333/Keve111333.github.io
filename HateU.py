import os
import random
import string

def generate_random_string(length):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for _ in range(length))

def create_large_text_file(file_path, num_characters):
    try:
        with open(file_path, 'w') as f:
            for _ in range(num_characters // 100):
                random_text = generate_random_string(100)
                f.write(random_text + "\n")
        print(f"Created file '{file_path}' with {num_characters} characters")
    except Exception as e:
        print(f"Error creating file: {e}")

# Get the path to the current user's desktop
desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")

# Specify the file name and number of characters (1 billion)
file_name = "IHateYou.txt"
file_path = os.path.join(desktop_path, file_name)
num_characters = 25000000000  # 1 billion characters

create_large_text_file(file_path, num_characters)

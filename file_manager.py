def save_message(message):
    try:
        with open("user_message.txt", "w") as file:
            file.write(message)
        print("Message saved successfully.")
    except Exception as e:
        print(f"Error saving message: {e}")

def read_message():
    try:
        print("Reading saved message")
        with open("user_message.txt", "r") as file:
            content = file.read()
            print(content)
    except FileNotFoundError:
        print("Error: File not found. Please save a message first.")
    except Exception as e:
        print(f"Error reading message: {e}")
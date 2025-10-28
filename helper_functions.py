def validate_input(user_input):
    if isinstance(user_input, str) and user_input.strip() != "":
        return True
    return False

def create_message(name, age, name_binary, age_binary):
    message = f"Hello {name}, you are {age} years old!\n"
    message = f"Name in binary: {name_binary}\n"
    message = f"Age in binary: {age_binary}"
    return message

def convert_to_binary(text):
    if str(text).isdigit():
        return bin(int(text))
    else:
        binary_list = []
        for char in text:
            binary_char = bin(ord(char))[2:]
            binary_char = binary_char.zfill(8)
            binary_list.append(binary_char)
        return " ".join(binary_list)

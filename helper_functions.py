def validate_input(user_input):
    if isinstance(user_input, str) and user_input.strip() != "":
        return True
    return False

def ceate_message(name, age, name_binary, age_binary):
    message = f"Hello {name}, you are {age} years old!\n"
    message = f"Name in binary: {name_binary}\n"
    message = f"Age in binary: {age_binary}"
    return message
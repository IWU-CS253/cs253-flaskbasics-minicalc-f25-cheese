def average_length(user_string):
    words = user_string.split()
    if words:  # Ensure the string is not empty
        avg = sum(len(word) for word in words) / len(words)
    else:
        avg = 0
    return avg

def reverse_string(user_string):
    reversed_string = user_string[::-1]
    return reversed_string

def word_counter(user_string):
    return len(user_string.split())

def total_characters(user_string):
    character_count = 0
    for word in user_string.split():
        character_count += len(word)
    return character_count
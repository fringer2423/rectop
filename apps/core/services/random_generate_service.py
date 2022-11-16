import random
import string


def generate_random_string_service(length):
    letters = string.ascii_letters
    rand_string = ''.join(random.choice(letters) for i in range(length))
    print("Random string of length", length, "is:", rand_string)
    return rand_string


def generate_random_number_service(length):
    letters = string.digits
    rand_number = ''.join(random.choice(letters) for i in range(length))
    print("Random string of length", length, "is:", rand_number)
    return rand_number

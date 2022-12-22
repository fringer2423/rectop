import random
import string


def _generate_random(length, letters):
    return ''.join(random.choice(letters) for i in range(length))


def generate_random_string_service(length):
    letters = string.ascii_letters
    return _generate_random(length, letters)


def generate_random_number_service(length):
    letters = string.digits
    return _generate_random(length, letters)

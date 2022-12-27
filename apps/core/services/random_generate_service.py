import random
import string
from enum import Enum


class Letters(Enum):
    DIGITS: str = string.digits
    ASCII: str = string.ascii_letters


def _generate_random(length: int, letters: str) -> str:
    return ''.join(random.choice(letters) for i in range(length))


def generate_random_string_service(length: int) -> str:
    return _generate_random(length, string.ascii_letters)


def generate_random_number_service(length: int) -> str:
    return _generate_random(length, string.digits)

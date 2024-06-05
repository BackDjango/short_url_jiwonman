import string
import random


class Base62:
    def encode(self):
        characters = string.ascii_letters + string.digits
        key_length = 6
        return "".join(random.choice(characters) for _ in range(key_length))

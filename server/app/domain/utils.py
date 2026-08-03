import random
import string

def generate_short_code(length: int = 6) -> str:
    char = string.ascii_letters + string.digits
    return "".join(random.choice(char) for _ in range(length))
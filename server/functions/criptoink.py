import string
import random

def get_next_verification_token():
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(32))
    return result_str


def hand_shake(instance):
    return None

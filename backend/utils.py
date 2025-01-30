# this is basically for checking the password strength, didn't want to muddle up the code
from pyzxcvbn import zxcvbn
import random
import string

def check_password_strength(password):
    """
    Check password strength using zxcvbn.

    Returns:
        - Strength Score (0 to 4)
        - Feedback message (suggestions for improvement)
    """
    result = zxcvbn(password)

    strength_levels = ["Very Weak", "Weak", "Medium", "Strong", "Very Strong"]
    strength = strength_levels[result["score"]]

    feedback = result["feedback"]["suggestions"] or ["Good password choice!"]

    return strength, feedback

def generate_password():
    """
    Generate a completely random, strong password between 8 and 16 characters.

    Returns:
        - str: Generated password.
    """
    length = random.randint(8, 16)  # Random length between 8 and 16

    all_chars = string.ascii_letters + string.digits + "!@#$%^&*()-_=+[]{}|;:,.<>?/"

    # Generate a completely random password
    password = "".join(random.choices(all_chars, k=length))

    return password

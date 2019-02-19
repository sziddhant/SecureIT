import random


def generate_otp():
    otp = random.randint(1000, 10000)
    print(otp)
    return otp

from random import choice,randint

OTP=lambda len: "".join([str(randint(0,9)) for _ in range(len)])

print("Ranom 4 length OTP is  : ",OTP(4))
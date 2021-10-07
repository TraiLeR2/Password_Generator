def generator():
    from random import randint
    small = "abcdefghijklmnopqrstuvwxyz"
    large = small.upper()
    numbers = "1234567890"
    special = "!@#$%^&*()=_+-?"
    password_together = small + large + numbers + special

    password_length = int(input("Insert length of password > "))
    password = ""
    length = 0

    if password_length < 6:
        print("Choose from over 6 characters!")
    else:
        while length < password_length:
            password = password + password_together[randint(0,len(password_together)-1)]
            length += 1
        print("Generated password is > {0}".format(password))

print("~!~ This Tool Has Been Created By Idan - TraiLeR ~!~")
print("All Credit reserved for Idan Malihi\n")

generator()
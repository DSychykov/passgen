import random
import string
gps = []
def generate_passw(min_length):
    letters = string.ascii_letters
    letters_list = list(letters.strip(" "))
    digits = string.digits
    digits_list = list(digits.strip(" "))
    if min_length < 10:
        print("the password is too short")
    else:
        while True:
            gp = random.choice(digits_list)
            gp2 = random.choice(letters_list)
            gps.append(gp)
            gps.append(gp2)
            if len(gps) < min_length:
                continue
            else:
                break
        separator = ""
        mypassword = separator.join(gps)
        print(mypassword)

generate_passw(16) #only even numbers
print(len(gps))
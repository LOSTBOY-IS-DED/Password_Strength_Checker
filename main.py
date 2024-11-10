import string 
import getpass

def check_pwd():
    password = getpass.getpass("Enter password: ")
    strength = 0
    remarks = ""
    lower_count = upper_count = num_count = wspace_count = special_count = 0

    for char in password:
        if char in string.ascii_lowercase:
            lower_count += 1
        elif char in string.ascii_uppercase:
            upper_count += 1
        elif char in string.digits:
            num_count += 1
        elif char == ' ':
            wspace_count += 1
        else:
            special_count += 1

    if lower_count >= 1:
        strength += 1
    if upper_count >= 1:
        strength += 1
    if num_count >= 1:
        strength += 1
    if wspace_count >= 1:
        strength += 1
    if special_count >= 1:
        strength += 1
    
    if strength == 1:
        remarks = "Very Bad Password!!! Maa chudao !!!"
    elif strength == 2:
        remarks = "Bad Password!!! Bhag Madarchod !!!"
    elif strength == 3:
        remarks = "Good Password!!! Thik krle bhai !!!"
    elif strength == 4:
        remarks = "Great Password!!! gand fati padi hai bc !!!"
    elif strength == 5:
        remarks = "Great Password!!! Aree bhenchod !!!"

    print('Your password has : ')
    print(f'{lower_count} lowercase letters')
    print(f'{upper_count} uppercase letters')
    print(f'{num_count} numeric characters')
    print(f'{wspace_count} whitespace characters')
    print(f'{special_count} special characters')
    print(f'Password Strength : {strength}')
    print(f'Hint : {remarks}')

def ask_for_another_password(another_pwd=False):
    while True:
        choice = input("Do you want to enter another password? [Y/N]: " if another_pwd else "Do you want to check a password? [Y/N]: ")
        if choice.lower() == 'y':
            return True
        elif choice.lower() == 'n':
            return False
        else:
            print("Invalid input. Please enter 'Y' or 'N'.")

if __name__ == "__main__":
    print("Welcome to Password Checker")
    while ask_for_another_password():
        check_pwd()

##################################################################################################################################################
#   __    __    _____      __     ______    ________     __________     ______    __    ___   __________    _________    __          _______     #
#  |  |  |  |  |     \    |  |   /   ___\  /   ___  \   /   ____   \   /   ___\  |  |  /  /  /   ____   \  /   ____  \  |  |        |  _____|    #
#  |  |  |  |  |  |\  \   |  |  /   /      |  |___|  |  |   |__|   |  /   /      |  | /  /   |   |__|   |  |  |____| |  |  |        |  |____     #
#  |  |  |  |  |  | \  \  |  | |   |       |   _____/   |  ______  | |   |       |  |/  /    |  ______  |  |  _______/  |  |        |       |    #
#  |  |  |  |  |  |  \  \ |  | |   |       |   __  \    |  |    |  | |   |       |  |\  \    |  |    |  |  |   ____  \  |  |        |  _____|    #
#  |  |__|  |  |  |   \  \|  |  \   \____  |  |  \  \   |  |    |  |  \   \____  |  | \  \   |  |    |  |  |  |____| |  |  |_____   |  |____     #
#   \______/   |__|    \_____|   \______/  |__|   \__\  |__|    |__|   \______/  |__|  \__\  |__|    |__|  \_________/  |________|  |_______|    #
#                                                                                                                                                #
#  This program has been created by nalili.                                                                 Contact me : nalili0000007@gmail.com #
#  Optimized by SH4FS0c13ty.                                                                                                                     #
##################################################################################################################################################
# Information:            #
#       Version: V1.2     #
#       Date: 01/10/2021  #
###########################  

import random

def random_number(length, strength): # Generate random numbers that will be used to generate the password afterward
    list_random = []
    for i in range(0, length):
        if strength == 1:
            list_random.append(random.randint(0, 51)) # Alphabetic characters [a-Z]
        elif strength == 2:
            list_random.append(random.randint(0, 61)) # Alphanumerical characters [A-Z0-9]
        elif strength == 3:
            list_random.append(random.randint(0, 102)) # Alphanumerical + special characters [a-Z0-9&é"'(-è_çà)=~#{[|`\^@]}°+^$ù*,;:!¨£%µ?./§]
    return list_random

def replace_numbers(nb_list):
    characters_string = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789&é\"'(-è_çà)=~#{[|`\^@]}°+^$ù*,;:!¨£%µ?./§"
    password = ""
    for x in nb_list:
        password += characters_string[x]
    return password

def main():
    print("How many characters must your password be composed of?")
    try:
        nbchar = int(input(">>> "))
    except ValueError:
        print("The value you entered is not a valid number.")
        return
    print("\nWhich characters should your password be composed of?")
    print("1 (Weak) - Alphabetic characters [a-Z]")
    print("2 (Medium) - Alphanumerical characters [A-Z0-9]")
    print("3 (Strong) - Alphanumerical + special characters [a-Z0-9&é\"'(-è_çà)=~#{[|`\^@]}°+^$ù*,;:!¨£%µ?./§]")
    try:
        strength = 0
        while strength < 1 or strength > 3:
            strength = int(input(">>> "))
            if strength < 1 or strength > 3:
                print("Please enter a number between 1 and 3.")
    except ValueError:
        print("The value you entered is not a valid number.")
        return
    list_random = random_number(nbchar, strength)
    password = replace_numbers(list_random)
    print("\nYour newly generated password is:")
    print(password, "\n")
    input("Press ENTER to close the program ...")
    
if __name__ == "__main__":
    main()

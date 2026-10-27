#!/usr/bin/python3

import time
import string
import secrets

def user_input():
    how_many = 0
    the_length = 0

    
    print("Enter how many passwords you want to generate.")
    
    the_amount_to_generate = int(input(">> "))
    how_many += the_amount_to_generate
    
    print("Enter how long the passwords should be.")
    
    the_length_to_generate = int(input(">> "))
    the_length += the_length_to_generate

    
    validation(how_many, the_length)



def validation(how_many, the_length):
    if how_many <= 0 or the_length <= 0:
        print("\nOne, or both two of these conditions were met: \n1) The number of passwords was entered as 0 or lower. \n2) The length of the passwords was entered as 0 or lower. \nNothing to generate.")
    
    else:
        password_generation(how_many, the_length)



def password_generation(how_many, the_length):
    the_symbols = string.ascii_letters + string.digits + string.punctuation
    
    the_characters_for_password = []
    how_many = how_many
    the_length = the_length
    
    start = time.perf_counter()
    
    match how_many:
        case 1:
            print("\nPassword Generated:-")
        
        case _:
            print("\nPasswords Generated:-")
    
    
    for p in range(how_many):
        for l in range(the_length):
            the_characters_for_password.append(secrets.choice(the_symbols))
                        
        print(f"The password: {''.join(the_characters_for_password)}")
        the_characters_for_password.clear()
    
    end = time.perf_counter()
    print(f"\nTime To Execute The Random Password Generation Algorithm: {end - start} seconds.")



def main():
    try:
        user_input()
    
    except KeyboardInterrupt:
        print("KEYBOARD INTERRUPT!\nPROGRAM INTERRUPTED BY USER!")

    except ValueError:
        print("ERROR: EXCEPTED VALUE AS INTEGER! GOT NONE!")



if __name__ == "__main__":
    main()

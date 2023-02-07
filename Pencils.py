# Second player is always a bot

import random
import string

def request_initial_number_of_pencils():
    exit_bool = False
    while exit_bool == False:
        user_input = input()
        if not user_input.isdigit():
            print("The number of pencils should be numeric")
            exit_bool = False
        elif int(user_input) < 1:
            print("The number of pencils should be positive")
            exit_bool = False
        else:
            exit_bool = True
    return int(user_input)

def choose_who_will_play_first():
    exit_bool = False
    while exit_bool == False:
        user_input = input()
        if string.capwords(user_input) not in ["John","Jack"]:
            print("Choose between 'John' and 'Jack'")
            exit_bool = False
        else:
            exit_bool = True
    return user_input

def examine_pencils_requested(num_pencils_left):
    exit_bool = False
    while exit_bool == False:
        user_input = input()
        if user_input not in string.digits:
            print("Possible values: '1', '2' or '3'")
            exit_bool = False
        elif int(user_input) not in range(1,4):
            print("Possible values: '1', '2' or '3'")
            exit_bool = False
        elif int(user_input) > num_pencils_left:
            print("Too many pencils were taken")
            exit_bool = False
        else:
            exit_bool = True
    return int(user_input)

def bot_request_pencils(num_pencils_left):
    if (num_pencils_left % 4) == 0:
        return 3
    n = 1
    while True:
        next_num_sequence = 3 + (4 * (n - 1))
        if num_pencils_left == next_num_sequence:
            return 2
        if num_pencils_left < next_num_sequence:
            break
        else:
            n += 1

    n = 1
    while True:
        next_num_sequence = 2 + (4 * (n - 1))
        if num_pencils_left == next_num_sequence:
            return 1
        if num_pencils_left < next_num_sequence:
            break
        else:
            n += 1

    while True:
        next_num_sequence = 5 + (4 * (n - 1))
        if num_pencils_left == next_num_sequence:
            return random.randint(1, 3)
        if num_pencils_left < next_num_sequence:
            break
        else:
            n += 1
    return 1

print("How many pencils would you like to use:")
number_of_pencils = request_initial_number_of_pencils()

print("Who will be the first (John, Jack):")
who_is_first = choose_who_will_play_first()
print(number_of_pencils * "|")

who_is_next = who_is_first
pencils_left = number_of_pencils
while pencils_left > 0:
    if who_is_next == "Jack":
        print("Jack's turn:")
        who_is_next = "John"
    else:
        print("John's turn!")
        who_is_next = "Jack"

    if who_is_next == "Jack":
        pencils_taken = examine_pencils_requested(pencils_left)
    else:
        pencils_taken = bot_request_pencils(pencils_left)
        print(pencils_taken)
    pencils_left -= pencils_taken
    if pencils_left > 0:
        print(pencils_left  * "|")
    else:
        print(f"{who_is_next} won!")

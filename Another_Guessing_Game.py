import random
list_of_numbers = []
for x in range(1,101):
    list_of_numbers.append(x)
    my_number = random.choice(list_of_numbers)
print ("I'm thinking of a number between 0 and 100")
x = 101
number_of_guesses = 0
while x != my_number:
    guessed_number = input("Enter your guess: ")
    if int(guessed_number) == int(my_number):
        print ("Wow you have guessed my number correctly! You win!")
        x = my_number
        number_of_guesses += 1
    elif int(guessed_number) < int(my_number):
        print ("Aww. Your guess is to low.")
        number_of_guesses += 1
    else:
        print ("Aww. Your guess is to high.")
        number_of_guesses += 1
print ("It took you this many guesses:" + str(number_of_guesses))
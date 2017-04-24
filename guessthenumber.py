#beginner notes throughout

# STEP 1
# not_guessed = True
# while not_guessed:
#     guess_a_number = raw_input("Guess a number between 1 and 10.")
#     if (int(guess_a_number) == random_number):
#         print "You guessed the number!";
#         not_guessed = False; #if you guess wrong it loops until you guess right

# not_guessed = True
# secret_number = 5
# while not_guessed:
#         guess_number = raw_input("I am thinking of a number between 1 and 10. What's the number?")
#         if (int(guess_number) == 5):
#             print "You win!"
#             not_guessed = False #make sure false is within if statement
#         else:
#             print "Nope! Try again!"


#your mistake was that you made assigned secret_number as raw input thus ending the loop


#STEP 2
# not_guessed = True
# secret_number = 5
# while not_guessed:
#         guess_number = raw_input("I am thinking of a number between 1 and 10. What's the number?")
#         if (int(guess_number) == 5):
#             print "You win!"
#             not_guessed = False #make sure false is within if statement
#         else:
#             if (int(guess_number) > 5):
#                 #print "Nope! " + guess_number + "  is too high!" #longer way
#                 print "Nope! %d is too high!" % (int(guess_number))
#             if (int(guess_number) < 5 ):
#                 #print "Nope! " + guess_number + " is too low!" #longer way
#                 print "Nope! %d is too low!" %(int(guess_number))


#STEP 3
# import random
# my_random_number = random.randint(1, 10)
# not_guessed = True
# while not_guessed:
#         guess_number = raw_input("I am thinking of a number between 1 and 10. What's the number?")
#         if (int(guess_number) == my_random_number):
#             print "You win!"
#             not_guessed = False #make sure false is within if statement #False stops the loop
#         else:
#             if (int(guess_number) > my_random_number):
#                 print "Nope! " + guess_number + "  is too high!"
#             if (int(guess_number) < my_random_number ):
#                 print "Nope! " + guess_number + " is too low!"


#STEP 4
# import random
# my_random_number = random.randint(1, 10)
# #tries = 0 #user starts with zero so set to zero
# tries = 5
# while tries > 5: #while this condition is true less than 5 then
#     guess_number = raw_input("I am thinking of a number between 1 and 10. What's the number?")
#     # print ("You have %d guesses left") % (tries)
#     if (int(guess_number) == my_random_number):
#         print "You win!"
#     else:
#         if (int(guess_number) > my_random_number):
#             #print "Nope! " + guess_number + "  is too high!"
#             print "Nope! %d is too high!" %(int(guess_number))
#             tries -= 1 #decreases by 1
#         if (int(guess_number) < my_random_number ):
#             #print "Nope! " + guess_number + " is too low!"
#             print "Nope! %d is too low!" %(int(guess_number))
#             tries -= 1
#     tries = tries + 1 #remember where you started; tries = 0 so can't subtract
#     if tries == 5:
#         print "You lose!"


import random
secret_number = random.randint(1,10);
# print secret_number

# Hard code for now
# secret_number = 5
keep_asking = True
number_of_guess = 5
while (keep_asking):
	if(number_of_guess == 0):
		play_again = raw_input("You ran out of guesses. Would you like to play again. Y or N?")
		if(play_again == "Y"):
			number_of_guess = 5
		elif(play_again == "N"):
			keep_asking = False;
			print "Goodbye, coward"
	else:
		print ("You have %d guesses left")  % (number_of_guess)
		guess_a_number = raw_input("Guess a number between 1 and 10.")
		if (int(guess_a_number) == secret_number):
			print "You guessed the number!";
			keep_asking = False;
			# number_of_guess = 0;

		elif (int(guess_a_number) < secret_number):
			print "%d is too low" % (int(guess_a_number))
			# number_of_guess = number_of_guess - 1
			# number_of_guess += 1
		elif(int(guess_a_number) > secret_number):
			print "%d is too high" % (int(guess_a_number))
			# number_of_guess = number_of_guess - 1
		number_of_guess -= 1





# count = 5
# while count > 0:
#     print (count)
#     count = count - 1
#     count -= 1 <same as previous line>
#
# count = 0
#
# while count < 5:
#     print count
#     count = count + 1
#     count += 1

#STEP 5
#if the user reaches more than 5 tries, then prompt "Play again? Y/N"
#if the user input == "Y"; reset the count so tries = 0
#if the user input == "N" ; print BYE!
#if user wins prompt "" tries = 0
#need a break statement; stops the loop

# import random
# user_cont = "Y" #outside of the while loop
# while user_cont == "Y":
#     my_random_number = random.randint(1, 10)
#     tries = 0 #user starts with zero so set to zero
#     #while loop promting user to play again or quit #need true and false statement
#     while tries <= 4: #while this condition is true less than 5 then
#         guess_number = raw_input("I am thinking of a number between 1 and 10. What's the number?")
#         if (int(guess_number) == my_random_number):
#             print "You win!"
#         else:
#             if (int(guess_number) > my_random_number):
#                 print "Nope! " + guess_number + "  is too high!"
#             if (int(guess_number) < my_random_number ):
#                 print "Nope! " + guess_number + " is too low!"
#         if tries == 4:
#             print "You lose!"
#         tries = tries + 1 #remember where you started; tries = 0 so can't subtract #keep in mind what this means in total; tries += 1
#     user_cont = raw_input ("Play again? Y or N") #make it the last line of the biggest while loop

# #question 1
# a_string = "This is a string"
# prac_string = ""
# for letter in a_string: #don't forget the colon!
#     #print(letter)
#     prac_string += letter.upper()
# print(prac_string)
#
# a_string = "This is a string"
# print a_string.upper()

#question 2
# a_string = "this is a string"
# print "a_string.capitalize (): " , a_string.capitalize()

# prac_string = ""
# for letter in a_string: #don't forget the colon!
#     #print(letter)
#     prac_string += a_string.capitalize()
# print(prac_string) #why is it repeating?
#
# #question 3
# a_string = "This is a string"
# print "".join(reversed(a_string))

# reverse_me = "I'm a string"
# print "".join(reversed(a_string))
#
# characters_from_string = []
# for character in reverse_me:
#     characters_from_string.append(character)
# characters_from_string.reverse()
# print ("").join(characters_from_string)

#string = hello
#list = [h][e][l]
#reverse list = [o][l]...

# new_String = reverse_me[::-1]

#can only reverse lists not strings
#strings are immutable

# a_string = "My name is Rob"
# new string = ""
# for i in range (0, len(a_string)):
#     #print letter
#     last_index = len(a_string)
# #     new_string += a_string[len(a_string) -1 - i]
# # print new_stringi
# new_string += a_string[letter_stepping_backwards]
# print new_string

#name = raw_input("WHAT IS YOUR NAME? ")

#Question 4 leetspeak #use a function?

#
# leet_string = "Leet"
# leet_string_as_list = list(leet_string)
# leet_speak = ""
# leetspeak_user = raw_input ("Enter text to translate into leetspeak: ").upper()
# # def leetspeak_user (string):
# for character in leet_string_as_list:
#     if(character.upper() == "A"):
#         leet_speak += "4"




#shift to highlight cmd shift l
#cmd z to undo

# leet_string = "Leet"
# leet_string_as_list = list(leet_string)
# leet_speak = ""
# for character in leet_string_as_list:
#     if(character.upper() == "A"):
#         leet_speak += "4"
#     elif(character.upper() == "E"):
#         leet_speak += "3"
#     else:
#         leet_speak += character
# etc.. so use if statements to translate

# leet_list = [
#     ["A", "4"]
#     etc..
#
# ]


# leet_string = "Leet"
# leet_string_as_list = list(leet_string)
# leet_speak = ""


#create a dictionary to translate



        # leet_string_as_list.remove(character)


        # elif (i == "E"):
        #     print "3"

# def double(str):
#     outstr = ''
#     for character in str:
#         outstr = outstr + char + char
#     return outstr

# Question 7 Long-long Vowels
#
# Given a word as a string, print the result of extending any long vowels to the length of 5. Examples:
#
# Good => Goooood
# Cheese => Cheeeeese
# Man => Man
# Spoon => Spooooon

# string_to_test = "Spoon"
# result = ""
# current =""
# previous = ""
#
# for i in range (0, len(string_to_test)):
#     current = string_to_test[i]
#     if (current == previous) and (current != "n"):
#         result = result + 4 * current
#     else:
#         result = result + current
#     previous  = current
# print result
#
# #set up a dictionary

#Question 8

def decrypt_function(encrypted_letter):
	try:
		number = encrypted_list.index(encrypted_letter)
	except ValueError:
		# Do this!
		decrpyted_message.append(encrypted_letter)
	else:
		decrpyted_message.append(decrpyted_list[number])

message = "lbh zhfg hayrnea jung lbh unir yrnearq!"
decrpyted = "abcdefghijklmnopqrstuvwxyz"
encrypted = "nopqrstuvwxyzabcdefghijklm"
message_list =  list(message)
decrpyted_list = list(decrpyted)
encrypted_list = list(encrypted)
decrpyted_message = []

for i in range(0,len(message_list)):
	decrypt_function(message_list[i])

final_decrypted_message = "".join(decrpyted_message)
print (final_decrypted_message)

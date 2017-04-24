# # #
#for question # 1dictionary
# #1 Print Elizabeth's phone number.
# #2 Add a entry to the dictionary: Kareem's number is 938-489-1234.
# #3 Delete Alice's phone entry.
# #4 Change Bob's phone number to '968-345-2345'.
# #5 Print all the phone entries.
# #6 In this exercise, are you using dynamic keys or fixed keys?
# #

#1
# # phonebook_dict = {
# #   'Alice': '703-493-1834',
# #   'Bob': '857-384-1234',
# #   'Elizabeth': '484-584-2923'
# # }
# #
# #2
# print (phonebook_dict["Elizabeth"])


# # phonebook_dict['Kareem'] = "938-489-1234"

 #3
# phonebook_dict.pop('Alice')
# del(phonebook_dict['Alice'])


# # #4
# # phonebook_dict["Bob"] = "968-345-2345"



#5 print all
# # print(phonebook_dict).values()
# # print (phonebook_dict)
# for key, value in phonebook_dic.iteries


#NOTES
# #using fixed keys: they're yellow (fixed) cause they're strings; white (dynamic)

# # get the second zomebie speed [::2 go through the list]
# #  print(zombie[1] ["speed"])

# # print (person["name"])  #contain all data within one variable #associative arrays

# # # zombiee = {}
# # # zombie['weapon'] = "axe"
# # # zombie['health'] = 100
# # # zombie['startX'] =
# # # zombie['startY'] =


#Exercise

# ramit = {
#   'name': 'Ramit',
#   'email': 'ramit@gmail.com',
#   'interests': ['movies', 'tennis'],
#   'friends': [
#     {
#       'name': 'Jasmine',
#       'email': 'jasmine@yahoo.com',
#       'interests': ['photography', 'tennis']
#     },
#     {
#       'name': 'Jan',
#       'email': 'jan@hotmail.com',
#       'interests': ['movies', 'tv']
#     }
#   ]
# }


# # 1. Write a python expression that gets the email address of Ramit.
# ramit_email = ramit["email"]
#print ramit_email

# # 2. Write a python expression that gets the first of Ramit's interests.
# ramit_first_interest = ramit['interests'][0]
#print ramit_first_interest


#
# # 3. Write a python expression that gets the email address of Jasmine.
# jasmine_email = ramit['friends'][0]["email"]
#print jasemine_email
#
# # 4. Write a python expression that gets the second of Jan's two interests.
# ramit_first_interest ['friends'][1]['interests'][1]


#Letter Summary

#Write a letter_histogram function that takes a word as its input, and
#returns a dictionary containing the tally of how many times each letter in
#the alphabet was used in the word. For example:

#1
# >>> letter_histogram('banana')
# {'a': 3, 'b': 1, 'n': 2}
# In this exercise, are you using dynamic keys or fixed keys?

# notes: dict() #returns an empty dictionary
#
# user_word = list(raw_input("Enter a word:"))
# empty_dictionary = {}
#
# for letter in user_word:
#     if i in empty_dictionary:
#         empty_dictionary += 1
#     else:
#         empty_dictionary = 1
#
# print empty_dictionary







# #using a function
#
# def letter_histogram(word):
#     word_list = list(word)
#     for n in word_list:
#         if n in empty_dictionary:
#             empty_dictionary[n] += 1
#         else:
#             empty_dictionary[n]= 1
#         return empty_dictionary
# print letter_histogram ("cheese")
#
#
# # 2 Word Summary
# #
# # Write a word_histogram function that takes a paragraph of text as its input,
#and returns a dictionary containing the tally of how many times
# each letter in the alphabet was used in the text. For example:
# #
# # >>> word_histogram('To be or not to be')
# # {'to': 2, 'be': 2, 'or': 1, 'not': 1}
# # In this exercise, are you using dynamic keys or fixed keys?
#
# def letter_histogram(word):
#     word_list = list(word)
#     for n in word_list:
#         if n in empty_dictionary:
#             empty_dictionary[n] += 1
#         else:
#             empty_dictionary[n]= 1
#         return empty_dictionary
# print letter_histogram ("cheese")



#

#
# empty_dictionary_para = {}

# def para_hist(paragraph):
#     paragraph_list = paragraph.split(" ")
#     for word in paragraph_list:
#         if word in empty_dictionary_para:
#             empty_dictionary_para[word] +=1
#         else:
#             empty_dictionary_para[word] = 1
#     return empty_dictionary_para
# print para_hist("lets go and do this")


# Bonus Challenge
#
# Given a histogram tally (one returned from
# either letter_histogram or word_summary),
# print the top 3 words or letters.


user_word = raw_input("Please enter a word to histo: ")
histo = letter_histogram(user_word)
histogram_list = []
for key in histo:
    histogram_list.append([key, histo[key]])
histogram_list.sort(key = lambda x: x[1])
print histogram_list[-1]
print histogram_list[-2]
print histogram_list[-3]



#  word_list = ['Jellicle', 'Cats', 'are', 'black', 'and', 'white,', 'Jellicle', 'Cats', 'are', 'rather', 'small;', 'Jellicle', 'Cats', 'are', 'merry', 'and', 'bright,', 'And', 'pleasant', 'to', 'hear', 'when', 'they', 'caterwaul.', 'Jellicle', 'Cats', 'have', 'cheerful', 'faces,', 'Jellicle', 'Cats', 'have', 'bright', 'black', 'eyes;', 'They', 'like', 'to', 'practise', 'their', 'airs', 'and', 'graces', 'And', 'wait', 'for', 'the', 'Jellicle', 'Moon', 'to', 'rise.', '']
# >>> word_counter = {}
# >>> for word in word_list:
#        if word in word_counter:
#           word_counter[word] += 1
#              else:
#               word_counter[word] = 1
#
# popular_words = sorted(word_counter, key = word_counter.get, reverse = True)
# >>>
# >>> top_3 = popular_words[:3]
# >>>
# top_3
# ['Jellicle', 'Cats', 'and']








#
# letter_histogram("helloworld")
# top_three = sorted(word_counter, key = word_counter.get, reverse = True)
# >>>







#
# word_list = list(word)
# from collections import Counter
# lettrs_to_count = (letter for letter in word_list if word[:1].isupper())
# c = Counter(words_to_count)
# print c.most_common(3)
#
#
#
# down vote
# To just return a list containing the most common words:
#
# from collections import Counter
# words=["i", "love", "you", "i", "you", "a", "are", "you", "you", "fine", "green"]
# most_common_words= [word for word, word_count in Counter(words).max(3)]
# print most_common_words

#
# fullname = "John Doe"
# namelist = fullname.split()
# for word in namelist:
#     print word[:2].lower(),
#
# str = "this is really a string example....wow!!!";
# print "Max character: " + max(str)

# histogram = "This is a sentence"




# empty_dictionary_para = {}

# def para_hist(paragraph):
#     paragraph_list = paragraph.split(" ")
#     for word in paragraph_list:
